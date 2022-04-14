from app.models import db, Video

def seed_videos():
    # TODO
    
    db.session.commit()



def undo_videos():
    db.session.execute('TRUNCATE videos RESTART IDENTITY CASCADE;')
    db.session.commit()
