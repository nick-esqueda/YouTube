from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, Email, ValidationError, Length, URL
from app.models import Channel


class ChannelEditForm(FlaskForm):
    profileImageUrl = StringField('profileImageUrl', validators=[URL(), Length(max=255)])
    bannerImageUrl = StringField('bannerImageUrl', validators=[URL(), Length(max=255)])
    about = StringField('about', validators=[Length(max=5000)])
    
    
class ChannelEditFormNoPfp(FlaskForm):
    profileImageUrl = StringField('profileImageUrl', validators=[Length(max=255)])
    bannerImageUrl = StringField('bannerImageUrl', validators=[URL(), Length(max=255)])
    about = StringField('about', validators=[Length(max=5000)])
