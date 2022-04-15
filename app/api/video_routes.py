from flask import Blueprint, jsonify, session
from sqlalchemy import desc
from app.models import Video, Channel

video_routes = Blueprint('videos', __name__)


@video_routes.route('/<int:videoId>/')
def get_video(videoId):
    """
    GET /api/videos/:videoId\n
    Get a single video and its associated data.
    NOTE: 
    """
    video = Video.query.get(videoId).to_dict()
    return jsonify(video)


@video_routes.route('pages/<int:pageNum>/')
def get_videos(pageNum):
    """
    GET /api/videos/ \n
    Get all videos, for the home page. \n
    NOTE: for now, just respond with all videos, paginated. \n
    goal is to send suggested videos based on session user id
    """
    # id = int(session['_user_id'])
    # sessionUser = Channel.query.get(id)

    videos = Video.query.order_by(desc(Video.createdAt)).paginate(page=pageNum, per_page=10, error_out=False)
    videos = [video.to_dict() for video in videos.items]

    return jsonify(videos)
    