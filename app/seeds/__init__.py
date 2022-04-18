from flask.cli import AppGroup
from .channels import seed_channels, undo_channels
from .videos import seed_videos, undo_videos

# Creates a seed group to hold our commands
# So we can type `flask seed --help`
seed_commands = AppGroup('seed')


# Creates the `flask seed all` command
@seed_commands.command('all')
def seed():
    seed_channels()
    seed_videos()
    # Add other seed functions here


# Creates the `flask seed undo` command
@seed_commands.command('undo')
def undo():
    undo_videos()
    undo_channels()
    # Add other undo functions here
