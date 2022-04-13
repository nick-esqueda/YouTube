from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, Email, ValidationError
from app.models import Channel


def user_exists(form, field):
    # Checking if user exists
    email = field.data
    user = Channel.query.filter(Channel.email == email).first()
    if user:
        raise ValidationError('Email address is already in use.')


def username_exists(form, field):
    # Checking if username is already in use
    channelName = field.data
    user = Channel.query.filter(Channel.channelName == channelName).first()
    if user:
        raise ValidationError('Username is already in use.')


class SignUpForm(FlaskForm):
    channelName = StringField(
        'channelName', validators=[DataRequired(), username_exists])
    email = StringField('email', validators=[DataRequired(), user_exists])
    password = StringField('password', validators=[DataRequired()])
