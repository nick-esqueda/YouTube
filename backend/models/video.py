from .db import db
from .types import TSVector
from sqlalchemy.sql import func
from sqlalchemy import Index


class Video(db.Model):
    __tablename__ = "videos"

    id = db.Column(db.Integer, primary_key=True)
    channelId = db.Column(db.Integer, db.ForeignKey("channels.id"), nullable=False)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(50000), nullable=True)
    videoUrl = db.Column(db.String(255), nullable=False)
    thumbnailUrl = db.Column(db.String(255), nullable=False)
    createdAt = db.Column(
        db.DateTime(timezone=True), server_default=func.now(), nullable=False
    )
    updatedAt = db.Column(
        db.DateTime(timezone=True),
        server_onupdate=func.now(),
        server_default=func.now(),
    )

    channel = db.relationship("Channel", back_populates="videos")
    comments = db.relationship(
        "Comment", back_populates="video", lazy=True, cascade="all, delete"
    )

    # must create a tsvector column to store pre-computed values for faster full text search.
    document_fts = db.Column(
        TSVector(),
        db.Computed(
            "setweight(to_tsvector('english', title), 'A') || setweight(to_tsvector('english', coalesce(description, '')), 'B')",
            persisted=True,
        ),
    )
    __table_args__ = (Index("document_fts_idx", document_fts, postgresql_using="gin"),)

    def to_dict(self):
        return {
            "id": self.id,
            "channelId": self.channelId,
            "title": self.title,
            "description": self.description,
            "videoUrl": self.videoUrl,
            "thumbnailUrl": self.thumbnailUrl,
            "createdAt": self.createdAt,
            "channel": self.channel.to_dict_no_relations(),
        }

    def to_dict_no_relations(self):
        return {
            "id": self.id,
            "channelId": self.channelId,
            "title": self.title,
            "description": self.description,
            "videoUrl": self.videoUrl,
            "thumbnailUrl": self.thumbnailUrl,
            "createdAt": self.createdAt,
        }
