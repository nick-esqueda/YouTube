from app.models import db, Channel

def get_pfp(channelName):
    try:
        letter = channelName[0].upper()
        return f"/default-pfps/{letter}.png"
    except:
        return f"/default-pfps/default.jpg"

# Adds a demo user, you can add other users here if you want
def seed_channels():
    demo = Channel(
        channelName='Demo', email='demo@aa.io', password='password', profileImageUrl=get_pfp("Demo"))
    nick = Channel(
        channelName='Nick Esqueda', email='ne@ne.com', password='password', profileImageUrl=get_pfp("Nick"))
    charlie_puth = Channel(
        channelName='Charlie Puth', email='cp@cp.com', password='password', profileImageUrl="https://youtube-bucket-nick-esqueda.s3.amazonaws.com/charlie-puth.jpg", createdAt="2009-09-09T21:32:32Z", about="""Over the past three years, Charlie Puth has proven himself commercially with the extraordinary success of four multi-platinum hits, “One Call Away,” “Marvin Gaye,” and “We Don’t Talk Anymore” from his platinum-selling, Top 10 debut album Nine Track Mind, as well as his breakout hit “See You Again” — the best-selling song of 2015 worldwide that spent 12 weeks atop the Billboard Hot 100, earned him three Grammy nominations (including Song of the Year), a Golden Globe nomination, and 9x-platinum certification in the U.S. But the New Jersey-born singer, songwriter, musician, and producer was also eager to prove himself artistically when it came time to make his second album, Voicenotes, named after the trusty iPhone app he uses to collect his musical ideas. Puth co-wrote every song and recorded and produced the album entirely himself (barring one song he co- produced with Max Martin) mainly at his home studio in Los Angeles.A meticulously crafted game-changer replete with sparkling melodies and sleek, danceable grooves, Voicenotes decimates everything people may think they know about this musical polymath, who has not only written and produced his own massive hits, but also for other artists spanning a range of genres, including Jason Derulo, Trey Songz, Thomas Rhett, Maroon 5, and G-Eazy. On Voicenotes, Puth allows himself to truly be seen, not only as an artist but also as a human, which meant stepping out from behind the detached façade of lovelorn balladeering and being transparent about his emotions and influences. On the lyrical front, Voicenotes is an album that is largely about Puth’s struggle to find a normal relationship when his own life has hardly been normal since finding multiplatinum success, and the anxiety that pursuit has induced. “I wanted it to be a story of my travels from the East Coast to the West Coast and how my growing fame has affected my mind in good and bad ways,” he says. The first three singles — “Attention,” “How Long,” and “Done For Me” featuring Kehlani — cover that territory. “Whenever I met anybody, they often knew more about me than I knew about myself,” he says. “I’d never dealt with anything like that before.” Songs like “LA Girls,” “Like A Boy,” and “Slow It Down” detail different aspects of the rarified life of someone who feels like he should be enjoying the glittering lifestyle of fabulous parties and ample romantic opportunities, but just doesn’t — something Puth addresses on self-acceptance anthem “The Way I Am,” which opens with the following lines: “Maybe I’m a get a little anxious / Maybe I’m a get a little shy / Cuz everybody’s trying to be famous / And I’m just trying to find a place to hide”). “I thought I was supposed to go to all these parties and be this type of person so I’ve always shoved my anxiety under the carpet because I didn’t think anyone cared to hear about it,” he says. “This album touches on that, but I also wanted to make sure that these songs, at the end of the day, are fun because some people choose not to listen to the lyrics. They just want to go to the club, listen to the beat, and have a great time. And that’s totally fine, too.” """)
    dude_perfect = Channel(
        channelName='Dude Perfect', email='dp@dp.com', password='password', profileImageUrl="https://youtube-bucket-nick-esqueda.s3.amazonaws.com/dude-perfect.jpg", bannerImageUrl="https://youtube-bucket-nick-esqueda.s3.amazonaws.com/dude-perfect-banner.png", createdAt="2009-03-17T05:44:36Z", about="5 best buds just kickin' it. If you like Sports + Comedy, come join the Dude Perfect team!")
    web_dev_simplified = Channel(
        channelName='Web Dev Simplified', email='wds@wds.com', password='password', profileImageUrl="https://youtube-bucket-nick-esqueda.s3.amazonaws.com/web-dev-simplified.jpg", createdAt="2018-05-24T16:26:39Z", about="""Web Dev Simplified is all about teaching web development skills and techniques in an efficient and practical manner. If you are just getting started in web development Web Dev Simplified has all the tools you need to learn the newest and most popular technologies to convert you from a no stack to full stack developer. Web Dev Simplified also deep dives into advanced topics using the latest best practices for you seasoned web developers. I started Web Dev Simplified in order to share my passion for web development, and do what I truly love. Teach and inspire new web developers. I have been in love with full stack web development since 2015 when I did my first internship as a web developer. Ever since then I have pursued my passion, learning everything there is to know about web development. Over the years I have taught many colleagues and friends the joys of web development, and cannot wait to teach you. Thank you for watching!""")

    db.session.add(demo)
    db.session.add(nick)
    db.session.add(charlie_puth)
    db.session.add(dude_perfect)
    db.session.add(web_dev_simplified)

    db.session.commit()


# Uses a raw SQL query to TRUNCATE the users table.
# SQLAlchemy doesn't have a built in function to do this
# TRUNCATE Removes all the data from the table, and RESET IDENTITY
# resets the auto incrementing primary key, CASCADE deletes any
# dependent entities
def undo_channels():
    db.session.execute('TRUNCATE channels RESTART IDENTITY CASCADE;')
    db.session.commit()
