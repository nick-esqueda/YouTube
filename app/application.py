import os
from flask import Flask, render_template, request, session, redirect
from flask_cors import CORS
from flask_migrate import Migrate
from flask_wtf.csrf import CSRFProtect, generate_csrf
from flask_login import LoginManager
# from dotenv import load_dotenv
# load_dotenv()

from models import db, Channel
from api.auth_routes import auth_routes
from api.channel_routes import channel_routes
from api.video_routes import video_routes
from api.comment_routes import comment_routes
from api.s3_routes import s3_routes

from seeds import seed_commands

from config import Config

application = Flask(__name__)

# Setup login manager
login = LoginManager(application)
login.login_view = 'auth.unauthorized'


@login.user_loader
def load_user(id):
    return Channel.query.get(int(id))


# Tell flask about our seed commands
application.cli.add_command(seed_commands)

application.config.from_object(Config)
application.register_blueprint(auth_routes, url_prefix='/api/auth')
application.register_blueprint(channel_routes, url_prefix='/api/channels')
application.register_blueprint(video_routes, url_prefix='/api/videos')
application.register_blueprint(comment_routes, url_prefix='/api/videos')
application.register_blueprint(s3_routes, url_prefix='/api/s3')
db.init_app(application)
Migrate(application, db)

# Application Security
CORS(application, supports_credentials=True)


# Since we are deploying with Docker and Flask,
# we won't be using a buildpack when we deploy to Heroku.
# Therefore, we need to make sure that in production any
# request made over http is redirected to https.
# Well.........
@application.before_request
def https_redirect():
    if os.environ.get('FLASK_ENV') == 'production':
        if request.headers.get('X-Forwarded-Proto') == 'http':
            url = request.url.replace('http://', 'https://', 1)
            code = 301
            return redirect(url, code=code)


@application.after_request
def inject_csrf_token(response):
    response.set_cookie(
        'csrf_token',
        generate_csrf(),
        secure=True if os.environ.get('FLASK_ENV') == 'production' else False,
        samesite='Strict' if os.environ.get(
            'FLASK_ENV') == 'production' else None,
        httponly=True)
    return response


@application.route('/', defaults={'path': ''})
@application.route('/<path:path>')
def react_root(path):
    if path == 'favicon.ico':
        return application.send_static_file('favicon.ico')
    return application.send_static_file('index.html')


if __name__ == "__main__":
    application.run(debug=True)

