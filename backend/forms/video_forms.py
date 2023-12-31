from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, Length, URL
# from app.models import User, Post

class CreateVideoForm(FlaskForm):
    title = StringField('title', validators=[DataRequired(), Length(min=1, max=100)])
    description = StringField('description', validators=[Length(max=5000)])
    videoUrl = StringField('videoUrl', validators=[DataRequired(), URL(), Length(max=255)])
    thumbnailUrl = StringField('thumbnailUrl', validators=[DataRequired(), URL(), Length(max=255)])


class EditVideoForm(FlaskForm):
    title = StringField('title', validators=[DataRequired(), Length(min=1, max=100)])
    description = StringField('description', validators=[Length(max=5000)])
    thumbnailUrl = StringField('thumbnailUrl', validators=[DataRequired(), URL(), Length(max=255)])
