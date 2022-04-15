from flask import Blueprint, jsonify
from app.models import Video, Channel

video_routes = Blueprint('videos', __name__)


@video_routes.route('/<int:videoId>')
def get_video(id):
    pass
