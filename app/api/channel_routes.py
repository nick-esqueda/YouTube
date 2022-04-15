from flask import Blueprint, jsonify
from flask_login import login_required
from sqlalchemy import desc
from app.models import Channel, Video

channel_routes = Blueprint('channels', __name__)


@channel_routes.route('/')
@login_required
def channels():
    channels = Channel.query.all()
    return {'channels': [channel.to_dict() for channel in channels]}


@channel_routes.route('/<int:id>')
@login_required
def channel(id):
    channel = Channel.query.get(id)
    return channel.to_dict()


@channel_routes.route('/videos/<int:channelId>/pages/<int:pageNum>')
def get_videos_for_channel(channelId, pageNum):
    """
    GET /api/channels/videos/:channelId/pages/:pageNum \n
    Get a paginated collection of a channel's videos. \n
    NOTE: right now, only returns videos in order of 'createdAt' descending
    goal is to return two sets of videos, one in order of 'popular uploads (most viewed)'
    and 'latest uploads' 
    """
    videos = Video.query.filter(Video.channelId == channelId).order_by(desc(Video.createdAt)).paginate(page=pageNum, per_page=5, error_out=False)
    videos = [video.to_dict() for video in videos.items]
