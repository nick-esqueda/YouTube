from .db import db
from sqlalchemy.sql import func

class Comment(db.Model):
    __tablename__ = 'comments'

    id = db.Column(db.Integer, primary_key=True)
    videoId = db.Column(db.Integer, db.ForeignKey('videos.id'), nullable=False)
    channelId = db.Column(db.Integer, db.ForeignKey('channels.id'), nullable=False)
    content = db.Column(db.String(255), nullable=False)
    createdAt = db.Column(db.DateTime(timezone=True), server_default=func.now(), nullable=False)
    updatedAt = db.Column(db.DateTime(timezone=True), server_onupdate=func.now(), server_default=func.now())

    channel = db.relationship('Channel', back_populates='comments')
    video = db.relationship('Video', back_populates='comments')

    def to_dict(self):
        return {
            'id': self.id,
            'videoId': self.videoId,
            'channelId': self.channelId,
            'content': self.content,
            'channel': self.channel.to_dict_lite(),
            'createdAt': self.createdAt,
            'updatedAt': self.updatedAt
        }
