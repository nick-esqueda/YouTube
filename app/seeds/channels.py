from app.models import db, Channel


# Adds a demo user, you can add other users here if you want
def seed_channels():
    demo = Channel(
        channelName='Demo', email='demo@aa.io', password='password')
    marnie = Channel(
        channelName='marnie', email='marnie@aa.io', password='password')
    bobbie = Channel(
        channelName='bobbie', email='bobbie@aa.io', password='password')

    db.session.add(demo)
    db.session.add(marnie)
    db.session.add(bobbie)

    db.session.commit()


# Uses a raw SQL query to TRUNCATE the users table.
# SQLAlchemy doesn't have a built in function to do this
# TRUNCATE Removes all the data from the table, and RESET IDENTITY
# resets the auto incrementing primary key, CASCADE deletes any
# dependent entities
def undo_channels():
    db.session.execute('TRUNCATE channels RESTART IDENTITY CASCADE;')
    db.session.commit()
