from .db import db
from sqlalchemy.sql import func

class Video(db.Model):
    __tablename__ = 'videos'

    id = db.Column(db.Integer, primary_key=True)
    channelId = db.Column(db.Integer, db.ForeignKey('channels.id'), nullable=False)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(50000), nullable=True)
    videoUrl = db.Column(db.String(255), nullable=False)
    thumbnailUrl = db.Column(db.String(255), nullable=False)
    createdAt = db.Column(db.DateTime(timezone=True), server_default=func.now(), nullable=False)
    updatedAt = db.Column(db.DateTime(timezone=True), server_onupdate=func.now(), server_default=func.now())

    channel = db.relationship('Channel', back_populates='videos')
    comments = db.relationship('Comment', back_populates='video', cascade="all, delete")

    def to_dict(self):
        return {
            'id': self.id,
            'channelId': self.channelId,
            'title': self.title,
            'description': self.description,
            'videoUrl': self.videoUrl,
            'thumbnailUrl': self.thumbnailUrl,
            'createdAt': self.createdAt,
            'channel': self.channel.to_dict(),
            'comments': [comment.to_dict() for comment in self.comments]
        }
        
    def to_dict_channel(self):
        return {
            'id': self.id,
            'channelId': self.channelId,
            'title': self.title,
            'description': self.description,
            'videoUrl': self.videoUrl,
            'thumbnailUrl': self.thumbnailUrl,
            'createdAt': self.createdAt,
        }
        
