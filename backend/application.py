from flask import Flask
from flask_cors import CORS
from flask_migrate import Migrate
from flask_wtf.csrf import generate_csrf
from flask_login import LoginManager

from models import db, Channel
from api.auth_routes import auth_routes
from api.channel_routes import channel_routes
from api.video_routes import video_routes
from api.comment_routes import comment_routes
from api.s3_routes import s3_routes
from api.videos_likes_and_dislikes_routes import videos_likes_and_dislikes_routes
from api.search_routes import search_routes

from seeds import seed_commands

from config import Config

application = Flask(__name__)

# Setup login manager
login = LoginManager(application)
login.login_view = "auth.unauthorized"


@login.user_loader
def load_user(id):
    return Channel.query.get(int(id))


# Tell flask about our seed commands
application.cli.add_command(seed_commands)

application.config.from_object(Config)
application.register_blueprint(auth_routes, url_prefix="/api/auth")
application.register_blueprint(channel_routes, url_prefix="/api/channels")
application.register_blueprint(video_routes, url_prefix="/api/videos")
application.register_blueprint(comment_routes, url_prefix="/api/videos")
application.register_blueprint(s3_routes, url_prefix="/api/s3")
application.register_blueprint(
    videos_likes_and_dislikes_routes, url_prefix="/api/videos"
)
application.register_blueprint(search_routes, url_prefix="/api/search")
db.init_app(application)
Migrate(application, db)

# Application Security
CORS(application, supports_credentials=True)


@application.after_request
def inject_csrf_token(response):
    response.set_cookie(
        "csrf_token", generate_csrf(), secure=True, samesite="None", httponly=True
    )
    return response


@application.route("/health")
def health_check():
    return {"success": True}, 200, {"ContentType": "application/json"}


if __name__ == "__main__":
    application.run(debug=True)
