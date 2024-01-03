from .db import db
from sqlalchemy.sql import func

video_dislike = db.Table(
    "videos_dislikes",
    db.Column("id", db.Integer, primary_key=True),
    db.Column("channelId", db.Integer, db.ForeignKey("channels.id"), nullable=False),
    db.Column("videoId", db.Integer, db.ForeignKey("videos.id"), nullable=False),
    db.Column(
        "created_at",
        db.DateTime(timezone=True),
        server_default=func.now(),
        nullable=False,
    ),
)
