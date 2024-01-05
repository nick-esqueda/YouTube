from flask import Blueprint
from flask_login import login_required, current_user
from models import db, Video, video_like, video_dislike

videos_likes_and_dislikes_routes = Blueprint("videos_likes_and_dislikes", __name__)


@videos_likes_and_dislikes_routes.route("/<int:videoId>/likes/", methods=["POST"])
@login_required
def toggle_video_like(videoId):
    video = Video.query.get(videoId)

    # NOTE: querying DB twice to avoid iterating through a very large video.likes list.
    is_video_liked_by_current_user = (
        Video.query.filter_by(id=videoId)
        .join(video_like)
        .filter_by(channelId=current_user.id)
        .count()
        > 0
    )

    if is_video_liked_by_current_user:
        video.likes.remove(current_user)
    else:
        video.likes.append(current_user)

    db.session.commit()
    return {
        "likeCount": len(video.likes),
        "isLikedByCurrentUser": not is_video_liked_by_current_user,
    }, 201


@videos_likes_and_dislikes_routes.route("/<int:videoId>/dislikes/", methods=["POST"])
@login_required
def toggle_video_dislike(videoId):
    video = Video.query.get(videoId)

    # NOTE: querying DB twice to avoid iterating through a very large video.likes list.
    is_video_disliked_by_current_user = (
        Video.query.filter_by(id=videoId)
        .join(video_dislike)
        .filter_by(channelId=current_user.id)
        .count()
        > 0
    )

    if is_video_disliked_by_current_user:
        video.dislikes.remove(current_user)
    else:
        video.dislikes.append(current_user)

    db.session.commit()
    return {
        "dislikeCount": len(video.dislikes),
        "isDislikedByCurrentUser": not is_video_disliked_by_current_user,
    }, 201
