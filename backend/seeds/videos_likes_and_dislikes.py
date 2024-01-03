from models import Video
from models import Channel
from models import db
import random


def seed_videos_likes_and_dislikes():
    channels = Channel.query.all()
    videos = Video.query.all()

    for channel in channels:
        random_video_ids = random.sample(
            range(len(videos)),
            random.randint(0, len(videos)),
        )
        for id in random_video_ids:
            video = videos[id]
            is_like = random.randint(0, 1)
            if is_like:
                channel.video_likes.append(video)
            else:
                channel.video_dislikes.append(video)

    db.session.commit()


def undo_videos_likes_and_dislikes():
    db.session.execute("TRUNCATE videos_likes RESTART IDENTITY CASCADE;")
    db.session.commit()
