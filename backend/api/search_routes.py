from flask import Blueprint, jsonify, session, request
from sqlalchemy import desc, func
from api.utils import validation_errors_to_error_messages
from forms.video_forms import CreateVideoForm, EditVideoForm
from models import db, Video, Channel

search_routes = Blueprint("search", __name__)


@search_routes.route("/")
def search():
    query = request.args.get("query")
    print("query in request: ", query)

    # TODO: pagination
    video_results = (
        Video.query.filter(
            Video.document_fts.op("@@")(func.websearch_to_tsquery(query))
        )
        .order_by(
            desc(
                func.ts_rank(Video.document_fts, func.websearch_to_tsquery(query)),
            )
        )
        .all()
    )

    video_results = [video.to_dict() for video in video_results]
    return jsonify(video_results)
