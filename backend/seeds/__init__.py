from flask.cli import AppGroup
from .channels import seed_channels, undo_channels
from .videos import seed_videos, undo_videos
from .comments import seed_comments, undo_comments
from .videos_likes_and_dislikes import (
    seed_videos_likes_and_dislikes,
    undo_videos_likes_and_dislikes,
)

# Creates a seed group to hold our commands
# So we can type `flask seed --help`
seed_commands = AppGroup("seed")


# Creates the `flask seed all` command
@seed_commands.command("all")
def seed():
    seed_channels()
    seed_videos()
    seed_comments()
    seed_videos_likes_and_dislikes()
    # Add other seed functions here


# Creates the `flask seed undo` command
@seed_commands.command("undo")
def undo():
    undo_videos()
    undo_channels()
    undo_comments()
    undo_videos_likes_and_dislikes()
    # Add other undo functions here
