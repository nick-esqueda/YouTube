from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, Length
# from app.models import User, Post

class CreateCommentForm(FlaskForm):
    content = StringField('Content', validators=[DataRequired(), Length(min=1, max=255)])


class EditCommentForm(FlaskForm):
    content = StringField('Content', validators=[DataRequired(), Length(min=1, max=255)])
