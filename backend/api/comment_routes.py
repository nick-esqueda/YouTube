from flask import Blueprint, session, request, jsonify
from forms.comment_forms import CreateCommentForm, EditCommentForm
from models import db, Comment
from api.utils import validation_errors_to_error_messages

comment_routes = Blueprint('comments', __name__)


# ROUTES #############################################################################
@comment_routes.route('/<int:videoId>/comments')
def get_videos_comments(videoId):
    videos_comments = Comment.query.filter_by(videoId=videoId).order_by(Comment.createdAt.desc()).all()
    videos_comments = [comment.to_dict() for comment in videos_comments]
    return jsonify(videos_comments)

    
@comment_routes.route('/<int:videoId>/comments/', methods=["POST"])
def create_comment(videoId):
    form = CreateCommentForm()

    form['csrf_token'].data = request.cookies['csrf_token']

    if form.validate_on_submit():
        data = {
            "channelId": session['_user_id'],
            "videoId": videoId,
            "content": form.data["content"],
        }

        comment = Comment(**data)
        db.session.add(comment)
        db.session.commit()
        print(comment.to_dict())
        return jsonify(comment.to_dict())

    return {'errors': validation_errors_to_error_messages(form.errors)}, 401


@comment_routes.route('/<int:videoId>/comments/<int:commentId>/', methods=["PUT"])
def edit_comment(videoId, commentId):
    form = EditCommentForm()
    comment = request.get_json()

    form['csrf_token'].data = request.cookies['csrf_token']
    sessionUserId = int(session['_user_id'])

    if form.validate_on_submit():
        comment = Comment.query.get(commentId)
        if sessionUserId == comment.channelId:
            comment.content = form['content'].data
            db.session.commit()
            print(comment.to_dict())
            return jsonify(comment.to_dict())

    return {'errors': validation_errors_to_error_messages(form.errors)}, 401


@comment_routes.route('/<int:videoId>/comments/<int:commentId>/', methods=["DELETE"])
def delete_comment(videoId, commentId):
    comment = Comment.query.get(commentId)
    sessionUserId = int(session['_user_id'])

    if comment.to_dict()['channelId'] == sessionUserId:
        db.session.delete(comment)
        db.session.commit()
        return jsonify(commentId)
    else:
        return jsonify('not authorized'), 401
