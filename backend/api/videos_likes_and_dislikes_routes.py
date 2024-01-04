from flask import Blueprint
from flask_login import login_required, current_user
from models import db, Video

videos_likes_and_dislikes_routes = Blueprint("videos_likes_and_dislikes", __name__)


@videos_likes_and_dislikes_routes.route("/<int:videoId>/likes/", methods=["POST"])
@login_required
def create_video_like(videoId):
    video = Video.query.get(videoId)
    video.likes.append(current_user)
    db.session.commit()
    return "", 201


@videos_likes_and_dislikes_routes.route("/<int:videoId>/likes/", methods=["DELETE"])
@login_required
def delete_video_like(videoId):
    # TODO: delete only if current_user is the one who created the like.
    video = Video.query.get(videoId)
    video.likes = filter(lambda channel: channel.id != current_user.id, video.likes)
    db.session.commit()
    return "", 204


@videos_likes_and_dislikes_routes.route("/<int:videoId>/dislikes/", methods=["POST"])
@login_required
def create_video_dislike(videoId):
    video = Video.query.get(videoId)
    video.dislikes.append(current_user)
    db.session.commit()
    return "", 201


@videos_likes_and_dislikes_routes.route("/<int:videoId>/dislikes/", methods=["DELETE"])
@login_required
def delete_video_dislike(videoId):
    # TODO: delete only if current_user is the one who created the like.
    video = Video.query.get(videoId)
    video.dislikes = filter(
        lambda channel: channel.id != current_user.id, video.dislikes
    )
    db.session.commit()
    return "", 204
