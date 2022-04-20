from app.models import db, Channel

def get_pfp(channelName):
    try:
        letter = channelName[0].upper()
        return f"/default-pfps/{letter}.png"
    except:
        return f"/default-pfps/default.jpg"

# Adds a demo user, you can add other users here if you want
def seed_channels():
    # YT API SEEDS ###########################################################################################
    ##########################################################################################################
    Beast = Channel(channelName="Beast Reacts", password="password", profileImageUrl="https://yt3.ggpht.com/ytc/AKedOLREDyzQ-3o32vvhe7W0Iq2miFl7FOpLYIKHKq9_8A=s800-c-k-c0x00ffffff-no-rj", bannerImageUrl="https://yt3.ggpht.com/DxYzGkl2tw1cuie4GGDy34aJNUkjSCysgk2lQMmW_2xZdmffGiiJqWCydbxPReAZdANpe08s", channelTrailerId="v9WSjE3tIkg", createdAt="2016-04-24T20:43:46Z", email="beast_reacts@beast_reacts.com", about='''SUBSCRIBE FOR A COOKIE
    MrBeast and Chris react to the internet's favorite videos.''')



    TheOdd1sOut = Channel(channelName="TheOdd1sOut", password="password", profileImageUrl="https://yt3.ggpht.com/ytc/AKedOLS78NKu_RlcazIsIik9qIzE9CoYH94AzH-0d4xn4Q=s800-c-k-c0x00ffffff-no-rj", bannerImageUrl="https://lh3.googleusercontent.com/9H68iXklwmIxppTL3ussJNcwMDbPDUogzc-PvzeASOdK3wUdxAwTmd5YRayKNM_b6O1Fu724aQ", channelTrailerId="CAb_bCtKuXg", createdAt="2014-08-30T18:08:02Z", email="theodd1sout@theodd1sout.com", about='''What I use:
    I draw my pictures on Paint Tools Sai and I edit it all in Adobe Premiere. (Really? You don't use any animation software??) (Yeah, I know it's ''''not real animation''''') 

    I have a Wacom Cintiq Pro 24

    a Smudge Guard Glove. 
    https://amzn.to/2zvvUzj

    I record on a Shure sm7b, 
    https://amzn.to/2NKBtwP

    I have an Scarlett 2i 4 Audio interface 
    https://amzn.to/2uqIdqX

    and this thing called a 'Cloudlifter.'
    https://amzn.to/2ucIT42


    If these items are out of your price range then this is what I use(d) (The cheaper stuff)

    -My first tablet was a Bamboo Create for ~$100. Really good tablet 5/7. 
    https://amzn.to/2zudkYs

    I know alot of people like the intuos's 
    https://amzn.to/2L3eMFK

    -A good Microphone that a lot of people use is a Blue Yeti (keep in mind where you record is important.)
    https://amzn.to/2zri016''')



    AlishaMarie = Channel(channelName="AlishaMarie", password="password", profileImageUrl="https://yt3.ggpht.com/r0-3VbVeHXacTjDi6VwkLA7HYDqnooU4ys2UZzEVWiVP34NZHKH2NPmW-S-l_l4ZcCrx4y2rQfg=s800-c-k-c0x00ffffff-no-rj", bannerImageUrl="https://yt3.ggpht.com/_kWye6Wa_QLjpCX-Y1zIL6wiF8IKT3JbU1su_I2NgoBDnoIvFfHaumJi0Y3lRlBinBKVFXO4LA", channelTrailerId="Kizc5cEOTeg", createdAt="2008-04-18T23:32:57Z", email="alishamarie@alishamarie.com", about='''i do that thing called ~iNfLuEnCiNg~''')



    Cosmobyhaley = Channel(channelName="Cosmobyhaley", password="password", profileImageUrl="https://yt3.ggpht.com/ytc/AKedOLQ1daE3EBnj1pUcf9F2RhBTBynguHuOVZxppiGWWg=s800-c-k-c0x00ffffff-no-rj", bannerImageUrl="https://lh3.googleusercontent.com/9YMDQ4ob-az_dgnIKI4oVZRpU55i11x3S5J9yb3bdBh6lkBOsrt1aWGlsSq5q8msHZ94ltPfCQ", channelTrailerId="EFjZt8AU9Gw", createdAt="2015-04-16T19:58:31Z", email="cosmobyhaley@cosmobyhaley.com", about='''Hi friends! My name is Haley Wight, better known as Cosmobyhaley! I am a beauty vlogger here on the good ole youtube. Lets be BFFs!''')



    Milana = Channel(channelName="Milana Coco", password="password", profileImageUrl="https://yt3.ggpht.com/ytc/AKedOLR7IR_x9RSpbTW3iNeyv7sLEy2VfeOLIO-5ws7aRw=s800-c-k-c0x00ffffff-no-rj", bannerImageUrl="https://yt3.ggpht.com/Pm2WR-7XT0ztrXmT4JL2tUUYnV50upNGW-Q73l4mHEEUj2fsVwtx55GM-1C8GOL0gI2LJk0C-3k", channelTrailerId="GtBDxkUWTh0", createdAt="2013-07-30T16:49:34Z", email="milana_coco@milana_coco.com", about='''Hello to whoever is reading this right now :) My name is Milana. I joined Youtube back in July/2013 just to be subscribed to my favourite Youtubers, then during April 2015, I thought it would be an interesting idea to become a youtuber, so i posted my first video and now I created a Coco Puff family that keeps growing daily! 

    Important Milestones so far on my Youtube Channel: 

    April 2015: 300 

    July 2015: 10k 

    September 2015: 50k

    October 2015: 80K 

    November 28, 2015: 100K 

    June 15, 2016: 400K 

    August 8,2016: 700K 

    December 30, 2016: 1,000,000!!!!

    xoxo
    Milana Coco

    Insta: @milana.coco
    Twitter: @milana_coco''')



    Sharee = Channel(channelName="Sharee Love", password="password", profileImageUrl="https://yt3.ggpht.com/ytc/AKedOLRCmGLsm3fMGyDpNPtDZhVijiJ3npAql3VWgggOTw=s800-c-k-c0x00ffffff-no-rj", bannerImageUrl="https://yt3.ggpht.com/q8WUif5WQvevbKauCsE5cB0WXIinoMQEAXhIB6DNd-cYjODULtFeS2AlzbF6OdqxlxCG4Ti2YTw", channelTrailerId="JM8spE0K6Yo", createdAt="2010-12-28T07:07:28Z", email="sharee_love@sharee_love.com", about='''For collaborations and business inquiries, please contact: shareeslove@gmail.com''')



    Belinda = Channel(channelName="Belinda Selene", password="password", profileImageUrl="https://yt3.ggpht.com/ytc/AKedOLTVWw9gD6IxeVVJ2dnfg8krb2q7VqpvnUszzpZtUQ=s800-c-k-c0x00ffffff-no-rj", bannerImageUrl="https://lh3.googleusercontent.com/K-OMT5P0a5LiZoutAmQ4mbjKkmEakgjgAWu0pfXy0YVSSX8D1tp_UqrmgMpTxoyHC-UE0YLWZw", channelTrailerId="D559jWTpi-8", createdAt="2010-05-18T00:46:34Z", email="belinda_selene@belinda_selene.com", about='''
    INSTAGRAM: @BelindaSelene & @PlanWithBelinda

    PINTEREST: Belinda Selene

    TWITTER: @MissBelindaxox

    FACEBOOK: belindaseleneyt

    I love reading your letters!
    Belinda Selene
    PO Box 3292
    Munster, IN 46321

    Business inquiries: BelindaSelene@yahoo.com''')



    Derek = Channel(channelName="Derek Gerard", password="password", profileImageUrl="https://yt3.ggpht.com/ytc/AKedOLTDQVIOEFKh4fnnhkzPSlq5_rtKjSE-erA9QbxJMQ=s800-c-k-c0x00ffffff-no-rj", bannerImageUrl="https://yt3.ggpht.com/HjZZ4Q63I2qr_Zmc4JP0XqCfdbGnjuoY3rkwNNmbbbjq7pI9kmyiaWUgjDmvsPrdVTPHODPaJg", channelTrailerId="HBn-oHi-zoE", createdAt="2010-09-15T02:00:27Z", email="derek_gerard@derek_gerard.com", about='''My name is Derek Gerard and I make comedy videos on YouTube for the d-squad! 

    Thank you so much for checking out my channel!
    Love you! tehe

    For the d-squad:  DerekGerard@gmail.com
    Business and Brand Inquiries: derekgerard@ellifyagency.com''')



    People = Channel(channelName="People Vs Food", password="password", profileImageUrl="https://yt3.ggpht.com/byGVXGEG1Lqj5DE_yK1h_GEt7TWa_3eOWCGsIlDtEr52g0beqfk60Nv9luAiFmvUFEExomq6=s800-c-k-c0x00ffffff-no-rj", bannerImageUrl="https://yt3.ggpht.com/2u97IH0sITvmKDn0b9CTK2adzVt4bypBe3VATTCL11s9rvwn27eMWvsSpe7qHOc4IMQ3rNdlVg", channelTrailerId="9Smck0SxjMU", createdAt="2013-07-30T10:19:47Z", email="people_vs_food@people_vs_food.com", about='''People Vs Food is the newest channel from React Media! React's Replay has become your #1 food and cooking destination, People vs Food, with Replay favorites like TRY NOT TO EAT, along with a ton of insanely cool new shows for you to sink your teeth into like THE ULTIMATE COLLEGE COOKING SHOW, KITCHEN VS, and TOO MANY COOKS. Subscribe today!

    Subscribe to our other channels!
    REACT: http://www.youtube.com/REACT
    KIDS REACT: https://www.youtube.com/KidsREACTOfficial

    ''')



    TwinCoconuts = Channel(channelName="TwinCoconuts", password="password", profileImageUrl="https://yt3.ggpht.com/ytc/AKedOLRRhvdNRhNQjOcItXpNiSttbU11QNWPeHZzCTD3tw=s800-c-k-c0x00ffffff-no-rj", bannerImageUrl="https://yt3.ggpht.com/hq0Zmzx-g2nEZBdoRTC8PpYuZYA5nfMhdV1iuyz4-e5MnaSPLHVCMj2AqQ9oE5k3m-HOnHQ4_A", channelTrailerId="j4AQCkNwfl8", createdAt="2013-01-16T23:27:01Z", email="twincoconuts@twincoconuts.com", about='''Just some Ginger English Twins that get a buzz out of making people Smile.

    Harrison Bradley (Left)

    Jay Bradley (Right)

    Find Harrison here:

    Twitter ➨ @HarrisonB123
    Instagram ➨ HarrisonBradley_

    Find Jay here:

    Twitter ➨ @JayBradley5
    Instagram ➨JayBradley5

    For business inquiries, please contact via email. business.twincoconuts@gmail.com''')



    loveliveserve = Channel(channelName="loveliveserve", password="password", profileImageUrl="https://yt3.ggpht.com/ytc/AKedOLRrsq8iQN5Td_3K3fo0qepxmshPqh54qfiua_8Xbw=s800-c-k-c0x00ffffff-no-rj", bannerImageUrl="https://yt3.ggpht.com/S9tq-en6WqHJVfb7hPSw2TSwzG6CFKmfmOF50FSlXvlhNP1n5BDIPEnFBZ0kjiAXvUsdTkuf-g", channelTrailerId="myzAJnhvCcM", createdAt="2010-11-20T19:24:59Z", email="loveliveserve@loveliveserve.com", about='''Wuz Goodie! Welcome to LoveLiveServe! We go by Rhino & Noah Boat. We have a passion for making relatable and entertaining video content. We produce a variety of material on this channel that is suitable for a wide range of audiences. We look forward to creating a lot more videos for you guys!

    For business contact, email us at brian.sokolik@authenticm.com''')



    ashens = Channel(channelName="ashens", password="password", profileImageUrl="https://yt3.ggpht.com/ytc/AKedOLTVDeMlMVfH7CvQDi3U8karn780pKe8myEW4kM3=s800-c-k-c0x00ffffff-no-rj", bannerImageUrl="https://lh3.googleusercontent.com/8dwgpP3_r50p4Ir4ol324l-ItSs7-lmV4HhGsAbFG42Apcutr16DARlhMQwgchxq9onfPbo1Vw", channelTrailerId="mligzDh4s9A", createdAt="2006-02-23T22:09:52Z", email="ashens@ashens.com", about='''Comedy videos and gadget reviews from a British idiot in an ill-fitting suit.  New videos every week!  Usually!


    ''')



    POVPOOL = Channel(channelName="POVPOOL", password="password", profileImageUrl="https://yt3.ggpht.com/ytc/AKedOLRl3Moas5UsBIizYIx2fXNHckWqw43D4-IHz0M-=s800-c-k-c0x00ffffff-no-rj", bannerImageUrl="https://lh3.googleusercontent.com/6tx7ix6xHsdBIBJBbomxT_rlgO-7Ed1Y10xEqQ8bCu72QGqQgf-A2xjTODk40RLoZQh6Pmk8Mw", channelTrailerId="2WZrR3jLf58", createdAt="2010-12-02T07:55:50Z", email="povpool@povpool.com", about='''Welcome to Point Of View Pool! 

    90% of the videos on this channel are all produced and directed by us. We take pride in only posting our original footage. Please Subscribe to this channel and watch coverage of live-streamed pool action, videotaped at some of the best billiard venues in the U.S. 

    Please be sure to visit POV Pool's website to find a schedule of our 'LIVE' events. We live stream at least 30 per year. 

    POV Pool would like to begin posting pool footage taken by some of its followers to be played on our live streams. Please contact us at povpool@gmail.com where you can find out how to submit your footage to be used on our regular show!

    More action is always on the way!''')



    Secret = Channel(channelName="Secret Base", password="password", profileImageUrl="https://yt3.ggpht.com/ytc/AKedOLS_b5jtZBHfWpCoJgxVMv60dqRCcYFrhOxXW7Fkl3U=s800-c-k-c0x00ffffff-no-rj", bannerImageUrl="https://yt3.ggpht.com/3bdQr8IPLiVChigHtvMBxc21WK5xW_bsnPRa_PI5NK8VSXWdJHJsVEiXlT-IBe2iFOZzkvgC7w", channelTrailerId="XwXEndQ4PNE", createdAt="2007-05-20T09:18:54Z", email="secret_base@secret_base.com", about='''Welcome to Secret Base. You used to know us as SB Nation, or you used to know us not at all, either way - this is a community made just for you.

    We want to explore, explain, and experiment with sports. There are countless stories that we all know and love, or that we have all forgotten about, so if you want to dive into sports in every way possible - you've come to the right place.

    Want to know more about this Secret Base?
    https://www.sbnation.com/secret-base/21408368/welcome-to-secret-base''')



    World = Channel(channelName="World Rugby", password="password", profileImageUrl="https://yt3.ggpht.com/ytc/AKedOLQbtuUwCh06xZRtu-EPBfwyetnZrtvRgCEvmIUx_Q=s800-c-k-c0x00ffffff-no-rj", bannerImageUrl="https://yt3.ggpht.com/ms5buiSnWXPxJlwLZ0dsfvfxWAxmIeGk6ZpwWzrENNmu7p1gR5g-NCdSRtuFklwAV7B84JAY", channelTrailerId="A2rN_QCtRDQ", createdAt="2006-05-17T15:42:39Z", email="world_rugby@world_rugby.com", about='''Subscribe to our YouTube channel for highlights, features, behind-the-scenes footage, player interviews and much more.
    World Rugby is the world governing and Law making body for the Game of Rugby Union. 

    To find out more about World Rugby visit:
    http://www.worldrugby.org

    Abonnez-vous à World Rugby France: https://www.youtube.com/channel/UC8yDQBIfghpQCrJufJCGmIA

    ワールドラグビー日本のチャンネル登録をお願いします: https://www.youtube.com/channel/UCINNL-f2HyUQP1y_UG682hQ

    Follow us on Twitter:
    https://twitter.com/worldrugby

    Follow us on Instagram
    https://instagram.com/worldrugby

    Follow us on TikTok
    https://www.tiktok.com/@rugbyworldcup2019

    Rugby World Cup on Facebook
    https://www.facebook.com/rugbyworldcup

    Add us on Snapchat
    https://www.snapchat.com/add/rugbyworldcup''')



    Kobe = Channel(channelName="Kobe Can", password="password", profileImageUrl="https://yt3.ggpht.com/ytc/AKedOLQJ6Aobu9w5zczil78KHzEDO8qNhGcsj2n3uRumeQ=s800-c-k-c0x00ffffff-no-rj", bannerImageUrl="https://lh3.googleusercontent.com/6DC7FMhI7ckFxW6IuKUE9vZ-MxFFlKHpNb19QSN-XC6vSSAer-Gf_l3hvyuQmRGXKUXSN7ggMlc", channelTrailerId="None", createdAt="2013-08-29T09:27:11Z", email="kobe_can@kobe_can.com", about='''None''')



    nbaworthy = Channel(channelName="nbaworthy", password="password", profileImageUrl="https://yt3.ggpht.com/ytc/AKedOLQKChVa7iBJKGvzcrTH_DLaiRVVi45OJAMelVpJew=s800-c-k-c0x00ffffff-no-rj", bannerImageUrl="https://lh3.googleusercontent.com/TP8vncFqKb_-NH4EATLzrNeN1AazN_wlYbbuEhNdH8U6kgwuNSfBdiU6Jppg77M7DRvXgb3B_1o", channelTrailerId="2bzATww1wrI", createdAt="2014-03-02T20:58:04Z", email="nbaworthy@nbaworthy.com", about='''This channel is NOT affiliated with the National Basketball Association. I do NOT own the media that is posted on this channel, the National Basketball Association are the rightful property owners of all of the footage that displayed in EVERY video on this channel. NO Copyright Infringement is Intended.''')



    Rihanna = Channel(channelName="Rihanna", password="password", profileImageUrl="https://yt3.ggpht.com/ytc/AKedOLRFI8riEKgjEmT88Edyy4xN2j0pStUQaejKNpKsCA=s800-c-k-c0x00ffffff-no-rj-mo", bannerImageUrl="https://lh3.googleusercontent.com/gyqqVnFtlFj_d0qbnIkodWiI9A1esXBnS90J4u47iwTtK6egFi1EjFMxO7JKBzKKfm0GGyD7Pa0", channelTrailerId="m4UxyXbwHE4", createdAt="2005-11-06T16:14:28Z", email="rihanna@rihanna.com", about='''It’s hard to believe that Rihanna is only 30 years old. Yet within the 10 years since the start of her musical career, she’s become the youngest solo artist to score 14 No. 1 singles on the Billboard Hot 100 — the fastest to do so — she’s sold more than 54 million albums and 210 million tracks worldwide.
    
    Rihanna is the “Best Selling Digital Artist of All Time" with more than 100 million [RIAA] Gold & Platinum song certifications” and an eight-time Grammy Award winner who also counts 14 Billboard Music Awards among other countless music accolades.
    
    Aside from her musical achievements, Rihanna is a bona fide business woman with multiple entrepreneurial ventures. However, most importantly, her undeniable cultural influence has forever imprinted her in history as a global Icon despite her young age.''')



    Justin = Channel(channelName="Justin Bieber", password="password", profileImageUrl="https://yt3.ggpht.com/ytc/AKedOLRJKV4nAcZgct6Z8NM8PyRpCGNUrOlEx0Xx-f9_dQ=s800-c-k-c0x00ffffff-no-rj-mo", bannerImageUrl="https://yt3.ggpht.com/wdx69TNM4Nmkigh0j6Cor8rFVDNhXZWgLly3qaIgs1_ZyNQaIsKo4qCAyirDWM2CgHB5yy-Cyw", channelTrailerId="kF4QRGQM2ig", createdAt="2007-01-15T21:17:27Z", email="justin_bieber@justin_bieber.com", about='''Help change the world. JUSTICE the album out now https://JustinBieber.lnk.to/Justice''')



    Nicki = Channel(channelName="Nicki Minaj", password="password", profileImageUrl="https://yt3.ggpht.com/YBK-xoUZew5qdvoVQorZuzdm_WbzjFlqDaoUXkyZSxYNBh-Oayxy_8q_V95Y0wv0GoFOt1_U=s800-c-k-c0x00ffffff-no-nd-rj", bannerImageUrl="https://yt3.ggpht.com/Vi5YcgVUESmZ8888YQ-qPC0ZDq4Zglb8AYBCamXg0Dhh8JkctGYYFSV6_6V8a-9Gcp7roqO8hQ", channelTrailerId="yrGR11TDRYM", createdAt="2013-08-28T15:19:24Z", email="nicki_minaj@nicki_minaj.com", about='''Subscribe to the official Nicki Minaj channel on YouTube for new music and exclusive videos.''')



    Beyoncé = Channel(channelName="Beyoncé", password="password", profileImageUrl="https://yt3.ggpht.com/4L1ExpzYqU3_98CNo-d5xLZPQfAZ-e9hfsxdZUNdEgyN6rsdSoiR7heo5SS9D3Zt_NKml-2l_qI=s800-c-k-c0x00ffffff-no-nd-rj", bannerImageUrl="https://yt3.ggpht.com/cxI8cVfg0Hp2vzcqX0UEVAz9ywpCLoV6erA7B95aNleaeKmneEg3ckeECecJ4tkEwCo42oPSDw", channelTrailerId="4aeDlZOD-B0", createdAt="2005-11-07T06:09:32Z", email="beyoncé@beyoncé.com", about='''The Official Beyoncé Youtube Channel''')



    Juice = Channel(channelName="Juice WRLD", password="password", profileImageUrl="https://yt3.ggpht.com/ytc/AKedOLRQMYUY-0L5VJVJSKEC8Chlq8xHnFYWhaK7149FSw=s800-c-k-c0x00ffffff-no-rj-mo", bannerImageUrl="https://yt3.ggpht.com/JTDtxwisrhUht3FN4aUlM_8Eoe3n41_YDimhLTXqXefPOLiGIlWafMwx3EdYs6VP8LZpwopQzQ", channelTrailerId="ym9MpAz5PNI", createdAt="2018-01-30T20:54:16Z", email="juice_wrld@juice_wrld.com", about='''This is Juice WRLD's official channel.

    Chicago-area hip-hop musician Juice WRLD delivers introspective lyrics atop melodic production, echoing Travis Scott and Post Malone. Born Jarad Higgins in 1998, the Calumet Park artist grew up playing piano, drums, and guitar, turning to rap freestyling in high school. Influenced by rock music and Chicago drill from Lil Durk and Chief Keef, Higgins began recording as Juice TheKidd, a moniker derived from his haircut, which resembled 2Pac's in the film Juice.

    His early tracks were all posted online, leading up to 2017's Juice WRLD 999 EP. Produced by Nick Mira and Sidepce, the set included the singles "Lucid Dreams (Forget Me)" and "All Girls Are the Same". Both tracks would also land on his official debut full-length album, Goodbye & Good Riddance, which peaked at number 15 on the Billboard 200 upon release in May 2018.''')



    The = Channel(channelName="The YouTube Tech Guy", password="password", profileImageUrl="https://yt3.ggpht.com/ytc/AKedOLRW2-fIzYouQy0M3_vnXB-z-Gr4ArTrjf-5EfrW=s800-c-k-c0x00ffffff-no-rj", bannerImageUrl="https://yt3.ggpht.com/a69XKRiRKmFfXrA3zr6BmTV2U-5omvNbVV-ymuTbWnooWxFRqWHmg0egNu8njthhF-ujLv-cig", channelTrailerId="mf-BI1y9bbk", createdAt="2012-02-16T20:13:31Z", email="the_youtube_tech_guy@the_youtube_tech_guy.com", about='''This channel is dedicated to informing people about the best mobile industry, all computer technology and smart home innovations.  I am here to help you answer 3 questions:
    1 - Should you buy it? 
    2 - How does it compare to the competition? 
    3 - How do you use it?''')



    TechRadar = Channel(channelName="TechRadar", password="password", profileImageUrl="https://yt3.ggpht.com/ytc/AKedOLSnkko-26iJCHKBYnqVJV2JrCvbtYLl1q34sMXs5g=s800-c-k-c0x00ffffff-no-rj", bannerImageUrl="https://lh3.googleusercontent.com/oHPqAJgHt7WGPFW6loGBnUdalp-R8pSk9yD6JCvRhgkADrVhO3WImQc8wveTtbN3hVfrR5JkSw", channelTrailerId="167OpMCDJqQ", createdAt="2009-02-22T21:44:22Z", email="techradar@techradar.com", about='''The latest technology news and reviews, covering phones, computing, home entertainment systems, gadgets, cameras, video games and more.''')



    Jonathan = Channel(channelName="Jonathan Morrison", password="password", profileImageUrl="https://yt3.ggpht.com/ytc/AKedOLRrg3x2IqBZSQcPHy8Me1bfiXDlWr4bTd0OBSDY6g=s800-c-k-c0x00ffffff-no-rj", bannerImageUrl="https://lh3.googleusercontent.com/T0E8BWTuCR9vFqG1OAJG-fVVLW41LCz5isuQ76l_phQpuJwUvx7MElTSTnosOWv6lQ9Q8e1b-A", channelTrailerId="EyKnTA1sjxk", createdAt="2010-03-24T22:28:10Z", email="jonathan_morrison@jonathan_morrison.com", about='''High quality videos blending tech + aesthetic, showcasing the latest products & gadgets.''')
    
    
    
    Austin = Channel(channelName="Austin Evans", password="password", profileImageUrl="https://yt3.ggpht.com/ytc/AKedOLRxREsvWCc3gdgs-9IWBVAGIoK9vcGJSgWuy7V2BQ=s800-c-k-c0x00ffffff-no-rj", bannerImageUrl="https://lh3.googleusercontent.com/pIQqwytMF0aQENnsrtcH7_YTP0nUiyv_o2AZtJoUCVdMqojfL6ShC3WWOPRkRqNFVbUzKA_FxPo", channelTrailerId="KdVM2RhDaAM", createdAt="2007-08-05T01:39:45Z", email="austin_evans@austin_evans.com", about='''The best of technology from gaming PCs to smartphones and everything in between. Whether it's finding out if that new gadget is worth it, discovering the coolest of retro and cutting edge tech or testing the latest smartphone you'll find it all here. 

    Want to send something for me to take a look at?

    Austin Evans
    112 Harvard Avenue #49
    Claremont, CA 91711

    Channel Staff:

    Host - Austin Evans
    Creative Director - Kenneth Bolido
    Producer - Matt Ansini
    Producer/Writer - Jared Peterson
    Senior Video Editor - Joshua Blackey
    Junior Video Editor - Griffin Schiller

    ''')



    Android = Channel(channelName="Android Authority", password="password", profileImageUrl="https://yt3.ggpht.com/_Tya4y1GTYtsEzEztJIoeHV8ZQhKZN11GyyUx3VFBNnKa_CfN8csGDhiACHfMB519iCHgDjh8ls=s800-c-k-c0x00ffffff-no-rj", bannerImageUrl="https://yt3.ggpht.com/41ST6yYyHFs1kcxPxMMbogZoioEPKCowTn4fYv0gLM3BMOnZ8hh1fyjy9R2C5Sc5d4KItjenEA", channelTrailerId="aH5aDAD9wCA", createdAt="2011-04-03T15:19:11Z", email="android_authority@android_authority.com", about='''Android Authority is the largest independent publication dedicated to the world's most widely used operating system. Every month, we influence an audience of 50 million technology enthusiasts, industry professionals, and savvy millennials. Our team is a diverse coalition of expert writers, device reviewers, videographers, journalists and Android developers who have come together under a united passion: a love of mobile technology and the determination to deliver top-notch content.''')



    Thinknoodles = Channel(channelName="Thinknoodles", password="password", profileImageUrl="https://yt3.ggpht.com/nOZB48rn67uMwwG15LFTaPdNf5GJyNyj8pmIpfzh_qMndyWLC-05Xjeyo3c8r1F25yiMWJekQA=s800-c-k-c0x00ffffff-no-rj", bannerImageUrl="https://yt3.ggpht.com/8l5TpE0y3-eiD-yOfz5y7c6xFITaC5hT3zTAmc9Nq-Vvk9lroKKTqn4hnw0Y70Y67Kq213d2", channelTrailerId="L0dtvX831uI", createdAt="2011-12-15T20:08:51Z", email="thinknoodles@thinknoodles.com", about='''Hey everyone, it's your friend #Thinknoodles and welcome to my YouTube channel! Join me, my dogs Kopi & Kloi and other friends on our adventures in video games. Here you can find all kinds of family-friendly gaming videos. I play lots of different games from Minecraft, Horror Escape Games, ROBLOX Piggy, to your favorites or just plain random mobile games, indie games and more!

    Noodle on, Noodlers!
    ''')



    PewDiePie = Channel(channelName="PewDiePie", password="password", profileImageUrl="https://yt3.ggpht.com/5oUY3tashyxfqsjO5SGhjT4dus8FkN9CsAHwXWISFrdPYii1FudD4ICtLfuCw6-THJsJbgoY=s800-c-k-c0x00ffffff-no-rj", bannerImageUrl="https://yt3.ggpht.com/S44q51b0k25RH1oPdgXOaOSNpbZIL8TCrxCBqUigoMUoai_Cu99psc7zkd-BBgli4pOfzAzk", channelTrailerId="None", createdAt="2010-04-29T10:54:00Z", email="pewdiepie@pewdiepie.com", about='''I make videos.''')



    WILDCAT = Channel(channelName="WILDCAT", password="password", profileImageUrl="https://yt3.ggpht.com/ytc/AKedOLRcFXoThiXyCKq5NxRoBPkcBnJPeToQwrws6eqTww=s800-c-k-c0x00ffffff-no-rj", bannerImageUrl="https://yt3.ggpht.com/zWensFQZOtSkxHgpZVGYiEe6HSvdwdc8HjOQNsO9XedFFENN6ZEyH9y6zNMeactCc6rnptRE0Q", channelTrailerId="Aix8Ex7lH40", createdAt="2011-09-25T19:08:25Z", email="wildcat@wildcat.com", about='''Tyler - I AM WILDCAT

    For Business Inquiries Contact: business@iamwildcat.net

    About Me:
    My name is Tyler and I make my videos for fun and to get a couple laughs out of my viewers. I do my best to make entertaining content and upload as often as I see fit. Feel free to subscribe, it's free :D''')



    Oroboro = Channel(channelName="Oroboro", password="password", profileImageUrl="https://yt3.ggpht.com/ytc/AKedOLQI7zGPeMORHJN3dKwkX2XcBTSK_9xp7O6fdwRs0Q=s800-c-k-c0x00ffffff-no-rj", bannerImageUrl="https://yt3.ggpht.com/AvEklj46fI2lIuVbn6QUYuboqirZ2fZDlS82OWradZJgcrZ2ronpDatMxT1OhRDYt4CzZU44RA", channelTrailerId="None", createdAt="2010-04-03T07:19:35Z", email="oroboro@oroboro.com", about='''King nerd, creator of OP builds, hacker slayer, & hatemail master.''')



    nKuch = Channel(channelName="nKuch", password="password", profileImageUrl="https://yt3.ggpht.com/ytc/AKedOLQ1ThtKF6U04LybVcO4RRl_ZD2t6Wuto2PYc5Szrw=s800-c-k-c0x00ffffff-no-rj", bannerImageUrl="https://yt3.ggpht.com/zulDKsnW1IBz1WtnMmERA0WJz7_i749Y_kE-Zj_Yz3vmF1l153hCSkzK7C9uKkrYWM4eI_vOJpE", channelTrailerId="None", createdAt="2014-08-08T01:24:46Z", email="nkuch@nkuch.com", about='''Hey! My name is Nestor and I'm 24 Years old from Toronto, Canada. Dedicated to uploading daily content from a wide range of looter-shooter games, including Destiny, CoD & more! Hopefully my videos will entertain, inform and help you all! You can expect competitive insight from me as intense PvP is my specialty, I also love battle royale games. 

    **Please only contact me by email if you have a business related question or inquiry, I am not interested in network offers**''')



    Just = Channel(channelName="Just One Cookbook", password="password", profileImageUrl="https://yt3.ggpht.com/ytc/AKedOLSY6HIRSQOBAWjcClLyruMBSxdwRVskrackB0zDPA=s800-c-k-c0x00ffffff-no-rj", bannerImageUrl="https://yt3.ggpht.com/TdgCQ0facsQuQh2Zcg-vmJ6iFc7K12A5DzCI3EvStuzIpNaUYbaGHTt76jha0lsxCgadjgib2e8", channelTrailerId="-bK4f8VCPBo", createdAt="2011-04-14T04:55:24Z", email="just_one_cookbook@just_one_cookbook.com", about='''Namiko Hirasawa Chen, the host of Just One Cookbook® channel, shows you how to make authentic Japanese recipes easily in your own kitchen.  Join her as she introduces savory and tasty dishes every week!


    SUBSCRIBE — https://www.youtube.com/justonecookbook
    WEBSITE (recipes with step-by-step pictures) — https://www.justonecookbook.com
    FAN PAGE — https://www.facebook.com/justonecookbook
    INSTAGRAM — https://instagram.com/justonecookbook/
    COOKBOOKS (Essential Japanese Recipes Vol 1-3) — https://www.justonecookbook.com/cookbooks/

    Konnichiwa!  

    I'm Namiko Chen, the blogger behind Just One Cookbook.com. I'm a native Japanese, born and raised in Yokohama, Japan. I now live in SF, California. I have been sharing Japanese home-cooked recipes for over 11 years on JustOneCookbook.com, with a collection of over 1,000 recipes. I’ve also written 3 cookbooks on Essential Japanese Recipes. I hope you enjoy cooking with me!

    Thank you for watching my videos and for subscribing!  
    ''')



    KEEMI = Channel(channelName="KEEMI", password="password", profileImageUrl="https://yt3.ggpht.com/ZfjWdD0et1AezYFgu8bhrUHfuSnAj6zcOZSsUqLtSgmsoA5mevgr-B2DOj72LNLLvoJUnXc0zA=s800-c-k-c0x00ffffff-no-rj", bannerImageUrl="https://yt3.ggpht.com/uxs0EMyW0tieh6idu2lKwcR3jvjZ9PfrimRGAiZjamJP2g1L5x-UbsoAjwxJJUQTv7GrxJ9P5g", channelTrailerId="None", createdAt="2015-09-07T01:10:13Z", email="keemi@keemi.com", about='''Welcome :)''')



    Sanjeev = Channel(channelName="Sanjeev Kapoor Khazana ", password="password", profileImageUrl="https://yt3.ggpht.com/ENz1Y3ZQ4YONAF0Fq2SX7OJkhfzTiO2p7TAzoamWf1oCzhnfVMLAOE_wDGvDVa8Ww3pscCXA=s800-c-k-c0x00ffffff-no-rj", bannerImageUrl="https://yt3.ggpht.com/h4bUdaWUCyfe9db8buHFdw5mTkNZvCI-nj0GFPkVDTkuIw_ZF1wwVJmlA-D5wbCFY18H_pl1", channelTrailerId="jdAK5PnOZ5E", createdAt="2009-07-29T04:09:28Z", email="sanjeev_kapoor_khazana@sanjeev_kapoor_khazana.com", about='''None''')



    Bon = Channel(channelName="Bon Appétit", password="password", profileImageUrl="https://yt3.ggpht.com/ytc/AKedOLTIXilSgcswUNC8TAOHgxisVFkbnEAckge8TFJtFj0=s800-c-k-c0x00ffffff-no-rj", bannerImageUrl="https://yt3.ggpht.com/DU5xZCVpr5dvMatqlSXvMLt1D-DTdzr5x8CjXvaUHaJGhhB-tFoGr44lIb9NQ-PEMwezjMeN9mE", channelTrailerId="bwjT8n3Yw4c", createdAt="2008-04-29T22:26:01Z", email="bon_appétit@bon_appétit.com", about='''Welcome to Bon Appétit, where we want everyone to love cooking and eating as much as we do. Recipes you want to make. Cooking advice that works. Restaurant recommendations you trust.
    ''')



    emmymade = Channel(channelName="emmymade", password="password", profileImageUrl="https://yt3.ggpht.com/ytc/AKedOLTK2f9vRtTpbzKAEhpgXlJ565bvC_TIX2UPMWvrqA=s800-c-k-c0x00ffffff-no-rj", bannerImageUrl="https://yt3.ggpht.com/ySceWajo9pi14PtlhP6cyD8c7wlGTY4DLlaHLh0L1-tD2F1rXJ2Qd3skXjHiWW2u8YX8g9Mg", channelTrailerId="v_5qYM-qs1I", createdAt="2010-11-11T07:08:15Z", email="emmymade@emmymade.com", about='''Welcome to the official YouTube channel for Emmymade formerly known as Emmymadeinjapan. 

    I love learning about our world through food and invite you to come along for the ride. 

    If you have something which you think is extra special or unique in some way, or timely for me to try, please send me a direct message here on YouTube, or on FaceBook, and I'll see if I can fit it in. 

    Thanks for your continued support!

    Hugs,  
    Emmy

    contact: emmy@emmymade.com

    👩🏻 Website: https://www.emmymade.com/
    🐦 Twitter: https://twitter.com/emmymadeinjapan
    🌈 Instagram: http://instagram.com/emmymade
    🙃 Facebook: https://www.facebook.com/itsemmymadeinjapan/
    ⏰ Tiktok: https://www.tiktok.com/@emmymadetok
    🎂 Cameo: https://www.cameo.com/emmymade
    🐝: emmymade extras: https://www.youtube.com/channel/UCQjEdAaQ0zzbrsD-biel8eg


    ''')



    Clintus = Channel(channelName="Clintus.tv", password="password", profileImageUrl="https://yt3.ggpht.com/ytc/AKedOLR5s0E5fIlUDrhDtSZiEeQje0h0rQMU0TJqOMF5yQ=s800-c-k-c0x00ffffff-no-rj", bannerImageUrl="https://yt3.ggpht.com/Ok6h8dpny_ZMnrhH54DNYaXb32SCWKPeK6Z1r0Aeb04SENl3XlriqJJzoaAGnB_dfKkxpoWc", channelTrailerId="QfrLwhSRRs4", createdAt="2006-07-09T22:58:54Z", email="clintus.tv@clintus.tv.com", about='''Hi there, I'm Clintus and this is my life. I'm a father and full time content creator. I've been sharing my thoughts and experiences online since 2006 and don't plan on stopping any time soon. This channel is family friendly so everyone can enjoy it. Thank you for your time.

    500 N Estrella Pkwy Ste #B2 Box #617
    Goodyear, AZ 85338

    #VlogOn''')



    SiriusXM = Channel(channelName="SiriusXM", password="password", profileImageUrl="https://yt3.ggpht.com/ytc/AKedOLSslfJ0h9gkPCDWyAymaOV3fTGnNUpIv6nuFpAJ1Q=s800-c-k-c0x00ffffff-no-rj", bannerImageUrl="https://yt3.ggpht.com/8aohoH5J7Ov50jt9zIV9eQis8Qk0kF0KvB6HRo94T2cwBBqU5fAxKKh06tkG8iLRHi8f2ew5", channelTrailerId="E0Krpkccq2k", createdAt="2005-12-13T19:00:37Z", email="siriusxm@siriusxm.com", about='''Your favorite music performances and interviews, plus talk, sports and more.


    SiriusXM is the largest audio entertainment company in the world, broadcasting over 150 channels of commercial-free music, premier sports, live news, talk, comedy, entertainment, traffic and weather. We are one of the world's largest pure-play audio entertainment companies and we are among the largest subscription media companies in the United States. SiriusXM broadcasts to subscribers everywhere they want to listen on more than 800 devices for cars, boats, the home or office, and through a wide range of mobile devices.''')



    Yung = Channel(channelName="Yung Afro", password="password", profileImageUrl="https://yt3.ggpht.com/ytc/AKedOLS6Fl9A1w8ZaCj-s2FpIl5Pym7oA2BFAsC-hhBDBg=s800-c-k-c0x00ffffff-no-rj", bannerImageUrl="https://yt3.ggpht.com/nbqfWlXUwyYzZen2DE7C1W68oLrNtFJE3nl3LOsR6aa8P30MjNKaQHfv9dmBAHMmywUHFkaGyg", channelTrailerId="XLyvFTSn1O4", createdAt="2015-01-30T06:18:53Z", email="yung_afro@yung_afro.com", about='''Not the most confident person however entertaining 
    people has always made me happy
    subscribe to keep the Afro Army growing :D''')



    JonJorgenson = Channel(channelName="JonJorgenson", password="password", profileImageUrl="https://yt3.ggpht.com/ytc/AKedOLRbJaHPLvQN8OPL5fpJiB9gLb4TnFf2LEQtNnwIEw=s800-c-k-c0x00ffffff-no-rj", bannerImageUrl="https://yt3.ggpht.com/d1ruXxBfW6UwN_COMjyic2dmY75dn1Q33a8LTAnT3on-sozLMxLs_Vv_9ixzSQ30BKE1MrqSBaE", channelTrailerId="5wxhSBHcpPI", createdAt="2013-02-24T18:28:41Z", email="jonjorgenson@jonjorgenson.com", about='''Jon Jorgenson is an author, speaker, and spoken word poet whose YouTube videos have been viewed by more than 15 million people. Jon partners with numerous organizations including Awana International, Moody Bible Institute, the Willow Creek Association, and hundreds of other churches, colleges, and conferences all over the globe. His spoken word poetry provides a dynamic and creative experience that captures the imagination of audiences everywhere. As a former Broadway actor, Chicago native, and very lucky husband, Jon hopes to provide a fresh, unique voice to some of life’s most difficult and challenging questions.''')



    Family = Channel(channelName="Family Fun Pack", password="password", profileImageUrl="https://yt3.ggpht.com/ytc/AKedOLTCR3_EnI8WfmdMbgGucNUNQPgAwCneePlOK5z2eg=s800-c-k-c0x00ffffff-no-rj", bannerImageUrl="https://yt3.ggpht.com/FgE8ZBnsBb027J1XakE7_0uZjRY1NV0exwn2xiNwpGIDDMZGQ9SmTPdpFPtBTRcO4AwfT5zsbA", channelTrailerId="bg1BFOdE3wQ", createdAt="2011-10-03T05:00:09Z", email="family_fun_pack@family_fun_pack.com", about='''Hi guys, I'm Kristine, and I invite you to follow my journey as a mom. I have been documenting my life as a mother since 2011 here on YouTube.  I have 7 beautiful children, including identical twins, and a wonderful husband.  We love to travel and spend as much time together as we can. We usually travel about half the year. We love to be creative!  Our motto is find fun in everything, so if someone's having fun, it's our family!
    Thanks for visiting our channel. Please subscribe so you can come along on our adventures! 

    Be sure to follow me on Instagram (FamilyFunPack) for giveaways!

    Want to send fan mail? For companies wanting to send samples, please email first.
    Address: 
    Family Fun Pack
    1968 S. Coast Hwy #2655
    Laguna Beach CA 92651

    You can find our merch at https://www.flashfomo.com/collections/family-fun-pack

    People have been asking the kids sizes. Here are some guidelines: Alyssa and David (adult medium), twins 14, Michael 10, Owen, 6, Chloe (baby) #familyfunpack''')



    grav3yardgirl = Channel(channelName="grav3yardgirl", password="password", profileImageUrl="https://yt3.ggpht.com/ytc/AKedOLR3ynKmCofQZ4IiR0kgPm7niePuSPGrqIXN7Hcdmw=s800-c-k-c0x00ffffff-no-rj", bannerImageUrl="https://yt3.ggpht.com/Wl2uoJPhqD-L_kwkQuJUTIrkiCo2DeGnK245FCIXKpshpL4HHINY07__f5iO4cEEYQO8pqQR", channelTrailerId="l8_ig-iPCn0", createdAt="2010-12-03T07:48:33Z", email="grav3yardgirl@grav3yardgirl.com", about='''GRAV3YARDGIRL
    PO BOX #2263
    PEARLAND, TEXAS
    77588

    † JOSHUA 1:9

    BUSINESS ONLY e-mail me at:
    bunnymeyer@gmail.com''')



    Nicoletta = Channel(channelName="Nicoletta xo", password="password", profileImageUrl="https://yt3.ggpht.com/Qk-SyuSOOTi4ypTRtDP0o_NVsshuT3osilakq4U4OAC89qinCCiTChCzFhzEcy8vWZfzVfHy_w=s800-c-k-c0x00ffffff-no-rj", bannerImageUrl="https://yt3.ggpht.com/3VKbKRPsXmaC8IdCteTJEOXQCpBcKTKGvxy7Avbml71a2UFGzrTdbyYkvo7HYm0hOolVDmf7fA", channelTrailerId="81rA4-zFMX0", createdAt="2012-12-27T22:31:20Z", email="nicoletta_xo@nicoletta_xo.com", about='''For business inquiries:
    xonicoletta@gmail.com 

    Hello Gorgeous! My name is Nicoletta, welcome to my lifestyle channel we talk anywhere from beauty, fashion, fitness and even advice
    New Uploads EVERY WEEK Tuesdays & Thursdays.
    please subscribe and join me through this experience ♡
    Instagram: @nicolettaxoyt
    Twitter: https://twitter.com/nicolettaxo''')



    Beardbrand = Channel(channelName="Beardbrand", password="password", profileImageUrl="https://yt3.ggpht.com/ytc/AKedOLRrlO3UK976znNYdgw3k3bEUsW2NUW811dWYJIS1g=s800-c-k-c0x00ffffff-no-rj", bannerImageUrl="https://yt3.ggpht.com/ohUIkaDZmCiw5XkdBYls211W3SD_0FimvDUfkjsxOrbjrHf8OIMZJXLaoMwgPLNkYeqVvTD1srQ", channelTrailerId="Vx99n8pTl4g", createdAt="2012-02-08T20:34:32Z", email="beardbrand@beardbrand.com", about='''Since 2012, Beardbrand has been dedicated to providing educational and inspirational content to help men Keep on Growing. Our line of highly versatile grooming products for beard, hair, and skin supports an ever-growing online community that includes more than 1,000,000 YouTube Subscribers. 

    With over 1,000 videos related to beards, men’s grooming, and lifestyle, you’re sure to find something on our channel to help you grow. New content is released weekly and features some of the most legendary barbers on YouTube. 

    For beard, hair, and style tutorials, self-improvement, and inspiration, check out our second channel, Beardbrand Alliance, over at www.youtube.com/beardbrandalliance.

    Subscribe, comment, and welcome to the community. 

    Visit www.beardbrand.com to learn more.

    Keep on Growing.''')



    Tasmin = Channel(channelName="Tasmin Dhaliwal", password="password", profileImageUrl="https://yt3.ggpht.com/ytc/AKedOLSB6ce-8-LodHz7uZ4wuPAq85tdl4SfsynSObuuhw=s800-c-k-c0x00ffffff-no-rj", bannerImageUrl="https://yt3.ggpht.com/dOi_TPRJyA0VuMq3XWE2dpLpiivZI_ImbyCtjESo3gHHWaKYGtn8jx8W1jykPrP5X9bzEGmO", channelTrailerId="EvNpYUqo5FM", createdAt="2013-08-29T00:47:21Z", email="tasmin_dhaliwal@tasmin_dhaliwal.com", about='''Hey my names Tasmin, but you can call me Taz. 

    I create beauty and fashion videos but my main goal is to promote inner beauty ♥ I hope my channel inspires you & you join the famila 

    Love ya even if you dont know it yet! 

    Tasmin 

    Follow me so we can chat all day er'day 

    Tumblr-http://r-e-a-d-my-mind.tumblr.com/
    twitter-https://twitter.com/Crystalbeauty9
    instagram-https://www.instagram.com/tasdhaliwal

    For business inquires contact me at: tasmindhaliwal@outlook.com 

    xoxoxo''')



    Sage = Channel(channelName="Sage Lescher", password="password", profileImageUrl="https://yt3.ggpht.com/ytc/AKedOLQqsw0dzz6KVYn-_XfmAlwsbjpbuUCk9xoyBxs8vg=s800-c-k-c0x00ffffff-no-rj", bannerImageUrl="https://yt3.ggpht.com/XhvuO0mAYdfnXgTHEf_JBvOmFJ9DiqlzrNNnEWW87si1TSGz0GfEV9T0QjYaZg-ADAMbVPDM", channelTrailerId="Hfjd3IjRBiE", createdAt="2013-06-29T23:44:17Z", email="sage_lescher@sage_lescher.com", about='''None''')



    AFV = Channel(channelName="AFV Classics", password="password", profileImageUrl="https://yt3.ggpht.com/ytc/AKedOLTxQGSpOtxxEp3aNDahPlSC3eAA0GeWoMrrNBIQoA=s800-c-k-c0x00ffffff-no-rj", bannerImageUrl="https://yt3.ggpht.com/JnIPRxb9LTEEGBRquqUIQmXacGGNqcp2Iv4BkGtdcWBLwcIzgW6yTOe6WIb8h54HtpPSPYZIXA", channelTrailerId="AM9NSsRRagQ", createdAt="2011-06-09T03:29:08Z", email="afv_classics@afv_classics.com", about='''Welcome to the AFV fan channel made just for AFV fans. 
    America's Funniest Home Videos, has been an American institution for 30 seasons! The hit show presents the unexpected funny moments that happen when things don't go quite as planned. From practical jokes to home improvement fails, from funny animals and pets to cute babies and tots, America's Funniest Home Videos is a hilarious look at everyday moments caught on tape. Stay up to date with our latest uploads. Don't forget to Subscribe for more great classic AFV fun!

    SUBSCRIBE: http://www.youtube.com/subscription_center?add_user=BestAFVonU2BE

    Connect with AFV Online:
    Visit the AFV WEBSITE: http://afv.tv/AFVWeb
    Like AFV on FACEBOOK: http://afv.tv/AFVfb2
    Follow AFV on TWITTER: http://afv.tv/AFVtwitter 
    Follow AFV on INSTAGRAM: @afvofficial
    Follow AFV on MUSICAL.LY: @afvofficial 

    For all licensing inquiries please contact: info(at)homevideolicensing(dot)com''')



    Jinx = Channel(channelName="Jinx", password="password", profileImageUrl="https://yt3.ggpht.com/ytc/AKedOLTEQ2MXZm5GjpCFApUKkOiSmhF3IqPdhMYHWO1Z7A=s800-c-k-c0x00ffffff-no-rj", bannerImageUrl="https://yt3.ggpht.com/tgmYZN_pftOgGt3YxWBbLOzOCj-PTCba9V79iFZIymFBSV6_F2kuSopO_K6ZAFz_9lemNYlhHg", channelTrailerId="wwzs1mZjOy8", createdAt="2013-04-30T08:32:56Z", email="jinx@jinx.com", about='''Home of the funniest reactions! 
    Check out my music here! https://youtu.be/GlmDq4pplaw''')



    qbanguy = Channel(channelName="qbanguy", password="password", profileImageUrl="https://yt3.ggpht.com/ytc/AKedOLT-6f_RFrLI4M-O5YrH1Obw-fOtmBpIW_Qz0Ww6sA=s800-c-k-c0x00ffffff-no-rj", bannerImageUrl="https://yt3.ggpht.com/w-e6JtCyScQ9mrIUcnf2XxDxf9qobrgGjKr29etnu0BwviJ9Oyjz_RWE7kIGmkMuMlPO64RaDA", channelTrailerId="XEbJ915CQqk", createdAt="2006-10-10T23:41:42Z", email="qbanguy@qbanguy.com", about='''SUBSCRIBE for weekly funny sketches and parodies!''')
    
    
        
    Colleen = Channel(channelName="Colleen Ballinger", password="password", profileImageUrl="https://yt3.ggpht.com/ytc/AKedOLRNgYgXFIvrsQkRWb0QgaK-MC0uHV84od_7wi5vbQ=s800-c-k-c0x00ffffff-no-rj", bannerImageUrl="https://yt3.ggpht.com/ZgQ8w50vsbQGobtLnxiFmnK83z5ITeu6gxgODsHbCTeJFN9XKDnt1N2o4YNlq1MrIoQuwU_hWw", channelTrailerId="D1kvZsGSJ6c", createdAt="2006-07-31T02:46:42Z", email="colleen_ballinger@colleen_ballinger.com", about='''I enjoy singing, laughing, my family and sharing it all on youtube.  Enjoy!''')



    Adult = Channel(channelName="Adult Swim", password="password", profileImageUrl="https://yt3.ggpht.com/edxjf6DeK4ba1LKNafNR-5IqpPypjuxkc9IKf1NNRptsQNQFVs_GXpY6sT5uahtKPIuVjq0Udbg=s800-c-k-c0x00ffffff-no-rj", bannerImageUrl="https://yt3.ggpht.com/5yb8AvEhOKHMn3KLGcp4iLUMSiD1z3JSVWECXQ6P4kFkwg2zsPGa-FgqmDbul_QClJSaN_OIIg", channelTrailerId="YCKO1qgotHY", createdAt="2006-03-03T02:37:54Z", email="adult_swim@adult_swim.com", about='''Watch Adult Swim on HBO Max, www.adultswim.com, or by downloading the Adult Swim app. Binge marathons or watch selected episodes of many of your favorite shows including Rick and Morty, Robot Chicken, Venture Bros., Aqua Teen Hunger Force and many more.''')



    James = Channel(channelName="James Kingston", password="password", profileImageUrl="https://yt3.ggpht.com/xLGXo1wctbDv-2ZVFK82oomhZN2w5iTMVA8fY1QQ1mKUCr0PDg9EEAQw4pzxecpVC_PDxdeA=s800-c-k-c0x00ffffff-no-rj", bannerImageUrl="https://yt3.ggpht.com/SbcMnPPj4S9g-9Lf9Jl5jL7f7dmbxAmbwxTGHDa5J3XC3knLTk9q_geqHlyxQYNX-7J7z2tndg", channelTrailerId="dIqXaB4fpZs", createdAt="2008-11-17T22:42:22Z", email="james_kingston@james_kingston.com", about='''Climbing the worlds tallest buildings & exploring the unexplored...''')



    Kick = Channel(channelName="Kick Genius", password="password", profileImageUrl="https://yt3.ggpht.com/ytc/AKedOLRWRtGIbEajkjezmts6_EQXRWoQ-KNmjp9f0Nor6w=s800-c-k-c0x00ffffff-no-rj", bannerImageUrl="https://yt3.ggpht.com/tVfEswTxTeZVxmmNbDyqdOSQVfO7bUNyWdiKV8FRT7TKv54BB1qW_pQp6s7xb-jWM9_RGVEL", channelTrailerId="Qpfkls1z_r0", createdAt="2012-10-10T04:38:46Z", email="kick_genius@kick_genius.com", about='''The intersection between hoops and sneakers''')



    WhatCulture = Channel(channelName="WhatCulture Wrestling", password="password", profileImageUrl="https://yt3.ggpht.com/RhL67i0JF-N9gX75aKb6Bgel_jAX037zbGRocCNLOG8EaqtVcC5fID7hxJ5NaVUn5aV6oeGGPA=s800-c-k-c0x00ffffff-no-rj", bannerImageUrl="https://yt3.ggpht.com/KeSqxU7fMuLU2Vm6fGKEwDpWzz_WpWLp-2vhOASpxkw19nRcbjCEdPxXCQueGNKwOWPIyYYySA", channelTrailerId="529TkJWg874", createdAt="2014-12-11T10:29:41Z", email="whatculture_wrestling@whatculture_wrestling.com", about='''WhatCulture Wrestling offers you all the latest wrestling and WWE news, insider perspectives, interviews and entertaining features on the world of professional wrestling!''')



    Paul = Channel(channelName="Paul Rabil", password="password", profileImageUrl="https://yt3.ggpht.com/ytc/AKedOLTAcVqQ5fWJOnUl7_QsHdIcEZ9th5KaXAtrIN_tJA=s800-c-k-c0x00ffffff-no-rj", bannerImageUrl="https://yt3.ggpht.com/jxkSTKfkm1gTY2KcND5GiZNpHew8SB7Qjj6yjqorlwbfJEL-UTRB4aaOn8ZOJZK80ezB6L3dgg", channelTrailerId="pVvX8EPcZRk", createdAt="2008-05-07T03:25:23Z", email="paul_rabil@paul_rabil.com", about='''When I was 12, my friend gave me his backup stick. 
    I took it with me everywhere. Now we’re taking the sport into the future. 

    Watch our daily vlogs, workout edits, Rabil's Kitchen series, and more. And, of course, subscribe + comment your questions below!

    https://paulrabil.com

    https://premierlacrosseleague.com''')



    NBA = Channel(channelName="NBA G League", password="password", profileImageUrl="https://yt3.ggpht.com/Fw0Y0BmkhsyBATq0w9xHrX2x1hJZPH0hrKn_489Id28p2f2qHJHYzIrF-nXTAr6E5hhfpzYdjw=s800-c-k-c0x00ffffff-no-rj", bannerImageUrl="https://yt3.ggpht.com/EoKialjwVKnsvjaAmWtFXkSsu5Yn6d-mtE0OIaliBHXxva6eEZhHQxqJnB9j7jnYdaZ8WePxmA", channelTrailerId="ixZokzWVd4k", createdAt="2008-05-09T15:31:57Z", email="nba_g_league@nba_g_league.com", about='''The NBA G League is the NBA's official minor league, preparing players, coaches, officials, trainers, and front-office staff for the NBA while acting as the league's research and development laboratory. A record 45% of players on start-of-season NBA rosters in 2020-21, including those under NBA two-way contracts, have NBA G League experience.  In fostering the league's connection to the community, its teams, players and staff promote health and wellness, support local needs and interests, and assist in educational development through NBA G League Cares programs.

    Visit us on the web: http://www.NBAGLeague.com
    Like us on Facebook: http://www.facebook.com/nbagleague
    Follow us on Twitter: http://www.twitter.com/nbagleague
    Follow us on Instagram: http://www.instagram.com/nbagleague
    Follow us on TikTok: https://www.tiktok.com/@nbagleague
    ''')



    Wiz = Channel(channelName="Wiz Khalifa", password="password", profileImageUrl="https://yt3.ggpht.com/MehoWv8wE9h6ptkL1vmRKhjDNKq2HvDcDRucCF9IPyl8-8LqR83OD1G2Oa1T64mAKGDa3zSS=s800-c-k-c0x00ffffff-no-nd-rj", bannerImageUrl="https://yt3.ggpht.com/24BghJCfhrLs_ITokK8bWlPGotqYKgs3X4gnQXQ6HXHN8cC1sviewqmdp7X0Q5PWjZAj5-09ZA", channelTrailerId="LNPnz5LDbr8", createdAt="2008-05-09T02:49:21Z", email="wiz_khalifa@wiz_khalifa.com", about='''Wiz Khalifa's Official YouTube Channel
    Taylor Gang Ent. / Atlantic Records''')



    Bruno = Channel(channelName="Bruno Mars", password="password", profileImageUrl="https://yt3.ggpht.com/vE1ESBld6LqHBv7339FuPAn1WBKJR5PFnZRzwqQ78Gp3zxB7seqCw6HfQLJIMTaz-iIjUj72=s800-c-k-c0x00ffffff-no-nd-rj", bannerImageUrl="https://yt3.ggpht.com/ly_K2xiytpu4yw2GqlJciQf22Ve78-NdSxIQ8bqiYVMjI3OZTYze7zTNjpogg-okPAEgWBwr", channelTrailerId="eEQMtIX61LA", createdAt="2006-09-19T01:34:43Z", email="bruno_mars@bruno_mars.com", about='''An Evening With Silk Sonic: https://SilkSonic.lnk.to/AEWSSID

    The official YouTube channel of Bruno Mars. 

    Subscribe for the latest official music videos, live performances, official audio, and more: https://Atlantic.lnk.to/BMsubscribe
    
    11x GRAMMY Award winner and 27x GRAMMY Award nominee Bruno Mars is a celebrated singer, songwriter, producer, and musician with iconic hits like "The Lazy Song", "That's What I Like", "Just The Way You Are", "24K Magic", "Locked Out Of Heaven", and "When I Was Your Man". His legendary body of work also includes blockbuster albums such as Doo-Wops & Hooligans, Unorthodox Jukebox, and 24K Magic, as well as era-defining collaborations like "Uptown Funk" with Mark Ronson, "Finesse" with Cardi B, and "Nothin' On You" with B.o.B. Forever classic, yet supremely innovative, Bruno continues to redefine music, style, and popular culture, pushing the boundaries of pop, R&B, funk, soul, hip-hop, and dance, and remains as influential as ever.
    ''')



    Katy = Channel(channelName="Katy Perry", password="password", profileImageUrl="https://yt3.ggpht.com/8s2hH6UfSKbED2-UUVgCALU5BXXxvnk2ueNzBaCU-exfeoC9X1OZzDa6uqzI4cOA3ZDqyXjIsg=s800-c-k-c0x00ffffff-no-nd-rj", bannerImageUrl="https://yt3.ggpht.com/ZFp8La3dGMvEYzqzu5n_-sIBYQXLk3X3wtdvtioIcjnaoJCa9zwkUvz21Z3s1cA-GyigmNKcug", channelTrailerId="N-4YMlihRf4", createdAt="2008-06-01T19:58:36Z", email="katy_perry@katy_perry.com", about='''https://www.katyperry.com/''')



    EminemMusic = Channel(channelName="EminemMusic", password="password", profileImageUrl="https://yt3.ggpht.com/ytc/AKedOLTl3oEyE5erZSJL6T3AqzFUo2pjsbI2f595a8gvQQ=s800-c-k-c0x00ffffff-no-rj-mo", bannerImageUrl="https://yt3.ggpht.com/67JN6u-y2P0tk0Mdj0kaD9Gr-eMxZ5fN7mekALTP2QEhTRphu4GLUHZaBPzkocUHu3lkvazk9YQ", channelTrailerId="jfobiCq0YUc", createdAt="2007-02-09T00:01:36Z", email="eminemmusic@eminemmusic.com", about='''Marshall Bruce Mathers III, better known by his stage name Eminem (stylized as EMINƎM) and by his alter ego Slim Shady, is an American rapper, record producer, songwriter and actor. Eminem, along with his solo career, is a member of his group D12, and also one half of the hip hop duo Bad Meets Evil, with Royce da 5'9". Eminem is one of the best-selling artists in the world and is the best-selling artist of the 2000s.''')



    Ariana = Channel(channelName="Ariana Grande", password="password", profileImageUrl="https://yt3.ggpht.com/ytc/AKedOLQwKqgKtpTJS809vJQNVrpPlNffgDeZkVlQFDpAtA=s800-c-k-c0x00ffffff-no-rj-mo", bannerImageUrl="https://yt3.ggpht.com/z8dPdOBqWg36cVZbYtIvPz6mkriM7CkacKFmqNUi78s8MP16ZEHaMGAzy5lTl62j_y2_Fvz15EM", channelTrailerId="BnyvDBGojoQ", createdAt="2007-01-22T01:53:12Z", email="ariana_grande@ariana_grande.com", about='''https://arianagrande.lnk.to/positions
    ''')
    
    
    
    web_dev_simplified = Channel(channelName='Web Dev Simplified', email='wds@wds.com', password='password', profileImageUrl="https://youtube-bucket-nick-esqueda.s3.amazonaws.com/web-dev-simplified.jpg", createdAt="2018-05-24T16:26:39Z", about="""Web Dev Simplified is all about teaching web development skills and techniques in an efficient and practical manner. If you are just getting started in web development Web Dev Simplified has all the tools you need to learn the newest and most popular technologies to convert you from a no stack to full stack developer. Web Dev Simplified also deep dives into advanced topics using the latest best practices for you seasoned web developers. I started Web Dev Simplified in order to share my passion for web development, and do what I truly love. Teach and inspire new web developers. I have been in love with full stack web development since 2015 when I did my first internship as a web developer. Ever since then I have pursued my passion, learning everything there is to know about web development. Over the years I have taught many colleagues and friends the joys of web development, and cannot wait to teach you. Thank you for watching!""")
    
    # NORMAL USER SEEDS ######################################################################################
    # TODO
    ##########################################################################################################
    
    channels = [
        Beast,
        TheOdd1sOut,
        AlishaMarie,
        Cosmobyhaley,
        Milana,
        Sharee,
        Belinda,
        Derek,
        People,
        TwinCoconuts,
        loveliveserve,
        ashens,
        POVPOOL,
        Secret,
        World,
        Kobe,
        nbaworthy,
        Rihanna,
        Justin,
        Nicki,
        Beyoncé,
        Juice,
        The,
        TechRadar,
        Jonathan,
        Austin,
        Android,
        Thinknoodles,
        PewDiePie,
        WILDCAT,
        Oroboro,
        nKuch,
        Just,
        KEEMI,
        Sanjeev,
        Bon,
        emmymade,
        Clintus,
        SiriusXM,
        Yung,
        JonJorgenson,
        Family,
        grav3yardgirl,
        Nicoletta,
        Beardbrand,
        Tasmin,
        Sage,
        AFV,
        Jinx,
        qbanguy,
        Colleen,
        # Adult,
        James,
        Kick,
        # WhatCulture,
        Paul,
        NBA,
        # Wiz,
        Bruno,
        Katy,
        EminemMusic,
        Ariana,
        web_dev_simplified,
    ]
    
    demo = Channel(
        channelName='Demo', email='demo@aa.io', password='password', profileImageUrl=get_pfp("Demo"))
    nick = Channel(
        channelName='Nick Esqueda', email='ne@ne.com', password='password', profileImageUrl=get_pfp("Nick"))


    for channel in channels:
        db.session.add(channel)
    db.session.add(demo)
    db.session.add(nick)

    db.session.commit()


# Uses a raw SQL query to TRUNCATE the users table.
# SQLAlchemy doesn't have a built in function to do this
# TRUNCATE Removes all the data from the table, and RESET IDENTITY
# resets the auto incrementing primary key, CASCADE deletes any
# dependent entities
def undo_channels():
    db.session.execute('TRUNCATE channels RESTART IDENTITY CASCADE;')
    db.session.commit()
