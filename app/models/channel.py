from sqlalchemy.sql import func
from .db import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


class Channel(db.Model, UserMixin):
    __tablename__ = 'channels'

    id = db.Column(db.Integer, primary_key=True)
    channelName = db.Column(db.String(50), nullable=False, unique=True)
    profileImageUrl = db.Column(db.String(255), nullable=False)
    about = db.Column(db.String(255), nullable=True)
    email = db.Column(db.String(150), nullable=False, unique=True)
    hashedPassword = db.Column(db.String(255), nullable=False)
    createdAt = db.Column(db.DateTime(timezone=True), server_default=func.now(), nullable=False)
    updatedAt = db.Column(db.DateTime(timezone=True), server_onupdate=func.now(), server_default=func.now())


    @property
    def password(self):
        return self.hashed_password

    @password.setter
    def password(self, password):
        self.hashed_password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def to_dict(self):
        return {
            'id': self.id,
            'channelName': self.channelName,
            'email': self.email
        }
