from flask import Blueprint, jsonify, session, request
from sqlalchemy import desc
from app.api.utils import validation_errors_to_error_messages
from app.models import db, Video, Channel

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
    GET /api/videos/pages/:pageNum \n
    Get all videos, for the home page. \n
    NOTE: for now, just respond with all videos, paginated. \n
    goal is to send suggested videos based on session user id
    """
    # id = int(session['_user_id'])
    # sessionUser = Channel.query.get(id)

    videos = Video.query.order_by(desc(Video.createdAt)).paginate(page=pageNum, per_page=10, error_out=False)
    videos = [video.to_dict() for video in videos.items]

    return jsonify(videos)
    

@video_routes.route('/', methods=["POST"])
def create_video():
    """
    POST /api/videos/ \n
    Create a new video, and return the newly created video. \n
    TODO: CREATE THE NEW VIDEO FORM! \n
    """
    # TODO CREATE THIS FORM
    form = CreateVideoForm()

    form['csrf_token'].data = request.cookies['csrf_token']

    if form.validate_on_submit():
        data = {
            "channelId": session['_user_id'],
            "title": form.data["title"],
            "description": form.data["description"],
            "videoUrl": form.data["videoUrl"],
            "thumbnailUrl": form.data["thumbnailUrl"],
        }

        video = Video(**data)
        db.session.add(video)
        db.session.commit()
        return jsonify(video.to_dict())
        
    print('\n\n\n FORM ERRORS HERE:', form.errors, '\n\n\n')
    return {'errors': validation_errors_to_error_messages(form.errors)}, 401
