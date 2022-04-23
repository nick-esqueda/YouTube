from flask import Blueprint, jsonify, request, session
from flask_login import login_required
from sqlalchemy import desc
from app.models import db, Channel, Video
from app.forms import ChannelEditForm, ChannelEditFormDefaultPfp
from app.api.utils import validation_errors_to_error_messages

channel_routes = Blueprint('channels', __name__)


@channel_routes.route('/')
@login_required
def channels():
    channels = Channel.query.all()
    return {'channels': [channel.to_dict() for channel in channels]}


@channel_routes.route('/<int:id>/')
@login_required
def channel(id):
    channel = Channel.query.get(id)
    return channel.to_dict()
    
    
# @channel_routes.route('/other/<int:id>/')
# def get_other_channel(id):
#     channel = Channel.query.get(id)
#     return channel.to_dict()


@channel_routes.route('/videos/<int:channelId>/pages/<int:pageNum>')
def get_videos_for_channel(channelId, pageNum):
    """
    GET /api/channels/videos/:channelId/pages/:pageNum \n
    Get a paginated collection of a channel's videos. (not paginating currently) \n
    NOTE: right now, only returns videos in order of 'createdAt' descending
    goal is to return two sets of videos, one in order of 'popular uploads (most viewed)'
    and 'latest uploads' 
    """
    # videos = Video.query.filter(Video.channelId == channelId).order_by(desc(Video.createdAt)).paginate(page=pageNum, per_page=5, error_out=False)
    # videos = [video.to_dict() for video in videos.items]
    videos = Video.query.filter(Video.channelId == channelId).order_by(desc(Video.createdAt)).all()
    videos = [video.to_dict() for video in videos.items]
    return jsonify(videos)


@channel_routes.route('/<int:channelId>/', methods=["PATCH"])
def edit_channel(channelId):
    """
    PATCH /api/channels/:channelId \n
    Update a channel by :channelId, then return the updated channel info. \n
    """
    if request.json["profileImageUrl"].startswith('/default-pfps'):
        form = ChannelEditFormDefaultPfp()
    else:
        form = ChannelEditForm()

    form['csrf_token'].data = request.cookies['csrf_token']

    if form.validate_on_submit():
        sessionUserId = int(session['_user_id'])

        channel = Channel.query.get(channelId)
        if channel.id != sessionUserId:
            return { 'not authorized': 'you are not authorized to update this video.' }, 403
        else:
            channel.profileImageUrl = form['profileImageUrl'].data
            channel.bannerimageUrl = form['bannerImageUrl'].data
            channel.about = form['about'].data
            db.session.commit()
            
            return jsonify(channel.to_dict())
    
    print('\n\n\n FORM ERRORS HERE:', form.errors, '\n\n\n')
    return {'errors': validation_errors_to_error_messages(form.errors)}, 401
