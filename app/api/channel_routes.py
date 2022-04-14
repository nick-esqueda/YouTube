from flask import Blueprint, jsonify
from flask_login import login_required
from app.models import Channel

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
