from .db import db
from .video_like import video_like
from .video_dislike import video_dislike
from sqlalchemy.sql import func
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


class Channel(db.Model, UserMixin):
    __tablename__ = "channels"

    id = db.Column(db.Integer, primary_key=True)
    channelName = db.Column(db.String(50), nullable=False, unique=True)
    profileImageUrl = db.Column(db.String(255), nullable=False)
    bannerImageUrl = db.Column(db.String(255), nullable=True)
    channelTrailerId = db.Column(db.String(100), nullable=True)
    about = db.Column(db.String(5000), nullable=True)
    email = db.Column(db.String(150), nullable=False, unique=True)
    hashedPassword = db.Column(db.String(255), nullable=False)
    createdAt = db.Column(
        db.DateTime(timezone=True), server_default=func.now(), nullable=False
    )
    updatedAt = db.Column(
        db.DateTime(timezone=True),
        server_onupdate=func.now(),
        server_default=func.now(),
    )

    videos = db.relationship(
        "Video", back_populates="channel", lazy=True, cascade="all, delete"
    )
    comments = db.relationship(
        "Comment", back_populates="channel", lazy=True, cascade="all, delete"
    )
    video_likes = db.relationship(
        "Video",
        secondary=video_like,
        back_populates="likes",
        lazy=True,
        cascade="all, delete",
    )
    video_dislikes = db.relationship(
        "Video",
        secondary=video_dislike,
        back_populates="dislikes",
        lazy=True,
        cascade="all, delete",
    )

    @property
    def password(self):
        return self.hashedPassword

    @password.setter
    def password(self, password):
        self.hashedPassword = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def to_dict(self):
        return {
            "id": self.id,
            "channelName": self.channelName,
            "profileImageUrl": self.profileImageUrl,
            "bannerImageUrl": self.bannerImageUrl,
            "about": self.about,
            "email": self.email,
            "createdAt": self.createdAt,
            # TODO: remove videos so that frontend has to call GET /api/channels/:channelId/videos
            "videos": [video.to_dict_no_relations() for video in self.videos],
            "videoLikeCount": len(self.video_likes),
            "videoDislikeCount": len(self.video_dislikes),
        }

    def to_dict_no_relations(self):
        return {
            "id": self.id,
            "channelName": self.channelName,
            "profileImageUrl": self.profileImageUrl,
            "bannerImageUrl": self.bannerImageUrl,
            "about": self.about,
            "email": self.email,
            "createdAt": self.createdAt,
        }
