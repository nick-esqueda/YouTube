from models import db, Comment

def seed_comments():
    comment1 = Comment(videoId=746, channelId=25, content="It was a really good Monday for being a Saturday.", createdAt="Mon Mar 14 2022 17:56:29", updatedAt="Wed Jul 21 2021 12:05:56")
    comment2 = Comment(videoId=404, channelId=90, content="It's not often you find a soggy banana on the street.", createdAt="Sat Jan 01 2022 23:08:06", updatedAt="Mon Aug 09 2021 23:54:22")
    comment3 = Comment(videoId=78, channelId=46, content="Abstraction is often one floor above you.", createdAt="Thu Jul 22 2021 07:48:18", updatedAt="Mon Oct 18 2021 16:31:18")
    comment4 = Comment(videoId=685, channelId=78, content="Warm beer on a cold day isn't my idea of fun.", createdAt="Sat Oct 02 2021 20:49:23", updatedAt="Fri Nov 19 2021 21:42:27")
    comment5 = Comment(videoId=148, channelId=31, content="It's never comforting to know that your fate depends on something as unpredictable as the popping of corn.", createdAt="Fri Apr 08 2022 18:59:10", updatedAt="Tue Jan 04 2022 00:03:11")
    comment6 = Comment(videoId=88, channelId=44, content="Bill ran from the giraffe toward the dolphin.", createdAt="Fri Jul 30 2021 10:08:49", updatedAt="Wed Jan 26 2022 07:25:44")
    comment7 = Comment(videoId=282, channelId=63, content="Giving directions that the mountains are to the west only works when you can see them.", createdAt="Wed May 19 2021 18:01:14", updatedAt="Thu Oct 14 2021 05:48:40")
    comment8 = Comment(videoId=441, channelId=92, content="I often see the time 11:11 or 12:34 on clocks.", createdAt="Wed Dec 08 2021 15:56:12", updatedAt="Wed Sep 22 2021 19:36:52")
    comment9 = Comment(videoId=307, channelId=9, content="Their argument could be heard across the parking lot.", createdAt="Wed Oct 27 2021 17:53:15", updatedAt="Thu May 13 2021 03:17:48")
    comment10 = Comment(videoId=326, channelId=96, content="I want to buy a onesie… but know it won’t suit me.", createdAt="Wed Apr 14 2021 06:18:21", updatedAt="Thu Jul 01 2021 22:29:01")
    comment11 = Comment(videoId=563, channelId=24, content="Buried deep in the snow, he hoped his batteries were fresh in his avalanche beacon.", createdAt="Sun Dec 26 2021 22:28:55", updatedAt="Thu Oct 21 2021 10:58:27")
    comment12 = Comment(videoId=308, channelId=78, content="Three years later, the coffin was still full of Jello.", createdAt="Mon Aug 16 2021 03:37:08", updatedAt="Sun Apr 03 2022 05:59:56")
    comment13 = Comment(videoId=503, channelId=8, content="If you spin around three times, you'll start to feel melancholy.", createdAt="Thu Jul 29 2021 01:19:38", updatedAt="Thu Aug 26 2021 10:46:20")
    comment14 = Comment(videoId=275, channelId=91, content="I really want to go to work, but I am too sick to drive.", createdAt="Mon Nov 08 2021 19:40:05", updatedAt="Sun Oct 17 2021 23:42:37")
    comment15 = Comment(videoId=537, channelId=78, content="Let me help you with your baggage.", createdAt="Mon Jul 12 2021 04:42:16", updatedAt="Wed Jul 21 2021 05:12:54")
    comment16 = Comment(videoId=227, channelId=66, content="Some bathing suits just shouldn’t be worn by some people.", createdAt="Mon Jan 24 2022 02:53:03", updatedAt="Fri Aug 27 2021 01:47:54")
    comment17 = Comment(videoId=569, channelId=40, content="Mary plays the piano.", createdAt="Tue Jan 25 2022 14:41:46", updatedAt="Thu Mar 17 2022 20:08:02")
    comment18 = Comment(videoId=102, channelId=49, content="Erin accidentally created a new universe.", createdAt="Tue Oct 26 2021 18:36:23", updatedAt="Tue May 18 2021 22:20:51")
    comment19 = Comment(videoId=453, channelId=94, content="Peanuts don't grow on trees, but cashews do.", createdAt="Wed Jun 16 2021 17:46:11", updatedAt="Fri Nov 19 2021 11:05:49")
    comment20 = Comment(videoId=97, channelId=92, content="At that moment I was the most fearsome weasel in the entire swamp.", createdAt="Tue May 18 2021 21:18:32", updatedAt="Wed Apr 21 2021 03:17:47")
    comment21 = Comment(videoId=405, channelId=71, content="She had some amazing news to share but nobody to share it with.", createdAt="Wed Jan 19 2022 07:49:28", updatedAt="Thu Apr 22 2021 06:19:01")
    comment22 = Comment(videoId=739, channelId=76, content="As the years pass by, we all know owners look more and more like their dogs.", createdAt="Fri Apr 16 2021 17:10:46", updatedAt="Mon Feb 28 2022 17:23:13")
    comment23 = Comment(videoId=666, channelId=21, content="Being unacquainted with the chief raccoon was harming his prospects for promotion.", createdAt="Sat May 15 2021 01:27:38", updatedAt="Mon Nov 15 2021 20:35:48")
    comment24 = Comment(videoId=152, channelId=24, content="Having no hair made him look even hairier.", createdAt="Thu Sep 16 2021 12:07:05", updatedAt="Thu Nov 25 2021 01:06:56")
    comment25 = Comment(videoId=478, channelId=92, content="As he dangled from the rope deep inside the crevasse", createdAt="Mon Apr 26 2021 15:26:14", updatedAt="Tue Aug 03 2021 04:08:14")
    comment26 = Comment(videoId=379, channelId=37, content="She always speaks to him in a loud voice.", createdAt="Wed Nov 10 2021 12:59:50", updatedAt="Fri Feb 11 2022 14:39:59")
    comment27 = Comment(videoId=264, channelId=6, content="I never knew what hardship looked like until it started raining bowling balls.", createdAt="Tue Jan 04 2022 23:08:05", updatedAt="Mon Jan 24 2022 23:52:18")
    comment28 = Comment(videoId=250, channelId=21, content="The door slammed on the watermelon.", createdAt="Sun Dec 19 2021 06:18:02", updatedAt="Sun Mar 27 2022 00:12:43")
    comment29 = Comment(videoId=725, channelId=88, content="Greetings from the real universe.", createdAt="Sun Jul 18 2021 21:12:49", updatedAt="Sun Jun 13 2021 06:05:44")
    comment30 = Comment(videoId=650, channelId=95, content="Everyone was curious about the large white blimp that appeared overnight.", createdAt="Tue Sep 07 2021 01:00:26", updatedAt="Wed Oct 20 2021 03:46:12")
    comment31 = Comment(videoId=59, channelId=85, content="Today arrived with a crash of my car through the garage door.", createdAt="Mon Nov 15 2021 22:20:56", updatedAt="Fri Oct 01 2021 02:41:12")
    comment32 = Comment(videoId=184, channelId=6, content="After coating myself in vegetable oil I found my success rate skyrocketed.", createdAt="Tue Nov 09 2021 05:01:25", updatedAt="Wed Dec 08 2021 09:54:17")
    comment33 = Comment(videoId=463, channelId=42, content="I know many children ask for a pony, but I wanted a bicycle with rockets strapped to it.", createdAt="Wed May 05 2021 02:20:30", updatedAt="Mon Jun 07 2021 17:23:25")
    comment34 = Comment(videoId=270, channelId=89, content="The balloons floated away along with all my hopes and dreams.", createdAt="Mon Dec 13 2021 14:22:52", updatedAt="Sat Dec 25 2021 22:02:03")
    comment35 = Comment(videoId=201, channelId=79, content="Patricia loves the sound of nails strongly pressed against the chalkboard.", createdAt="Tue Mar 01 2022 20:05:26", updatedAt="Sun Apr 18 2021 06:16:34")
    comment37 = Comment(videoId=390, channelId=23, content="The sign said there was road work ahead so he decided to speed up.", createdAt="Tue Apr 05 2022 20:01:13", updatedAt="Sat Nov 27 2021 14:05:33")
    comment38 = Comment(videoId=306, channelId=58, content="8% of 25 is the same as 25% of 8 and one of them is much easier to do in your head.", createdAt="Tue Apr 13 2021 05:28:50", updatedAt="Fri Aug 06 2021 08:48:54")
    comment39 = Comment(videoId=417, channelId=80, content="Pink horses galloped across the sea.", createdAt="Fri Mar 18 2022 20:26:34", updatedAt="Sat Jan 01 2022 22:21:28")
    comment40 = Comment(videoId=405, channelId=59, content="The waves were crashing on the shore; it was a lovely sight.", createdAt="Thu Jul 01 2021 18:30:05", updatedAt="Fri May 28 2021 05:47:51")
    comment41 = Comment(videoId=753, channelId=86, content="She learned that water bottles are no longer just to hold liquid, but they're also status symbols.", createdAt="Tue Sep 28 2021 11:25:10", updatedAt="Fri Jul 02 2021 13:00:59")
    comment42 = Comment(videoId=118, channelId=26, content="She did her best to help him.", createdAt="Sun Jun 20 2021 08:57:17", updatedAt="Wed Sep 08 2021 03:11:35")
    comment43 = Comment(videoId=474, channelId=12, content="He walked into the basement with the horror movie from the night before playing in his head.", createdAt="Mon Dec 20 2021 06:25:04", updatedAt="Thu Jul 08 2021 12:06:21")
    comment44 = Comment(videoId=351, channelId=27, content="She wore green lipstick like a fashion icon.", createdAt="Sat Jun 26 2021 22:32:00", updatedAt="Wed Dec 29 2021 04:49:19")
    comment45 = Comment(videoId=5, channelId=12, content="He colored deep space a soft yellow.", createdAt="Tue Dec 28 2021 14:23:21", updatedAt="Fri Jul 09 2021 10:11:47")
    comment46 = Comment(videoId=679, channelId=62, content="He poured rocks in the dungeon of his mind.", createdAt="Thu Nov 25 2021 03:51:46", updatedAt="Mon Aug 02 2021 10:39:39")
    comment47 = Comment(videoId=704, channelId=31, content="Mr. Montoya knows the way to the bakery even though he's never been there.", createdAt="Sat Jul 03 2021 09:33:21", updatedAt="Sun Oct 03 2021 21:13:04")
    comment48 = Comment(videoId=763, channelId=26, content="Gwen had her best sleep ever on her new bed of nails.", createdAt="Wed Oct 06 2021 23:55:45", updatedAt="Wed Dec 29 2021 19:21:43")
    comment49 = Comment(videoId=415, channelId=38, content="She had a habit of taking showers in lemonade.", createdAt="Mon Jan 03 2022 08:47:10", updatedAt="Wed Apr 14 2021 15:49:08")
    comment50 = Comment(videoId=772, channelId=50, content="He used to get confused between soldiers and shoulders, but as a military man, he now soldiers responsibility.", createdAt="Fri Jan 14 2022 03:24:31", updatedAt="Tue Nov 09 2021 14:17:33")
    comment51 = Comment(videoId=192, channelId=94, content="The group quickly understood that toxic waste was the most effective barrier to use against the zombies.", createdAt="Fri Nov 05 2021 02:40:53", updatedAt="Sat Sep 18 2021 10:42:56")
    comment52 = Comment(videoId=338, channelId=55, content="The chic gangster liked to start the day with a pink scarf.", createdAt="Tue Nov 09 2021 21:51:00", updatedAt="Mon Mar 07 2022 15:03:45")
    comment53 = Comment(videoId=450, channelId=30, content="The teens wondered what was kept in the red shed on the far edge of the school grounds.", createdAt="Wed Mar 16 2022 09:12:30", updatedAt="Mon Oct 11 2021 17:26:45")
    comment54 = Comment(videoId=300, channelId=22, content="He had decided to accept his fate of accepting his fate.", createdAt="Fri Jun 11 2021 07:07:38", updatedAt="Fri Mar 25 2022 11:14:06")
    comment55 = Comment(videoId=774, channelId=10, content="I caught my squirrel rustling through my gym bag.", createdAt="Tue Feb 01 2022 05:40:03", updatedAt="Sat Apr 24 2021 06:26:44")
    comment56 = Comment(videoId=292, channelId=12, content="He walked into the basement with the horror movie from the night before playing in his head.", createdAt="Wed Nov 10 2021 06:40:44", updatedAt="Sat Jul 10 2021 00:23:32")
    comment57 = Comment(videoId=148, channelId=89, content="The secret ingredient to his wonderful life was crime.", createdAt="Wed Feb 23 2022 15:57:15", updatedAt="Sat Sep 18 2021 23:30:05")
    comment58 = Comment(videoId=420, channelId=43, content="Honestly, I didn't care much for the first season, so I didn't bother with the second.", createdAt="Sun Apr 11 2021 12:50:37", updatedAt="Mon Jan 10 2022 05:48:50")
    comment59 = Comment(videoId=591, channelId=18, content="She moved forward only because she trusted that the ending she now was going through must be followed by a new beginning.", createdAt="Sat Jun 19 2021 03:59:14", updatedAt="Thu Jul 01 2021 13:18:03")
    comment60 = Comment(videoId=476, channelId=97, content="There's a message for you if you look up.", createdAt="Wed Sep 01 2021 09:43:48", updatedAt="Thu Sep 16 2021 07:05:57")
    comment61 = Comment(videoId=446, channelId=43, content="The paintbrush was angry at the color the artist chose to use.", createdAt="Thu Apr 07 2022 01:25:18", updatedAt="Sat Jun 12 2021 11:20:07")
    comment62 = Comment(videoId=162, channelId=75, content="Seek success, but always be prepared for random cats.", createdAt="Thu Oct 14 2021 03:03:22", updatedAt="Sat Jun 05 2021 14:01:18")
    comment63 = Comment(videoId=457, channelId=88, content="He uses onomatopoeia as a weapon of mental destruction.", createdAt="Tue May 25 2021 20:34:52", updatedAt="Mon Jul 12 2021 00:27:59")
    comment64 = Comment(videoId=365, channelId=52, content="I used to live in my neighbor's fishpond, but the aesthetic wasn't to my taste.", createdAt="Thu Mar 31 2022 05:44:16", updatedAt="Mon Jun 28 2021 11:24:47")
    comment65 = Comment(videoId=680, channelId=30, content="He was all business when he wore his clown suit.", createdAt="Wed Nov 17 2021 08:55:47", updatedAt="Mon May 24 2021 15:31:40")
    comment66 = Comment(videoId=759, channelId=30, content="If any cop asks you where you were, just say you were visiting Kansas.", createdAt="Mon Aug 16 2021 07:16:48", updatedAt="Wed Sep 01 2021 07:09:52")
    comment67 = Comment(videoId=231, channelId=49, content="The fact that there's a stairway to heaven and a highway to hell explains life well.", createdAt="Tue Sep 21 2021 17:06:05", updatedAt="Thu Jul 01 2021 17:51:26")
    comment68 = Comment(videoId=85, channelId=11, content="She couldn't understand why nobody else could see that the sky is full of cotton candy.", createdAt="Wed Jan 26 2022 02:56:04", updatedAt="Sun May 23 2021 05:23:49")
    comment69 = Comment(videoId=345, channelId=54, content="The fox in the tophat whispered into the ear of the rabbit.", createdAt="Sun Jul 18 2021 18:49:34", updatedAt="Fri Aug 20 2021 05:42:30")
    comment70 = Comment(videoId=287, channelId=63, content="She insisted that cleaning out your closet was the key to good driving.", createdAt="Fri Jan 21 2022 22:52:05", updatedAt="Wed Nov 24 2021 11:14:41")
    comment71 = Comment(videoId=659, channelId=70, content="The efficiency we have at removing trash has made creating trash more acceptable.", createdAt="Sun Dec 05 2021 14:17:39", updatedAt="Sun Mar 06 2022 02:48:41")
    comment72 = Comment(videoId=463, channelId=91, content="Everybody should read Chaucer to improve their everyday vocabulary.", createdAt="Sun May 30 2021 11:03:28", updatedAt="Wed Jun 30 2021 08:10:03")
    comment73 = Comment(videoId=637, channelId=93, content="The clock within this blog and the clock on my laptop are 1 hour different from each other.", createdAt="Wed Oct 13 2021 16:36:20", updatedAt="Sun Dec 05 2021 08:23:53")
    comment74 = Comment(videoId=10, channelId=29, content="I am happy to take your donation; any amount will be greatly appreciated.", createdAt="Mon Nov 22 2021 20:52:32", updatedAt="Mon Jun 07 2021 00:08:31")
    comment75 = Comment(videoId=242, channelId=64, content="The estate agent quickly marked out his territory on the dance floor.", createdAt="Tue Aug 24 2021 13:37:03", updatedAt="Tue Feb 08 2022 19:08:19")
    comment76 = Comment(videoId=516, channelId=99, content="Carol drank the blood as if she were a vampire.", createdAt="Tue Nov 09 2021 20:56:47", updatedAt="Tue Aug 10 2021 19:29:50")
    comment77 = Comment(videoId=512, channelId=7, content="Art doesn't have to be intentional.", createdAt="Sun Aug 15 2021 05:02:01", updatedAt="Sun Jan 23 2022 11:02:14")
    comment78 = Comment(videoId=533, channelId=9, content="The toy brought back fond memories of being lost in the rain forest.", createdAt="Thu Sep 02 2021 22:43:03", updatedAt="Sun Jan 02 2022 04:30:48")
    comment79 = Comment(videoId=201, channelId=35, content="The busker hoped that the people passing by would throw money, but they threw tomatoes instead, so he exchanged his hat for a juicer.", createdAt="Sat Nov 20 2021 04:23:38", updatedAt="Thu Mar 03 2022 19:00:01")
    comment80 = Comment(videoId=731, channelId=62, content="It was the best sandcastle he had ever seen.", createdAt="Thu Apr 07 2022 06:18:45", updatedAt="Wed Aug 25 2021 06:46:05")
    comment81 = Comment(videoId=516, channelId=8, content="Improve your goldfish's physical fitness by getting him a bicycle.", createdAt="Thu Apr 22 2021 22:57:36", updatedAt="Sun Feb 20 2022 16:10:11")
    comment82 = Comment(videoId=300, channelId=35, content="The family’s excitement over going to Disneyland was crazier than she anticipated.", createdAt="Thu Feb 24 2022 15:11:52", updatedAt="Sat Jul 17 2021 21:54:27")
    comment83 = Comment(videoId=550, channelId=3, content="Twin 4-month-olds slept in the shade of the palm tree while the mother tanned in the sun.", createdAt="Fri Oct 01 2021 14:43:19", updatedAt="Sun Jan 23 2022 08:37:12")
    comment84 = Comment(videoId=65, channelId=55, content="I ate a sock because people on the Internet told me to.", createdAt="Wed Nov 17 2021 14:27:18", updatedAt="Fri Feb 04 2022 23:38:51")
    comment85 = Comment(videoId=307, channelId=56, content="The tour bus was packed with teenage girls heading toward their next adventure.", createdAt="Sun Sep 12 2021 01:07:08", updatedAt="Sat Nov 13 2021 07:36:53")
    comment86 = Comment(videoId=670, channelId=75, content="Stop waiting for exceptional things to just happen.", createdAt="Sun Sep 12 2021 05:53:39", updatedAt="Sun Oct 10 2021 19:53:22")
    comment87 = Comment(videoId=752, channelId=38, content="Erin accidentally created a new universe.", createdAt="Tue Jun 22 2021 01:31:01", updatedAt="Sun Jan 23 2022 05:03:52")
    comment88 = Comment(videoId=74, channelId=70, content="My Mum tries to be cool by saying that she likes all the same things that I do.", createdAt="Sun Sep 19 2021 11:37:47", updatedAt="Fri May 21 2021 17:13:21")
    comment89 = Comment(videoId=466, channelId=61, content="She traveled because it cost the same as therapy and was a lot more enjoyable.", createdAt="Tue Jul 06 2021 23:43:43", updatedAt="Fri Jul 16 2021 23:05:38")
    comment90 = Comment(videoId=620, channelId=91, content="As the years pass by, we all know owners look more and more like their dogs.", createdAt="Fri Mar 18 2022 08:28:15", updatedAt="Fri Nov 19 2021 01:45:52")
    comment91 = Comment(videoId=70, channelId=96, content="The pet shop stocks everything you need to keep your anaconda happy.", createdAt="Thu Dec 16 2021 06:40:34", updatedAt="Sat Jun 05 2021 06:09:57")
    comment92 = Comment(videoId=750, channelId=52, content="The doll spun around in circles in hopes of coming alive.", createdAt="Wed Dec 01 2021 00:36:15", updatedAt="Mon Apr 19 2021 01:24:59")
    comment93 = Comment(videoId=32, channelId=74, content="Nobody loves a pig wearing lipstick.", createdAt="Sat Mar 19 2022 15:42:00", updatedAt="Sat Jan 15 2022 10:25:33")
    comment94 = Comment(videoId=493, channelId=43, content="The sunblock was handed to the girl before practice, but the burned skin was proof she did not apply it.", createdAt="Wed Jun 02 2021 06:45:42", updatedAt="Wed Oct 27 2021 06:14:15")
    comment95 = Comment(videoId=272, channelId=22, content="He stomped on his fruit loops and thus became a cereal killer.", createdAt="Sat Dec 25 2021 22:07:55", updatedAt="Sat Jun 26 2021 16:00:29")
    comment96 = Comment(videoId=20, channelId=17, content="Even though he thought the world was flat he didn’t see the irony of wanting to travel around the world.", createdAt="Mon Oct 04 2021 01:41:56", updatedAt="Thu Jan 06 2022 08:51:58")
    comment97 = Comment(videoId=691, channelId=12, content="The manager of the fruit stand always sat and only sold vegetables.", createdAt="Thu Jul 08 2021 14:04:05", updatedAt="Sat Dec 18 2021 21:35:38")
    comment98 = Comment(videoId=456, channelId=97, content="A kangaroo is really just a rabbit on steroids.", createdAt="Wed Jun 16 2021 13:17:21", updatedAt="Sat Nov 13 2021 13:26:36")
    comment99 = Comment(videoId=55, channelId=90, content="They're playing the piano while flying in the plane.", createdAt="Sun Aug 22 2021 20:36:42", updatedAt="Wed Sep 29 2021 16:38:41")
    comment100 = Comment(videoId=347, channelId=3, content="Today I dressed my unicorn in preparation for the race.", createdAt="Thu Jul 22 2021 23:43:58", updatedAt="Sun Dec 05 2021 09:40:21")
    comment101 = Comment(videoId=455, channelId=56, content="The llama couldn't resist trying the lemonade.", createdAt="Tue Jun 01 2021 18:50:01", updatedAt="Thu May 13 2021 20:50:40")
    comment102 = Comment(videoId=529, channelId=36, content="I'd always thought lightning was something only I could see.", createdAt="Wed Mar 02 2022 15:52:17", updatedAt="Wed Feb 23 2022 08:46:36")
    comment103 = Comment(videoId=200, channelId=51, content="She had a habit of taking showers in lemonade.", createdAt="Fri Apr 08 2022 08:42:17", updatedAt="Sat Aug 14 2021 10:48:10")
    comment104 = Comment(videoId=546, channelId=6, content="Separation anxiety is what happens when you can't find your phone.", createdAt="Sat Sep 18 2021 16:01:33", updatedAt="Sun Jan 09 2022 11:14:44")
    comment105 = Comment(videoId=92, channelId=41, content="I love eating toasted cheese and tuna sandwiches.", createdAt="Sat Jan 01 2022 07:03:14", updatedAt="Mon Jan 10 2022 06:47:51")
    comment106 = Comment(videoId=168, channelId=80, content="So long and thanks for the fish.", createdAt="Fri Apr 23 2021 16:03:51", updatedAt="Mon Dec 06 2021 04:32:32")
    comment107 = Comment(videoId=156, channelId=8, content="He was sitting in a trash can with high street class.", createdAt="Thu Dec 23 2021 08:37:59", updatedAt="Sun Apr 18 2021 15:33:19")
    comment108 = Comment(videoId=243, channelId=12, content="Despite multiple complications and her near-death experience", createdAt="Wed Jan 19 2022 23:08:03", updatedAt="Thu Sep 30 2021 01:42:32")
    comment109 = Comment(videoId=621, channelId=9, content="It isn't difficult to do a handstand if you just stand on your hands.", createdAt="Thu Feb 17 2022 00:39:12", updatedAt="Tue Sep 14 2021 15:56:51")
    comment110 = Comment(videoId=147, channelId=97, content="The old apple revels in its authority.", createdAt="Tue Mar 22 2022 03:07:49", updatedAt="Thu Jul 29 2021 05:08:27")
    comment111 = Comment(videoId=521, channelId=80, content="The minute she landed she understood the reason this was a fly-over state.", createdAt="Wed Oct 20 2021 17:47:25", updatedAt="Sun Mar 06 2022 16:36:37")
    comment112 = Comment(videoId=507, channelId=2, content="You've been eyeing me all day and waiting for your move like a lion stalking a gazelle in a savannah.", createdAt="Wed Jan 26 2022 21:43:46", updatedAt="Sat Oct 09 2021 05:07:58")
    comment113 = Comment(videoId=724, channelId=94, content="Blue sounded too cold at the time and yet it seemed to work for gin.", createdAt="Mon May 10 2021 02:57:50", updatedAt="Sat Aug 28 2021 04:13:18")
    comment114 = Comment(videoId=644, channelId=89, content="Whenever he saw a red flag warning at the beach he grabbed his surfboard.", createdAt="Fri Dec 10 2021 12:41:54", updatedAt="Sun Aug 29 2021 09:16:41")
    comment115 = Comment(videoId=199, channelId=79, content="He said he was not there yesterday; however, many people saw him there.", createdAt="Thu Jul 01 2021 20:29:27", updatedAt="Sun Oct 24 2021 00:34:38")
    comment116 = Comment(videoId=197, channelId=57, content="Baby wipes are made of chocolate stardust.", createdAt="Thu Oct 28 2021 07:01:41", updatedAt="Thu Jul 08 2021 20:20:12")
    comment117 = Comment(videoId=474, channelId=45, content="Beach-combing replaced wine tasting as his new obsession.", createdAt="Sun May 16 2021 22:40:48", updatedAt="Sun Jan 23 2022 05:35:31")
    comment118 = Comment(videoId=278, channelId=30, content="The teenage boy was accused of breaking his arm simply to get out of the test.", createdAt="Tue Mar 01 2022 06:04:40", updatedAt="Wed Nov 24 2021 12:06:57")
    comment119 = Comment(videoId=196, channelId=41, content="She was too short to see over the fence.", createdAt="Thu Aug 12 2021 08:02:37", updatedAt="Wed Apr 14 2021 09:47:04")
    comment120 = Comment(videoId=501, channelId=93, content="The golden retriever loved the fireworks each Fourth of July.", createdAt="Fri Apr 08 2022 20:58:51", updatedAt="Sat May 08 2021 07:25:04")
    comment121 = Comment(videoId=737, channelId=76, content="A kangaroo is really just a rabbit on steroids.", createdAt="Wed Dec 01 2021 01:18:20", updatedAt="Sun Mar 20 2022 14:50:14")
    comment122 = Comment(videoId=82, channelId=31, content="At that moment I was the most fearsome weasel in the entire swamp.", createdAt="Wed Sep 08 2021 00:42:57", updatedAt="Thu Sep 30 2021 12:08:22")
    comment123 = Comment(videoId=30, channelId=87, content="In that instant, everything changed.", createdAt="Fri May 21 2021 04:03:28", updatedAt="Sun Apr 03 2022 17:27:35")
    comment124 = Comment(videoId=269, channelId=69, content="The stranger officiates the meal.", createdAt="Tue Aug 31 2021 11:45:35", updatedAt="Thu Sep 30 2021 12:29:06")
    comment125 = Comment(videoId=49, channelId=93, content="Being unacquainted with the chief raccoon was harming his prospects for promotion.", createdAt="Tue Jun 08 2021 23:45:28", updatedAt="Sat May 08 2021 15:29:19")
    comment126 = Comment(videoId=751, channelId=72, content="The most exciting eureka moment I've had was when I realized that the instructions on food packets were just guidelines.", createdAt="Sun Mar 20 2022 04:07:31", updatedAt="Fri Sep 03 2021 14:19:16")
    comment127 = Comment(videoId=513, channelId=95, content="The small white buoys marked the location of hundreds of crab pots.", createdAt="Mon Oct 04 2021 03:29:53", updatedAt="Sat Nov 20 2021 07:07:33")
    comment128 = Comment(videoId=79, channelId=30, content="She only paints with bold colors; she does not like pastels.", createdAt="Sun Sep 26 2021 00:58:40", updatedAt="Tue Nov 16 2021 06:38:06")
    comment129 = Comment(videoId=120, channelId=88, content="He was sure the Devil created red sparkly glitter.", createdAt="Wed Jul 21 2021 03:07:22", updatedAt="Sat Apr 09 2022 22:13:24")
    comment130 = Comment(videoId=141, channelId=15, content="The wake behind the boat told of the past while the open sea for told life in the unknown future.", createdAt="Wed Jun 30 2021 18:55:21", updatedAt="Mon Aug 09 2021 08:15:12")
    comment131 = Comment(videoId=442, channelId=88, content="Pink horses galloped across the sea.", createdAt="Thu Jun 24 2021 04:59:10", updatedAt="Thu Sep 16 2021 09:45:25")
    comment132 = Comment(videoId=405, channelId=46, content="She had that tint of craziness in her soul that made her believe she could actually make a difference.", createdAt="Tue Feb 15 2022 15:53:50", updatedAt="Sun Sep 05 2021 08:14:29")
    comment133 = Comment(videoId=732, channelId=83, content="There was coal in his stocking and he was thrilled.", createdAt="Fri Sep 03 2021 02:30:00", updatedAt="Sat Sep 25 2021 02:44:20")
    comment134 = Comment(videoId=176, channelId=79, content="He fumbled in the darkness looking for the light switch, but when he finally found it there was someone already there.", createdAt="Fri Feb 11 2022 14:15:35", updatedAt="Sat Jul 10 2021 12:37:30")
    comment135 = Comment(videoId=490, channelId=84, content="He learned the hardest lesson of his life and had the scars, both physical and mental, to prove it.", createdAt="Wed Feb 23 2022 01:39:25", updatedAt="Sat May 15 2021 16:14:11")
    comment136 = Comment(videoId=81, channelId=41, content="Gary didn't understand why Doug went upstairs to get one dollar bills when he invited him to go cow tipping.", createdAt="Tue Nov 30 2021 20:44:33", updatedAt="Sat Apr 09 2022 18:04:52")
    comment137 = Comment(videoId=710, channelId=81, content="I’m working on a sweet potato farm.", createdAt="Thu Nov 25 2021 23:55:59", updatedAt="Thu Dec 09 2021 23:44:52")
    comment138 = Comment(videoId=77, channelId=98, content="If any cop asks you where you were, just say you were visiting Kansas.", createdAt="Fri Apr 23 2021 03:48:34", updatedAt="Thu Aug 05 2021 19:44:03")
    comment139 = Comment(videoId=638, channelId=33, content="Nobody loves a pig wearing lipstick.", createdAt="Tue Jun 29 2021 22:16:54", updatedAt="Tue May 04 2021 15:12:38")
    comment140 = Comment(videoId=309, channelId=100, content="As he entered the church he could hear the soft voice of someone whispering into a cell phone.", createdAt="Thu Sep 09 2021 01:27:35", updatedAt="Mon Jun 07 2021 01:11:23")
    comment141 = Comment(videoId=416, channelId=52, content="The blue parrot drove by the hitchhiking mongoose.", createdAt="Tue Jul 06 2021 20:03:53", updatedAt="Mon Mar 21 2022 02:19:20")
    comment142 = Comment(videoId=516, channelId=45, content="It didn't make sense unless you had the power to eat colors.", createdAt="Sat Dec 04 2021 21:31:32", updatedAt="Fri Dec 17 2021 02:39:01")
    comment143 = Comment(videoId=761, channelId=22, content="The Tsunami wave crashed against the raised houses and broke the pilings as if they were toothpicks.", createdAt="Tue Jul 13 2021 06:43:06", updatedAt="Mon Feb 07 2022 23:04:37")
    comment144 = Comment(videoId=419, channelId=87, content="The random sentence generator generated a random sentence about a random sentence.", createdAt="Mon Sep 27 2021 02:22:18", updatedAt="Sun Feb 20 2022 14:50:11")
    comment145 = Comment(videoId=39, channelId=11, content="He went back to the video to see what had been recorded and was shocked at what he saw.", createdAt="Sat Jan 22 2022 03:50:49", updatedAt="Thu Dec 16 2021 17:23:30")
    comment146 = Comment(videoId=159, channelId=7, content="Please wait outside of the house.", createdAt="Thu Jul 15 2021 05:38:31", updatedAt="Wed Sep 29 2021 01:12:43")
    comment147 = Comment(videoId=536, channelId=27, content="I only enjoy window shopping when the windows are transparent.", createdAt="Thu Jun 17 2021 01:40:24", updatedAt="Tue Oct 19 2021 09:07:52")
    comment149 = Comment(videoId=475, channelId=90, content="Flash photography is best used in full sunlight.", createdAt="Mon Mar 07 2022 13:41:04", updatedAt="Mon Jan 31 2022 15:36:36")
    comment150 = Comment(videoId=670, channelId=61, content="The truth is that you pay for your lifestyle in hours.", createdAt="Fri Jan 28 2022 09:30:18", updatedAt="Thu May 27 2021 02:23:33")
    comment151 = Comment(videoId=351, channelId=57, content="Let me help you with your baggage.", createdAt="Fri Dec 17 2021 15:11:39", updatedAt="Mon Jun 21 2021 12:26:32")
    comment152 = Comment(videoId=556, channelId=30, content="Trash covered the landscape like sprinkles do a birthday cake.", createdAt="Tue Mar 29 2022 15:57:53", updatedAt="Mon Nov 29 2021 17:36:21")
    comment153 = Comment(videoId=283, channelId=69, content="I was offended by the suggestion that my baby brother was a jewel thief.", createdAt="Thu May 13 2021 06:40:33", updatedAt="Fri Nov 26 2021 11:58:50")
    comment154 = Comment(videoId=93, channelId=30, content="Patricia found the meaning of life in a bowl of Cheerios.", createdAt="Fri Sep 10 2021 10:44:24", updatedAt="Fri Feb 04 2022 00:16:22")
    comment155 = Comment(videoId=281, channelId=52, content="I always dreamed about being stranded on a desert island until it actually happened.", createdAt="Mon Mar 14 2022 06:11:57", updatedAt="Fri Apr 08 2022 23:19:01")
    comment156 = Comment(videoId=505, channelId=25, content="Normal activities took extraordinary amounts of concentration at the high altitude.", createdAt="Tue Aug 03 2021 07:54:44", updatedAt="Sat Jun 12 2021 23:00:31")
    comment157 = Comment(videoId=627, channelId=54, content="I'm confused: when people ask me what's up, and I point, they groan.", createdAt="Fri Jul 09 2021 15:18:48", updatedAt="Fri Oct 08 2021 22:06:20")
    comment158 = Comment(videoId=594, channelId=50, content="He didn't heed the warning and it had turned out surprisingly well.", createdAt="Sun Sep 26 2021 23:30:08", updatedAt="Mon Dec 13 2021 16:12:10")
    comment160 = Comment(videoId=156, channelId=63, content="100 years old is such a young age if you happen to be a bristlecone pine.", createdAt="Thu Aug 19 2021 01:37:35", updatedAt="Fri Apr 08 2022 14:46:59")
    comment161 = Comment(videoId=633, channelId=68, content="The sudden rainstorm washed crocodiles into the ocean.", createdAt="Thu Jan 27 2022 15:16:41", updatedAt="Fri Apr 01 2022 18:59:49")
    comment162 = Comment(videoId=650, channelId=71, content="She felt that chill that makes the hairs on the back of your neck when he walked into the room.", createdAt="Sun Apr 25 2021 10:13:37", updatedAt="Wed Jun 02 2021 21:05:00")
    comment163 = Comment(videoId=347, channelId=37, content="The body piercing didn't go exactly as he expected.", createdAt="Wed Dec 15 2021 15:37:59", updatedAt="Fri Nov 12 2021 08:34:42")
    comment164 = Comment(videoId=506, channelId=38, content="I want more detailed information.", createdAt="Sat Aug 07 2021 18:28:29", updatedAt="Sat May 22 2021 18:03:59")
    comment165 = Comment(videoId=698, channelId=91, content="The secret code they created made no sense, even to them.", createdAt="Sat Oct 02 2021 16:21:52", updatedAt="Sat Dec 11 2021 00:21:10")
    comment166 = Comment(videoId=15, channelId=86, content="Gary didn't understand why Doug went upstairs to get one dollar bills when he invited him to go cow tipping.", createdAt="Tue Aug 03 2021 20:47:08", updatedAt="Sat Oct 02 2021 19:25:08")
    comment167 = Comment(videoId=778, channelId=25, content="Purple is the best city in the forest.", createdAt="Tue Oct 19 2021 14:09:32", updatedAt="Wed Sep 15 2021 04:37:47")
    comment168 = Comment(videoId=731, channelId=41, content="He had a hidden stash underneath the floorboards in the back room of the house.", createdAt="Sat Feb 05 2022 16:38:53", updatedAt="Mon May 17 2021 16:00:36")
    comment169 = Comment(videoId=281, channelId=53, content="She wasn't sure whether to be impressed or concerned that he folded underwear in neat little packages.", createdAt="Fri Jan 28 2022 03:27:42", updatedAt="Tue May 11 2021 01:02:59")
    comment170 = Comment(videoId=517, channelId=43, content="The tree fell unexpectedly short.", createdAt="Tue Mar 22 2022 11:46:24", updatedAt="Sun Mar 20 2022 14:43:54")
    comment171 = Comment(videoId=83, channelId=79, content="Lightning Paradise was the local hangout joint where the group usually ended up spending the night.", createdAt="Wed Sep 29 2021 14:18:13", updatedAt="Tue Nov 30 2021 22:05:12")
    comment172 = Comment(videoId=761, channelId=6, content="After fighting off the alligator, Brian still had to face the anaconda.", createdAt="Fri Jul 16 2021 02:25:01", updatedAt="Thu Nov 11 2021 18:46:32")
    comment173 = Comment(videoId=62, channelId=2, content="He was sitting in a trash can with high street class.", createdAt="Wed Jun 23 2021 17:42:32", updatedAt="Fri Jan 28 2022 22:56:21")
    comment174 = Comment(videoId=545, channelId=1, content="The delicious aroma from the kitchen was ruined by cigarette smoke.", createdAt="Sun Dec 26 2021 11:40:59", updatedAt="Tue Nov 16 2021 15:31:29")
    comment175 = Comment(videoId=668, channelId=13, content="I'd rather be a bird than a fish.", createdAt="Sun Sep 19 2021 09:09:15", updatedAt="Mon Aug 23 2021 00:16:39")
    comment176 = Comment(videoId=167, channelId=81, content="I had a friend in high school named Rick Shaw, but he was fairly useless as a mode of transport.", createdAt="Tue Jul 06 2021 18:28:57", updatedAt="Wed Jun 23 2021 11:52:30")
    comment177 = Comment(videoId=196, channelId=54, content="The water flowing down the river didn’t look that powerful from the car", createdAt="Tue May 25 2021 01:42:25", updatedAt="Sat Dec 25 2021 09:25:24")
    comment178 = Comment(videoId=261, channelId=29, content="He walked into the basement with the horror movie from the night before playing in his head.", createdAt="Mon Jan 10 2022 22:52:24", updatedAt="Thu Jul 22 2021 09:22:46")
    comment179 = Comment(videoId=505, channelId=84, content="Jason lived his life by the motto, \"Anything worth doing is worth doing poorly.", createdAt="Sun Jan 23 2022 16:16:49", updatedAt="Fri Sep 24 2021 04:50:17")
    comment180 = Comment(videoId=210, channelId=10, content="Today I heard something new and unmemorable.", createdAt="Thu Jul 01 2021 18:34:03", updatedAt="Tue Jul 06 2021 00:57:08")
    comment181 = Comment(videoId=732, channelId=30, content="Her hair was windswept as she rode in the black convertible.", createdAt="Sat Jan 08 2022 08:22:00", updatedAt="Tue Mar 29 2022 06:21:15")
    comment182 = Comment(videoId=610, channelId=96, content="She borrowed the book from him many years ago and hasn't yet returned it.", createdAt="Sun Aug 22 2021 15:00:12", updatedAt="Mon Nov 01 2021 15:07:04")
    comment183 = Comment(videoId=518, channelId=55, content="There are few things better in life than a slice of pie.", createdAt="Thu Oct 28 2021 08:57:03", updatedAt="Mon Aug 16 2021 15:46:48")
    comment184 = Comment(videoId=103, channelId=91, content="It was a slippery slope and he was willing to slide all the way to the deepest depths.", createdAt="Sat May 15 2021 01:47:22", updatedAt="Wed Jun 02 2021 16:01:05")
    comment185 = Comment(videoId=33, channelId=25, content="The trick to getting kids to eat anything is to put catchup on it.", createdAt="Tue Jan 25 2022 19:24:42", updatedAt="Sat Dec 11 2021 18:35:33")
    comment186 = Comment(videoId=670, channelId=3, content="When he asked her favorite number, she answered without hesitation that it was diamonds.", createdAt="Fri Jan 14 2022 06:22:01", updatedAt="Thu May 27 2021 14:01:06")
    comment187 = Comment(videoId=429, channelId=96, content="Please wait outside of the house.", createdAt="Sat Sep 25 2021 14:26:50", updatedAt="Sun Apr 03 2022 12:43:50")
    comment188 = Comment(videoId=596, channelId=11, content="As time wore on, simple dog commands turned into full paragraphs explaining why the dog couldn’t do something.", createdAt="Wed Oct 20 2021 18:54:28", updatedAt="Tue Nov 16 2021 05:48:27")
    comment189 = Comment(videoId=550, channelId=89, content="It turns out you don't need all that stuff you insisted you did.", createdAt="Sun Oct 31 2021 04:21:21", updatedAt="Wed Dec 15 2021 21:54:49")
    comment190 = Comment(videoId=552, channelId=2, content="I like to leave work after my eight-hour tea-break.", createdAt="Sat Jan 29 2022 15:00:51", updatedAt="Wed Apr 21 2021 10:29:58")
    comment191 = Comment(videoId=681, channelId=83, content="Toddlers feeding raccoons surprised even the seasoned park ranger.", createdAt="Sun Dec 12 2021 07:24:24", updatedAt="Thu Jul 29 2021 12:58:24")
    comment192 = Comment(videoId=85, channelId=5, content="Honestly, I didn't care much for the first season, so I didn't bother with the second.", createdAt="Wed Sep 15 2021 01:38:20", updatedAt="Sun Sep 05 2021 01:04:45")
    comment193 = Comment(videoId=296, channelId=33, content="Check back tomorrow; I will see if the book has arrived.", createdAt="Thu Apr 07 2022 11:55:01", updatedAt="Sat Nov 13 2021 23:36:12")
    comment194 = Comment(videoId=16, channelId=86, content="It doesn't sound like that will ever be on my travel list.", createdAt="Mon Oct 04 2021 21:55:29", updatedAt="Sun Sep 19 2021 19:04:15")
    comment195 = Comment(videoId=348, channelId=94, content="He was the type of guy who liked Christmas lights on his house in the middle of July.", createdAt="Fri Apr 08 2022 02:22:45", updatedAt="Tue Mar 15 2022 19:52:38")
    comment196 = Comment(videoId=281, channelId=97, content="Imagine his surprise when he discovered that the safe was full of pudding.", createdAt="Mon Nov 01 2021 04:26:31", updatedAt="Fri Dec 17 2021 19:15:18")
    comment197 = Comment(videoId=270, channelId=15, content="Everyone says they love nature until they realize how dangerous she can be.", createdAt="Wed Mar 23 2022 09:26:54", updatedAt="Sun Oct 10 2021 00:09:59")
    comment198 = Comment(videoId=749, channelId=72, content="The light in his life was actually a fire burning all around him.", createdAt="Sat Mar 19 2022 01:10:03", updatedAt="Sat Apr 17 2021 13:26:42")
    comment199 = Comment(videoId=458, channelId=51, content="Getting up at dawn is for the birds.", createdAt="Fri Aug 13 2021 11:43:02", updatedAt="Fri Jan 07 2022 14:24:38")
    comment200 = Comment(videoId=251, channelId=67, content="It's never been my responsibility to glaze the donuts.", createdAt="Mon May 03 2021 18:11:31", updatedAt="Thu May 06 2021 12:11:54")
    comment201 = Comment(videoId=379, channelId=27, content="Excitement replaced fear until the final moment.", createdAt="Thu Aug 19 2021 08:20:11", updatedAt="Tue Mar 22 2022 01:51:12")
    comment202 = Comment(videoId=198, channelId=3, content="They say that dogs are man's best friend, but this cat was setting out to sabotage that theory.", createdAt="Fri May 07 2021 13:29:52", updatedAt="Wed Sep 15 2021 22:30:59")
    comment203 = Comment(videoId=417, channelId=39, content="Jim liked driving around town with his hazard lights on.", createdAt="Tue Apr 13 2021 00:37:33", updatedAt="Sat Mar 12 2022 19:40:07")
    comment204 = Comment(videoId=336, channelId=48, content="He loved eating his bananas in hot dog buns.", createdAt="Sun Jul 04 2021 20:30:55", updatedAt="Thu Nov 18 2021 16:24:42")
    comment205 = Comment(videoId=28, channelId=16, content="I cheated while playing the darts tournament by using a longbow.", createdAt="Tue May 25 2021 06:19:44", updatedAt="Thu Aug 05 2021 17:04:24")
    comment206 = Comment(videoId=726, channelId=22, content="Homesickness became contagious in the young campers' cabin.", createdAt="Mon Oct 18 2021 03:55:41", updatedAt="Thu Aug 12 2021 16:38:14")
    comment207 = Comment(videoId=679, channelId=2, content="Behind the window was a reflection that only instilled fear.", createdAt="Fri Nov 19 2021 13:25:56", updatedAt="Sun Sep 26 2021 03:03:18")
    comment208 = Comment(videoId=531, channelId=23, content="Strawberries must be the one food that doesn't go well with this brand of paint.", createdAt="Fri Sep 24 2021 10:31:14", updatedAt="Sat May 22 2021 15:35:19")
    comment209 = Comment(videoId=416, channelId=16, content="He didn't heed the warning and it had turned out surprisingly well.", createdAt="Wed May 26 2021 05:16:33", updatedAt="Tue May 25 2021 17:39:40")
    comment210 = Comment(videoId=610, channelId=27, content="She traveled because it cost the same as therapy and was a lot more enjoyable.", createdAt="Thu Jun 17 2021 00:42:30", updatedAt="Sat Dec 11 2021 14:39:00")
    comment211 = Comment(videoId=566, channelId=99, content="The minute she landed she understood the reason this was a fly-over state.", createdAt="Wed Jun 02 2021 10:43:23", updatedAt="Sun Dec 26 2021 21:16:27")
    comment212 = Comment(videoId=473, channelId=49, content="Her scream silenced the rowdy teenagers.", createdAt="Mon Jan 17 2022 19:12:18", updatedAt="Fri Jan 14 2022 02:59:44")
    comment213 = Comment(videoId=534, channelId=53, content="A purple pig and a green donkey flew a kite in the middle of the night and ended up sunburnt.", createdAt="Tue Jun 15 2021 22:31:22", updatedAt="Thu Feb 17 2022 11:58:49")
    comment214 = Comment(videoId=639, channelId=44, content="It didn't make sense unless you had the power to eat colors.", createdAt="Tue Sep 14 2021 11:02:43", updatedAt="Sat Feb 19 2022 10:44:37")
    comment215 = Comment(videoId=188, channelId=69, content="He poured rocks in the dungeon of his mind.", createdAt="Wed Nov 24 2021 17:19:55", updatedAt="Tue Nov 09 2021 10:48:40")
    comment216 = Comment(videoId=189, channelId=84, content="Nothing is as cautiously cuddly as a pet porcupine.", createdAt="Fri Oct 01 2021 16:59:31", updatedAt="Thu Apr 07 2022 13:31:54")
    comment217 = Comment(videoId=129, channelId=16, content="The truth is that you pay for your lifestyle in hours.", createdAt="Wed Apr 06 2022 03:15:22", updatedAt="Sat Jan 22 2022 16:02:17")
    comment218 = Comment(videoId=120, channelId=35, content="You're unsure whether or not to trust him, but very thankful that you wore a turtle neck.", createdAt="Thu Nov 18 2021 02:07:45", updatedAt="Sat Jun 05 2021 00:55:55")
    comment219 = Comment(videoId=647, channelId=13, content="They did nothing as the raccoon attacked the lady’s bag of food.", createdAt="Thu Nov 04 2021 10:01:09", updatedAt="Fri Jan 14 2022 05:59:05")
    comment220 = Comment(videoId=339, channelId=8, content="It's much more difficult to play tennis with a bowling ball than it is to bowl with a tennis ball.", createdAt="Thu Nov 18 2021 22:30:15", updatedAt="Fri Nov 19 2021 21:59:28")
    comment222 = Comment(videoId=408, channelId=34, content="He fumbled in the darkness looking for the light switch, but when he finally found it there was someone already there.", createdAt="Thu Oct 21 2021 08:22:44", updatedAt="Wed Mar 16 2022 23:39:12")
    comment223 = Comment(videoId=182, channelId=9, content="Hang on, my kittens are scratching at the bathtub and they'll upset by the lack of biscuits.", createdAt="Thu May 06 2021 19:16:42", updatedAt="Fri Mar 11 2022 10:49:50")
    comment224 = Comment(videoId=91, channelId=89, content="There was coal in his stocking and he was thrilled.", createdAt="Sat Jul 24 2021 10:10:10", updatedAt="Tue Dec 28 2021 00:45:08")
    comment225 = Comment(videoId=205, channelId=71, content="He was disappointed when he found the beach to be so sandy and the sun so sunny.", createdAt="Wed Jan 19 2022 10:18:39", updatedAt="Thu Jun 10 2021 12:43:02")
    comment226 = Comment(videoId=165, channelId=59, content="The ice-cream trucks bring back bad memories for all of us.", createdAt="Mon Aug 30 2021 06:32:25", updatedAt="Thu Mar 10 2022 21:03:30")
    comment227 = Comment(videoId=696, channelId=34, content="The Tsunami wave crashed against the raised houses and broke the pilings as if they were toothpicks.", createdAt="Thu Jan 06 2022 00:13:25", updatedAt="Thu Dec 16 2021 16:02:58")
    comment228 = Comment(videoId=383, channelId=46, content="When she didn’t like a guy who was trying to pick her up, she started using sign language.", createdAt="Sat Oct 23 2021 15:36:25", updatedAt="Sun Mar 13 2022 18:39:24")
    comment229 = Comment(videoId=617, channelId=18, content="Her daily goal was to improve on yesterday.", createdAt="Wed Dec 08 2021 23:28:16", updatedAt="Sun Mar 13 2022 19:16:20")
    comment230 = Comment(videoId=226, channelId=100, content="I would be delighted if the sea were full of cucumber juice.", createdAt="Thu Sep 16 2021 23:16:27", updatedAt="Wed Jan 12 2022 14:09:06")
    comment231 = Comment(videoId=489, channelId=19, content="He picked up trash in his spare time to dump in his neighbor's yard.", createdAt="Sun Aug 29 2021 06:01:36", updatedAt="Thu Jun 03 2021 04:05:09")
    comment232 = Comment(videoId=692, channelId=51, content="Their argument could be heard across the parking lot.", createdAt="Tue Feb 22 2022 07:44:15", updatedAt="Sat Nov 20 2021 08:44:48")
    comment233 = Comment(videoId=482, channelId=49, content="It was at that moment that he learned there are certain parts of the body that you should never Nair.", createdAt="Sat Jul 24 2021 01:13:46", updatedAt="Wed Feb 02 2022 07:39:28")
    comment234 = Comment(videoId=372, channelId=38, content="Abstraction is often one floor above you.", createdAt="Sun Aug 01 2021 19:03:00", updatedAt="Tue Apr 05 2022 13:40:38")
    comment235 = Comment(videoId=304, channelId=75, content="Written warnings in instruction manuals are worthless since rabbits can't read.", createdAt="Tue Mar 08 2022 04:04:20", updatedAt="Sun Dec 12 2021 06:28:58")
    comment236 = Comment(videoId=12, channelId=98, content="The tortoise jumped into the lake with dreams of becoming a sea turtle.", createdAt="Fri Feb 04 2022 07:22:41", updatedAt="Fri Feb 18 2022 22:47:44")
    comment237 = Comment(videoId=184, channelId=62, content="Despite what your teacher may have told you, there is a wrong way to wield a lasso.", createdAt="Wed Mar 23 2022 21:37:03", updatedAt="Wed Jan 19 2022 19:10:25")
    comment238 = Comment(videoId=724, channelId=52, content="Pink horses galloped across the sea.", createdAt="Fri Jan 07 2022 21:43:14", updatedAt="Sun Sep 19 2021 10:03:41")
    comment239 = Comment(videoId=17, channelId=77, content="It's not often you find a soggy banana on the street.", createdAt="Tue Apr 05 2022 04:45:29", updatedAt="Sun Aug 29 2021 19:46:57")
    comment240 = Comment(videoId=195, channelId=29, content="She says she has the ability to hear the soundtrack of your life.", createdAt="Tue Aug 24 2021 09:50:05", updatedAt="Mon Feb 21 2022 22:12:46")
    comment241 = Comment(videoId=720, channelId=51, content="They desperately needed another drummer since the current one only knew how to play bongos.", createdAt="Sat Apr 09 2022 05:09:43", updatedAt="Mon Nov 22 2021 19:20:45")
    comment242 = Comment(videoId=213, channelId=91, content="It was a really good Monday for being a Saturday.", createdAt="Mon Jan 03 2022 06:12:45", updatedAt="Mon Sep 27 2021 04:26:10")
    comment243 = Comment(videoId=460, channelId=30, content="The thick foliage and intertwined vines made the hike nearly impossible.", createdAt="Sat Mar 05 2022 18:38:26", updatedAt="Sun Aug 08 2021 02:50:59")
    comment244 = Comment(videoId=487, channelId=90, content="Let me help you with your baggage.", createdAt="Wed May 05 2021 13:46:05", updatedAt="Wed Aug 04 2021 17:17:16")
    comment245 = Comment(videoId=29, channelId=86, content="Lets all be unique together until we realise we are all the same.", createdAt="Sat May 08 2021 00:50:45", updatedAt="Fri Dec 31 2021 02:08:45")
    comment246 = Comment(videoId=408, channelId=38, content="The sky is clear; the stars are twinkling.", createdAt="Fri Nov 05 2021 03:46:31", updatedAt="Sun Apr 18 2021 21:04:28")
    comment247 = Comment(videoId=529, channelId=81, content="The sign said there was road work ahead so he decided to speed up.", createdAt="Tue Jan 18 2022 13:25:11", updatedAt="Fri May 28 2021 05:08:41")
    comment248 = Comment(videoId=235, channelId=87, content="I caught my squirrel rustling through my gym bag.", createdAt="Sat Feb 26 2022 00:15:24", updatedAt="Fri Jun 18 2021 03:44:07")
    comment249 = Comment(videoId=767, channelId=7, content="They finished building the road they knew no one would ever use.", createdAt="Fri Aug 27 2021 07:23:54", updatedAt="Tue Jan 11 2022 01:16:48")
    comment250 = Comment(videoId=174, channelId=5, content="The tumbleweed refused to tumble but was more than willing to prance.", createdAt="Fri Jul 02 2021 03:21:19", updatedAt="Sun Sep 19 2021 15:43:40")
    comment251 = Comment(videoId=74, channelId=22, content="She had a habit of taking showers in lemonade.", createdAt="Thu Aug 26 2021 00:19:39", updatedAt="Thu Apr 15 2021 00:37:06")
    comment252 = Comment(videoId=84, channelId=51, content="This is the last random sentence I will be writing and I am going to stop mid-sent", createdAt="Mon Jan 03 2022 21:53:48", updatedAt="Mon Jul 26 2021 02:07:34")
    comment253 = Comment(videoId=567, channelId=42, content="She can live her life however she wants as long as she listens to what I have to say.", createdAt="Thu Oct 07 2021 07:50:50", updatedAt="Thu Jan 20 2022 03:07:00")
    comment254 = Comment(videoId=219, channelId=67, content="My Mum tries to be cool by saying that she likes all the same things that I do.", createdAt="Fri Nov 05 2021 15:31:18", updatedAt="Fri May 07 2021 03:35:39")
    comment255 = Comment(videoId=43, channelId=48, content="Improve your goldfish's physical fitness by getting him a bicycle.", createdAt="Wed Jun 02 2021 06:44:56", updatedAt="Sat May 01 2021 23:38:46")
    comment256 = Comment(videoId=195, channelId=67, content="They called out her name time and again, but were met with nothing but silence.", createdAt="Sat May 01 2021 14:44:35", updatedAt="Sun Dec 26 2021 04:18:32")
    comment257 = Comment(videoId=709, channelId=92, content="We need to rent a room for our party.", createdAt="Mon Feb 28 2022 17:39:57", updatedAt="Fri Jun 11 2021 09:56:37")
    comment258 = Comment(videoId=224, channelId=31, content="Buried deep in the snow, he hoped his batteries were fresh in his avalanche beacon.", createdAt="Tue Aug 03 2021 03:41:35", updatedAt="Sun Mar 06 2022 19:27:06")
    comment259 = Comment(videoId=560, channelId=38, content="She wore green lipstick like a fashion icon.", createdAt="Thu Apr 15 2021 23:06:49", updatedAt="Wed Jul 14 2021 17:32:19")
    comment260 = Comment(videoId=21, channelId=24, content="When I cook spaghetti, I like to boil it a few minutes past al dente so the noodles are super slippery.", createdAt="Thu Mar 24 2022 07:33:37", updatedAt="Wed Dec 29 2021 01:00:43")
    comment261 = Comment(videoId=316, channelId=98, content="Strawberries must be the one food that doesn't go well with this brand of paint.", createdAt="Fri Feb 11 2022 02:13:00", updatedAt="Sat May 22 2021 18:04:32")
    comment262 = Comment(videoId=469, channelId=64, content="The Japanese yen for commerce is still well-known.", createdAt="Mon Aug 23 2021 19:42:40", updatedAt="Tue Mar 22 2022 23:46:52")
    comment263 = Comment(videoId=744, channelId=60, content="Everyone pretends to like wheat until you mention barley.", createdAt="Mon Nov 29 2021 02:57:50", updatedAt="Thu Jul 01 2021 06:14:01")
    comment264 = Comment(videoId=210, channelId=3, content="He is good at eating pickles and telling women about his emotional problems.", createdAt="Mon Oct 11 2021 01:28:16", updatedAt="Tue Jan 18 2022 08:16:31")
    comment265 = Comment(videoId=20, channelId=91, content="He was the only member of the club who didn't like plum pudding.", createdAt="Sat Sep 25 2021 11:11:06", updatedAt="Thu Nov 18 2021 09:04:55")
    comment266 = Comment(videoId=394, channelId=34, content="The pigs were insulted that they were named hamburgers.", createdAt="Thu Sep 16 2021 00:39:00", updatedAt="Mon Jul 19 2021 18:30:23")
    comment267 = Comment(videoId=467, channelId=44, content="Today is the day I'll finally know what brick tastes like.", createdAt="Fri Apr 01 2022 20:05:00", updatedAt="Fri Aug 06 2021 18:45:44")
    comment268 = Comment(videoId=508, channelId=31, content="My uncle's favorite pastime was building cars out of noodles.", createdAt="Sat Jan 15 2022 19:39:18", updatedAt="Tue Mar 08 2022 06:34:30")
    comment269 = Comment(videoId=274, channelId=57, content="He's in a boy band which doesn't make much sense for a snake.", createdAt="Fri Nov 05 2021 14:13:01", updatedAt="Fri Nov 05 2021 12:28:55")
    comment270 = Comment(videoId=181, channelId=91, content="She did not cheat on the test, for it was not the right thing to do.", createdAt="Sat Jul 03 2021 22:32:48", updatedAt="Tue Jun 22 2021 09:31:05")
    comment271 = Comment(videoId=628, channelId=43, content="She was sad to hear that fireflies are facing extinction due to artificial light, habitat loss, and pesticides.", createdAt="Sun Mar 20 2022 22:32:56", updatedAt="Mon Mar 28 2022 12:30:59")
    comment272 = Comment(videoId=244, channelId=97, content="It doesn't sound like that will ever be on my travel list.", createdAt="Fri Jul 16 2021 20:18:52", updatedAt="Mon Jan 10 2022 01:02:06")
    comment273 = Comment(videoId=528, channelId=89, content="The Guinea fowl flies through the air with all the grace of a turtle.", createdAt="Mon Mar 07 2022 02:35:16", updatedAt="Mon Jan 03 2022 21:40:01")
    comment274 = Comment(videoId=297, channelId=99, content="Plans for this weekend include turning wine into water.", createdAt="Fri Jul 23 2021 02:07:30", updatedAt="Sun Nov 28 2021 04:35:35")
    comment275 = Comment(videoId=467, channelId=60, content="People generally approve of dogs eating cat food but not cats eating dog food.", createdAt="Sun Aug 08 2021 14:49:30", updatedAt="Thu Mar 24 2022 15:24:51")
    comment276 = Comment(videoId=260, channelId=6, content="The urgent care center was flooded with patients after the news of a new deadly virus was made public.", createdAt="Wed Jan 19 2022 10:09:53", updatedAt="Thu Jul 01 2021 01:19:31")
    comment277 = Comment(videoId=500, channelId=14, content="It took him a while to realize that everything he decided not to change, he was actually choosing.", createdAt="Tue Dec 07 2021 20:03:01", updatedAt="Wed Jan 19 2022 20:55:57")
    comment278 = Comment(videoId=444, channelId=53, content="Every manager should be able to recite at least ten nursery rhymes backward.", createdAt="Sun Apr 03 2022 10:05:52", updatedAt="Sat Mar 19 2022 22:58:30")
    comment279 = Comment(videoId=7, channelId=85, content="The fish dreamed of escaping the fishbowl and into the toilet where he saw his friend go.", createdAt="Wed Jul 14 2021 06:13:19", updatedAt="Wed Nov 17 2021 23:50:02")
    comment280 = Comment(videoId=306, channelId=38, content="He had accidentally hacked into his company's server.", createdAt="Fri Mar 25 2022 04:19:22", updatedAt="Fri Sep 10 2021 12:25:30")
    comment281 = Comment(videoId=77, channelId=94, content="I only enjoy window shopping when the windows are transparent.", createdAt="Sat Jan 29 2022 20:11:07", updatedAt="Tue Oct 12 2021 09:49:44")
    comment282 = Comment(videoId=583, channelId=91, content="I come from a tribe of head-hunters, so I will never need a shrink.", createdAt="Sat Jan 15 2022 18:01:44", updatedAt="Mon Feb 14 2022 13:32:45")
    comment283 = Comment(videoId=280, channelId=17, content="He played the game as if his life depended on it and the truth was that it did.", createdAt="Tue Jul 06 2021 23:15:32", updatedAt="Sat Dec 04 2021 07:36:36")
    comment284 = Comment(videoId=450, channelId=58, content="She hadn't had her cup of coffee, and that made things all the worse.", createdAt="Fri Dec 03 2021 06:01:09", updatedAt="Sun Mar 27 2022 04:41:22")
    comment285 = Comment(videoId=90, channelId=51, content="If you don't like toenails, you probably shouldn't look at your feet.", createdAt="Thu Jul 29 2021 11:42:25", updatedAt="Sat Nov 20 2021 18:06:53")
    comment286 = Comment(videoId=729, channelId=1, content="The secret code they created made no sense, even to them.", createdAt="Thu Apr 22 2021 19:36:25", updatedAt="Sun Nov 21 2021 03:53:26")
    comment287 = Comment(videoId=224, channelId=59, content="The best key lime pie is still up for debate.", createdAt="Thu Mar 24 2022 10:13:42", updatedAt="Wed Jul 28 2021 21:37:00")
    comment288 = Comment(videoId=434, channelId=47, content="Pair your designer cowboy hat with scuba gear for a memorable occasion.", createdAt="Thu Nov 18 2021 08:12:37", updatedAt="Wed Aug 18 2021 19:35:51")
    comment289 = Comment(videoId=558, channelId=2, content="Sometimes, all you need to do is completely make an ass of yourself and laugh it off to realise that life isn’t so bad after all.", createdAt="Fri Jul 09 2021 13:06:48", updatedAt="Thu Mar 10 2022 00:39:41")
    comment290 = Comment(videoId=370, channelId=74, content="We have a lot of rain in June.", createdAt="Thu Apr 22 2021 17:58:45", updatedAt="Mon Aug 02 2021 06:26:11")
    comment291 = Comment(videoId=413, channelId=62, content="The spa attendant applied the deep cleaning mask to the gentleman’s back.", createdAt="Fri Dec 31 2021 04:53:17", updatedAt="Sat Dec 25 2021 04:29:18")
    comment292 = Comment(videoId=765, channelId=56, content="I want more detailed information.", createdAt="Mon Jun 21 2021 18:26:52", updatedAt="Mon Jul 26 2021 07:32:13")
    comment293 = Comment(videoId=408, channelId=35, content="There were three sphered rocks congregating in a cubed room.", createdAt="Sun May 02 2021 13:10:14", updatedAt="Mon Dec 27 2021 02:25:06")
    comment294 = Comment(videoId=170, channelId=23, content="Happiness can be found in the depths of chocolate pudding.", createdAt="Mon Sep 13 2021 17:59:12", updatedAt="Mon Feb 28 2022 19:34:56")
    comment295 = Comment(videoId=108, channelId=10, content="People keep telling me \"orange\" but I still prefer \"pink\".", createdAt="Sat Jul 31 2021 18:10:14", updatedAt="Wed Mar 23 2022 02:41:55")
    comment296 = Comment(videoId=624, channelId=24, content="He would only survive if he kept the fire going and he could hear thunder in the distance.", createdAt="Mon Jan 17 2022 18:14:31", updatedAt="Fri Sep 03 2021 01:58:23")
    comment297 = Comment(videoId=343, channelId=34, content="Random words in front of other random words create a random sentence.", createdAt="Wed May 12 2021 12:23:36", updatedAt="Wed Jan 26 2022 19:45:50")
    comment298 = Comment(videoId=524, channelId=15, content="The team members were hard to tell apart since they all wore their hair in a ponytail.", createdAt="Wed Aug 18 2021 12:31:52", updatedAt="Thu Jul 01 2021 02:55:23")
    comment299 = Comment(videoId=356, channelId=18, content="So long and thanks for the fish.", createdAt="Tue Jan 04 2022 01:00:27", updatedAt="Sat Jul 31 2021 10:02:39")
    comment300 = Comment(videoId=109, channelId=64, content="Traveling became almost extinct during the pandemic.", createdAt="Mon Jan 03 2022 12:54:40", updatedAt="Sat Jul 03 2021 18:33:48")
    comment301 = Comment(videoId=739, channelId=59, content="He invested some skill points in Charisma and Strength.", createdAt="Sat Sep 25 2021 08:31:21", updatedAt="Fri May 07 2021 14:59:53")
    comment302 = Comment(videoId=326, channelId=27, content="The busker hoped that the people passing by would throw money, but they threw tomatoes instead, so he exchanged his hat for a juicer.", createdAt="Wed Dec 22 2021 18:00:25", updatedAt="Tue Mar 22 2022 15:35:51")
    comment303 = Comment(videoId=314, channelId=96, content="She wondered what his eyes were saying beneath his mirrored sunglasses.", createdAt="Mon Sep 13 2021 18:56:01", updatedAt="Tue Nov 16 2021 13:07:52")
    comment304 = Comment(videoId=767, channelId=94, content="The toddler’s endless tantrum caused the entire plane anxiety.", createdAt="Sun Oct 03 2021 21:44:41", updatedAt="Mon Jun 28 2021 19:54:59")
    comment305 = Comment(videoId=767, channelId=15, content="Thirty years later, she still thought it was okay to put the toilet paper roll under rather than over.", createdAt="Mon Feb 14 2022 17:01:09", updatedAt="Fri Aug 13 2021 05:48:11")
    comment306 = Comment(videoId=369, channelId=51, content="You should never take advice from someone who thinks red paint dries quicker than blue paint.", createdAt="Thu Jun 03 2021 22:28:17", updatedAt="Sun Mar 20 2022 19:47:22")
    comment307 = Comment(videoId=389, channelId=91, content="She couldn't decide of the glass was half empty or half full so she drank it.", createdAt="Sun Nov 21 2021 08:07:24", updatedAt="Mon Nov 01 2021 06:16:51")
    comment308 = Comment(videoId=78, channelId=12, content="He was the only member of the club who didn't like plum pudding.", createdAt="Mon May 17 2021 17:32:25", updatedAt="Sat Apr 24 2021 04:37:02")
    comment309 = Comment(videoId=269, channelId=77, content="The bees decided to have a mutiny against their queen.", createdAt="Tue Nov 09 2021 07:04:13", updatedAt="Sat Apr 17 2021 10:41:19")
    comment310 = Comment(videoId=89, channelId=9, content="He dreamed of eating green apples with worms.", createdAt="Sat Jan 08 2022 22:11:34", updatedAt="Sat Dec 25 2021 18:37:59")
    comment311 = Comment(videoId=76, channelId=23, content="The near-death experience brought new ideas to light.", createdAt="Tue Feb 08 2022 18:48:42", updatedAt="Sun Jan 09 2022 08:53:22")
    comment312 = Comment(videoId=502, channelId=4, content="Potato wedges probably are not best for relationships.", createdAt="Tue Sep 28 2021 02:07:57", updatedAt="Sun Aug 01 2021 06:24:22")
    comment313 = Comment(videoId=686, channelId=90, content="It's always a good idea to seek shelter from the evil gaze of the sun.", createdAt="Sun Nov 07 2021 23:34:45", updatedAt="Sat Feb 26 2022 07:10:32")
    comment314 = Comment(videoId=753, channelId=87, content="As he entered the church he could hear the soft voice of someone whispering into a cell phone.", createdAt="Sun Jan 23 2022 16:37:44", updatedAt="Tue Sep 14 2021 04:40:38")
    comment315 = Comment(videoId=458, channelId=44, content="There was no ice cream in the freezer, nor did they have money to go to the store.", createdAt="Mon Jul 12 2021 20:17:52", updatedAt="Mon Nov 22 2021 13:33:12")
    comment316 = Comment(videoId=593, channelId=93, content="He wondered if it could be called a beach if there was no sand.", createdAt="Wed Nov 03 2021 07:37:06", updatedAt="Mon Nov 22 2021 23:11:55")
    comment317 = Comment(videoId=426, channelId=28, content="Watching the geriatric men’s softball team brought back memories of 3 yr olds playing t-ball.", createdAt="Mon Mar 14 2022 23:33:52", updatedAt="Mon Mar 21 2022 20:35:29")
    comment318 = Comment(videoId=662, channelId=29, content="The teenage boy was accused of breaking his arm simply to get out of the test.", createdAt="Mon Dec 27 2021 00:01:18", updatedAt="Sun Jul 25 2021 21:54:36")
    comment319 = Comment(videoId=227, channelId=43, content="Harrold felt confident that nobody would ever suspect his spy pigeon.", createdAt="Sat Apr 09 2022 08:15:45", updatedAt="Thu Aug 19 2021 22:11:37")
    comment320 = Comment(videoId=64, channelId=92, content="Bill ran from the giraffe toward the dolphin.", createdAt="Thu Feb 17 2022 08:06:59", updatedAt="Sun Oct 10 2021 13:43:38")
    comment321 = Comment(videoId=506, channelId=95, content="Although it wasn't a pot of gold, Nancy was still enthralled at what she found at the end of the rainbow.", createdAt="Tue Dec 21 2021 11:00:16", updatedAt="Sat Nov 06 2021 04:09:51")
    comment322 = Comment(videoId=162, channelId=74, content="There was no telling what thoughts would come from the machine.", createdAt="Sat Jun 05 2021 15:15:18", updatedAt="Thu Nov 04 2021 08:17:16")
    comment323 = Comment(videoId=320, channelId=71, content="The fence was confused about whether it was supposed to keep things in or keep things out.", createdAt="Tue Mar 08 2022 18:07:49", updatedAt="Mon Oct 18 2021 19:14:11")
    comment324 = Comment(videoId=641, channelId=26, content="The memory we used to share is no longer coherent.", createdAt="Sat Mar 26 2022 10:08:11", updatedAt="Mon Feb 28 2022 14:36:48")
    comment325 = Comment(videoId=744, channelId=31, content="She opened up her third bottle of wine of the night.", createdAt="Thu Oct 21 2021 18:41:34", updatedAt="Mon Apr 26 2021 15:01:43")
    comment326 = Comment(videoId=558, channelId=55, content="She folded her handkerchief neatly.", createdAt="Sun Oct 03 2021 22:59:07", updatedAt="Sun Nov 21 2021 09:59:15")
    comment327 = Comment(videoId=549, channelId=18, content="She had some amazing news to share but nobody to share it with.", createdAt="Thu Jan 20 2022 14:20:21", updatedAt="Mon Jun 21 2021 05:31:18")
    comment328 = Comment(videoId=437, channelId=66, content="It doesn't sound like that will ever be on my travel list.", createdAt="Sat Sep 25 2021 19:20:41", updatedAt="Wed Jan 12 2022 00:39:35")
    comment329 = Comment(videoId=710, channelId=19, content="They throw cabbage that turns your brain into emotional baggage.", createdAt="Sat Nov 13 2021 12:16:41", updatedAt="Sun Dec 12 2021 14:04:24")
    comment330 = Comment(videoId=57, channelId=14, content="Gary didn't understand why Doug went upstairs to get one dollar bills when he invited him to go cow tipping.", createdAt="Sat Apr 17 2021 16:11:23", updatedAt="Sun May 16 2021 03:21:36")
    comment331 = Comment(videoId=310, channelId=97, content="I liked their first two albums but changed my mind after that charity gig.", createdAt="Sun Apr 25 2021 07:58:48", updatedAt="Wed Oct 20 2021 00:40:04")
    comment332 = Comment(videoId=432, channelId=36, content="Twin 4-month-olds slept in the shade of the palm tree while the mother tanned in the sun.", createdAt="Mon Feb 14 2022 00:27:09", updatedAt="Wed Feb 16 2022 01:09:39")
    comment333 = Comment(videoId=58, channelId=77, content="Always bring cinnamon buns on a deep-sea diving expedition.", createdAt="Tue Jul 27 2021 21:56:13", updatedAt="Wed Mar 09 2022 00:58:25")
    comment334 = Comment(videoId=408, channelId=41, content="The body piercing didn't go exactly as he expected.", createdAt="Sat Oct 16 2021 15:30:13", updatedAt="Wed Dec 15 2021 18:56:58")
    comment335 = Comment(videoId=713, channelId=80, content="You'll see the rainbow bridge after it rains cats and dogs.", createdAt="Thu Feb 24 2022 08:51:20", updatedAt="Sat Jul 10 2021 20:03:47")
    comment336 = Comment(videoId=438, channelId=52, content="You realize you're not alone as you sit in your bedroom massaging your calves after a long day of playing tug-of-war with Grandpa Joe in the hospital.", createdAt="Fri Dec 31 2021 19:11:36", updatedAt="Fri Mar 11 2022 21:19:38")
    comment337 = Comment(videoId=454, channelId=64, content="In hopes of finding out the truth, he entered the one-room library.", createdAt="Wed Jul 21 2021 09:22:16", updatedAt="Thu Feb 17 2022 00:39:43")
    comment338 = Comment(videoId=318, channelId=28, content="You bite up because of your lower jaw.", createdAt="Fri Mar 11 2022 11:16:38", updatedAt="Fri Apr 08 2022 19:42:17")
    comment339 = Comment(videoId=617, channelId=5, content="As time wore on, simple dog commands turned into full paragraphs explaining why the dog couldn’t do something.", createdAt="Thu Aug 12 2021 16:36:32", updatedAt="Sun Sep 05 2021 11:40:57")
    comment340 = Comment(videoId=609, channelId=72, content="The opportunity of a lifetime passed before him as he tried to decide between a cone or a cup.", createdAt="Tue May 04 2021 04:30:00", updatedAt="Tue Jan 11 2022 19:36:19")
    comment341 = Comment(videoId=123, channelId=45, content="It was difficult for Mary to admit that most of her workout consisted of exercising poor judgment.", createdAt="Sun Apr 10 2022 09:10:47", updatedAt="Wed Jun 23 2021 13:03:10")
    comment342 = Comment(videoId=272, channelId=4, content="Thigh-high in the water, the fisherman’s hope for dinner soon turned to despair.", createdAt="Tue Mar 15 2022 11:07:37", updatedAt="Wed Nov 24 2021 22:19:08")
    comment343 = Comment(videoId=769, channelId=31, content="I had a friend in high school named Rick Shaw, but he was fairly useless as a mode of transport.", createdAt="Sat Mar 26 2022 16:00:34", updatedAt="Thu Oct 14 2021 15:58:11")
    comment344 = Comment(videoId=23, channelId=83, content="Joe discovered that traffic cones make excellent megaphones.", createdAt="Mon Apr 26 2021 21:31:50", updatedAt="Mon Feb 14 2022 04:53:03")
    comment345 = Comment(videoId=662, channelId=30, content="I love bacon, beer, birds, and baboons.", createdAt="Thu Oct 07 2021 00:07:37", updatedAt="Sun Nov 07 2021 03:49:38")
    comment346 = Comment(videoId=113, channelId=58, content="The secret ingredient to his wonderful life was crime.", createdAt="Fri Oct 15 2021 03:11:02", updatedAt="Sun Jun 27 2021 12:53:07")
    comment347 = Comment(videoId=672, channelId=25, content="Mom didn’t understand why no one else wanted a hot tub full of jello.", createdAt="Mon Aug 09 2021 09:29:46", updatedAt="Thu Aug 05 2021 04:09:43")
    comment348 = Comment(videoId=620, channelId=24, content="While on the first date he accidentally hit his head on the beam.", createdAt="Sun Apr 03 2022 15:13:41", updatedAt="Mon Mar 28 2022 06:13:37")
    comment349 = Comment(videoId=4, channelId=50, content="The bug was having an excellent day until he hit the windshield.", createdAt="Tue Feb 15 2022 01:57:01", updatedAt="Fri Apr 01 2022 22:13:22")
    comment350 = Comment(videoId=657, channelId=67, content="She did her best to help him.", createdAt="Sat Dec 11 2021 00:01:53", updatedAt="Mon May 17 2021 23:46:57")
    comment351 = Comment(videoId=428, channelId=28, content="One small action would change her life, but whether it would be for better or for worse was yet to be determined.", createdAt="Tue Jul 13 2021 13:05:28", updatedAt="Sun Aug 29 2021 09:20:02")
    comment352 = Comment(videoId=7, channelId=57, content="He had a vague sense that trees gave birth to dinosaurs.", createdAt="Tue Nov 09 2021 05:44:46", updatedAt="Thu Jun 10 2021 00:17:13")
    comment353 = Comment(videoId=89, channelId=50, content="The external scars tell only part of the story.", createdAt="Sat Jun 19 2021 10:59:56", updatedAt="Mon Jan 03 2022 04:16:39")
    comment354 = Comment(videoId=551, channelId=67, content="Mary plays the piano.", createdAt="Tue Nov 30 2021 23:27:49", updatedAt="Tue Aug 24 2021 12:42:38")
    comment355 = Comment(videoId=285, channelId=98, content="She had the gift of being able to paint songs.", createdAt="Tue Oct 05 2021 14:12:59", updatedAt="Fri Nov 12 2021 04:57:43")
    comment356 = Comment(videoId=77, channelId=86, content="His confidence would have bee admirable if it wasn't for his stupidity.", createdAt="Wed Mar 02 2022 03:57:53", updatedAt="Tue Sep 07 2021 20:40:10")
    comment357 = Comment(videoId=80, channelId=71, content="I had a friend in high school named Rick Shaw, but he was fairly useless as a mode of transport.", createdAt="Wed Dec 29 2021 18:28:37", updatedAt="Wed May 12 2021 06:34:44")
    comment358 = Comment(videoId=146, channelId=96, content="The waves were crashing on the shore; it was a lovely sight.", createdAt="Fri May 14 2021 02:02:10", updatedAt="Wed Sep 08 2021 12:13:02")
    comment359 = Comment(videoId=615, channelId=36, content="She finally understood that grief was her love with no place for it to go.", createdAt="Sat Aug 07 2021 13:22:51", updatedAt="Mon May 17 2021 14:14:42")
    comment360 = Comment(videoId=230, channelId=48, content="Joe made the sugar cookies; Susan decorated them.", createdAt="Mon Nov 29 2021 22:27:43", updatedAt="Thu Sep 16 2021 19:42:17")
    comment362 = Comment(videoId=243, channelId=15, content="She used her own hair in the soup to give it more flavor.", createdAt="Wed Aug 18 2021 16:58:05", updatedAt="Sun Mar 27 2022 21:13:32")
    comment363 = Comment(videoId=629, channelId=55, content="He was disappointed when he found the beach to be so sandy and the sun so sunny.", createdAt="Fri May 14 2021 23:07:48", updatedAt="Wed Dec 15 2021 16:44:58")
    comment364 = Comment(videoId=387, channelId=1, content="For the 216th time, he said he would quit drinking soda after this last Coke.", createdAt="Sun Sep 19 2021 08:41:42", updatedAt="Sun Feb 13 2022 12:29:26")
    comment365 = Comment(videoId=375, channelId=56, content="He had decided to accept his fate of accepting his fate.", createdAt="Tue Aug 03 2021 20:47:16", updatedAt="Mon Mar 28 2022 17:41:09")
    comment366 = Comment(videoId=81, channelId=1, content="It's never comforting to know that your fate depends on something as unpredictable as the popping of corn.", createdAt="Wed Jul 14 2021 00:14:43", updatedAt="Mon Dec 06 2021 00:31:54")
    comment367 = Comment(videoId=57, channelId=69, content="The fog was so dense even a laser decided it wasn't worth the effort.", createdAt="Wed Sep 15 2021 01:09:25", updatedAt="Thu Apr 15 2021 03:59:00")
    comment368 = Comment(videoId=248, channelId=4, content="The pet shop stocks everything you need to keep your anaconda happy.", createdAt="Thu Feb 03 2022 03:32:28", updatedAt="Sat Sep 11 2021 09:37:32")
    comment369 = Comment(videoId=438, channelId=48, content="Mary realized if her calculator had a history, it would be more embarrassing than her computer browser history.", createdAt="Mon Apr 26 2021 02:54:47", updatedAt="Thu Jun 24 2021 02:37:45")
    comment370 = Comment(videoId=82, channelId=27, content="Poison ivy grew through the fence they said was impenetrable.", createdAt="Sat Oct 02 2021 22:35:43", updatedAt="Thu Dec 30 2021 13:13:06")
    comment371 = Comment(videoId=108, channelId=18, content="Pink horses galloped across the sea.", createdAt="Fri Jan 21 2022 16:02:14", updatedAt="Thu Aug 26 2021 10:32:03")
    comment372 = Comment(videoId=697, channelId=6, content="Most shark attacks occur about 10 feet from the beach since that's where the people are.", createdAt="Wed Oct 20 2021 17:46:14", updatedAt="Mon May 03 2021 07:15:46")
    comment373 = Comment(videoId=692, channelId=82, content="He learned the hardest lesson of his life and had the scars, both physical and mental, to prove it.", createdAt="Tue Nov 02 2021 17:28:15", updatedAt="Sat Apr 02 2022 11:18:44")
    comment374 = Comment(videoId=145, channelId=47, content="If you really strain your ears, you can just about hear the sound of no one giving a damn.", createdAt="Sat Jan 22 2022 06:36:23", updatedAt="Sat Jan 22 2022 02:50:37")
    comment375 = Comment(videoId=379, channelId=48, content="Three generations with six decades of life experience.", createdAt="Thu Sep 09 2021 07:14:47", updatedAt="Fri Nov 26 2021 02:27:38")
    comment376 = Comment(videoId=178, channelId=58, content="This made him feel like an old-style rootbeer float smells.", createdAt="Wed Mar 02 2022 21:13:59", updatedAt="Tue May 04 2021 20:40:28")
    comment377 = Comment(videoId=530, channelId=52, content="Despite multiple complications and her near-death experience", createdAt="Wed Jun 02 2021 11:48:27", updatedAt="Mon Jan 03 2022 14:11:45")
    comment378 = Comment(videoId=760, channelId=40, content="He wore the surgical mask in public not to keep from catching a virus, but to keep people away from him.", createdAt="Mon Apr 26 2021 05:00:12", updatedAt="Thu Mar 03 2022 03:19:15")
    comment379 = Comment(videoId=230, channelId=94, content="She wrote him a long letter, but he didn't read it.", createdAt="Mon Jan 31 2022 12:20:24", updatedAt="Tue Mar 29 2022 18:34:23")
    comment380 = Comment(videoId=618, channelId=85, content="The most exciting eureka moment I've had was when I realized that the instructions on food packets were just guidelines.", createdAt="Thu Jul 15 2021 12:51:14", updatedAt="Tue May 04 2021 08:54:20")
    comment381 = Comment(videoId=4, channelId=32, content="There should have been a time and a place, but this wasn't it.", createdAt="Mon Jan 17 2022 06:46:14", updatedAt="Sun Jul 11 2021 21:22:31")
    comment382 = Comment(videoId=596, channelId=63, content="Everybody should read Chaucer to improve their everyday vocabulary.", createdAt="Sun Sep 12 2021 05:37:10", updatedAt="Mon Jan 10 2022 20:14:17")
    comment383 = Comment(videoId=345, channelId=15, content="Andy loved to sleep on a bed of nails.", createdAt="Mon Jun 07 2021 12:08:23", updatedAt="Tue Jul 27 2021 12:54:32")
    comment384 = Comment(videoId=183, channelId=6, content="He wasn't bitter that she had moved on but from the radish.", createdAt="Sat Jan 15 2022 15:14:06", updatedAt="Sat Jul 10 2021 13:32:31")
    comment385 = Comment(videoId=55, channelId=90, content="We have a lot of rain in June.", createdAt="Tue Aug 03 2021 10:38:30", updatedAt="Mon May 17 2021 13:50:11")
    comment386 = Comment(videoId=45, channelId=88, content="Everyone pretends to like wheat until you mention barley.", createdAt="Sat Feb 12 2022 21:00:15", updatedAt="Sat Jan 29 2022 13:03:43")
    comment387 = Comment(videoId=499, channelId=10, content="He was all business when he wore his clown suit.", createdAt="Fri Jan 21 2022 09:12:10", updatedAt="Fri Apr 30 2021 00:59:32")
    comment388 = Comment(videoId=467, channelId=70, content="I used to live in my neighbor's fishpond, but the aesthetic wasn't to my taste.", createdAt="Wed Jan 12 2022 17:20:33", updatedAt="Fri Feb 04 2022 07:40:24")
    comment389 = Comment(videoId=585, channelId=21, content="Honestly, I didn't care much for the first season, so I didn't bother with the second.", createdAt="Tue Aug 24 2021 01:12:39", updatedAt="Sun Jan 23 2022 01:16:40")
    comment390 = Comment(videoId=692, channelId=27, content="Some bathing suits just shouldn’t be worn by some people.", createdAt="Sat May 15 2021 08:21:57", updatedAt="Wed Sep 01 2021 22:41:38")
    comment391 = Comment(videoId=297, channelId=29, content="Martha came to the conclusion that shake weights are a great gift for any occasion.", createdAt="Thu Jul 22 2021 23:12:55", updatedAt="Tue Jun 29 2021 20:03:49")
    comment392 = Comment(videoId=318, channelId=5, content="He appeared to be confusingly perplexed.", createdAt="Sat Apr 02 2022 03:37:06", updatedAt="Fri Jul 23 2021 05:57:32")
    comment393 = Comment(videoId=276, channelId=25, content="I’m a living furnace.", createdAt="Fri Jun 11 2021 15:43:28", updatedAt="Thu Apr 29 2021 23:07:42")
    comment394 = Comment(videoId=184, channelId=52, content="She is never happy until she finds something to be unhappy about; then, she is overjoyed.", createdAt="Wed Nov 10 2021 01:24:19", updatedAt="Mon Dec 06 2021 09:40:54")
    comment395 = Comment(videoId=154, channelId=72, content="Today I bought a raincoat and wore it on a sunny day.", createdAt="Sun Jan 23 2022 17:35:01", updatedAt="Tue Jul 13 2021 02:15:29")
    comment396 = Comment(videoId=646, channelId=91, content="Jeanne wished she has chosen the red button.", createdAt="Wed Dec 22 2021 22:23:42", updatedAt="Fri Apr 08 2022 08:09:52")
    comment397 = Comment(videoId=604, channelId=54, content="The elephant didn't want to talk about the person in the room.", createdAt="Fri Dec 03 2021 17:38:00", updatedAt="Tue Jun 15 2021 01:32:39")
    comment398 = Comment(videoId=593, channelId=49, content="The teenage boy was accused of breaking his arm simply to get out of the test.", createdAt="Fri Oct 08 2021 13:40:07", updatedAt="Mon Feb 21 2022 00:08:18")
    comment399 = Comment(videoId=672, channelId=29, content="Stop waiting for exceptional things to just happen.", createdAt="Sun Sep 05 2021 05:29:08", updatedAt="Fri Feb 25 2022 22:32:14")
    comment400 = Comment(videoId=20, channelId=13, content="I really want to go to work, but I am too sick to drive.", createdAt="Tue Jan 04 2022 10:41:30", updatedAt="Sun Aug 22 2021 15:18:00")
    comment401 = Comment(videoId=671, channelId=57, content="Let me help you with your baggage.", createdAt="Wed Apr 28 2021 05:48:57", updatedAt="Sat Jan 01 2022 03:44:33")
    comment402 = Comment(videoId=486, channelId=79, content="Giving directions that the mountains are to the west only works when you can see them.", createdAt="Sun Jan 02 2022 11:03:44", updatedAt="Sat Apr 24 2021 13:42:14")
    comment403 = Comment(videoId=92, channelId=50, content="He put heat on the wound to see what would grow.", createdAt="Thu Feb 03 2022 05:34:28", updatedAt="Tue Apr 05 2022 05:14:24")
    comment404 = Comment(videoId=244, channelId=23, content="I became paranoid that the school of jellyfish was spying on me.", createdAt="Sun Dec 26 2021 01:54:51", updatedAt="Thu Dec 23 2021 14:45:15")
    comment405 = Comment(videoId=634, channelId=49, content="Thigh-high in the water, the fisherman’s hope for dinner soon turned to despair.", createdAt="Thu Aug 12 2021 20:14:51", updatedAt="Wed Nov 10 2021 08:12:22")
    comment406 = Comment(videoId=416, channelId=94, content="It isn't difficult to do a handstand if you just stand on your hands.", createdAt="Wed Jul 14 2021 19:40:54", updatedAt="Fri Jan 14 2022 15:09:59")
    comment407 = Comment(videoId=227, channelId=72, content="Everyone was curious about the large white blimp that appeared overnight.", createdAt="Sat Jun 26 2021 04:14:17", updatedAt="Mon Apr 12 2021 14:30:34")
    comment408 = Comment(videoId=360, channelId=97, content="On a scale from one to ten, what's your favorite flavor of random grammar?", createdAt="Fri Oct 15 2021 11:59:05", updatedAt="Mon Mar 21 2022 23:28:29")
    comment409 = Comment(videoId=266, channelId=18, content="The furnace repairman indicated the heating system was acting as an air conditioner.", createdAt="Fri May 14 2021 23:09:30", updatedAt="Sun Feb 20 2022 12:20:27")
    comment410 = Comment(videoId=286, channelId=29, content="She wanted a pet platypus but ended up getting a duck and a ferret instead.", createdAt="Mon Jul 12 2021 19:40:46", updatedAt="Mon Oct 18 2021 13:21:05")
    comment411 = Comment(videoId=660, channelId=82, content="He kept telling himself that one day it would all somehow make sense.", createdAt="Sun Apr 18 2021 01:54:52", updatedAt="Fri Dec 10 2021 16:35:45")
    comment412 = Comment(videoId=724, channelId=40, content="Patricia loves the sound of nails strongly pressed against the chalkboard.", createdAt="Sat Feb 05 2022 02:58:13", updatedAt="Tue May 11 2021 21:06:58")
    comment413 = Comment(videoId=517, channelId=19, content="He felt that dining on the bridge brought romance to his relationship with his cat.", createdAt="Sat Mar 26 2022 14:19:47", updatedAt="Mon Aug 02 2021 07:40:29")
    comment414 = Comment(videoId=504, channelId=8, content="The minute she landed she understood the reason this was a fly-over state.", createdAt="Sun Feb 27 2022 00:49:54", updatedAt="Tue Apr 05 2022 20:31:41")
    comment415 = Comment(videoId=673, channelId=40, content="Henry couldn't decide if he was an auto mechanic or a priest.", createdAt="Fri Jun 04 2021 01:48:52", updatedAt="Thu Jul 08 2021 00:57:13")
    comment416 = Comment(videoId=695, channelId=99, content="Her life in the confines of the house became her new normal.", createdAt="Sun Aug 01 2021 22:28:47", updatedAt="Tue Mar 01 2022 06:42:35")
    comment417 = Comment(videoId=84, channelId=85, content="The elderly neighborhood became enraged over the coyotes who had been blamed for the poodle’s disappearance.", createdAt="Tue Apr 13 2021 02:09:06", updatedAt="Thu Sep 02 2021 07:50:38")
    comment418 = Comment(videoId=429, channelId=31, content="Greetings from the galaxy MACS0647-JD, or what we call home.", createdAt="Thu Oct 21 2021 11:20:27", updatedAt="Wed Feb 16 2022 08:56:57")
    comment419 = Comment(videoId=704, channelId=88, content="There's a reason that roses have thorns.", createdAt="Tue Mar 08 2022 22:35:00", updatedAt="Thu Sep 09 2021 15:51:09")
    comment420 = Comment(videoId=134, channelId=3, content="He excelled at firing people nicely.", createdAt="Mon Aug 23 2021 20:59:36", updatedAt="Tue Oct 12 2021 08:52:46")
    comment421 = Comment(videoId=768, channelId=56, content="So long and thanks for the fish.", createdAt="Mon May 03 2021 15:59:27", updatedAt="Fri Oct 29 2021 04:53:28")
    comment422 = Comment(videoId=186, channelId=86, content="I covered my friend in baby oil.", createdAt="Sat Dec 18 2021 17:59:59", updatedAt="Thu Sep 30 2021 14:16:59")
    comment423 = Comment(videoId=162, channelId=3, content="He wondered why at 18 he was old enough to go to war, but not old enough to buy cigarettes.", createdAt="Thu Mar 10 2022 22:38:50", updatedAt="Sat Aug 28 2021 10:06:54")
    comment424 = Comment(videoId=82, channelId=72, content="She wore green lipstick like a fashion icon.", createdAt="Sat Apr 09 2022 18:54:13", updatedAt="Thu Jun 17 2021 00:28:26")
    comment425 = Comment(videoId=290, channelId=69, content="He loved eating his bananas in hot dog buns.", createdAt="Sun Oct 24 2021 11:37:21", updatedAt="Fri Dec 24 2021 23:27:02")
    comment426 = Comment(videoId=543, channelId=14, content="Although it wasn't a pot of gold, Nancy was still enthralled at what she found at the end of the rainbow.", createdAt="Sat Apr 24 2021 04:54:01", updatedAt="Tue Sep 21 2021 21:39:18")
    comment427 = Comment(videoId=434, channelId=39, content="My Mum tries to be cool by saying that she likes all the same things that I do.", createdAt="Sat May 01 2021 05:04:02", updatedAt="Sat Feb 19 2022 19:10:48")
    comment428 = Comment(videoId=695, channelId=37, content="I liked their first two albums but changed my mind after that charity gig.", createdAt="Mon Apr 12 2021 12:14:58", updatedAt="Sat Dec 04 2021 11:14:43")
    comment429 = Comment(videoId=564, channelId=55, content="He went back to the video to see what had been recorded and was shocked at what he saw.", createdAt="Sun Dec 12 2021 03:26:47", updatedAt="Wed Jan 19 2022 09:56:12")
    comment430 = Comment(videoId=258, channelId=90, content="It doesn't sound like that will ever be on my travel list.", createdAt="Wed Oct 27 2021 20:47:46", updatedAt="Wed Aug 04 2021 02:27:57")
    comment431 = Comment(videoId=291, channelId=42, content="He decided water-skiing on a frozen lake wasn’t a good idea.", createdAt="Fri Feb 18 2022 09:43:16", updatedAt="Thu Jul 15 2021 05:49:11")
    comment432 = Comment(videoId=479, channelId=58, content="She did her best to help him.", createdAt="Sun Dec 05 2021 23:23:18", updatedAt="Tue Jun 08 2021 01:09:37")
    comment433 = Comment(videoId=675, channelId=31, content="I've always wanted to go to Tajikistan, but my cat would miss me.", createdAt="Tue Dec 21 2021 07:20:27", updatedAt="Wed May 19 2021 01:36:13")
    comment434 = Comment(videoId=25, channelId=61, content="Baby wipes are made of chocolate stardust.", createdAt="Mon Apr 19 2021 20:20:34", updatedAt="Wed Jun 09 2021 20:33:24")
    comment435 = Comment(videoId=210, channelId=87, content="He watched the dancing piglets with panda bear tummies in the swimming pool.", createdAt="Sun Jun 27 2021 23:03:30", updatedAt="Sat Oct 09 2021 22:48:56")
    comment436 = Comment(videoId=186, channelId=47, content="The hand sanitizer was actually clear glue.", createdAt="Tue May 25 2021 23:14:42", updatedAt="Wed May 05 2021 14:14:37")
    comment437 = Comment(videoId=79, channelId=76, content="If you like tuna and tomato sauce, try combining the two, it’s really not as bad as it sounds.", createdAt="Thu Sep 02 2021 12:32:43", updatedAt="Sat Aug 28 2021 19:04:24")
    comment438 = Comment(videoId=319, channelId=58, content="There are over 500 starfish in the bathroom drawer.", createdAt="Sat Jul 31 2021 21:16:21", updatedAt="Tue Jun 15 2021 06:18:13")
    comment439 = Comment(videoId=69, channelId=32, content="The knives were out and she was sharpening hers.", createdAt="Tue Mar 01 2022 18:55:53", updatedAt="Sat May 15 2021 08:15:56")
    comment440 = Comment(videoId=724, channelId=6, content="Even though he thought the world was flat he didn’t see the irony of wanting to travel around the world.", createdAt="Wed Oct 20 2021 16:30:24", updatedAt="Tue Nov 02 2021 22:54:39")
    comment441 = Comment(videoId=364, channelId=4, content="He hated that he loved what she hated about hate.", createdAt="Wed Mar 02 2022 13:25:59", updatedAt="Mon Dec 27 2021 07:08:28")
    comment442 = Comment(videoId=464, channelId=98, content="Siri became confused when we reused to follow her directions.", createdAt="Fri Aug 27 2021 02:00:17", updatedAt="Fri Oct 01 2021 20:22:39")
    comment443 = Comment(videoId=301, channelId=88, content="Three years later, the coffin was still full of Jello.", createdAt="Thu Sep 16 2021 22:29:42", updatedAt="Wed Jul 14 2021 18:13:57")
    comment444 = Comment(videoId=365, channelId=57, content="I used to practice weaving with spaghetti three hours a day but stopped because I didn't want to die alone.", createdAt="Sun Nov 21 2021 04:15:24", updatedAt="Mon Mar 21 2022 22:43:30")
    comment445 = Comment(videoId=11, channelId=41, content="Most shark attacks occur about 10 feet from the beach since that's where the people are.", createdAt="Thu Feb 17 2022 13:41:51", updatedAt="Wed Dec 29 2021 17:36:08")
    comment446 = Comment(videoId=524, channelId=66, content="She wanted to be rescued, but only if it was Tuesday and raining.", createdAt="Sat Oct 30 2021 09:30:28", updatedAt="Tue Feb 01 2022 09:59:34")
    comment447 = Comment(videoId=15, channelId=79, content="The waves were crashing on the shore; it was a lovely sight.", createdAt="Wed Mar 30 2022 09:27:41", updatedAt="Sun Apr 25 2021 09:07:08")
    comment449 = Comment(videoId=297, channelId=14, content="It dawned on her that others could make her happier, but only she could make herself happy.", createdAt="Tue Sep 21 2021 04:52:24", updatedAt="Thu May 20 2021 03:49:07")
    comment450 = Comment(videoId=95, channelId=63, content="Charles ate the french fries knowing they would be his last meal.", createdAt="Fri Sep 03 2021 14:32:18", updatedAt="Tue May 25 2021 06:17:57")
    comment451 = Comment(videoId=261, channelId=100, content="The body piercing didn't go exactly as he expected.", createdAt="Thu Jun 03 2021 03:07:17", updatedAt="Fri Nov 05 2021 04:37:24")
    comment452 = Comment(videoId=462, channelId=24, content="The water flowing down the river didn’t look that powerful from the car", createdAt="Tue May 11 2021 13:42:33", updatedAt="Wed Jun 23 2021 12:19:09")
    comment453 = Comment(videoId=84, channelId=29, content="The skeleton had skeletons of his own in the closet.", createdAt="Sun May 16 2021 04:59:31", updatedAt="Thu Nov 18 2021 08:04:58")
    comment454 = Comment(videoId=333, channelId=86, content="The light that burns twice as bright burns half as long.", createdAt="Thu Jul 29 2021 04:35:08", updatedAt="Thu Jun 03 2021 11:19:18")
    comment455 = Comment(videoId=295, channelId=67, content="It must be five o'clock somewhere.", createdAt="Tue Aug 03 2021 05:18:43", updatedAt="Thu Sep 02 2021 17:04:37")
    comment456 = Comment(videoId=531, channelId=100, content="I used to practice weaving with spaghetti three hours a day but stopped because I didn't want to die alone.", createdAt="Mon Mar 14 2022 03:32:57", updatedAt="Thu Jul 08 2021 19:51:01")
    comment457 = Comment(videoId=678, channelId=100, content="You realize you're not alone as you sit in your bedroom massaging your calves after a long day of playing tug-of-war with Grandpa Joe in the hospital.", createdAt="Sat Jul 17 2021 23:20:35", updatedAt="Wed Oct 13 2021 03:15:44")
    comment458 = Comment(videoId=689, channelId=82, content="The book is in front of the table.", createdAt="Thu Jan 06 2022 16:47:31", updatedAt="Thu Apr 07 2022 02:23:57")
    comment459 = Comment(videoId=343, channelId=18, content="My secretary is the only person who truly understands my stamp-collecting obsession.", createdAt="Sun Jan 30 2022 22:40:54", updatedAt="Fri Nov 26 2021 00:14:55")
    comment460 = Comment(videoId=435, channelId=37, content="He didn't understand why the bird wanted to ride the bicycle.", createdAt="Wed Sep 08 2021 12:35:34", updatedAt="Wed Jun 09 2021 23:19:41")
    comment461 = Comment(videoId=115, channelId=53, content="Although it wasn't a pot of gold, Nancy was still enthralled at what she found at the end of the rainbow.", createdAt="Thu Dec 16 2021 15:06:50", updatedAt="Fri Apr 08 2022 15:46:01")
    comment462 = Comment(videoId=577, channelId=73, content="He stomped on his fruit loops and thus became a cereal killer.", createdAt="Wed Sep 22 2021 22:09:41", updatedAt="Sun Apr 18 2021 16:15:59")
    comment463 = Comment(videoId=535, channelId=72, content="Standing on one's head at job interviews forms a lasting impression.", createdAt="Wed Jan 26 2022 09:01:58", updatedAt="Mon Jan 10 2022 23:48:51")
    comment464 = Comment(videoId=362, channelId=49, content="The dead trees waited to be ignited by the smallest spark and seek their revenge.", createdAt="Wed Jul 07 2021 17:29:40", updatedAt="Wed Dec 22 2021 01:05:50")
    comment465 = Comment(videoId=107, channelId=70, content="There are over 500 starfish in the bathroom drawer.", createdAt="Mon Feb 21 2022 11:36:13", updatedAt="Fri Sep 10 2021 20:19:34")
    comment466 = Comment(videoId=747, channelId=95, content="My Mum tries to be cool by saying that she likes all the same things that I do.", createdAt="Fri Jan 14 2022 18:48:12", updatedAt="Fri Mar 18 2022 12:48:16")
    comment467 = Comment(videoId=429, channelId=79, content="Writing a list of random sentences is harder than I initially thought it would be.", createdAt="Sat Jan 01 2022 09:48:29", updatedAt="Sun Apr 11 2021 13:16:00")
    comment468 = Comment(videoId=263, channelId=58, content="The overpass went under the highway and into a secret world.", createdAt="Sun May 30 2021 16:44:47", updatedAt="Thu Apr 07 2022 13:25:12")
    comment469 = Comment(videoId=318, channelId=82, content="His son quipped that power bars were nothing more than adult candy bars.", createdAt="Fri Jan 07 2022 03:48:03", updatedAt="Wed Jul 21 2021 01:34:34")
    comment470 = Comment(videoId=507, channelId=84, content="When nobody is around, the trees gossip about the people who have walked under them.", createdAt="Fri Oct 01 2021 23:23:39", updatedAt="Sun Aug 15 2021 14:04:34")
    comment471 = Comment(videoId=548, channelId=82, content="We will not allow you to bring your pet armadillo along.", createdAt="Mon Aug 16 2021 10:45:34", updatedAt="Wed May 19 2021 18:37:06")
    comment472 = Comment(videoId=116, channelId=47, content="Grape jelly was leaking out the hole in the roof.", createdAt="Fri Sep 24 2021 21:19:07", updatedAt="Mon Nov 08 2021 15:25:10")
    comment473 = Comment(videoId=728, channelId=36, content="The toddler’s endless tantrum caused the entire plane anxiety.", createdAt="Thu May 20 2021 11:12:31", updatedAt="Thu Sep 09 2021 07:09:06")
    comment474 = Comment(videoId=347, channelId=67, content="She learned that water bottles are no longer just to hold liquid, but they're also status symbols.", createdAt="Mon Jun 28 2021 01:12:05", updatedAt="Wed Jun 30 2021 11:27:02")
    comment475 = Comment(videoId=177, channelId=30, content="Imagine his surprise when he discovered that the safe was full of pudding.", createdAt="Mon Aug 02 2021 01:10:06", updatedAt="Sun Oct 17 2021 20:06:36")
    comment476 = Comment(videoId=580, channelId=25, content="I often see the time 11:11 or 12:34 on clocks.", createdAt="Sat Sep 11 2021 15:38:51", updatedAt="Tue Mar 22 2022 17:39:41")
    comment477 = Comment(videoId=225, channelId=18, content="She opened up her third bottle of wine of the night.", createdAt="Sat Mar 05 2022 04:31:15", updatedAt="Sat Mar 12 2022 20:32:54")
    comment479 = Comment(videoId=659, channelId=39, content="The spa attendant applied the deep cleaning mask to the gentleman’s back.", createdAt="Thu Jun 24 2021 17:58:33", updatedAt="Fri Oct 01 2021 12:24:16")
    comment480 = Comment(videoId=387, channelId=35, content="With a single flip of the coin, his life changed forever.", createdAt="Fri Oct 22 2021 03:55:10", updatedAt="Sun Nov 14 2021 04:15:13")
    comment481 = Comment(videoId=683, channelId=97, content="Flash photography is best used in full sunlight.", createdAt="Sat Sep 25 2021 08:36:02", updatedAt="Thu Jun 03 2021 09:33:17")
    comment482 = Comment(videoId=254, channelId=75, content="The trick to getting kids to eat anything is to put catchup on it.", createdAt="Fri Jan 07 2022 01:11:51", updatedAt="Fri Nov 19 2021 00:21:08")
    comment483 = Comment(videoId=649, channelId=14, content="Iguanas were falling out of the trees.", createdAt="Tue Mar 15 2022 14:45:00", updatedAt="Mon May 03 2021 03:23:41")
    comment484 = Comment(videoId=330, channelId=52, content="Charles ate the french fries knowing they would be his last meal.", createdAt="Wed Jul 28 2021 22:29:36", updatedAt="Sat Mar 12 2022 09:07:45")
    comment485 = Comment(videoId=479, channelId=13, content="People generally approve of dogs eating cat food but not cats eating dog food.", createdAt="Sun Aug 08 2021 03:09:48", updatedAt="Thu May 27 2021 10:29:04")
    comment486 = Comment(videoId=342, channelId=10, content="The father died during childbirth.", createdAt="Mon Apr 04 2022 18:56:36", updatedAt="Tue Nov 09 2021 01:04:34")
    comment487 = Comment(videoId=601, channelId=14, content="The waitress was not amused when he ordered green eggs and ham.", createdAt="Mon Nov 15 2021 04:22:09", updatedAt="Sun Feb 06 2022 04:15:44")
    comment488 = Comment(videoId=608, channelId=26, content="He decided to fake his disappearance to avoid jail.", createdAt="Mon Aug 16 2021 14:16:28", updatedAt="Thu Sep 23 2021 15:57:55")
    comment489 = Comment(videoId=728, channelId=84, content="Purple is the best city in the forest.", createdAt="Mon Nov 01 2021 19:23:25", updatedAt="Thu Feb 24 2022 23:12:31")
    comment490 = Comment(videoId=231, channelId=80, content="Buried deep in the snow, he hoped his batteries were fresh in his avalanche beacon.", createdAt="Wed Feb 09 2022 15:05:17", updatedAt="Tue May 11 2021 00:24:34")
    comment491 = Comment(videoId=471, channelId=100, content="He took one look at what was under the table and noped the hell out of there.", createdAt="Sat Mar 05 2022 13:55:28", updatedAt="Fri Aug 06 2021 03:02:57")
    comment492 = Comment(videoId=376, channelId=75, content="He kept telling himself that one day it would all somehow make sense.", createdAt="Tue Oct 12 2021 18:49:33", updatedAt="Fri Jan 07 2022 07:49:27")
    comment493 = Comment(videoId=34, channelId=14, content="Nothing seemed out of place except the washing machine in the bar.", createdAt="Sun Feb 20 2022 08:57:06", updatedAt="Mon Oct 18 2021 20:11:08")
    comment494 = Comment(videoId=446, channelId=71, content="I'd always thought lightning was something only I could see.", createdAt="Mon Mar 21 2022 18:22:14", updatedAt="Thu Jul 15 2021 08:43:34")
    comment495 = Comment(videoId=585, channelId=51, content="Chocolate covered crickets were his favorite snack.", createdAt="Wed Jul 07 2021 20:17:58", updatedAt="Thu Mar 03 2022 00:15:30")
    comment496 = Comment(videoId=229, channelId=28, content="Weather is not trivial - it's especially important when you're standing in it.", createdAt="Thu Jun 10 2021 14:24:48", updatedAt="Tue Mar 15 2022 23:27:55")
    comment497 = Comment(videoId=749, channelId=64, content="You're good at English when you know the difference between a man eating chicken and a man-eating chicken.", createdAt="Fri Jul 16 2021 23:20:36", updatedAt="Sun Aug 29 2021 11:48:06")
    comment498 = Comment(videoId=477, channelId=51, content="Dolores wouldn't have eaten the meal if she had known what it actually was.", createdAt="Tue Nov 30 2021 11:47:10", updatedAt="Mon Apr 12 2021 01:22:36")
    comment499 = Comment(videoId=597, channelId=26, content="He was the only member of the club who didn't like plum pudding.", createdAt="Sat Jan 15 2022 03:58:19", updatedAt="Sat Apr 17 2021 21:12:36")
    comment500 = Comment(videoId=723, channelId=36, content="They improved dramatically once the lead singer left.", createdAt="Wed Mar 16 2022 09:45:34", updatedAt="Mon Jun 14 2021 06:50:38")
    comment501 = Comment(videoId=234, channelId=54, content="Just go ahead and press that button.", createdAt="Thu Dec 16 2021 19:40:29", updatedAt="Mon Dec 13 2021 10:36:10")
    comment502 = Comment(videoId=234, channelId=45, content="All you need to do is pick up the pen and begin.", createdAt="Wed Jan 12 2022 23:30:14", updatedAt="Mon Mar 21 2022 17:07:36")
    comment503 = Comment(videoId=531, channelId=86, content="Art doesn't have to be intentional.", createdAt="Fri Apr 08 2022 08:20:25", updatedAt="Tue Jun 29 2021 21:33:31")
    comment504 = Comment(videoId=82, channelId=39, content="She had the gift of being able to paint songs.", createdAt="Tue Dec 07 2021 05:18:29", updatedAt="Wed Nov 17 2021 08:10:41")
    comment505 = Comment(videoId=108, channelId=66, content="He didn't heed the warning and it had turned out surprisingly well.", createdAt="Sun Aug 01 2021 23:42:46", updatedAt="Wed Dec 29 2021 20:40:21")
    comment506 = Comment(videoId=435, channelId=15, content="Cats are good pets, for they are clean and are not noisy.", createdAt="Wed Apr 21 2021 04:12:33", updatedAt="Mon Dec 20 2021 00:07:52")
    comment507 = Comment(videoId=500, channelId=48, content="On each full moon", createdAt="Wed May 19 2021 21:38:11", updatedAt="Sat Jun 12 2021 00:50:00")
    comment508 = Comment(videoId=643, channelId=12, content="When I cook spaghetti, I like to boil it a few minutes past al dente so the noodles are super slippery.", createdAt="Tue Mar 29 2022 17:32:10", updatedAt="Sun Nov 28 2021 18:29:24")
    comment509 = Comment(videoId=313, channelId=78, content="You bite up because of your lower jaw.", createdAt="Tue Oct 19 2021 20:43:56", updatedAt="Fri Dec 10 2021 10:08:48")
    comment510 = Comment(videoId=93, channelId=62, content="Don't put peanut butter on the dog's nose.", createdAt="Thu Jan 20 2022 06:40:12", updatedAt="Fri Nov 05 2021 07:16:37")
    comment511 = Comment(videoId=83, channelId=32, content="If eating three-egg omelets causes weight-gain, budgie eggs are a good substitute.", createdAt="Wed Apr 14 2021 09:44:22", updatedAt="Tue Aug 03 2021 10:21:54")
    comment512 = Comment(videoId=141, channelId=34, content="Imagine his surprise when he discovered that the safe was full of pudding.", createdAt="Thu Mar 17 2022 14:44:50", updatedAt="Sun Feb 06 2022 07:23:16")
    comment513 = Comment(videoId=522, channelId=26, content="The hand sanitizer was actually clear glue.", createdAt="Mon Jan 24 2022 19:39:39", updatedAt="Sun Dec 19 2021 14:46:02")
    comment514 = Comment(videoId=480, channelId=15, content="On a scale from one to ten, what's your favorite flavor of random grammar?", createdAt="Mon Jan 31 2022 18:03:42", updatedAt="Thu Nov 11 2021 01:53:31")
    comment515 = Comment(videoId=6, channelId=62, content="The father handed each child a roadmap at the beginning of the 2-day road trip and explained it was so they could find their way home.", createdAt="Sun Aug 15 2021 00:41:40", updatedAt="Mon Sep 13 2021 16:26:35")
    comment516 = Comment(videoId=15, channelId=96, content="It took me too long to realize that the ceiling hadn't been painted to look like the sky.", createdAt="Mon Nov 29 2021 16:34:36", updatedAt="Fri Jan 28 2022 15:34:22")
    comment517 = Comment(videoId=773, channelId=16, content="It's not often you find a soggy banana on the street.", createdAt="Sun Oct 31 2021 04:10:31", updatedAt="Sat Dec 25 2021 03:53:33")
    comment518 = Comment(videoId=14, channelId=45, content="Trash covered the landscape like sprinkles do a birthday cake.", createdAt="Sat Mar 26 2022 08:24:39", updatedAt="Sun Mar 20 2022 11:56:18")
    comment519 = Comment(videoId=569, channelId=55, content="He wondered why at 18 he was old enough to go to war, but not old enough to buy cigarettes.", createdAt="Tue Aug 17 2021 03:58:04", updatedAt="Mon Oct 25 2021 00:26:47")
    comment520 = Comment(videoId=135, channelId=38, content="They decided to plant an orchard of cotton candy.", createdAt="Wed May 26 2021 15:56:30", updatedAt="Sun May 30 2021 00:48:20")
    comment521 = Comment(videoId=724, channelId=94, content="So long and thanks for the fish.", createdAt="Sun Sep 05 2021 13:46:42", updatedAt="Mon Oct 25 2021 17:58:23")
    comment522 = Comment(videoId=442, channelId=92, content="He was sure the Devil created red sparkly glitter.", createdAt="Sat Aug 14 2021 08:29:34", updatedAt="Mon Jan 10 2022 01:04:32")
    comment523 = Comment(videoId=483, channelId=20, content="He created a pig burger out of beef.", createdAt="Tue Oct 05 2021 02:50:14", updatedAt="Thu Feb 03 2022 23:17:29")
    comment524 = Comment(videoId=637, channelId=78, content="It isn't true that my mattress is made of cotton candy.", createdAt="Sat Sep 11 2021 22:48:18", updatedAt="Thu Jan 27 2022 11:17:51")
    comment525 = Comment(videoId=721, channelId=12, content="At last", createdAt="Mon Apr 26 2021 21:42:32", updatedAt="Mon Aug 16 2021 15:35:26")
    comment526 = Comment(videoId=112, channelId=79, content="I was very proud of my nickname throughout high school but today- I couldn’t be any different to what my nickname was.", createdAt="Sun Aug 29 2021 00:59:23", updatedAt="Mon Nov 08 2021 02:44:53")
    comment527 = Comment(videoId=706, channelId=6, content="People generally approve of dogs eating cat food but not cats eating dog food.", createdAt="Sat Nov 13 2021 10:29:25", updatedAt="Mon Nov 15 2021 02:59:23")
    comment528 = Comment(videoId=162, channelId=23, content="She always had an interesting perspective on why the world must be flat.", createdAt="Mon Jul 19 2021 03:59:44", updatedAt="Wed Sep 01 2021 16:45:20")
    comment529 = Comment(videoId=157, channelId=36, content="She saw no irony asking me to change but wanting me to accept her for who she is.", createdAt="Sat Feb 26 2022 01:43:03", updatedAt="Sun Mar 13 2022 14:47:03")
    comment530 = Comment(videoId=84, channelId=20, content="All she wanted was the answer, but she had no idea how much she would hate it.", createdAt="Fri Jun 04 2021 10:51:56", updatedAt="Thu Jan 06 2022 10:40:50")
    comment531 = Comment(videoId=690, channelId=51, content="The glacier came alive as the climbers hiked closer.", createdAt="Sat Apr 17 2021 12:16:19", updatedAt="Tue Jul 20 2021 17:27:52")
    comment533 = Comment(videoId=332, channelId=2, content="The irony of the situation wasn't lost on anyone in the room.", createdAt="Thu Dec 09 2021 21:56:31", updatedAt="Wed Aug 04 2021 14:46:45")
    comment534 = Comment(videoId=190, channelId=39, content="Lucifer was surprised at the amount of life at Death Valley.", createdAt="Tue Feb 22 2022 18:34:26", updatedAt="Fri Sep 17 2021 14:14:58")
    comment535 = Comment(videoId=529, channelId=7, content="Everyone pretends to like wheat until you mention barley.", createdAt="Thu Aug 12 2021 02:01:23", updatedAt="Sat May 22 2021 21:04:35")
    comment536 = Comment(videoId=719, channelId=50, content="He decided water-skiing on a frozen lake wasn’t a good idea.", createdAt="Wed Sep 22 2021 08:29:48", updatedAt="Tue Jul 06 2021 10:28:08")
    comment537 = Comment(videoId=653, channelId=45, content="The manager of the fruit stand always sat and only sold vegetables.", createdAt="Thu Sep 23 2021 00:35:55", updatedAt="Fri Feb 18 2022 22:04:26")
    comment538 = Comment(videoId=238, channelId=19, content="When motorists sped in and out of traffic, all she could think of was those in need of a transplant.", createdAt="Thu Nov 04 2021 18:04:58", updatedAt="Sat Apr 24 2021 11:53:59")
    comment539 = Comment(videoId=195, channelId=18, content="There is no better feeling than staring at a wall with closed eyes.", createdAt="Wed Nov 24 2021 16:10:47", updatedAt="Fri Apr 16 2021 14:05:22")
    comment540 = Comment(videoId=684, channelId=28, content="The sight of his goatee made me want to run and hide under my sister-in-law's bed.", createdAt="Sun May 16 2021 14:00:36", updatedAt="Fri Aug 13 2021 06:58:23")
    comment541 = Comment(videoId=389, channelId=57, content="Peanuts don't grow on trees, but cashews do.", createdAt="Sun May 30 2021 16:34:08", updatedAt="Tue Jun 29 2021 07:18:29")
    comment542 = Comment(videoId=669, channelId=73, content="There's a message for you if you look up.", createdAt="Sat Nov 13 2021 04:42:13", updatedAt="Tue Dec 28 2021 09:58:49")
    comment543 = Comment(videoId=727, channelId=49, content="No matter how beautiful the sunset, it saddened her knowing she was one day older.", createdAt="Tue Oct 05 2021 02:57:59", updatedAt="Tue Apr 27 2021 12:47:50")
    comment544 = Comment(videoId=562, channelId=72, content="Standing on one's head at job interviews forms a lasting impression.", createdAt="Sun Mar 06 2022 02:41:55", updatedAt="Fri Dec 03 2021 03:13:56")
    comment545 = Comment(videoId=309, channelId=71, content="The random sentence generator generated a random sentence about a random sentence.", createdAt="Mon Aug 23 2021 10:16:40", updatedAt="Sun Feb 27 2022 06:23:30")
    comment546 = Comment(videoId=84, channelId=31, content="The tattered work gloves speak of the many hours of hard labor he endured throughout his life.", createdAt="Thu May 06 2021 00:12:36", updatedAt="Sat Oct 09 2021 12:12:49")
    comment547 = Comment(videoId=547, channelId=55, content="When he encountered maize for the first time, he thought it incredibly corny.", createdAt="Mon Sep 13 2021 13:23:27", updatedAt="Wed Mar 09 2022 17:30:00")
    comment548 = Comment(videoId=737, channelId=76, content="He had a hidden stash underneath the floorboards in the back room of the house.", createdAt="Wed Oct 13 2021 21:52:32", updatedAt="Mon Sep 13 2021 00:49:16")
    comment549 = Comment(videoId=747, channelId=84, content="Shakespeare was a famous 17th-century diesel mechanic.", createdAt="Sat Aug 07 2021 15:28:32", updatedAt="Fri Mar 04 2022 09:28:15")
    comment550 = Comment(videoId=72, channelId=23, content="I caught my squirrel rustling through my gym bag.", createdAt="Sat May 15 2021 18:03:44", updatedAt="Tue Aug 10 2021 08:47:40")
    comment551 = Comment(videoId=482, channelId=35, content="There were three sphered rocks congregating in a cubed room.", createdAt="Sun Jul 04 2021 02:22:47", updatedAt="Fri Aug 27 2021 11:01:22")
    comment552 = Comment(videoId=693, channelId=9, content="I was starting to worry that my pet turtle could tell what I was thinking.", createdAt="Wed Apr 21 2021 00:39:51", updatedAt="Mon Nov 29 2021 23:38:24")
    comment553 = Comment(videoId=559, channelId=87, content="Tuesdays are free if you bring a gnome costume.", createdAt="Thu Sep 02 2021 17:21:56", updatedAt="Tue Mar 22 2022 09:25:18")
    comment554 = Comment(videoId=338, channelId=61, content="Three years later, the coffin was still full of Jello.", createdAt="Sat Apr 10 2021 19:16:11", updatedAt="Tue May 25 2021 11:13:18")
    comment555 = Comment(videoId=331, channelId=16, content="I love eating toasted cheese and tuna sandwiches.", createdAt="Fri Jul 02 2021 20:40:07", updatedAt="Tue Feb 01 2022 03:32:42")
    comment556 = Comment(videoId=428, channelId=3, content="His ultimate dream fantasy consisted of being content and sleeping eight hours in a row.", createdAt="Sat Aug 07 2021 12:28:52", updatedAt="Mon Jun 28 2021 07:58:25")
    comment558 = Comment(videoId=584, channelId=96, content="He was the only member of the club who didn't like plum pudding.", createdAt="Tue Dec 21 2021 02:56:14", updatedAt="Fri Sep 10 2021 21:49:30")
    comment559 = Comment(videoId=95, channelId=57, content="The teens wondered what was kept in the red shed on the far edge of the school grounds.", createdAt="Fri Jan 07 2022 16:29:48", updatedAt="Sun Oct 10 2021 01:50:40")
    comment560 = Comment(videoId=585, channelId=75, content="Abstraction is often one floor above you.", createdAt="Sat Sep 04 2021 07:56:53", updatedAt="Fri Jan 21 2022 06:45:36")
    comment561 = Comment(videoId=276, channelId=57, content="Peter found road kill an excellent way to save money on dinner.", createdAt="Sat Apr 02 2022 20:48:53", updatedAt="Thu Jun 24 2021 23:49:55")
    comment562 = Comment(videoId=103, channelId=59, content="You should never take advice from someone who thinks red paint dries quicker than blue paint.", createdAt="Sat Apr 09 2022 02:53:29", updatedAt="Sat Mar 12 2022 14:56:23")
    comment563 = Comment(videoId=12, channelId=11, content="They did nothing as the raccoon attacked the lady’s bag of food.", createdAt="Thu Mar 03 2022 01:20:47", updatedAt="Mon May 10 2021 09:58:24")
    comment564 = Comment(videoId=634, channelId=64, content="The dead trees waited to be ignited by the smallest spark and seek their revenge.", createdAt="Wed Mar 23 2022 15:04:18", updatedAt="Mon Oct 11 2021 15:18:44")
    comment565 = Comment(videoId=666, channelId=71, content="Just go ahead and press that button.", createdAt="Sun May 16 2021 06:49:40", updatedAt="Wed Aug 25 2021 06:02:04")
    comment566 = Comment(videoId=67, channelId=1, content="Pantyhose and heels are an interesting choice of attire for the beach.", createdAt="Tue Dec 21 2021 10:32:35", updatedAt="Sat Jun 12 2021 09:01:19")
    comment567 = Comment(videoId=417, channelId=49, content="We should play with legos at camp.", createdAt="Wed Jun 23 2021 14:43:37", updatedAt="Mon Feb 07 2022 23:56:47")
    comment568 = Comment(videoId=643, channelId=74, content="Baby wipes are made of chocolate stardust.", createdAt="Sun Mar 06 2022 02:56:10", updatedAt="Wed Jul 21 2021 22:46:46")
    comment569 = Comment(videoId=293, channelId=86, content="Sometimes you have to just give up and win by cheating.", createdAt="Thu Oct 21 2021 10:43:37", updatedAt="Wed Dec 29 2021 00:52:20")
    comment570 = Comment(videoId=335, channelId=53, content="Jim liked driving around town with his hazard lights on.", createdAt="Sun Sep 05 2021 15:39:02", updatedAt="Thu Apr 15 2021 17:01:46")
    comment571 = Comment(videoId=569, channelId=96, content="The manager of the fruit stand always sat and only sold vegetables.", createdAt="Fri Aug 27 2021 18:18:32", updatedAt="Sat Feb 05 2022 10:28:21")
    comment572 = Comment(videoId=105, channelId=83, content="He hated that he loved what she hated about hate.", createdAt="Sun Jun 27 2021 04:22:01", updatedAt="Wed Oct 20 2021 03:24:41")
    comment573 = Comment(videoId=503, channelId=15, content="He realized there had been several deaths on this road, but his concern rose when he saw the exact number.", createdAt="Sun Feb 27 2022 09:48:14", updatedAt="Wed Aug 04 2021 07:39:38")
    comment574 = Comment(videoId=649, channelId=77, content="The hummingbird's wings blurred while it eagerly sipped the sugar water from the feeder.", createdAt="Thu Mar 24 2022 11:11:36", updatedAt="Tue Jul 20 2021 02:04:04")
    comment575 = Comment(videoId=578, channelId=29, content="Despite multiple complications and her near-death experience", createdAt="Tue Aug 31 2021 13:56:58", updatedAt="Sat Feb 12 2022 23:08:18")
    comment576 = Comment(videoId=665, channelId=26, content="I covered my friend in baby oil.", createdAt="Tue Apr 27 2021 18:13:07", updatedAt="Wed Jan 12 2022 18:28:37")
    comment577 = Comment(videoId=369, channelId=81, content="Choosing to do nothing is still a choice, after all.", createdAt="Sat Oct 23 2021 03:39:27", updatedAt="Wed Aug 25 2021 05:04:00")
    comment578 = Comment(videoId=615, channelId=56, content="This book is sure to liquefy your brain.", createdAt="Wed Jun 30 2021 09:01:01", updatedAt="Sun Jun 13 2021 21:44:46")
    comment579 = Comment(videoId=57, channelId=60, content="Green should have smelled more tranquil, but somehow it just tasted rotten.", createdAt="Wed Jun 16 2021 21:34:18", updatedAt="Sat Jan 01 2022 21:54:11")
    comment580 = Comment(videoId=486, channelId=39, content="At last", createdAt="Tue Dec 28 2021 02:26:10", updatedAt="Wed Mar 30 2022 13:28:18")
    comment581 = Comment(videoId=511, channelId=85, content="The book is in front of the table.", createdAt="Thu Mar 17 2022 17:04:16", updatedAt="Sat Jun 26 2021 19:57:23")
    comment582 = Comment(videoId=398, channelId=92, content="The sun had set and so had his dreams.", createdAt="Tue Dec 07 2021 07:04:10", updatedAt="Fri Oct 15 2021 23:40:49")
    comment583 = Comment(videoId=670, channelId=100, content="Normal activities took extraordinary amounts of concentration at the high altitude.", createdAt="Sun Aug 08 2021 17:48:16", updatedAt="Wed Sep 29 2021 00:18:20")
    comment584 = Comment(videoId=441, channelId=58, content="It was the best sandcastle he had ever seen.", createdAt="Thu Dec 23 2021 01:33:26", updatedAt="Sun Jul 04 2021 11:35:50")
    comment585 = Comment(videoId=285, channelId=61, content="It was the scarcity that fueled his creativity.", createdAt="Thu Sep 16 2021 09:14:26", updatedAt="Mon Mar 28 2022 02:53:54")
    comment586 = Comment(videoId=430, channelId=83, content="His son quipped that power bars were nothing more than adult candy bars.", createdAt="Tue Mar 08 2022 08:07:40", updatedAt="Sat May 22 2021 23:08:18")
    comment588 = Comment(videoId=47, channelId=32, content="You have no right to call yourself creative until you look at a trowel and think that it would make a great lockpick.", createdAt="Mon Oct 11 2021 10:01:16", updatedAt="Sun Aug 22 2021 13:44:56")
    comment589 = Comment(videoId=361, channelId=71, content="All she wanted was the answer, but she had no idea how much she would hate it.", createdAt="Sun May 09 2021 05:02:44", updatedAt="Fri Oct 01 2021 14:25:04")
    comment590 = Comment(videoId=756, channelId=39, content="Mr. Montoya knows the way to the bakery even though he's never been there.", createdAt="Sat Dec 18 2021 18:02:12", updatedAt="Wed Jan 26 2022 05:47:06")
    comment591 = Comment(videoId=299, channelId=95, content="Mary plays the piano.", createdAt="Thu Oct 28 2021 19:25:12", updatedAt="Thu Mar 31 2022 14:23:33")
    comment592 = Comment(videoId=10, channelId=8, content="I had a friend in high school named Rick Shaw, but he was fairly useless as a mode of transport.", createdAt="Mon Feb 21 2022 20:49:17", updatedAt="Mon Mar 28 2022 10:15:57")
    comment593 = Comment(videoId=585, channelId=70, content="I would have gotten the promotion, but my attendance wasn’t good enough.", createdAt="Sat Jan 15 2022 16:44:22", updatedAt="Sat Oct 09 2021 21:45:42")
    comment594 = Comment(videoId=725, channelId=73, content="There are no heroes in a punk rock band.", createdAt="Sun Oct 24 2021 03:22:04", updatedAt="Mon Apr 26 2021 01:21:43")
    comment595 = Comment(videoId=625, channelId=9, content="Let me help you with your baggage.", createdAt="Fri Sep 17 2021 13:30:14", updatedAt="Sun Feb 27 2022 22:18:20")
    comment596 = Comment(videoId=97, channelId=31, content="Siri became confused when we reused to follow her directions.", createdAt="Thu Apr 07 2022 14:39:55", updatedAt="Sat Dec 25 2021 10:55:52")
    comment597 = Comment(videoId=319, channelId=91, content="She wasn't sure whether to be impressed or concerned that he folded underwear in neat little packages.", createdAt="Sun Nov 14 2021 19:13:35", updatedAt="Sat Jan 29 2022 17:55:25")
    comment598 = Comment(videoId=322, channelId=49, content="Henry couldn't decide if he was an auto mechanic or a priest.", createdAt="Tue Mar 08 2022 21:40:43", updatedAt="Sun Oct 24 2021 22:31:36")
    comment599 = Comment(videoId=569, channelId=50, content="The efficiency with which he paired the socks in the drawer was quite admirable.", createdAt="Mon May 03 2021 07:41:51", updatedAt="Mon Oct 04 2021 17:14:14")
    comment600 = Comment(videoId=410, channelId=34, content="I used to practice weaving with spaghetti three hours a day but stopped because I didn't want to die alone.", createdAt="Wed Jun 09 2021 17:59:10", updatedAt="Thu Sep 09 2021 09:37:20")
    comment601 = Comment(videoId=385, channelId=1, content="Three years later, the coffin was still full of Jello.", createdAt="Wed Mar 30 2022 13:48:14", updatedAt="Tue Apr 20 2021 03:47:39")
    comment602 = Comment(videoId=601, channelId=22, content="Too many prisons have become early coffins.", createdAt="Thu Apr 07 2022 07:10:05", updatedAt="Tue Oct 26 2021 07:06:19")
    comment603 = Comment(videoId=74, channelId=2, content="As the years pass by, we all know owners look more and more like their dogs.", createdAt="Thu Apr 15 2021 15:44:08", updatedAt="Sun Jan 23 2022 18:32:34")
    comment604 = Comment(videoId=167, channelId=23, content="Twin 4-month-olds slept in the shade of the palm tree while the mother tanned in the sun.", createdAt="Thu Jun 10 2021 23:10:59", updatedAt="Thu Feb 03 2022 19:52:17")
    comment605 = Comment(videoId=743, channelId=55, content="The waitress was not amused when he ordered green eggs and ham.", createdAt="Sat Aug 07 2021 10:53:28", updatedAt="Wed Nov 10 2021 12:43:52")
    comment606 = Comment(videoId=35, channelId=55, content="Jenny made the announcement that her baby was an alien.", createdAt="Tue Sep 28 2021 20:38:17", updatedAt="Wed Aug 04 2021 17:41:49")
    comment607 = Comment(videoId=662, channelId=6, content="They decided to plant an orchard of cotton candy.", createdAt="Wed Jan 12 2022 10:50:59", updatedAt="Wed Sep 08 2021 21:01:51")
    comment608 = Comment(videoId=352, channelId=76, content="The minute she landed she understood the reason this was a fly-over state.", createdAt="Fri Jun 25 2021 20:58:25", updatedAt="Wed Sep 15 2021 00:15:16")
    comment609 = Comment(videoId=641, channelId=7, content="They got there early, and they got really good seats.", createdAt="Fri Dec 10 2021 00:32:14", updatedAt="Fri Jun 04 2021 11:36:50")
    comment610 = Comment(videoId=660, channelId=16, content="He embraced his new life as an eggplant.", createdAt="Fri Apr 01 2022 18:21:21", updatedAt="Tue Sep 14 2021 19:57:26")
    comment611 = Comment(videoId=669, channelId=28, content="I've never seen a more beautiful brandy glass filled with wine.", createdAt="Wed Aug 11 2021 12:10:10", updatedAt="Tue Oct 19 2021 11:44:56")
    comment612 = Comment(videoId=648, channelId=11, content="It didn't make sense unless you had the power to eat colors.", createdAt="Wed Nov 03 2021 00:02:16", updatedAt="Fri Oct 15 2021 01:35:08")
    comment613 = Comment(videoId=69, channelId=25, content="She had a difficult time owning up to her own crazy self.", createdAt="Sat Sep 04 2021 11:43:56", updatedAt="Sat Dec 11 2021 00:46:42")
    comment614 = Comment(videoId=211, channelId=97, content="They're playing the piano while flying in the plane.", createdAt="Wed Dec 22 2021 11:10:15", updatedAt="Sat Oct 23 2021 22:35:47")
    comment615 = Comment(videoId=575, channelId=30, content="Today I heard something new and unmemorable.", createdAt="Fri Sep 03 2021 17:32:56", updatedAt="Fri Jan 07 2022 10:05:23")
    comment616 = Comment(videoId=89, channelId=53, content="The blinking lights of the antenna tower came into focus just as I heard a loud snap.", createdAt="Wed Dec 15 2021 17:06:00", updatedAt="Fri Jul 16 2021 23:35:23")
    comment617 = Comment(videoId=690, channelId=70, content="The secret code they created made no sense, even to them.", createdAt="Fri Dec 24 2021 15:42:23", updatedAt="Tue May 25 2021 08:33:40")
    comment618 = Comment(videoId=73, channelId=9, content="The clouds formed beautiful animals in the sky that eventually created a tornado to wreak havoc.", createdAt="Tue Jul 06 2021 09:48:34", updatedAt="Sat Apr 09 2022 06:24:40")
    comment619 = Comment(videoId=624, channelId=13, content="It must be easy to commit crimes as a snake because you don't have to worry about leaving fingerprints.", createdAt="Mon Sep 06 2021 20:11:26", updatedAt="Sat Sep 25 2021 23:29:31")
    comment620 = Comment(videoId=106, channelId=80, content="The worst thing about being at the top of the career ladder is that there's a long way to fall.", createdAt="Fri Aug 27 2021 16:54:58", updatedAt="Wed Sep 01 2021 12:33:58")
    comment621 = Comment(videoId=656, channelId=98, content="She opened up her third bottle of wine of the night.", createdAt="Sun Aug 22 2021 19:36:28", updatedAt="Mon May 10 2021 04:45:19")
    comment622 = Comment(videoId=335, channelId=67, content="I thought red would have felt warmer in summer but I didn't think about the equator.", createdAt="Thu Jul 08 2021 11:43:02", updatedAt="Fri Jan 28 2022 19:19:36")
    comment623 = Comment(videoId=576, channelId=87, content="The doll spun around in circles in hopes of coming alive.", createdAt="Sun Jun 13 2021 07:59:25", updatedAt="Sun Feb 06 2022 10:57:32")
    comment624 = Comment(videoId=673, channelId=29, content="I honestly find her about as intimidating as a basket of kittens.", createdAt="Wed Nov 10 2021 20:43:21", updatedAt="Fri May 14 2021 19:31:11")
    comment625 = Comment(videoId=533, channelId=42, content="She saw the brake lights, but not in time.", createdAt="Wed Dec 08 2021 17:15:42", updatedAt="Wed May 12 2021 05:58:29")
    comment626 = Comment(videoId=357, channelId=94, content="My biggest joy is roasting almonds while stalking prey.", createdAt="Sat Apr 09 2022 07:27:43", updatedAt="Fri Jan 14 2022 08:58:48")
    comment627 = Comment(videoId=136, channelId=47, content="He was so preoccupied with whether or not he could that he failed to stop to consider if he should.", createdAt="Tue Jul 06 2021 03:08:06", updatedAt="Tue Jan 04 2022 03:17:07")
    comment628 = Comment(videoId=644, channelId=9, content="As he waited for the shower to warm, he noticed that he could hear water change temperature.", createdAt="Wed Sep 22 2021 14:31:46", updatedAt="Fri Apr 30 2021 05:00:04")
    comment629 = Comment(videoId=157, channelId=20, content="My Mum tries to be cool by saying that she likes all the same things that I do.", createdAt="Mon Oct 04 2021 09:10:07", updatedAt="Thu Jul 22 2021 11:33:07")
    comment630 = Comment(videoId=611, channelId=72, content="She did a happy dance because all of the socks from the dryer matched.", createdAt="Sat Apr 24 2021 13:22:19", updatedAt="Tue Jul 06 2021 06:20:02")
    comment631 = Comment(videoId=298, channelId=57, content="Sarah ran from the serial killer holding a jug of milk.", createdAt="Thu Feb 17 2022 02:36:08", updatedAt="Wed Oct 13 2021 05:43:20")
    comment632 = Comment(videoId=332, channelId=62, content="When motorists sped in and out of traffic, all she could think of was those in need of a transplant.", createdAt="Wed May 26 2021 18:13:51", updatedAt="Mon Jun 07 2021 21:28:45")
    comment633 = Comment(videoId=638, channelId=56, content="He dreamed of leaving his law firm to open a portable dog wash.", createdAt="Thu Apr 07 2022 03:45:26", updatedAt="Wed Aug 11 2021 13:25:47")
    comment634 = Comment(videoId=88, channelId=45, content="He found the end of the rainbow and was surprised at what he found there.", createdAt="Sun Jan 16 2022 08:39:41", updatedAt="Fri Jul 23 2021 09:14:43")
    comment635 = Comment(videoId=11, channelId=98, content="Sometimes, all you need to do is completely make an ass of yourself and laugh it off to realise that life isn’t so bad after all.", createdAt="Thu Apr 29 2021 23:03:39", updatedAt="Sat Jan 22 2022 08:20:41")
    comment636 = Comment(videoId=216, channelId=51, content="It's not often you find a soggy banana on the street.", createdAt="Tue Nov 30 2021 19:31:46", updatedAt="Mon Mar 28 2022 18:15:47")
    comment637 = Comment(videoId=296, channelId=39, content="Acres of almond trees lined the interstate highway which complimented the crazy driving nuts.", createdAt="Sat Aug 28 2021 11:14:16", updatedAt="Thu May 13 2021 22:45:03")
    comment638 = Comment(videoId=80, channelId=50, content="The opportunity of a lifetime passed before him as he tried to decide between a cone or a cup.", createdAt="Mon Apr 26 2021 09:07:53", updatedAt="Wed Jan 19 2022 22:02:57")
    comment639 = Comment(videoId=14, channelId=24, content="At last", createdAt="Fri Dec 10 2021 20:17:28", updatedAt="Sat Oct 30 2021 00:35:13")
    comment641 = Comment(videoId=602, channelId=40, content="The blue parrot drove by the hitchhiking mongoose.", createdAt="Fri Mar 18 2022 21:12:02", updatedAt="Fri Jun 04 2021 06:44:27")
    comment642 = Comment(videoId=208, channelId=86, content="It took him a while to realize that everything he decided not to change, he was actually choosing.", createdAt="Mon Nov 22 2021 11:28:04", updatedAt="Mon Apr 26 2021 15:59:00")
    comment643 = Comment(videoId=624, channelId=52, content="I am counting my calories, yet I really want dessert.", createdAt="Mon Dec 20 2021 10:12:07", updatedAt="Sun Jun 27 2021 06:18:38")
    comment645 = Comment(videoId=545, channelId=92, content="He walked into the basement with the horror movie from the night before playing in his head.", createdAt="Wed Feb 16 2022 19:19:40", updatedAt="Fri Jan 21 2022 06:56:57")
    comment646 = Comment(videoId=671, channelId=26, content="There's a reason that roses have thorns.", createdAt="Thu Jul 08 2021 21:01:31", updatedAt="Sat Sep 25 2021 19:19:54")
    comment647 = Comment(videoId=672, channelId=40, content="The tortoise jumped into the lake with dreams of becoming a sea turtle.", createdAt="Wed Jun 16 2021 09:08:32", updatedAt="Tue Dec 21 2021 18:29:49")
    comment648 = Comment(videoId=98, channelId=7, content="I never knew what hardship looked like until it started raining bowling balls.", createdAt="Mon Mar 28 2022 03:55:02", updatedAt="Fri Sep 24 2021 01:27:12")
    comment649 = Comment(videoId=515, channelId=18, content="Everyone was curious about the large white blimp that appeared overnight.", createdAt="Fri Mar 18 2022 13:23:40", updatedAt="Sun Aug 22 2021 21:24:54")
    comment650 = Comment(videoId=163, channelId=16, content="We should play with legos at camp.", createdAt="Tue Oct 05 2021 00:08:00", updatedAt="Sun Apr 18 2021 20:44:04")
    comment651 = Comment(videoId=207, channelId=48, content="If my calculator had a history, it would be more embarrassing than my browser history.", createdAt="Sun May 09 2021 20:33:00", updatedAt="Sat Jul 31 2021 01:54:17")
    comment652 = Comment(videoId=127, channelId=22, content="Mom didn’t understand why no one else wanted a hot tub full of jello.", createdAt="Sun Aug 22 2021 06:15:14", updatedAt="Mon Sep 20 2021 21:44:10")
    comment653 = Comment(videoId=420, channelId=14, content="I was very proud of my nickname throughout high school but today- I couldn’t be any different to what my nickname was.", createdAt="Tue Jul 20 2021 16:13:47", updatedAt="Tue Oct 19 2021 17:41:20")
    comment654 = Comment(videoId=383, channelId=36, content="The knives were out and she was sharpening hers.", createdAt="Sat Feb 19 2022 21:53:02", updatedAt="Wed Apr 21 2021 14:08:21")
    comment655 = Comment(videoId=11, channelId=74, content="She had a difficult time owning up to her own crazy self.", createdAt="Sun Feb 06 2022 10:49:30", updatedAt="Sun Jul 18 2021 05:10:05")
    comment656 = Comment(videoId=732, channelId=52, content="Erin accidentally created a new universe.", createdAt="Wed Feb 02 2022 12:57:00", updatedAt="Wed Apr 21 2021 12:37:09")
    comment657 = Comment(videoId=603, channelId=18, content="They wandered into a strange Tiki bar on the edge of the small beach town.", createdAt="Mon Nov 15 2021 07:42:52", updatedAt="Mon Dec 20 2021 16:54:36")
    comment658 = Comment(videoId=547, channelId=99, content="I think I will buy the red car, or I will lease the blue one.", createdAt="Fri Jun 18 2021 17:45:57", updatedAt="Sat Jul 24 2021 14:01:40")
    comment659 = Comment(videoId=76, channelId=41, content="She felt that chill that makes the hairs on the back of your neck when he walked into the room.", createdAt="Sun Mar 13 2022 16:30:46", updatedAt="Sat Apr 02 2022 18:12:23")
    comment660 = Comment(videoId=378, channelId=56, content="Bill ran from the giraffe toward the dolphin.", createdAt="Wed Jul 07 2021 09:22:34", updatedAt="Sat Mar 19 2022 09:37:33")
    comment661 = Comment(videoId=745, channelId=27, content="When she didn’t like a guy who was trying to pick her up, she started using sign language.", createdAt="Thu Feb 03 2022 01:12:51", updatedAt="Mon Aug 23 2021 02:10:40")
    comment662 = Comment(videoId=4, channelId=38, content="We need to rent a room for our party.", createdAt="Mon Jun 28 2021 15:04:27", updatedAt="Sat May 01 2021 01:48:07")
    comment663 = Comment(videoId=425, channelId=90, content="Nobody has encountered an explosive daisy and lived to tell the tale.", createdAt="Mon Dec 06 2021 23:47:43", updatedAt="Sat Sep 04 2021 06:52:07")
    comment665 = Comment(videoId=86, channelId=13, content="Of course, she loves her pink bunny slippers.", createdAt="Wed Jan 26 2022 08:59:07", updatedAt="Wed Sep 08 2021 12:05:46")
    comment666 = Comment(videoId=730, channelId=7, content="Her life in the confines of the house became her new normal.", createdAt="Fri Mar 11 2022 21:41:01", updatedAt="Sun Feb 06 2022 05:22:26")
    comment667 = Comment(videoId=461, channelId=43, content="I met an interesting turtle while the song on the radio blasted away.", createdAt="Fri Oct 01 2021 15:24:23", updatedAt="Wed Sep 08 2021 18:26:57")
    comment668 = Comment(videoId=509, channelId=68, content="The near-death experience brought new ideas to light.", createdAt="Tue Jul 20 2021 03:54:35", updatedAt="Sun Jun 20 2021 16:55:38")
    comment669 = Comment(videoId=75, channelId=27, content="Boulders lined the side of the road foretelling what could come next.", createdAt="Wed Dec 01 2021 07:28:16", updatedAt="Fri Jul 16 2021 16:45:20")
    comment670 = Comment(videoId=73, channelId=83, content="I'm not a party animal, but I do like animal parties.", createdAt="Sat Jan 08 2022 23:46:16", updatedAt="Sat Dec 11 2021 21:48:52")
    comment671 = Comment(videoId=82, channelId=85, content="We will not allow you to bring your pet armadillo along.", createdAt="Sun Jan 30 2022 06:51:50", updatedAt="Mon Jun 14 2021 06:25:54")
    comment672 = Comment(videoId=207, channelId=62, content="She wasn't sure whether to be impressed or concerned that he folded underwear in neat little packages.", createdAt="Fri Sep 10 2021 00:13:19", updatedAt="Mon Jul 19 2021 02:47:31")
    comment673 = Comment(videoId=210, channelId=64, content="The water flowing down the river didn’t look that powerful from the car", createdAt="Mon Mar 21 2022 04:01:53", updatedAt="Wed Mar 23 2022 19:03:57")
    comment674 = Comment(videoId=421, channelId=5, content="Nothing seemed out of place except the washing machine in the bar.", createdAt="Sat Aug 14 2021 02:41:20", updatedAt="Sun Mar 06 2022 22:52:58")
    comment675 = Comment(videoId=384, channelId=41, content="There have been days when I wished to be separated from my body, but today wasn’t one of those days.", createdAt="Sun Nov 21 2021 13:42:07", updatedAt="Fri Mar 04 2022 19:06:31")
    comment676 = Comment(videoId=418, channelId=82, content="He spiked his hair green to support his iguana.", createdAt="Mon Jul 19 2021 05:14:46", updatedAt="Wed Jul 07 2021 20:08:37")
    comment677 = Comment(videoId=188, channelId=29, content="He was the only member of the club who didn't like plum pudding.", createdAt="Sat Dec 18 2021 00:20:11", updatedAt="Sat Mar 19 2022 00:59:01")
    comment678 = Comment(videoId=428, channelId=98, content="Green should have smelled more tranquil, but somehow it just tasted rotten.", createdAt="Thu Jan 20 2022 20:12:41", updatedAt="Wed Oct 06 2021 03:23:57")
    comment679 = Comment(videoId=598, channelId=87, content="He found a leprechaun in his walnut shell.", createdAt="Mon Oct 11 2021 23:41:03", updatedAt="Sat May 22 2021 18:48:35")
    comment680 = Comment(videoId=674, channelId=2, content="The llama couldn't resist trying the lemonade.", createdAt="Tue Apr 27 2021 23:58:04", updatedAt="Thu Nov 25 2021 17:13:44")
    comment681 = Comment(videoId=325, channelId=26, content="I don’t respect anybody who can’t tell the difference between Pepsi and Coke.", createdAt="Tue Dec 21 2021 14:45:30", updatedAt="Fri Jul 23 2021 10:45:45")
    comment682 = Comment(videoId=370, channelId=43, content="It must be five o'clock somewhere.", createdAt="Tue Jan 11 2022 05:50:37", updatedAt="Fri Apr 16 2021 19:15:02")
    comment683 = Comment(videoId=193, channelId=93, content="Peanut butter and jelly caused the elderly lady to think about her past.", createdAt="Tue Jul 20 2021 03:28:12", updatedAt="Sat Jun 05 2021 07:40:37")
    comment684 = Comment(videoId=206, channelId=62, content="The light in his life was actually a fire burning all around him.", createdAt="Mon Dec 06 2021 18:29:21", updatedAt="Sun Mar 13 2022 17:31:08")
    comment685 = Comment(videoId=283, channelId=86, content="It was the scarcity that fueled his creativity.", createdAt="Wed Oct 06 2021 04:19:49", updatedAt="Fri Oct 15 2021 17:08:33")
    comment686 = Comment(videoId=289, channelId=72, content="Mothers spend months of their lives waiting on their children.", createdAt="Thu Jan 06 2022 01:03:58", updatedAt="Fri Jun 18 2021 16:04:47")
    comment687 = Comment(videoId=383, channelId=78, content="Poison ivy grew through the fence they said was impenetrable.", createdAt="Thu Jul 15 2021 17:42:58", updatedAt="Sun May 30 2021 23:26:16")
    comment688 = Comment(videoId=245, channelId=16, content="Always bring cinnamon buns on a deep-sea diving expedition.", createdAt="Mon Mar 14 2022 05:38:03", updatedAt="Thu Feb 10 2022 06:06:28")
    comment689 = Comment(videoId=285, channelId=54, content="I'd always thought lightning was something only I could see.", createdAt="Sat Nov 27 2021 07:59:27", updatedAt="Sun Jun 13 2021 23:29:16")
    comment690 = Comment(videoId=369, channelId=66, content="Never underestimate the willingness of the greedy to throw you under the bus.", createdAt="Wed Jul 14 2021 18:16:10", updatedAt="Tue Oct 19 2021 19:34:58")
    comment692 = Comment(videoId=776, channelId=28, content="He wondered if she would appreciate his toenail collection.", createdAt="Sat Oct 02 2021 16:42:06", updatedAt="Sun Oct 17 2021 11:16:04")
    comment693 = Comment(videoId=53, channelId=46, content="The furnace repairman indicated the heating system was acting as an air conditioner.", createdAt="Thu Dec 16 2021 16:35:59", updatedAt="Sun Oct 17 2021 11:21:39")
    comment694 = Comment(videoId=394, channelId=21, content="The toddler’s endless tantrum caused the entire plane anxiety.", createdAt="Fri Jul 09 2021 17:45:45", updatedAt="Wed Sep 08 2021 09:42:14")
    comment695 = Comment(videoId=496, channelId=7, content="The old apple revels in its authority.", createdAt="Mon Jan 10 2022 06:10:54", updatedAt="Sun Apr 25 2021 04:31:07")
    comment696 = Comment(videoId=323, channelId=52, content="The worst thing about being at the top of the career ladder is that there's a long way to fall.", createdAt="Sat Feb 26 2022 16:58:50", updatedAt="Thu Jan 27 2022 06:11:18")
    comment697 = Comment(videoId=333, channelId=73, content="She had some amazing news to share but nobody to share it with.", createdAt="Tue May 18 2021 17:16:45", updatedAt="Sun Feb 20 2022 05:10:27")
    comment698 = Comment(videoId=529, channelId=51, content="Sometimes I stare at a door or a wall and I wonder what is this reality, why am I alive, and what is this all about?", createdAt="Fri Mar 25 2022 09:46:19", updatedAt="Thu Oct 07 2021 01:12:00")
    comment699 = Comment(videoId=342, channelId=87, content="Let me help you with your baggage.", createdAt="Fri Jun 25 2021 05:02:05", updatedAt="Thu Jan 20 2022 16:55:59")
    comment700 = Comment(videoId=193, channelId=26, content="While all her friends were positive that Mary had a sixth sense, she knew she actually had a seventh sense.", createdAt="Fri Aug 27 2021 06:24:36", updatedAt="Tue Aug 24 2021 06:58:53")
    comment701 = Comment(videoId=774, channelId=71, content="Three generations with six decades of life experience.", createdAt="Sat Jun 05 2021 00:30:56", updatedAt="Mon Feb 28 2022 09:24:25")
    comment702 = Comment(videoId=465, channelId=50, content="They ran around the corner to find that they had traveled back in time.", createdAt="Wed Oct 27 2021 22:05:45", updatedAt="Fri Mar 18 2022 10:55:58")
    comment703 = Comment(videoId=380, channelId=100, content="his seven-layer cake only had six layers.", createdAt="Sat Dec 04 2021 23:20:55", updatedAt="Tue Apr 20 2021 12:08:49")
    comment704 = Comment(videoId=690, channelId=68, content="Jim liked driving around town with his hazard lights on.", createdAt="Wed Jun 02 2021 05:44:19", updatedAt="Sun Jun 13 2021 09:36:11")
    comment705 = Comment(videoId=726, channelId=87, content="The spa attendant applied the deep cleaning mask to the gentleman’s back.", createdAt="Tue Jan 11 2022 10:29:24", updatedAt="Tue Apr 05 2022 02:12:15")
    comment706 = Comment(videoId=453, channelId=63, content="I’m working on a sweet potato farm.", createdAt="Mon Sep 20 2021 16:39:25", updatedAt="Wed Sep 15 2021 01:31:44")
    comment707 = Comment(videoId=433, channelId=100, content="The hawk didn’t understand why the ground squirrels didn’t want to be his friend.", createdAt="Tue Nov 09 2021 10:03:20", updatedAt="Tue Dec 21 2021 02:12:36")
    comment708 = Comment(videoId=195, channelId=51, content="Twin 4-month-olds slept in the shade of the palm tree while the mother tanned in the sun.", createdAt="Sat Jan 15 2022 19:25:43", updatedAt="Sat Nov 06 2021 12:46:16")
    comment709 = Comment(videoId=349, channelId=95, content="She borrowed the book from him many years ago and hasn't yet returned it.", createdAt="Thu May 06 2021 09:17:54", updatedAt="Fri Oct 29 2021 18:39:46")
    comment710 = Comment(videoId=40, channelId=47, content="I've traveled all around Africa and still haven't found the gnu who stole my scarf.", createdAt="Wed Sep 22 2021 15:10:04", updatedAt="Fri Dec 10 2021 10:56:45")
    comment711 = Comment(videoId=115, channelId=98, content="He spiked his hair green to support his iguana.", createdAt="Wed Jul 28 2021 16:34:30", updatedAt="Sat Dec 25 2021 18:04:33")
    comment712 = Comment(videoId=1, channelId=99, content="She moved forward only because she trusted that the ending she now was going through must be followed by a new beginning.", createdAt="Fri Aug 06 2021 11:00:34", updatedAt="Mon Oct 11 2021 09:02:42")
    comment713 = Comment(videoId=739, channelId=69, content="They desperately needed another drummer since the current one only knew how to play bongos.", createdAt="Tue Jul 06 2021 00:59:10", updatedAt="Sat Oct 16 2021 00:58:10")
    comment714 = Comment(videoId=272, channelId=79, content="Buried deep in the snow, he hoped his batteries were fresh in his avalanche beacon.", createdAt="Sat Jul 24 2021 14:06:27", updatedAt="Fri Apr 08 2022 11:31:21")
    comment715 = Comment(videoId=258, channelId=27, content="I am never at home on Sundays.", createdAt="Fri Feb 11 2022 04:47:39", updatedAt="Sat Jan 15 2022 23:27:29")
    comment716 = Comment(videoId=340, channelId=11, content="Gwen had her best sleep ever on her new bed of nails.", createdAt="Mon Apr 26 2021 19:05:51", updatedAt="Tue Apr 27 2021 10:37:32")
    comment717 = Comment(videoId=710, channelId=17, content="The chic gangster liked to start the day with a pink scarf.", createdAt="Sun Nov 21 2021 13:11:53", updatedAt="Fri Jan 21 2022 15:50:22")
    comment718 = Comment(videoId=363, channelId=23, content="The overpass went under the highway and into a secret world.", createdAt="Wed Jun 23 2021 21:06:14", updatedAt="Sun Aug 15 2021 21:08:52")
    comment719 = Comment(videoId=552, channelId=81, content="In that instant, everything changed.", createdAt="Sat Jan 15 2022 22:02:29", updatedAt="Wed Oct 20 2021 05:20:44")
    comment720 = Comment(videoId=156, channelId=45, content="Malls are great places to shop; I can find everything I need under one roof.", createdAt="Tue May 25 2021 14:41:36", updatedAt="Fri Jun 25 2021 01:35:10")
    comment721 = Comment(videoId=560, channelId=69, content="My secretary is the only person who truly understands my stamp-collecting obsession.", createdAt="Wed Jun 23 2021 02:17:43", updatedAt="Mon May 17 2021 08:18:10")
    comment722 = Comment(videoId=250, channelId=5, content="He decided to count all the sand on the beach as a hobby.", createdAt="Tue Jul 20 2021 00:10:25", updatedAt="Sat Dec 11 2021 22:06:08")
    comment723 = Comment(videoId=388, channelId=99, content="There can never be too many cherries on an ice cream sundae.", createdAt="Thu Sep 23 2021 17:03:59", updatedAt="Fri Jan 21 2022 04:42:36")
    comment724 = Comment(videoId=3, channelId=4, content="It took him a month to finish the meal.", createdAt="Mon Apr 04 2022 06:12:39", updatedAt="Sat Nov 20 2021 22:56:13")
    comment725 = Comment(videoId=111, channelId=25, content="He found the end of the rainbow and was surprised at what he found there.", createdAt="Sun Oct 31 2021 08:56:19", updatedAt="Sun Jan 16 2022 21:49:03")
    comment726 = Comment(videoId=712, channelId=61, content="All you need to do is pick up the pen and begin.", createdAt="Tue Mar 08 2022 03:49:36", updatedAt="Wed Apr 28 2021 07:42:36")
    comment727 = Comment(videoId=112, channelId=84, content="Thigh-high in the water, the fisherman’s hope for dinner soon turned to despair.", createdAt="Mon Mar 28 2022 21:27:43", updatedAt="Sun Oct 03 2021 01:42:13")
    comment728 = Comment(videoId=587, channelId=77, content="It turns out you don't need all that stuff you insisted you did.", createdAt="Wed Nov 24 2021 09:15:14", updatedAt="Sun Jul 11 2021 06:44:56")
    comment729 = Comment(videoId=360, channelId=53, content="Acres of almond trees lined the interstate highway which complimented the crazy driving nuts.", createdAt="Mon Dec 27 2021 04:44:03", updatedAt="Wed Oct 06 2021 04:45:17")
    comment730 = Comment(videoId=763, channelId=87, content="Tomorrow will bring something new, so leave today as a memory.", createdAt="Sat Jan 08 2022 12:12:17", updatedAt="Tue Jun 29 2021 13:06:59")
    comment731 = Comment(videoId=633, channelId=40, content="It didn't make sense unless you had the power to eat colors.", createdAt="Sat Mar 26 2022 07:49:09", updatedAt="Sat May 01 2021 19:44:42")
    comment732 = Comment(videoId=185, channelId=58, content="Tomatoes make great weapons when water balloons aren’t available.", createdAt="Thu Jul 29 2021 14:41:23", updatedAt="Fri Jul 09 2021 14:15:53")
    comment733 = Comment(videoId=574, channelId=43, content="If eating three-egg omelets causes weight-gain, budgie eggs are a good substitute.", createdAt="Fri Aug 06 2021 05:12:41", updatedAt="Mon Oct 18 2021 15:52:48")
    comment734 = Comment(videoId=647, channelId=29, content="Mary plays the piano.", createdAt="Wed Apr 21 2021 03:26:01", updatedAt="Sun Nov 07 2021 00:49:08")
    comment735 = Comment(videoId=480, channelId=84, content="When money was tight, he'd get his lunch money from the local wishing well.", createdAt="Mon May 10 2021 15:50:06", updatedAt="Fri Apr 08 2022 15:53:46")
    comment736 = Comment(videoId=686, channelId=15, content="Some bathing suits just shouldn’t be worn by some people.", createdAt="Sun Sep 12 2021 19:06:45", updatedAt="Fri May 21 2021 06:54:54")
    comment737 = Comment(videoId=519, channelId=96, content="Martha came to the conclusion that shake weights are a great gift for any occasion.", createdAt="Fri Jun 18 2021 16:46:04", updatedAt="Thu Dec 30 2021 04:41:04")
    comment738 = Comment(videoId=647, channelId=83, content="The virus had powers none of us knew existed.", createdAt="Sun Feb 27 2022 04:59:58", updatedAt="Sun Dec 12 2021 23:51:44")
    comment739 = Comment(videoId=4, channelId=42, content="Despite multiple complications and her near-death experience", createdAt="Sat Dec 18 2021 16:46:05", updatedAt="Fri Jan 14 2022 11:48:16")
    comment740 = Comment(videoId=279, channelId=40, content="Today we gathered moss for my uncle's wedding.", createdAt="Sun Mar 27 2022 13:10:16", updatedAt="Fri Nov 05 2021 03:17:28")
    comment741 = Comment(videoId=493, channelId=99, content="He found a leprechaun in his walnut shell.", createdAt="Sat Feb 12 2022 06:01:10", updatedAt="Thu Dec 23 2021 11:44:34")
    comment742 = Comment(videoId=608, channelId=95, content="I'm a great listener, really good with empathy vs sympathy and all that, but I hate people.", createdAt="Fri Mar 11 2022 16:00:30", updatedAt="Mon Feb 28 2022 20:38:33")
    comment743 = Comment(videoId=694, channelId=67, content="The best part of marriage is animal crackers with peanut butter.", createdAt="Sun Oct 31 2021 07:43:11", updatedAt="Tue Jun 08 2021 01:50:38")
    comment744 = Comment(videoId=644, channelId=77, content="She always speaks to him in a loud voice.", createdAt="Mon Dec 20 2021 21:00:32", updatedAt="Thu Apr 07 2022 23:32:37")
    comment745 = Comment(videoId=244, channelId=72, content="The three-year-old girl ran down the beach as the kite flew behind her.", createdAt="Wed Jun 23 2021 06:40:23", updatedAt="Tue Nov 02 2021 18:47:42")
    comment746 = Comment(videoId=518, channelId=27, content="I've always wanted to go to Tajikistan, but my cat would miss me.", createdAt="Thu Dec 30 2021 09:37:00", updatedAt="Sat May 29 2021 07:38:52")
    comment747 = Comment(videoId=463, channelId=3, content="He had a vague sense that trees gave birth to dinosaurs.", createdAt="Mon Nov 08 2021 22:56:11", updatedAt="Thu Jan 20 2022 18:36:23")
    comment748 = Comment(videoId=267, channelId=38, content="He's in a boy band which doesn't make much sense for a snake.", createdAt="Fri Oct 29 2021 17:11:35", updatedAt="Mon Apr 19 2021 09:38:24")
    comment749 = Comment(videoId=403, channelId=82, content="He decided water-skiing on a frozen lake wasn’t a good idea.", createdAt="Sat Jul 31 2021 10:04:44", updatedAt="Sat Apr 09 2022 20:13:59")
    comment750 = Comment(videoId=347, channelId=80, content="The stench from the feedlot permeated the car despite having the air conditioning on recycled air.", createdAt="Sun Aug 22 2021 14:20:48", updatedAt="Fri Mar 04 2022 20:28:09")
    comment751 = Comment(videoId=256, channelId=64, content="Just go ahead and press that button.", createdAt="Sat Jan 22 2022 03:15:32", updatedAt="Mon Apr 26 2021 14:01:27")
    comment752 = Comment(videoId=257, channelId=3, content="They wandered into a strange Tiki bar on the edge of the small beach town.", createdAt="Sat Aug 14 2021 17:42:36", updatedAt="Wed Feb 02 2022 00:53:48")
    comment753 = Comment(videoId=611, channelId=31, content="The white water rafting trip was suddenly halted by the unexpected brick wall.", createdAt="Tue Nov 16 2021 21:05:32", updatedAt="Sat Oct 23 2021 13:36:08")
    comment754 = Comment(videoId=239, channelId=19, content="The beauty of the sunset was obscured by the industrial cranes.", createdAt="Wed Jul 21 2021 18:28:58", updatedAt="Wed Dec 22 2021 05:15:33")
    comment755 = Comment(videoId=14, channelId=90, content="He kept telling himself that one day it would all somehow make sense.", createdAt="Wed Nov 03 2021 00:24:41", updatedAt="Thu May 20 2021 01:19:37")
    comment756 = Comment(videoId=665, channelId=7, content="Carol drank the blood as if she were a vampire.", createdAt="Sat Jul 31 2021 20:58:03", updatedAt="Sun Aug 08 2021 21:44:32")
    comment757 = Comment(videoId=427, channelId=29, content="She only paints with bold colors; she does not like pastels.", createdAt="Fri Mar 04 2022 00:33:23", updatedAt="Fri Oct 22 2021 03:52:35")
    comment758 = Comment(videoId=398, channelId=79, content="I am happy to take your donation; any amount will be greatly appreciated.", createdAt="Wed Oct 20 2021 01:38:18", updatedAt="Tue Nov 30 2021 22:32:24")
    comment759 = Comment(videoId=217, channelId=86, content="Henry couldn't decide if he was an auto mechanic or a priest.", createdAt="Sun May 30 2021 21:33:43", updatedAt="Sun Feb 20 2022 10:37:40")
    comment760 = Comment(videoId=204, channelId=48, content="Malls are great places to shop; I can find everything I need under one roof.", createdAt="Sat Mar 12 2022 13:55:12", updatedAt="Sun Aug 08 2021 05:25:22")
    comment761 = Comment(videoId=144, channelId=25, content="He didn't understand why the bird wanted to ride the bicycle.", createdAt="Thu Jan 27 2022 20:50:56", updatedAt="Mon Mar 21 2022 18:20:11")
    comment762 = Comment(videoId=2, channelId=84, content="Stop waiting for exceptional things to just happen.", createdAt="Fri Aug 13 2021 05:47:43", updatedAt="Sat Jun 26 2021 23:54:12")
    comment763 = Comment(videoId=217, channelId=75, content="He uses onomatopoeia as a weapon of mental destruction.", createdAt="Wed Jun 16 2021 10:09:08", updatedAt="Sat Mar 19 2022 17:27:54")
    comment764 = Comment(videoId=692, channelId=97, content="He swore he just saw his sushi move.", createdAt="Mon Oct 25 2021 10:12:57", updatedAt="Sun Mar 20 2022 01:06:20")
    comment765 = Comment(videoId=611, channelId=53, content="They desperately needed another drummer since the current one only knew how to play bongos.", createdAt="Thu Oct 21 2021 06:03:17", updatedAt="Sat Jul 17 2021 06:39:51")
    comment766 = Comment(videoId=319, channelId=45, content="Joyce enjoyed eating pancakes with ketchup.", createdAt="Tue Mar 15 2022 23:59:39", updatedAt="Sat Mar 12 2022 07:07:46")
    comment767 = Comment(videoId=581, channelId=78, content="He colored deep space a soft yellow.", createdAt="Thu Jul 15 2021 05:47:52", updatedAt="Sat Mar 19 2022 17:35:35")
    comment768 = Comment(videoId=162, channelId=27, content="He set out for a short walk, but now all he could see were mangroves and water were for miles.", createdAt="Tue May 18 2021 09:34:52", updatedAt="Sat Mar 19 2022 21:40:34")
    comment769 = Comment(videoId=494, channelId=29, content="She wore green lipstick like a fashion icon.", createdAt="Wed May 12 2021 21:25:09", updatedAt="Fri May 07 2021 15:40:48")
    comment770 = Comment(videoId=181, channelId=24, content="We should play with legos at camp.", createdAt="Sun Jul 11 2021 05:36:27", updatedAt="Thu Aug 05 2021 05:23:34")
    comment771 = Comment(videoId=419, channelId=23, content="He created a pig burger out of beef.", createdAt="Mon Mar 14 2022 07:32:07", updatedAt="Thu Feb 10 2022 16:51:51")
    comment772 = Comment(videoId=536, channelId=100, content="Jason didn’t understand why his parents wouldn’t let him sell his little sister at the garage sale.", createdAt="Wed Jan 05 2022 20:44:37", updatedAt="Sat Jan 22 2022 19:27:07")
    comment773 = Comment(videoId=279, channelId=69, content="The crowd yells and screams for more memes.", createdAt="Wed Oct 13 2021 01:27:24", updatedAt="Mon Feb 07 2022 23:42:29")
    comment774 = Comment(videoId=452, channelId=4, content="The bird had a belief that it was really a groundhog.", createdAt="Fri Nov 12 2021 13:45:52", updatedAt="Fri Apr 08 2022 20:07:43")
    comment775 = Comment(videoId=11, channelId=89, content="Your girlfriend bought your favorite cookie crisp cereal but forgot to get milk.", createdAt="Wed Dec 08 2021 03:28:16", updatedAt="Wed Jan 19 2022 20:51:39")
    comment776 = Comment(videoId=772, channelId=67, content="Green should have smelled more tranquil, but somehow it just tasted rotten.", createdAt="Fri Jun 18 2021 07:50:04", updatedAt="Sun Sep 05 2021 09:46:22")
    comment777 = Comment(videoId=468, channelId=18, content="Going from child, to childish, to childlike is only a matter of time.", createdAt="Wed Feb 23 2022 03:09:40", updatedAt="Sun Nov 21 2021 02:01:04")
    comment778 = Comment(videoId=16, channelId=85, content="I'd rather be a bird than a fish.", createdAt="Mon Aug 02 2021 02:16:03", updatedAt="Sat Apr 09 2022 04:04:48")
    comment779 = Comment(videoId=50, channelId=1, content="I want to buy a onesie… but know it won’t suit me.", createdAt="Sat Oct 09 2021 10:29:59", updatedAt="Wed Jan 26 2022 21:22:09")
    comment780 = Comment(videoId=349, channelId=3, content="Erin accidentally created a new universe.", createdAt="Mon Apr 04 2022 12:47:52", updatedAt="Thu Sep 23 2021 20:16:57")
    comment781 = Comment(videoId=307, channelId=20, content="He decided to fake his disappearance to avoid jail.", createdAt="Tue Mar 22 2022 08:59:13", updatedAt="Tue Oct 05 2021 21:56:02")
    comment782 = Comment(videoId=55, channelId=19, content="He was all business when he wore his clown suit.", createdAt="Thu Jan 06 2022 13:06:31", updatedAt="Tue Sep 28 2021 02:56:14")
    comment783 = Comment(videoId=214, channelId=95, content="I don’t respect anybody who can’t tell the difference between Pepsi and Coke.", createdAt="Thu Mar 31 2022 02:51:35", updatedAt="Fri Nov 26 2021 12:34:59")
    comment785 = Comment(videoId=171, channelId=82, content="Before he moved to the inner city, he had always believed that security complexes were psychological.", createdAt="Thu Nov 18 2021 15:43:11", updatedAt="Tue Sep 14 2021 10:25:20")
    comment786 = Comment(videoId=286, channelId=53, content="I've always wanted to go to Tajikistan, but my cat would miss me.", createdAt="Sun Jul 04 2021 03:45:12", updatedAt="Sun Oct 03 2021 10:06:56")
    comment787 = Comment(videoId=769, channelId=54, content="For the 216th time, he said he would quit drinking soda after this last Coke.", createdAt="Sun Jul 18 2021 11:22:03", updatedAt="Fri Mar 25 2022 20:15:29")
    comment788 = Comment(videoId=515, channelId=56, content="I'll have you know I've written over fifty novels", createdAt="Thu Jun 17 2021 21:46:37", updatedAt="Mon Mar 21 2022 15:58:08")
    comment789 = Comment(videoId=271, channelId=23, content="It was the best sandcastle he had ever seen.", createdAt="Fri Mar 11 2022 09:10:56", updatedAt="Mon Mar 14 2022 09:00:36")
    comment790 = Comment(videoId=496, channelId=91, content="My biggest joy is roasting almonds while stalking prey.", createdAt="Mon Sep 20 2021 01:41:32", updatedAt="Mon Apr 04 2022 05:31:39")
    comment791 = Comment(videoId=682, channelId=56, content="Harrold felt confident that nobody would ever suspect his spy pigeon.", createdAt="Sun Nov 21 2021 12:54:35", updatedAt="Sun Jan 23 2022 22:52:03")
    comment792 = Comment(videoId=176, channelId=83, content="All they could see was the blue water surrounding their sailboat.", createdAt="Tue Nov 30 2021 07:34:59", updatedAt="Tue Mar 22 2022 16:06:19")
    comment793 = Comment(videoId=348, channelId=44, content="He felt that dining on the bridge brought romance to his relationship with his cat.", createdAt="Fri Nov 26 2021 00:50:13", updatedAt="Sat Jan 29 2022 18:03:33")
    comment794 = Comment(videoId=442, channelId=68, content="If any cop asks you where you were, just say you were visiting Kansas.", createdAt="Wed Nov 24 2021 03:04:13", updatedAt="Thu Oct 07 2021 00:30:02")
    comment795 = Comment(videoId=119, channelId=20, content="The trick to getting kids to eat anything is to put catchup on it.", createdAt="Sun Feb 20 2022 15:45:34", updatedAt="Wed Aug 25 2021 03:02:11")
    comment796 = Comment(videoId=353, channelId=84, content="He always wore his sunglasses at night.", createdAt="Mon Aug 16 2021 00:00:15", updatedAt="Sat Mar 26 2022 16:17:05")
    comment797 = Comment(videoId=22, channelId=19, content="She had that tint of craziness in her soul that made her believe she could actually make a difference.", createdAt="Tue Feb 15 2022 04:10:05", updatedAt="Sun Dec 26 2021 06:48:35")
    comment798 = Comment(videoId=181, channelId=14, content="She discovered van life is difficult with 2 cats and a dog.", createdAt="Tue Apr 20 2021 17:36:53", updatedAt="Sat Nov 27 2021 19:18:25")
    comment799 = Comment(videoId=512, channelId=64, content="She moved forward only because she trusted that the ending she now was going through must be followed by a new beginning.", createdAt="Fri Mar 25 2022 20:31:13", updatedAt="Wed Apr 28 2021 05:32:44")
    comment800 = Comment(videoId=439, channelId=32, content="If you like tuna and tomato sauce, try combining the two, it’s really not as bad as it sounds.", createdAt="Sat Sep 25 2021 01:39:19", updatedAt="Tue Jul 06 2021 16:49:38")
    comment801 = Comment(videoId=351, channelId=52, content="The best part of marriage is animal crackers with peanut butter.", createdAt="Sat Oct 23 2021 17:37:50", updatedAt="Sun Jul 11 2021 03:39:22")
    comment802 = Comment(videoId=559, channelId=45, content="For oil spots on the floor, nothing beats parking a motorbike in the lounge.", createdAt="Fri Aug 13 2021 15:46:51", updatedAt="Sun Oct 24 2021 12:47:08")
    comment803 = Comment(videoId=223, channelId=81, content="Yeah, I think it's a good environment for learning English.", createdAt="Thu Dec 16 2021 18:15:44", updatedAt="Mon Aug 02 2021 05:44:15")
    comment804 = Comment(videoId=367, channelId=81, content="The sun had set and so had his dreams.", createdAt="Wed Sep 29 2021 19:44:59", updatedAt="Wed May 05 2021 12:43:20")
    comment805 = Comment(videoId=224, channelId=23, content="She couldn't decide of the glass was half empty or half full so she drank it.", createdAt="Thu Jul 08 2021 11:13:10", updatedAt="Sun Apr 25 2021 10:57:31")
    comment806 = Comment(videoId=627, channelId=73, content="Art doesn't have to be intentional.", createdAt="Wed Jun 09 2021 04:41:13", updatedAt="Wed Aug 18 2021 06:51:27")
    comment807 = Comment(videoId=345, channelId=21, content="She cried diamonds.", createdAt="Wed Oct 06 2021 04:15:05", updatedAt="Fri Apr 01 2022 19:19:08")
    comment808 = Comment(videoId=554, channelId=80, content="Lightning Paradise was the local hangout joint where the group usually ended up spending the night.", createdAt="Sat Nov 20 2021 00:46:17", updatedAt="Wed Jun 02 2021 18:54:23")
    comment809 = Comment(videoId=485, channelId=79, content="Don't step on the broken glass.", createdAt="Sun Aug 29 2021 21:30:19", updatedAt="Tue Mar 15 2022 14:36:42")
    comment810 = Comment(videoId=661, channelId=66, content="He realized there had been several deaths on this road, but his concern rose when he saw the exact number.", createdAt="Thu Dec 30 2021 21:49:52", updatedAt="Tue Feb 22 2022 22:47:34")
    comment811 = Comment(videoId=488, channelId=94, content="At that moment he wasn't listening to music, he was living an experience.", createdAt="Sun Sep 05 2021 08:52:45", updatedAt="Mon Apr 12 2021 12:13:57")
    comment812 = Comment(videoId=264, channelId=8, content="She saw no irony asking me to change but wanting me to accept her for who she is.", createdAt="Sun Jan 09 2022 13:28:41", updatedAt="Sun Feb 06 2022 17:50:41")
    comment813 = Comment(videoId=686, channelId=38, content="Dan ate the clouds like cotton candy.", createdAt="Mon Sep 20 2021 13:24:35", updatedAt="Fri Dec 17 2021 20:26:42")
    comment814 = Comment(videoId=760, channelId=41, content="As he dangled from the rope deep inside the crevasse", createdAt="Thu Oct 28 2021 05:10:47", updatedAt="Sun Jun 13 2021 21:09:56")
    comment815 = Comment(videoId=682, channelId=51, content="The miniature pet elephant became the envy of the neighborhood.", createdAt="Sun Dec 19 2021 20:03:23", updatedAt="Tue Oct 26 2021 21:49:41")
    comment816 = Comment(videoId=58, channelId=57, content="On a scale from one to ten, what's your favorite flavor of random grammar?", createdAt="Wed Feb 23 2022 20:28:35", updatedAt="Wed Apr 06 2022 20:37:03")
    comment817 = Comment(videoId=56, channelId=97, content="I used to practice weaving with spaghetti three hours a day but stopped because I didn't want to die alone.", createdAt="Wed Oct 20 2021 17:38:35", updatedAt="Mon Mar 28 2022 15:59:21")
    comment818 = Comment(videoId=372, channelId=14, content="It was her first experience training a rainbow unicorn.", createdAt="Wed May 05 2021 05:20:00", updatedAt="Fri Jan 07 2022 03:04:54")
    comment819 = Comment(videoId=497, channelId=81, content="The truth is that you pay for your lifestyle in hours.", createdAt="Tue Oct 12 2021 06:04:56", updatedAt="Wed Mar 16 2022 07:01:46")
    comment820 = Comment(videoId=193, channelId=61, content="Three generations with six decades of life experience.", createdAt="Tue Sep 14 2021 03:54:04", updatedAt="Tue May 25 2021 22:55:42")
    comment821 = Comment(videoId=11, channelId=96, content="The urgent care center was flooded with patients after the news of a new deadly virus was made public.", createdAt="Fri Nov 19 2021 22:05:27", updatedAt="Wed Feb 16 2022 23:06:21")
    comment822 = Comment(videoId=414, channelId=78, content="His son quipped that power bars were nothing more than adult candy bars.", createdAt="Sun Dec 12 2021 05:21:02", updatedAt="Tue Oct 05 2021 06:38:33")
    comment823 = Comment(videoId=243, channelId=54, content="He dreamed of eating green apples with worms.", createdAt="Wed May 19 2021 05:25:55", updatedAt="Wed Feb 23 2022 03:23:31")
    comment824 = Comment(videoId=214, channelId=5, content="Siri became confused when we reused to follow her directions.", createdAt="Fri Mar 18 2022 16:32:27", updatedAt="Mon Apr 04 2022 07:18:09")
    comment825 = Comment(videoId=23, channelId=9, content="She was sad to hear that fireflies are facing extinction due to artificial light, habitat loss, and pesticides.", createdAt="Sat Jan 15 2022 18:59:01", updatedAt="Sun Dec 05 2021 20:46:17")
    comment826 = Comment(videoId=97, channelId=54, content="He was an introvert that extroverts seemed to love.", createdAt="Mon Nov 15 2021 22:22:10", updatedAt="Mon Dec 20 2021 19:01:10")
    comment827 = Comment(videoId=53, channelId=85, content="I really want to go to work, but I am too sick to drive.", createdAt="Sat Jul 10 2021 21:22:15", updatedAt="Tue Feb 01 2022 07:08:14")
    comment828 = Comment(videoId=247, channelId=35, content="The external scars tell only part of the story.", createdAt="Tue Sep 21 2021 09:26:07", updatedAt="Sat Oct 09 2021 12:57:14")
    comment829 = Comment(videoId=246, channelId=94, content="The book is in front of the table.", createdAt="Sat Aug 21 2021 01:58:44", updatedAt="Mon Aug 02 2021 03:46:01")
    comment830 = Comment(videoId=555, channelId=44, content="The father died during childbirth.", createdAt="Sat Dec 18 2021 05:18:29", updatedAt="Thu Sep 30 2021 12:41:29")
    comment831 = Comment(videoId=494, channelId=77, content="He was surprised that his immense laziness was inspirational to others.", createdAt="Tue Nov 02 2021 09:12:57", updatedAt="Mon May 24 2021 12:29:38")
    comment832 = Comment(videoId=591, channelId=43, content="Waffles are always better without fire ants and fleas.", createdAt="Sat Mar 26 2022 13:28:48", updatedAt="Sat Jul 10 2021 01:28:30")
    comment833 = Comment(videoId=487, channelId=63, content="He ended up burning his fingers poking someone else's fire.", createdAt="Thu Feb 24 2022 00:34:57", updatedAt="Wed Jul 14 2021 14:00:20")
    comment834 = Comment(videoId=364, channelId=46, content="If you like tuna and tomato sauce, try combining the two, it’s really not as bad as it sounds.", createdAt="Mon Sep 06 2021 20:44:55", updatedAt="Sun Oct 24 2021 00:09:47")
    comment835 = Comment(videoId=370, channelId=94, content="Please tell me you don't work in a morgue.", createdAt="Tue Apr 20 2021 17:29:58", updatedAt="Tue May 25 2021 01:03:44")
    comment836 = Comment(videoId=713, channelId=29, content="The water flowing down the river didn’t look that powerful from the car", createdAt="Tue Mar 08 2022 23:52:48", updatedAt="Fri Aug 06 2021 11:03:05")
    comment837 = Comment(videoId=311, channelId=90, content="The blue parrot drove by the hitchhiking mongoose.", createdAt="Sat Oct 09 2021 11:40:31", updatedAt="Mon Jun 21 2021 13:48:44")
    comment838 = Comment(videoId=27, channelId=10, content="The old apple revels in its authority.", createdAt="Sun Feb 20 2022 06:29:52", updatedAt="Mon Aug 02 2021 12:11:48")
    comment839 = Comment(videoId=296, channelId=35, content="Imagine his surprise when he discovered that the safe was full of pudding.", createdAt="Fri Mar 04 2022 23:10:22", updatedAt="Sun Nov 28 2021 20:52:30")
    comment840 = Comment(videoId=419, channelId=35, content="It turns out you don't need all that stuff you insisted you did.", createdAt="Thu Aug 26 2021 13:02:03", updatedAt="Tue Jul 20 2021 03:11:30")
    comment841 = Comment(videoId=608, channelId=29, content="I may struggle with geography, but I'm sure I'm somewhere around here.", createdAt="Fri Feb 04 2022 16:12:37", updatedAt="Wed Jun 30 2021 17:34:26")
    comment842 = Comment(videoId=228, channelId=1, content="One small action would change her life, but whether it would be for better or for worse was yet to be determined.", createdAt="Wed Mar 09 2022 14:45:04", updatedAt="Sun Dec 26 2021 21:56:53")
    comment843 = Comment(videoId=218, channelId=94, content="I often see the time 11:11 or 12:34 on clocks.", createdAt="Sat Nov 13 2021 22:31:00", updatedAt="Thu Nov 18 2021 13:48:04")
    comment844 = Comment(videoId=597, channelId=45, content="The furnace repairman indicated the heating system was acting as an air conditioner.", createdAt="Sun Jun 20 2021 08:02:15", updatedAt="Mon Jan 31 2022 03:45:04")
    comment845 = Comment(videoId=774, channelId=60, content="Behind the window was a reflection that only instilled fear.", createdAt="Fri Feb 11 2022 07:39:57", updatedAt="Thu Apr 29 2021 20:11:19")
    comment846 = Comment(videoId=342, channelId=54, content="his seven-layer cake only had six layers.", createdAt="Mon Aug 23 2021 05:42:04", updatedAt="Wed Feb 02 2022 21:59:19")
    comment847 = Comment(videoId=480, channelId=9, content="There's a message for you if you look up.", createdAt="Mon Nov 01 2021 10:33:02", updatedAt="Sun Feb 27 2022 14:38:10")
    comment848 = Comment(videoId=110, channelId=3, content="He kept telling himself that one day it would all somehow make sense.", createdAt="Sun Feb 06 2022 05:40:14", updatedAt="Tue Jan 25 2022 07:41:49")
    comment849 = Comment(videoId=763, channelId=31, content="As the asteroid hurtled toward earth, Becky was upset her dentist appointment had been canceled.", createdAt="Sun Jan 02 2022 11:36:44", updatedAt="Sun Apr 11 2021 00:18:34")
    comment850 = Comment(videoId=581, channelId=22, content="I'd always thought lightning was something only I could see.", createdAt="Wed Jul 21 2021 01:40:58", updatedAt="Wed Feb 16 2022 08:10:58")
    comment851 = Comment(videoId=98, channelId=12, content="It was the first time he had ever seen someone cook dinner on an elephant.", createdAt="Fri Apr 01 2022 20:26:14", updatedAt="Sun Jan 23 2022 10:35:24")
    comment852 = Comment(videoId=411, channelId=72, content="He went back to the video to see what had been recorded and was shocked at what he saw.", createdAt="Fri Jul 23 2021 13:04:52", updatedAt="Wed Apr 06 2022 05:43:27")
    comment853 = Comment(videoId=351, channelId=55, content="Dan ate the clouds like cotton candy.", createdAt="Wed Jan 05 2022 13:07:50", updatedAt="Fri Nov 19 2021 07:49:44")
    comment854 = Comment(videoId=108, channelId=88, content="Flying fish flew by the space station.", createdAt="Fri Jan 07 2022 20:43:26", updatedAt="Mon Feb 28 2022 00:16:38")
    comment856 = Comment(videoId=772, channelId=62, content="He stepped gingerly onto the bridge knowing that enchantment awaited on the other side.", createdAt="Sun Aug 15 2021 15:03:34", updatedAt="Fri Aug 20 2021 00:18:48")
    comment857 = Comment(videoId=635, channelId=67, content="The truth is that you pay for your lifestyle in hours.", createdAt="Sun May 23 2021 02:01:23", updatedAt="Thu Dec 16 2021 17:41:57")
    comment858 = Comment(videoId=47, channelId=73, content="Sometimes it is better to just walk away from things and go back to them later when you’re in a better frame of mind.", createdAt="Fri Apr 16 2021 16:46:08", updatedAt="Tue Aug 17 2021 07:56:14")
    comment859 = Comment(videoId=117, channelId=63, content="Sometimes I stare at a door or a wall and I wonder what is this reality, why am I alive, and what is this all about?", createdAt="Tue May 11 2021 02:48:46", updatedAt="Mon Oct 11 2021 20:42:51")
    comment860 = Comment(videoId=378, channelId=53, content="The secret ingredient to his wonderful life was crime.", createdAt="Thu Sep 23 2021 03:27:05", updatedAt="Sun Jul 04 2021 18:56:27")
    comment861 = Comment(videoId=640, channelId=70, content="The doll spun around in circles in hopes of coming alive.", createdAt="Thu Oct 21 2021 19:26:54", updatedAt="Fri Oct 29 2021 10:43:52")
    comment862 = Comment(videoId=779, channelId=72, content="Too many prisons have become early coffins.", createdAt="Wed Mar 23 2022 16:12:28", updatedAt="Wed Apr 06 2022 00:56:03")
    comment863 = Comment(videoId=264, channelId=53, content="He played the game as if his life depended on it and the truth was that it did.", createdAt="Mon Dec 06 2021 19:43:29", updatedAt="Wed Oct 20 2021 07:28:56")
    comment864 = Comment(videoId=552, channelId=52, content="The tour bus was packed with teenage girls heading toward their next adventure.", createdAt="Wed Sep 22 2021 03:15:49", updatedAt="Sun Feb 13 2022 05:41:36")
    comment865 = Comment(videoId=111, channelId=91, content="She saw no irony asking me to change but wanting me to accept her for who she is.", createdAt="Sun Nov 14 2021 00:38:45", updatedAt="Thu Nov 04 2021 01:41:44")
    comment866 = Comment(videoId=769, channelId=24, content="The furnace repairman indicated the heating system was acting as an air conditioner.", createdAt="Wed Jun 02 2021 10:22:31", updatedAt="Sun Feb 13 2022 11:30:50")
    comment867 = Comment(videoId=52, channelId=33, content="Some bathing suits just shouldn’t be worn by some people.", createdAt="Thu Jun 03 2021 07:09:38", updatedAt="Mon May 03 2021 05:17:50")
    comment868 = Comment(videoId=443, channelId=82, content="They did nothing as the raccoon attacked the lady’s bag of food.", createdAt="Sun Feb 20 2022 17:52:55", updatedAt="Sat May 01 2021 04:15:10")
    comment869 = Comment(videoId=679, channelId=88, content="He's in a boy band which doesn't make much sense for a snake.", createdAt="Fri Jan 07 2022 11:36:20", updatedAt="Tue Dec 14 2021 06:20:02")
    comment870 = Comment(videoId=402, channelId=47, content="Hit me with your pet shark!", createdAt="Sat Jul 03 2021 08:31:31", updatedAt="Mon Feb 14 2022 04:00:32")
    comment871 = Comment(videoId=492, channelId=29, content="The tree fell unexpectedly short.", createdAt="Sat Jul 03 2021 00:00:10", updatedAt="Tue Jan 11 2022 20:14:11")
    comment872 = Comment(videoId=128, channelId=25, content="The quick brown fox jumps over the lazy dog.", createdAt="Tue Jun 15 2021 14:56:32", updatedAt="Mon Jul 12 2021 21:44:18")
    comment873 = Comment(videoId=471, channelId=26, content="Jim liked driving around town with his hazard lights on.", createdAt="Sun Jul 25 2021 03:39:28", updatedAt="Wed Sep 29 2021 17:02:33")
    comment874 = Comment(videoId=741, channelId=75, content="There was no ice cream in the freezer, nor did they have money to go to the store.", createdAt="Sun Jul 25 2021 12:17:21", updatedAt="Sat Dec 04 2021 16:32:35")
    comment875 = Comment(videoId=80, channelId=51, content="He shaved the peach to prove a point.", createdAt="Fri Aug 27 2021 08:07:14", updatedAt="Fri Sep 17 2021 14:24:08")
    comment876 = Comment(videoId=360, channelId=1, content="The bees decided to have a mutiny against their queen.", createdAt="Sat Mar 05 2022 08:47:58", updatedAt="Sun Dec 12 2021 07:31:29")
    comment877 = Comment(videoId=775, channelId=31, content="The elephant didn't want to talk about the person in the room.", createdAt="Sat Nov 27 2021 14:25:46", updatedAt="Sat Apr 02 2022 05:13:05")
    comment878 = Comment(videoId=268, channelId=87, content="Imagine his surprise when he discovered that the safe was full of pudding.", createdAt="Sun Oct 10 2021 09:35:31", updatedAt="Sat May 01 2021 06:39:07")
    comment879 = Comment(videoId=282, channelId=14, content="He was disappointed when he found the beach to be so sandy and the sun so sunny.", createdAt="Sun Feb 27 2022 06:59:36", updatedAt="Sun Sep 19 2021 10:15:50")
    comment880 = Comment(videoId=758, channelId=28, content="Dolores wouldn't have eaten the meal if she had known what it actually was.", createdAt="Sun Dec 12 2021 17:28:08", updatedAt="Fri Mar 11 2022 06:52:39")
    comment881 = Comment(videoId=332, channelId=5, content="I honestly find her about as intimidating as a basket of kittens.", createdAt="Sun Feb 20 2022 05:57:08", updatedAt="Sat Dec 18 2021 04:27:40")
    comment882 = Comment(videoId=271, channelId=30, content="He kept telling himself that one day it would all somehow make sense.", createdAt="Tue Apr 27 2021 23:48:36", updatedAt="Wed Sep 08 2021 22:02:34")
    comment883 = Comment(videoId=80, channelId=43, content="She was disgusted he couldn’t tell the difference between lemonade and limeade.", createdAt="Fri Jul 09 2021 18:39:16", updatedAt="Fri Oct 29 2021 03:19:28")
    comment884 = Comment(videoId=54, channelId=89, content="There's a message for you if you look up.", createdAt="Sat Oct 02 2021 17:46:26", updatedAt="Mon Mar 07 2022 18:03:33")
    comment885 = Comment(videoId=524, channelId=88, content="Nobody questions who built the pyramids in Mexico.", createdAt="Wed May 19 2021 06:38:20", updatedAt="Wed Jun 02 2021 12:51:36")
    comment886 = Comment(videoId=720, channelId=92, content="You're unsure whether or not to trust him, but very thankful that you wore a turtle neck.", createdAt="Tue Jun 15 2021 10:30:53", updatedAt="Sun Aug 29 2021 02:40:31")
    comment887 = Comment(videoId=182, channelId=50, content="The bird had a belief that it was really a groundhog.", createdAt="Tue Mar 29 2022 16:15:28", updatedAt="Sat Nov 06 2021 06:39:06")
    comment888 = Comment(videoId=652, channelId=5, content="I purchased a baby clown from the Russian terrorist black market.", createdAt="Fri Jul 23 2021 00:06:20", updatedAt="Sat May 15 2021 14:13:36")
    comment889 = Comment(videoId=133, channelId=38, content="It's never comforting to know that your fate depends on something as unpredictable as the popping of corn.", createdAt="Tue Jul 27 2021 04:55:46", updatedAt="Fri May 14 2021 22:16:59")
    comment890 = Comment(videoId=105, channelId=69, content="I've traveled all around Africa and still haven't found the gnu who stole my scarf.", createdAt="Fri May 14 2021 07:15:18", updatedAt="Fri Sep 03 2021 06:03:22")
    comment891 = Comment(videoId=629, channelId=92, content="25 years later, she still regretted that specific moment.", createdAt="Wed Jun 09 2021 14:50:40", updatedAt="Tue Dec 14 2021 11:24:40")
    comment892 = Comment(videoId=686, channelId=31, content="There are no heroes in a punk rock band.", createdAt="Mon Oct 25 2021 04:07:20", updatedAt="Mon May 03 2021 04:42:11")
    comment893 = Comment(videoId=13, channelId=49, content="There have been days when I wished to be separated from my body, but today wasn’t one of those days.", createdAt="Mon Jul 12 2021 09:11:29", updatedAt="Wed Jun 23 2021 00:33:51")
    comment894 = Comment(videoId=511, channelId=75, content="You'll see the rainbow bridge after it rains cats and dogs.", createdAt="Sun Nov 21 2021 20:35:43", updatedAt="Sun Sep 05 2021 13:43:58")
    comment895 = Comment(videoId=516, channelId=20, content="Today I dressed my unicorn in preparation for the race.", createdAt="Thu Dec 09 2021 23:20:41", updatedAt="Fri Dec 31 2021 17:32:11")
    comment896 = Comment(videoId=757, channelId=15, content="He created a pig burger out of beef.", createdAt="Sun Dec 26 2021 06:16:42", updatedAt="Sun Jun 20 2021 21:42:07")
    comment897 = Comment(videoId=218, channelId=95, content="The miniature pet elephant became the envy of the neighborhood.", createdAt="Fri Apr 23 2021 06:20:30", updatedAt="Mon Dec 06 2021 15:25:02")
    comment898 = Comment(videoId=352, channelId=6, content="Pat ordered a ghost pepper pie.", createdAt="Wed Oct 20 2021 17:32:45", updatedAt="Thu Oct 14 2021 02:49:02")
    comment899 = Comment(videoId=531, channelId=90, content="He was surprised that his immense laziness was inspirational to others.", createdAt="Thu Apr 29 2021 21:57:15", updatedAt="Sun Sep 05 2021 23:46:53")
    comment900 = Comment(videoId=465, channelId=13, content="The external scars tell only part of the story.", createdAt="Fri Jul 16 2021 12:21:51", updatedAt="Mon May 24 2021 08:31:39")
    comment901 = Comment(videoId=726, channelId=36, content="I covered my friend in baby oil.", createdAt="Sun Oct 31 2021 08:27:17", updatedAt="Sun Apr 18 2021 09:19:50")
    comment902 = Comment(videoId=163, channelId=66, content="All you need to do is pick up the pen and begin.", createdAt="Fri Aug 27 2021 18:03:53", updatedAt="Wed Feb 23 2022 20:48:13")
    comment903 = Comment(videoId=134, channelId=90, content="Tomorrow will bring something new, so leave today as a memory.", createdAt="Tue Oct 05 2021 17:59:32", updatedAt="Thu Jul 01 2021 14:22:27")
    comment904 = Comment(videoId=89, channelId=77, content="I may struggle with geography, but I'm sure I'm somewhere around here.", createdAt="Thu Apr 29 2021 15:58:18", updatedAt="Thu Mar 31 2022 11:36:54")
    comment905 = Comment(videoId=303, channelId=89, content="I am never at home on Sundays.", createdAt="Tue Mar 01 2022 18:26:29", updatedAt="Thu Jul 22 2021 14:40:36")
    comment906 = Comment(videoId=339, channelId=50, content="Two seats were vacant.", createdAt="Thu Dec 23 2021 10:01:30", updatedAt="Fri Jan 14 2022 17:47:34")
    comment907 = Comment(videoId=259, channelId=11, content="She advised him to come back at once.", createdAt="Mon Jul 26 2021 20:21:09", updatedAt="Thu May 20 2021 10:57:56")
    comment908 = Comment(videoId=528, channelId=12, content="He waited for the stop sign to turn to a go sign.", createdAt="Thu Apr 22 2021 23:54:19", updatedAt="Mon Aug 02 2021 14:14:02")
    comment909 = Comment(videoId=306, channelId=2, content="Today is the day I'll finally know what brick tastes like.", createdAt="Sun Aug 22 2021 23:49:52", updatedAt="Sun Aug 15 2021 07:21:06")
    comment910 = Comment(videoId=510, channelId=95, content="Various sea birds are elegant, but nothing is as elegant as a gliding pelican.", createdAt="Mon Jan 03 2022 13:30:54", updatedAt="Fri Nov 12 2021 20:17:18")
    comment911 = Comment(videoId=594, channelId=44, content="She felt that chill that makes the hairs on the back of your neck when he walked into the room.", createdAt="Wed Nov 17 2021 01:45:51", updatedAt="Fri Jul 09 2021 16:50:39")
    comment912 = Comment(videoId=30, channelId=89, content="She had that tint of craziness in her soul that made her believe she could actually make a difference.", createdAt="Sat Jun 05 2021 12:29:14", updatedAt="Sat Jan 22 2022 15:34:37")
    comment913 = Comment(videoId=502, channelId=40, content="The overpass went under the highway and into a secret world.", createdAt="Sat May 08 2021 07:36:18", updatedAt="Wed Nov 24 2021 02:20:43")
    comment914 = Comment(videoId=676, channelId=8, content="We should play with legos at camp.", createdAt="Fri Jan 14 2022 13:15:35", updatedAt="Thu Dec 09 2021 11:50:00")
    comment915 = Comment(videoId=422, channelId=10, content="The sign said there was road work ahead so he decided to speed up.", createdAt="Sat Jan 01 2022 21:47:17", updatedAt="Thu Apr 29 2021 17:08:52")
    comment916 = Comment(videoId=415, channelId=57, content="Despite what your teacher may have told you, there is a wrong way to wield a lasso.", createdAt="Mon Apr 04 2022 04:06:22", updatedAt="Mon Jan 10 2022 22:49:25")
    comment917 = Comment(videoId=457, channelId=8, content="It was always dangerous to drive with him since he insisted the safety cones were a slalom course.", createdAt="Wed Dec 15 2021 16:08:13", updatedAt="Wed May 26 2021 23:27:19")
    comment918 = Comment(videoId=302, channelId=53, content="Greetings from the real universe.", createdAt="Tue Mar 15 2022 21:16:18", updatedAt="Sat Jul 10 2021 00:55:12")
    comment919 = Comment(videoId=492, channelId=28, content="The sight of his goatee made me want to run and hide under my sister-in-law's bed.", createdAt="Sat Apr 17 2021 23:19:25", updatedAt="Sat Dec 18 2021 01:58:21")
    comment920 = Comment(videoId=18, channelId=8, content="Tuesdays are free if you bring a gnome costume.", createdAt="Sat Aug 14 2021 05:54:54", updatedAt="Fri Dec 31 2021 15:23:05")
    comment921 = Comment(videoId=149, channelId=30, content="A purple pig and a green donkey flew a kite in the middle of the night and ended up sunburnt.", createdAt="Fri Nov 19 2021 10:54:53", updatedAt="Thu Mar 10 2022 02:06:16")
    comment922 = Comment(videoId=415, channelId=88, content="I've always wanted to go to Tajikistan, but my cat would miss me.", createdAt="Tue Jan 25 2022 03:35:56", updatedAt="Sat Jul 24 2021 00:38:52")
    comment923 = Comment(videoId=188, channelId=53, content="He's in a boy band which doesn't make much sense for a snake.", createdAt="Fri Nov 26 2021 09:36:35", updatedAt="Mon Jan 17 2022 10:46:28")
    comment924 = Comment(videoId=326, channelId=70, content="He excelled at firing people nicely.", createdAt="Mon Sep 13 2021 05:58:32", updatedAt="Mon Oct 11 2021 19:56:10")
    comment925 = Comment(videoId=724, channelId=3, content="You bite up because of your lower jaw.", createdAt="Sun Jul 18 2021 01:48:39", updatedAt="Tue Oct 05 2021 01:36:52")
    comment926 = Comment(videoId=579, channelId=77, content="The dead trees waited to be ignited by the smallest spark and seek their revenge.", createdAt="Thu Oct 28 2021 10:57:57", updatedAt="Sun Jun 27 2021 10:38:43")
    comment927 = Comment(videoId=615, channelId=16, content="At that moment I was the most fearsome weasel in the entire swamp.", createdAt="Sun Jul 11 2021 17:56:22", updatedAt="Thu Dec 02 2021 08:15:51")
    comment928 = Comment(videoId=128, channelId=12, content="When transplanting seedlings, candied teapots will make the task easier.", createdAt="Sun Sep 19 2021 14:40:19", updatedAt="Fri Nov 05 2021 01:42:07")
    comment929 = Comment(videoId=413, channelId=20, content="There's a message for you if you look up.", createdAt="Mon Apr 12 2021 14:02:50", updatedAt="Fri Mar 25 2022 03:49:43")
    comment930 = Comment(videoId=247, channelId=83, content="She couldn't decide of the glass was half empty or half full so she drank it.", createdAt="Tue Mar 01 2022 12:05:29", updatedAt="Fri Jul 23 2021 02:11:42")
    comment931 = Comment(videoId=716, channelId=62, content="All she wanted was the answer, but she had no idea how much she would hate it.", createdAt="Sun Jul 18 2021 11:27:13", updatedAt="Sat Apr 24 2021 05:58:06")
    comment932 = Comment(videoId=718, channelId=30, content="As he dangled from the rope deep inside the crevasse", createdAt="Tue Jul 13 2021 14:04:21", updatedAt="Sun Mar 27 2022 16:41:28")
    comment933 = Comment(videoId=655, channelId=72, content="The shark-infested South Pine channel was the only way in or out.", createdAt="Sat Jul 17 2021 16:28:52", updatedAt="Thu Jan 06 2022 04:21:49")
    comment934 = Comment(videoId=16, channelId=78, content="The lyrics of the song sounded like fingernails on a chalkboard.", createdAt="Sat Oct 09 2021 05:20:57", updatedAt="Mon Mar 21 2022 08:37:42")
    comment935 = Comment(videoId=650, channelId=42, content="They desperately needed another drummer since the current one only knew how to play bongos.", createdAt="Sat Aug 07 2021 15:04:17", updatedAt="Thu Sep 09 2021 21:15:41")
    comment936 = Comment(videoId=178, channelId=58, content="Sixty-Four comes asking for bread.", createdAt="Sun Feb 13 2022 21:16:47", updatedAt="Sat Nov 20 2021 23:06:07")
    comment937 = Comment(videoId=179, channelId=15, content="She was only made the society president because she can whistle with her toes.", createdAt="Mon Jul 26 2021 18:36:29", updatedAt="Sat Nov 20 2021 16:14:31")
    comment938 = Comment(videoId=482, channelId=44, content="He knew it was going to be a bad day when he saw mountain lions roaming the streets.", createdAt="Sun Jul 11 2021 19:29:00", updatedAt="Sun May 02 2021 11:01:35")
    comment939 = Comment(videoId=752, channelId=1, content="his seven-layer cake only had six layers.", createdAt="Wed Feb 02 2022 15:16:43", updatedAt="Fri Aug 27 2021 04:43:00")
    comment940 = Comment(videoId=734, channelId=4, content="Today I bought a raincoat and wore it on a sunny day.", createdAt="Sun Jun 13 2021 14:03:59", updatedAt="Tue Feb 08 2022 20:46:17")
    comment941 = Comment(videoId=164, channelId=26, content="I made myself a peanut butter sandwich as I didn't want to subsist on veggie crackers.", createdAt="Fri Apr 23 2021 22:53:44", updatedAt="Sat Sep 25 2021 11:00:11")
    comment942 = Comment(videoId=340, channelId=98, content="Nudist colonies shun fig-leaf couture.", createdAt="Sun May 09 2021 08:29:33", updatedAt="Thu May 20 2021 09:25:54")
    comment943 = Comment(videoId=240, channelId=10, content="It was at that moment that he learned there are certain parts of the body that you should never Nair.", createdAt="Tue Jun 29 2021 15:52:34", updatedAt="Mon May 03 2021 18:44:35")
    comment944 = Comment(videoId=509, channelId=2, content="Choosing to do nothing is still a choice, after all.", createdAt="Fri Apr 16 2021 03:55:45", updatedAt="Sat Mar 19 2022 09:57:36")
    comment945 = Comment(videoId=297, channelId=75, content="Nancy was proud that she ran a tight shipwreck.", createdAt="Sat Sep 11 2021 16:29:40", updatedAt="Sat May 08 2021 19:39:30")
    comment946 = Comment(videoId=120, channelId=39, content="For the 216th time, he said he would quit drinking soda after this last Coke.", createdAt="Sat Aug 07 2021 12:42:39", updatedAt="Tue Sep 07 2021 22:41:13")
    comment947 = Comment(videoId=181, channelId=19, content="The minute she landed she understood the reason this was a fly-over state.", createdAt="Sat Sep 25 2021 12:36:05", updatedAt="Sun May 02 2021 08:50:13")
    comment948 = Comment(videoId=429, channelId=4, content="The bird had a belief that it was really a groundhog.", createdAt="Sun Sep 26 2021 20:07:59", updatedAt="Tue Jan 11 2022 14:52:12")
    comment949 = Comment(videoId=325, channelId=14, content="We have young kids who often walk into our room at night for various reasons including clowns in the closet.", createdAt="Mon Apr 04 2022 15:33:28", updatedAt="Mon Apr 26 2021 02:00:48")
    comment950 = Comment(videoId=715, channelId=56, content="Garlic ice-cream was her favorite.", createdAt="Sat Oct 16 2021 04:53:51", updatedAt="Thu May 06 2021 16:58:35")
    comment952 = Comment(videoId=24, channelId=95, content="I only enjoy window shopping when the windows are transparent.", createdAt="Sat Aug 21 2021 15:01:58", updatedAt="Sun Aug 15 2021 02:55:37")
    comment953 = Comment(videoId=702, channelId=62, content="She learned that water bottles are no longer just to hold liquid, but they're also status symbols.", createdAt="Sun Mar 20 2022 12:05:45", updatedAt="Wed Dec 15 2021 20:43:05")
    comment954 = Comment(videoId=386, channelId=67, content="The underground bunker was filled with chips and candy.", createdAt="Thu Dec 09 2021 06:28:28", updatedAt="Sun Mar 20 2022 22:00:15")
    comment955 = Comment(videoId=434, channelId=59, content="When confronted with a rotary dial phone the teenager was perplexed.", createdAt="Mon Oct 18 2021 20:44:13", updatedAt="Wed Dec 08 2021 09:18:32")
    comment956 = Comment(videoId=457, channelId=91, content="She wasn't sure whether to be impressed or concerned that he folded underwear in neat little packages.", createdAt="Wed Apr 21 2021 13:53:03", updatedAt="Fri Jul 23 2021 21:07:47")
    comment958 = Comment(videoId=289, channelId=58, content="I checked to make sure that he was still alive.", createdAt="Thu Feb 03 2022 23:34:45", updatedAt="Sun Aug 08 2021 11:26:08")
    comment959 = Comment(videoId=40, channelId=55, content="It would have been a better night if the guys next to us weren't in the splash zone.", createdAt="Sat Feb 05 2022 05:27:10", updatedAt="Fri Apr 23 2021 10:27:02")
    comment960 = Comment(videoId=631, channelId=39, content="The tart lemonade quenched her thirst, but not her longing.", createdAt="Sun Mar 06 2022 12:16:35", updatedAt="Tue Mar 22 2022 06:32:22")
    comment961 = Comment(videoId=103, channelId=22, content="He never understood why what, when, and where left out who.", createdAt="Mon Mar 21 2022 09:31:17", updatedAt="Fri Apr 01 2022 12:33:15")
    comment962 = Comment(videoId=59, channelId=5, content="For some unfathomable reason, the response team didn't consider a lack of milk for my cereal as a proper emergency.", createdAt="Sun Jul 04 2021 08:12:57", updatedAt="Tue May 04 2021 17:26:06")
    comment963 = Comment(videoId=230, channelId=29, content="As you consider all the possible ways to improve yourself and the world, you notice John Travolta seems fairly unhappy.", createdAt="Sat Feb 05 2022 05:53:10", updatedAt="Tue Nov 02 2021 02:07:54")
    comment964 = Comment(videoId=491, channelId=15, content="I was very proud of my nickname throughout high school but today- I couldn’t be any different to what my nickname was.", createdAt="Tue Oct 12 2021 07:46:34", updatedAt="Sun Oct 10 2021 20:50:24")
    comment965 = Comment(videoId=245, channelId=89, content="You have no right to call yourself creative until you look at a trowel and think that it would make a great lockpick.", createdAt="Thu Sep 02 2021 10:22:22", updatedAt="Thu Oct 28 2021 01:08:50")
    comment966 = Comment(videoId=235, channelId=13, content="Having no hair made him look even hairier.", createdAt="Mon Oct 04 2021 07:02:29", updatedAt="Sat Feb 05 2022 20:51:06")
    comment967 = Comment(videoId=412, channelId=69, content="Sometimes you have to just give up and win by cheating.", createdAt="Tue Jul 06 2021 15:59:00", updatedAt="Mon Apr 26 2021 13:12:44")
    comment968 = Comment(videoId=225, channelId=4, content="When transplanting seedlings, candied teapots will make the task easier.", createdAt="Thu Sep 09 2021 21:10:46", updatedAt="Fri Oct 15 2021 17:59:27")
    comment969 = Comment(videoId=157, channelId=44, content="Too many prisons have become early coffins.", createdAt="Tue Apr 27 2021 22:32:37", updatedAt="Sat Jun 19 2021 08:27:00")
    comment970 = Comment(videoId=340, channelId=66, content="The waitress was not amused when he ordered green eggs and ham.", createdAt="Wed May 26 2021 03:37:40", updatedAt="Wed Oct 06 2021 04:24:31")
    comment971 = Comment(videoId=754, channelId=63, content="The fish listened intently to what the frogs had to say.", createdAt="Sun Feb 06 2022 17:56:28", updatedAt="Tue Mar 15 2022 06:02:18")
    comment972 = Comment(videoId=9, channelId=72, content="The bird had a belief that it was really a groundhog.", createdAt="Fri Feb 04 2022 12:08:01", updatedAt="Wed Jun 09 2021 13:37:51")
    comment973 = Comment(videoId=435, channelId=10, content="So long and thanks for the fish.", createdAt="Mon Apr 26 2021 17:38:12", updatedAt="Sat Jun 19 2021 15:06:24")
    comment974 = Comment(videoId=666, channelId=83, content="Iron pyrite is the most foolish of all minerals.", createdAt="Sun Dec 26 2021 11:48:16", updatedAt="Sat Feb 05 2022 14:18:51")
    comment975 = Comment(videoId=742, channelId=13, content="The heat", createdAt="Thu Oct 21 2021 14:37:08", updatedAt="Sun Mar 20 2022 03:53:47")
    comment976 = Comment(videoId=362, channelId=59, content="He turned in the research paper on Friday; otherwise, he would have not passed the class.", createdAt="Sat Jun 12 2021 19:18:13", updatedAt="Mon Apr 19 2021 21:27:02")
    comment977 = Comment(videoId=62, channelId=87, content="Potato wedges probably are not best for relationships.", createdAt="Sun Sep 05 2021 13:26:53", updatedAt="Tue Aug 17 2021 20:31:20")
    comment978 = Comment(videoId=749, channelId=31, content="He had accidentally hacked into his company's server.", createdAt="Tue Aug 17 2021 13:15:00", updatedAt="Tue Jan 04 2022 14:50:20")
    comment979 = Comment(videoId=545, channelId=34, content="We need to rent a room for our party.", createdAt="Wed Nov 03 2021 01:31:56", updatedAt="Tue Nov 30 2021 18:06:44")
    comment981 = Comment(videoId=458, channelId=93, content="The dead trees waited to be ignited by the smallest spark and seek their revenge.", createdAt="Sat May 15 2021 05:23:52", updatedAt="Sat Feb 05 2022 14:46:43")
    comment982 = Comment(videoId=170, channelId=47, content="Barking dogs and screaming toddlers have the unique ability to turn friendly neighbors into cranky enemies.", createdAt="Sat Jan 29 2022 17:45:15", updatedAt="Tue Oct 19 2021 11:32:56")
    comment983 = Comment(videoId=63, channelId=16, content="The father died during childbirth.", createdAt="Wed Sep 01 2021 03:02:27", updatedAt="Thu Aug 26 2021 11:27:22")
    comment984 = Comment(videoId=179, channelId=13, content="He found his art never progressed when he literally used his sweat and tears.", createdAt="Sun Aug 15 2021 05:18:09", updatedAt="Sat Mar 05 2022 07:28:39")
    comment985 = Comment(videoId=696, channelId=33, content="They say that dogs are man's best friend, but this cat was setting out to sabotage that theory.", createdAt="Fri Nov 19 2021 09:42:52", updatedAt="Sat Jan 29 2022 03:35:01")
    comment986 = Comment(videoId=268, channelId=85, content="Traveling became almost extinct during the pandemic.", createdAt="Thu May 06 2021 22:11:55", updatedAt="Sun Jul 25 2021 14:42:42")
    comment987 = Comment(videoId=195, channelId=67, content="Tomatoes make great weapons when water balloons aren’t available.", createdAt="Sat Oct 09 2021 00:00:33", updatedAt="Thu Jul 01 2021 04:53:47")
    comment988 = Comment(videoId=10, channelId=66, content="With the high wind warning", createdAt="Tue Mar 15 2022 04:04:10", updatedAt="Sun May 23 2021 23:45:41")
    comment989 = Comment(videoId=514, channelId=84, content="Mary realized if her calculator had a history, it would be more embarrassing than her computer browser history.", createdAt="Wed Apr 06 2022 15:05:19", updatedAt="Thu Feb 10 2022 06:29:18")
    comment990 = Comment(videoId=437, channelId=41, content="The family’s excitement over going to Disneyland was crazier than she anticipated.", createdAt="Fri May 21 2021 16:27:25", updatedAt="Tue Nov 16 2021 21:40:20")
    comment991 = Comment(videoId=189, channelId=59, content="Art doesn't have to be intentional.", createdAt="Tue Jun 22 2021 00:13:53", updatedAt="Mon Oct 04 2021 06:06:34")
    comment992 = Comment(videoId=294, channelId=88, content="The shooter says goodbye to his love.", createdAt="Sun Oct 24 2021 05:34:58", updatedAt="Sat Dec 18 2021 23:39:29")
    comment993 = Comment(videoId=461, channelId=69, content="Last Friday I saw a spotted striped blue worm shake hands with a legless lizard.", createdAt="Mon Oct 04 2021 07:51:57", updatedAt="Sat Aug 21 2021 11:58:38")
    comment994 = Comment(videoId=222, channelId=56, content="Mr. Montoya knows the way to the bakery even though he's never been there.", createdAt="Wed Dec 15 2021 05:53:35", updatedAt="Sat Mar 19 2022 09:42:52")
    comment995 = Comment(videoId=670, channelId=70, content="She had a habit of taking showers in lemonade.", createdAt="Tue Sep 21 2021 06:36:56", updatedAt="Thu Oct 28 2021 22:50:59")
    comment996 = Comment(videoId=592, channelId=72, content="Nothing is as cautiously cuddly as a pet porcupine.", createdAt="Tue May 18 2021 01:32:17", updatedAt="Thu Mar 03 2022 11:24:24")
    comment997 = Comment(videoId=758, channelId=61, content="That must be the tenth time I've been arrested for selling deep-fried cigars.", createdAt="Thu Feb 17 2022 23:53:34", updatedAt="Wed Mar 23 2022 11:13:40")
    comment998 = Comment(videoId=686, channelId=25, content="She had some amazing news to share but nobody to share it with.", createdAt="Sat Aug 28 2021 02:35:45", updatedAt="Thu Dec 30 2021 06:57:56")
    comment999 = Comment(videoId=634, channelId=73, content="Sometimes I stare at a door or a wall and I wonder what is this reality, why am I alive, and what is this all about?", createdAt="Tue Sep 21 2021 17:54:31", updatedAt="Fri Oct 08 2021 17:26:43")
    comment1000 = Comment(videoId=386, channelId=13, content="The rusty nail stood erect, angled at a 45-degree angle, just waiting for the perfect barefoot to come along.", createdAt="Sat May 15 2021 04:16:01", updatedAt="Fri Jan 07 2022 05:37:06")
    comment1001 = Comment(videoId=480, channelId=52, content="The complicated school homework left the parents trying to help their kids quite confused.", createdAt="Thu Apr 29 2021 10:16:23", updatedAt="Fri Apr 23 2021 03:31:22")
    comment1003 = Comment(videoId=54, channelId=47, content="She let the balloon float up into the air with her hopes and dreams.", createdAt="Thu Jan 27 2022 09:55:34", updatedAt="Fri Apr 30 2021 15:39:13")
    comment1004 = Comment(videoId=58, channelId=28, content="No matter how beautiful the sunset, it saddened her knowing she was one day older.", createdAt="Wed Aug 04 2021 17:12:55", updatedAt="Sat Mar 05 2022 22:54:34")
    comment1005 = Comment(videoId=764, channelId=90, content="The fish listened intently to what the frogs had to say.", createdAt="Fri Jun 11 2021 05:22:22", updatedAt="Thu Jan 27 2022 03:25:23")
    comment1006 = Comment(videoId=603, channelId=95, content="I currently have 4 windows open up… and I don’t know why.", createdAt="Sun Sep 26 2021 07:12:59", updatedAt="Tue Feb 08 2022 17:20:50")
    comment1007 = Comment(videoId=675, channelId=92, content="Nancy thought the best way to create a welcoming home was to line it with barbed wire.", createdAt="Mon Nov 01 2021 21:53:33", updatedAt="Fri Mar 04 2022 09:41:53")
    comment1008 = Comment(videoId=7, channelId=51, content="The external scars tell only part of the story.", createdAt="Thu May 06 2021 07:30:56", updatedAt="Sun Jul 25 2021 15:11:25")
    comment1009 = Comment(videoId=699, channelId=82, content="I always dreamed about being stranded on a desert island until it actually happened.", createdAt="Mon Jan 31 2022 06:39:54", updatedAt="Tue Sep 28 2021 21:23:31")
    comment1010 = Comment(videoId=467, channelId=62, content="They're playing the piano while flying in the plane.", createdAt="Fri Dec 10 2021 09:49:39", updatedAt="Wed Jul 28 2021 16:42:47")
    comment1011 = Comment(videoId=772, channelId=33, content="If you spin around three times, you'll start to feel melancholy.", createdAt="Mon Dec 20 2021 14:59:22", updatedAt="Sun Mar 20 2022 21:56:31")
    comment1012 = Comment(videoId=735, channelId=6, content="She was only made the society president because she can whistle with her toes.", createdAt="Sun Jan 23 2022 02:23:03", updatedAt="Sun Aug 22 2021 16:38:06")
    comment1013 = Comment(videoId=331, channelId=21, content="He put heat on the wound to see what would grow.", createdAt="Sun Apr 25 2021 01:12:10", updatedAt="Sun Jun 20 2021 13:54:23")
    comment1014 = Comment(videoId=563, channelId=62, content="He figured a few sticks of dynamite were easier than a fishing pole to catch fish.", createdAt="Sun Jun 20 2021 05:29:37", updatedAt="Fri Jun 25 2021 03:38:13")
    comment1015 = Comment(videoId=442, channelId=97, content="The blinking lights of the antenna tower came into focus just as I heard a loud snap.", createdAt="Fri Feb 11 2022 21:43:44", updatedAt="Mon Sep 13 2021 18:09:54")
    comment1016 = Comment(videoId=72, channelId=71, content="The elderly neighborhood became enraged over the coyotes who had been blamed for the poodle’s disappearance.", createdAt="Sun Nov 07 2021 19:53:39", updatedAt="Mon Apr 12 2021 14:49:09")
    comment1017 = Comment(videoId=216, channelId=87, content="She was amazed by the large chunks of ice washing up on the beach.", createdAt="Wed Oct 20 2021 07:54:02", updatedAt="Mon Apr 26 2021 16:25:24")
    comment1018 = Comment(videoId=744, channelId=56, content="It had been sixteen days since the zombies first attacked.", createdAt="Thu Jul 15 2021 09:24:04", updatedAt="Sun Aug 08 2021 17:17:09")
    comment1019 = Comment(videoId=298, channelId=59, content="So long and thanks for the fish.", createdAt="Wed Jan 26 2022 15:14:53", updatedAt="Sat Jun 05 2021 22:10:17")
    comment1020 = Comment(videoId=314, channelId=88, content="The Japanese yen for commerce is still well-known.", createdAt="Sat Feb 19 2022 21:01:17", updatedAt="Tue Jan 18 2022 17:18:06")
    comment1021 = Comment(videoId=73, channelId=14, content="He liked to play with words in the bathtub.", createdAt="Mon Jul 26 2021 19:36:57", updatedAt="Sat Feb 12 2022 17:26:34")
    comment1022 = Comment(videoId=770, channelId=73, content="The blue parrot drove by the hitchhiking mongoose.", createdAt="Mon Nov 29 2021 22:41:52", updatedAt="Mon Sep 27 2021 08:51:38")
    comment1023 = Comment(videoId=737, channelId=70, content="As the rental car rolled to a stop on the dark road, her fear increased by the moment.", createdAt="Wed Sep 08 2021 21:46:11", updatedAt="Wed Apr 28 2021 15:52:37")
    comment1024 = Comment(videoId=32, channelId=22, content="Jason lived his life by the motto, \"Anything worth doing is worth doing poorly.\"", createdAt="Wed Jun 16 2021 17:16:02", updatedAt="Fri Dec 24 2021 21:40:44")
    comment1025 = Comment(videoId=148, channelId=57, content="Normal activities took extraordinary amounts of concentration at the high altitude.", createdAt="Sun Sep 19 2021 20:29:11", updatedAt="Tue Jan 25 2022 05:01:47")
    comment1026 = Comment(videoId=176, channelId=84, content="She traveled because it cost the same as therapy and was a lot more enjoyable.", createdAt="Mon Nov 29 2021 10:06:53", updatedAt="Sat Sep 18 2021 22:09:01")
    comment1027 = Comment(videoId=762, channelId=11, content="Everyone was busy, so I went to the movie alone.", createdAt="Tue Jun 15 2021 20:58:39", updatedAt="Tue Aug 24 2021 22:24:10")
    comment1028 = Comment(videoId=394, channelId=70, content="It was a really good Monday for being a Saturday.", createdAt="Sat Apr 09 2022 20:07:31", updatedAt="Thu Mar 17 2022 20:12:32")
    comment1029 = Comment(videoId=122, channelId=47, content="There should have been a time and a place, but this wasn't it.", createdAt="Thu Oct 21 2021 18:42:10", updatedAt="Tue Jun 08 2021 15:39:58")
    comment1030 = Comment(videoId=89, channelId=19, content="Be careful with that butter knife.", createdAt="Sun Aug 08 2021 05:00:46", updatedAt="Sun Jun 20 2021 15:23:30")
    comment1031 = Comment(videoId=668, channelId=63, content="Three years later, the coffin was still full of Jello.", createdAt="Tue Oct 12 2021 09:12:42", updatedAt="Tue Jun 29 2021 20:05:52")
    comment1032 = Comment(videoId=304, channelId=16, content="She had a difficult time owning up to her own crazy self.", createdAt="Fri Sep 10 2021 17:06:38", updatedAt="Thu Sep 23 2021 02:09:05")
    comment1033 = Comment(videoId=483, channelId=85, content="The tortoise jumped into the lake with dreams of becoming a sea turtle.", createdAt="Mon Apr 19 2021 23:24:46", updatedAt="Mon Sep 13 2021 01:55:46")
    comment1034 = Comment(videoId=622, channelId=19, content="He stomped on his fruit loops and thus became a cereal killer.", createdAt="Sat Apr 24 2021 16:47:47", updatedAt="Wed Sep 01 2021 20:44:11")
    comment1035 = Comment(videoId=471, channelId=100, content="Nothing is as cautiously cuddly as a pet porcupine.", createdAt="Mon Nov 22 2021 04:26:02", updatedAt="Mon Oct 04 2021 08:43:36")
    comment1036 = Comment(videoId=485, channelId=4, content="Poison ivy grew through the fence they said was impenetrable.", createdAt="Tue Nov 16 2021 18:21:07", updatedAt="Tue Apr 13 2021 04:15:10")
    comment1037 = Comment(videoId=537, channelId=66, content="We have a lot of rain in June.", createdAt="Mon Feb 14 2022 11:43:31", updatedAt="Sat May 15 2021 17:17:58")
    comment1038 = Comment(videoId=273, channelId=72, content="It didn't take long for Gary to detect the robbers were amateurs.", createdAt="Fri Jan 14 2022 09:14:34", updatedAt="Mon Feb 28 2022 17:39:52")
    comment1039 = Comment(videoId=276, channelId=44, content="A quiet house is nice until you are ordered to stay in it for months.", createdAt="Wed Feb 02 2022 07:43:29", updatedAt="Thu Apr 22 2021 22:34:36")
    comment1040 = Comment(videoId=302, channelId=59, content="Situps are a terrible way to end your day.", createdAt="Mon Dec 13 2021 17:32:54", updatedAt="Sat Dec 04 2021 13:13:19")
    comment1041 = Comment(videoId=480, channelId=46, content="There's no reason a hula hoop can't also be a circus ring.", createdAt="Sun Feb 06 2022 11:12:07", updatedAt="Wed Oct 20 2021 16:33:15")
    comment1042 = Comment(videoId=392, channelId=33, content="The overpass went under the highway and into a secret world.", createdAt="Mon Jul 12 2021 09:57:32", updatedAt="Fri Jul 02 2021 08:34:05")
    comment1043 = Comment(videoId=357, channelId=71, content="Chocolate covered crickets were his favorite snack.", createdAt="Sun Mar 27 2022 06:45:15", updatedAt="Thu Sep 02 2021 14:24:51")
    comment1044 = Comment(videoId=291, channelId=95, content="The Tsunami wave crashed against the raised houses and broke the pilings as if they were toothpicks.", createdAt="Wed Nov 10 2021 01:48:06", updatedAt="Tue May 11 2021 17:53:51")
    comment1045 = Comment(videoId=128, channelId=78, content="Tom got a small piece of pie.", createdAt="Wed Jan 05 2022 11:44:34", updatedAt="Fri Apr 01 2022 12:12:26")
    comment1046 = Comment(videoId=130, channelId=15, content="They wandered into a strange Tiki bar on the edge of the small beach town.", createdAt="Mon Nov 08 2021 03:46:10", updatedAt="Thu Mar 17 2022 02:04:54")
    comment1047 = Comment(videoId=98, channelId=25, content="She was sad to hear that fireflies are facing extinction due to artificial light, habitat loss, and pesticides.", createdAt="Thu Nov 04 2021 13:20:49", updatedAt="Fri May 21 2021 21:07:29")
    comment1048 = Comment(videoId=495, channelId=86, content="The tattered work gloves speak of the many hours of hard labor he endured throughout his life.", createdAt="Fri Feb 25 2022 11:30:48", updatedAt="Wed Oct 20 2021 12:13:24")
    comment1049 = Comment(videoId=622, channelId=62, content="People who insist on picking their teeth with their elbows are so annoying!", createdAt="Sat Mar 19 2022 11:52:13", updatedAt="Thu Dec 02 2021 08:40:24")
    comment1050 = Comment(videoId=71, channelId=7, content="He was an introvert that extroverts seemed to love.", createdAt="Tue May 04 2021 01:53:30", updatedAt="Thu Jan 20 2022 21:18:10")
    comment1051 = Comment(videoId=139, channelId=92, content="The lake is a long way from here.", createdAt="Tue Apr 05 2022 07:54:13", updatedAt="Fri Apr 16 2021 06:34:48")
    comment1052 = Comment(videoId=755, channelId=4, content="Swim at your own risk was taken as a challenge for the group of Kansas City college students.", createdAt="Sun Sep 05 2021 04:09:39", updatedAt="Tue Nov 09 2021 05:29:13")
    comment1054 = Comment(videoId=690, channelId=81, content="She had that tint of craziness in her soul that made her believe she could actually make a difference.", createdAt="Sat Jun 05 2021 07:25:01", updatedAt="Sun Jul 25 2021 14:36:06")
    comment1055 = Comment(videoId=194, channelId=18, content="Too many prisons have become early coffins.", createdAt="Fri Dec 31 2021 12:53:43", updatedAt="Sun Apr 18 2021 22:05:52")
    comment1056 = Comment(videoId=389, channelId=92, content="Separation anxiety is what happens when you can't find your phone.", createdAt="Wed Jul 28 2021 18:46:15", updatedAt="Mon Feb 07 2022 11:45:16")
    comment1057 = Comment(videoId=470, channelId=25, content="I love bacon, beer, birds, and baboons.", createdAt="Sun Mar 20 2022 02:37:54", updatedAt="Fri Nov 12 2021 21:15:48")
    comment1058 = Comment(videoId=660, channelId=1, content="The Guinea fowl flies through the air with all the grace of a turtle.", createdAt="Fri Sep 10 2021 01:33:08", updatedAt="Sat Dec 18 2021 15:14:31")
    comment1059 = Comment(videoId=764, channelId=34, content="There's no reason a hula hoop can't also be a circus ring.", createdAt="Mon Sep 06 2021 14:12:16", updatedAt="Mon Jan 10 2022 11:01:28")
    comment1060 = Comment(videoId=241, channelId=44, content="The worst thing about being at the top of the career ladder is that there's a long way to fall.", createdAt="Fri Nov 19 2021 02:47:46", updatedAt="Wed Jun 16 2021 06:15:43")
    comment1061 = Comment(videoId=314, channelId=3, content="I am counting my calories, yet I really want dessert.", createdAt="Mon Oct 11 2021 08:43:47", updatedAt="Tue Aug 31 2021 02:08:15")
    comment1062 = Comment(videoId=677, channelId=95, content="All she wanted was the answer, but she had no idea how much she would hate it.", createdAt="Wed Oct 27 2021 08:56:27", updatedAt="Thu Sep 30 2021 23:29:02")
    comment1063 = Comment(videoId=582, channelId=18, content="There are over 500 starfish in the bathroom drawer.", createdAt="Wed Sep 22 2021 15:38:34", updatedAt="Fri Aug 06 2021 14:37:30")
    comment1064 = Comment(videoId=440, channelId=58, content="Charles ate the french fries knowing they would be his last meal.", createdAt="Mon Jul 05 2021 07:51:45", updatedAt="Fri Mar 25 2022 14:09:07")
    comment1065 = Comment(videoId=760, channelId=92, content="His mind was blown that there was nothing in space except space itself.", createdAt="Mon Aug 09 2021 15:42:17", updatedAt="Thu Jun 24 2021 22:01:52")
    comment1066 = Comment(videoId=488, channelId=43, content="The lake is a long way from here.", createdAt="Mon Jul 12 2021 09:15:08", updatedAt="Sun Nov 28 2021 01:18:38")
    comment1067 = Comment(videoId=769, channelId=87, content="She could hear him in the shower singing with a joy she hoped he'd retain after she delivered the news.", createdAt="Mon Jan 10 2022 08:29:01", updatedAt="Wed Dec 22 2021 22:23:24")
    comment1068 = Comment(videoId=186, channelId=52, content="It caught him off guard that space smelled of seared steak.", createdAt="Thu Jul 08 2021 09:34:05", updatedAt="Fri Dec 31 2021 18:26:13")
    comment1069 = Comment(videoId=366, channelId=10, content="You bite up because of your lower jaw.", createdAt="Wed Apr 14 2021 20:36:00", updatedAt="Wed Mar 30 2022 02:23:13")
    comment1070 = Comment(videoId=151, channelId=27, content="The heat", createdAt="Sat Jul 10 2021 00:16:22", updatedAt="Tue Apr 20 2021 19:47:51")
    comment1071 = Comment(videoId=648, channelId=23, content="This book is sure to liquefy your brain.", createdAt="Sat Dec 11 2021 09:16:46", updatedAt="Mon Dec 06 2021 04:24:55")
    comment1072 = Comment(videoId=353, channelId=60, content="She borrowed the book from him many years ago and hasn't yet returned it.", createdAt="Fri Nov 19 2021 09:33:50", updatedAt="Sun Sep 26 2021 18:45:10")
    comment1074 = Comment(videoId=429, channelId=49, content="Improve your goldfish's physical fitness by getting him a bicycle.", createdAt="Fri Jan 28 2022 19:30:43", updatedAt="Sun May 30 2021 11:56:42")
    comment1075 = Comment(videoId=344, channelId=28, content="Shingle color was not something the couple had ever talked about.", createdAt="Fri Mar 25 2022 04:48:56", updatedAt="Sun Oct 17 2021 16:49:24")
    comment1076 = Comment(videoId=690, channelId=60, content="When transplanting seedlings, candied teapots will make the task easier.", createdAt="Tue May 04 2021 07:37:00", updatedAt="Wed Jun 16 2021 09:57:51")
    comment1077 = Comment(videoId=34, channelId=51, content="8% of 25 is the same as 25% of 8 and one of them is much easier to do in your head.", createdAt="Sat Nov 13 2021 20:54:40", updatedAt="Mon May 24 2021 22:38:35")
    comment1078 = Comment(videoId=769, channelId=71, content="Today I dressed my unicorn in preparation for the race.", createdAt="Sat Oct 02 2021 11:35:09", updatedAt="Wed Aug 25 2021 18:17:47")
    comment1079 = Comment(videoId=131, channelId=92, content="His confidence would have bee admirable if it wasn't for his stupidity.", createdAt="Mon Aug 09 2021 01:28:09", updatedAt="Mon Nov 29 2021 08:55:16")
    comment1080 = Comment(videoId=487, channelId=68, content="I want more detailed information.", createdAt="Sun Jul 04 2021 01:31:47", updatedAt="Sun Feb 06 2022 11:04:52")
    comment1081 = Comment(videoId=281, channelId=7, content="Flying fish flew by the space station.", createdAt="Mon Oct 04 2021 19:30:18", updatedAt="Tue Mar 08 2022 00:41:12")
    comment1082 = Comment(videoId=559, channelId=39, content="Andy loved to sleep on a bed of nails.", createdAt="Wed Jan 12 2022 08:23:06", updatedAt="Mon Nov 08 2021 09:16:09")
    comment1083 = Comment(videoId=680, channelId=7, content="The bird had a belief that it was really a groundhog.", createdAt="Tue Dec 07 2021 07:03:38", updatedAt="Fri Jun 25 2021 05:36:50")
    comment1084 = Comment(videoId=651, channelId=89, content="It's not often you find a soggy banana on the street.", createdAt="Mon Dec 27 2021 18:09:29", updatedAt="Sun Feb 06 2022 06:14:03")
    comment1085 = Comment(videoId=660, channelId=50, content="This is a Japanese doll.", createdAt="Thu Dec 16 2021 09:17:45", updatedAt="Sun Jul 11 2021 13:49:29")
    comment1086 = Comment(videoId=594, channelId=87, content="Homesickness became contagious in the young campers' cabin.", createdAt="Thu May 06 2021 16:27:25", updatedAt="Fri May 28 2021 05:25:20")
    comment1087 = Comment(videoId=333, channelId=56, content="Although it wasn't a pot of gold, Nancy was still enthralled at what she found at the end of the rainbow.", createdAt="Fri May 14 2021 11:32:24", updatedAt="Wed Dec 08 2021 15:36:27")
    comment1088 = Comment(videoId=510, channelId=5, content="He used to get confused between soldiers and shoulders, but as a military man, he now soldiers responsibility.", createdAt="Sun Aug 01 2021 11:35:05", updatedAt="Wed Jul 21 2021 21:20:23")
    comment1089 = Comment(videoId=272, channelId=46, content="Some bathing suits just shouldn’t be worn by some people.", createdAt="Sun May 23 2021 08:04:02", updatedAt="Thu Jul 15 2021 17:24:37")
    comment1090 = Comment(videoId=315, channelId=43, content="We have young kids who often walk into our room at night for various reasons including clowns in the closet.", createdAt="Fri May 14 2021 15:38:10", updatedAt="Thu Feb 24 2022 01:47:03")
    comment1091 = Comment(videoId=391, channelId=54, content="Happiness can be found in the depths of chocolate pudding.", createdAt="Tue Mar 22 2022 22:52:00", updatedAt="Thu Sep 09 2021 04:03:52")
    comment1092 = Comment(videoId=667, channelId=23, content="She was too short to see over the fence.", createdAt="Mon Feb 07 2022 00:37:13", updatedAt="Sun Jul 11 2021 05:30:35")
    comment1093 = Comment(videoId=314, channelId=69, content="Mr. Montoya knows the way to the bakery even though he's never been there.", createdAt="Sun Jun 20 2021 19:16:47", updatedAt="Sun Sep 26 2021 12:24:52")
    comment1094 = Comment(videoId=428, channelId=2, content="With a single flip of the coin, his life changed forever.", createdAt="Thu Jun 24 2021 14:28:58", updatedAt="Fri Dec 31 2021 11:25:10")
    comment1095 = Comment(videoId=407, channelId=19, content="Situps are a terrible way to end your day.", createdAt="Tue Feb 01 2022 05:20:58", updatedAt="Wed Sep 15 2021 12:31:18")
    comment1096 = Comment(videoId=644, channelId=26, content="She hadn't had her cup of coffee, and that made things all the worse.", createdAt="Fri Aug 27 2021 14:16:47", updatedAt="Mon Nov 22 2021 01:16:37")
    comment1097 = Comment(videoId=169, channelId=53, content="They finished building the road they knew no one would ever use.", createdAt="Mon Mar 21 2022 17:32:58", updatedAt="Sat Nov 20 2021 05:26:19")
    comment1098 = Comment(videoId=190, channelId=25, content="It's never been my responsibility to glaze the donuts.", createdAt="Sat Aug 07 2021 20:27:33", updatedAt="Fri Sep 03 2021 05:53:13")
    comment1099 = Comment(videoId=620, channelId=3, content="Malls are great places to shop; I can find everything I need under one roof.", createdAt="Thu Mar 03 2022 21:11:06", updatedAt="Tue Aug 03 2021 06:02:36")
    comment1100 = Comment(videoId=387, channelId=70, content="He wondered if it could be called a beach if there was no sand.", createdAt="Tue Dec 21 2021 23:21:45", updatedAt="Sat Jan 08 2022 16:50:28")
    comment1101 = Comment(videoId=84, channelId=74, content="There is no better feeling than staring at a wall with closed eyes.", createdAt="Sat Jul 24 2021 13:27:52", updatedAt="Thu Nov 25 2021 20:21:58")
    comment1102 = Comment(videoId=169, channelId=11, content="The shark-infested South Pine channel was the only way in or out.", createdAt="Wed Nov 03 2021 02:26:24", updatedAt="Sun May 09 2021 02:40:16")
    comment1103 = Comment(videoId=97, channelId=2, content="Peter found road kill an excellent way to save money on dinner.", createdAt="Tue Nov 09 2021 02:03:01", updatedAt="Wed Jun 30 2021 08:59:39")
    comment1104 = Comment(videoId=348, channelId=32, content="Gary didn't understand why Doug went upstairs to get one dollar bills when he invited him to go cow tipping.", createdAt="Wed Aug 04 2021 18:54:26", updatedAt="Sat Oct 23 2021 22:52:11")
    comment1105 = Comment(videoId=130, channelId=7, content="I just wanted to tell you I could see the love you have for your child by the way you look at her.", createdAt="Sat Apr 17 2021 12:59:23", updatedAt="Wed Nov 10 2021 12:43:24")
    comment1106 = Comment(videoId=227, channelId=30, content="The stench from the feedlot permeated the car despite having the air conditioning on recycled air.", createdAt="Fri Nov 19 2021 13:51:30", updatedAt="Sun Jun 13 2021 11:10:27")
    comment1107 = Comment(videoId=140, channelId=44, content="Going from child, to childish, to childlike is only a matter of time.", createdAt="Mon Jan 17 2022 21:42:26", updatedAt="Wed Dec 22 2021 18:17:52")
    comment1108 = Comment(videoId=764, channelId=77, content="his seven-layer cake only had six layers.", createdAt="Sun Jul 18 2021 18:18:17", updatedAt="Fri Aug 06 2021 16:32:52")
    comment1109 = Comment(videoId=454, channelId=49, content="He was willing to find the depths of the rabbit hole in order to be with her.", createdAt="Tue Mar 22 2022 15:17:44", updatedAt="Thu Sep 02 2021 14:54:31")
    comment1110 = Comment(videoId=413, channelId=57, content="I like to leave work after my eight-hour tea-break.", createdAt="Mon Mar 21 2022 19:33:03", updatedAt="Wed Sep 15 2021 12:39:36")
    comment1111 = Comment(videoId=288, channelId=77, content="It took me too long to realize that the ceiling hadn't been painted to look like the sky.", createdAt="Tue Jan 11 2022 07:44:42", updatedAt="Sun Nov 14 2021 02:57:33")
    comment1112 = Comment(videoId=700, channelId=90, content="There have been days when I wished to be separated from my body, but today wasn’t one of those days.", createdAt="Tue Oct 19 2021 12:11:05", updatedAt="Sun Apr 25 2021 03:32:25")
    comment1113 = Comment(videoId=330, channelId=22, content="If eating three-egg omelets causes weight-gain, budgie eggs are a good substitute.", createdAt="Wed Mar 02 2022 06:18:50", updatedAt="Wed Aug 18 2021 15:06:20")
    comment1114 = Comment(videoId=333, channelId=61, content="Choosing to do nothing is still a choice, after all.", createdAt="Sat Jan 29 2022 06:17:18", updatedAt="Fri Feb 04 2022 00:28:54")
    comment1115 = Comment(videoId=599, channelId=25, content="He wondered if it could be called a beach if there was no sand.", createdAt="Sun Nov 28 2021 23:21:43", updatedAt="Sun Apr 25 2021 11:34:17")
    comment1116 = Comment(videoId=535, channelId=1, content="Her scream silenced the rowdy teenagers.", createdAt="Sun Apr 11 2021 11:04:21", updatedAt="Sat Jul 17 2021 13:02:58")
    comment1117 = Comment(videoId=664, channelId=67, content="For the 216th time, he said he would quit drinking soda after this last Coke.", createdAt="Sun Jul 25 2021 21:11:03", updatedAt="Fri Apr 30 2021 09:24:30")
    comment1118 = Comment(videoId=378, channelId=52, content="There was no telling what thoughts would come from the machine.", createdAt="Tue Sep 14 2021 03:41:26", updatedAt="Thu Sep 09 2021 10:29:26")
    comment1119 = Comment(videoId=613, channelId=70, content="In the end, he realized he could see sound and hear words.", createdAt="Sun Feb 13 2022 20:52:02", updatedAt="Thu Jan 06 2022 23:36:03")
    comment1120 = Comment(videoId=723, channelId=7, content="He had a vague sense that trees gave birth to dinosaurs.", createdAt="Sat Jan 29 2022 09:41:24", updatedAt="Tue Nov 30 2021 03:15:52")
    comment1121 = Comment(videoId=342, channelId=53, content="Buried deep in the snow, he hoped his batteries were fresh in his avalanche beacon.", createdAt="Sun Feb 13 2022 02:01:01", updatedAt="Wed Dec 29 2021 11:33:53")
    comment1122 = Comment(videoId=636, channelId=57, content="You should never take advice from someone who thinks red paint dries quicker than blue paint.", createdAt="Fri Aug 13 2021 04:51:51", updatedAt="Thu Aug 26 2021 10:18:03")
    comment1123 = Comment(videoId=144, channelId=54, content="It had been sixteen days since the zombies first attacked.", createdAt="Mon Oct 18 2021 11:41:43", updatedAt="Tue Jan 04 2022 07:04:55")
    comment1124 = Comment(videoId=418, channelId=23, content="She felt that chill that makes the hairs on the back of your neck when he walked into the room.", createdAt="Thu Jan 20 2022 14:00:18", updatedAt="Mon Nov 01 2021 16:00:50")
    comment1125 = Comment(videoId=313, channelId=3, content="He had concluded that pigs must be able to fly in Hog Heaven.", createdAt="Sun Dec 12 2021 02:32:24", updatedAt="Fri Jan 28 2022 21:17:04")
    comment1126 = Comment(videoId=315, channelId=4, content="He liked to play with words in the bathtub.", createdAt="Mon Jun 28 2021 14:47:08", updatedAt="Thu Mar 03 2022 16:13:41")
    comment1127 = Comment(videoId=298, channelId=81, content="I come from a tribe of head-hunters, so I will never need a shrink.", createdAt="Sun Mar 06 2022 05:45:02", updatedAt="Sat Sep 04 2021 20:38:20")
    comment1128 = Comment(videoId=128, channelId=17, content="I was fishing for compliments and accidentally caught a trout.", createdAt="Tue Feb 22 2022 05:08:58", updatedAt="Wed Dec 08 2021 03:19:46")
    comment1129 = Comment(videoId=341, channelId=33, content="I covered my friend in baby oil.", createdAt="Sat Jan 08 2022 12:46:31", updatedAt="Mon Jan 10 2022 13:49:23")
    comment1130 = Comment(videoId=293, channelId=48, content="His get rich quick scheme was to grow a cactus farm.", createdAt="Sat Jun 19 2021 03:51:56", updatedAt="Mon Nov 15 2021 20:55:33")
    comment1131 = Comment(videoId=673, channelId=17, content="For some unfathomable reason, the response team didn't consider a lack of milk for my cereal as a proper emergency.", createdAt="Thu Apr 07 2022 22:33:35", updatedAt="Tue Nov 02 2021 12:31:03")
    comment1132 = Comment(videoId=251, channelId=86, content="The sun had set and so had his dreams.", createdAt="Sat Apr 24 2021 05:08:53", updatedAt="Sat Nov 06 2021 06:51:19")
    comment1133 = Comment(videoId=197, channelId=53, content="The worst thing about being at the top of the career ladder is that there's a long way to fall.", createdAt="Thu Sep 23 2021 20:05:41", updatedAt="Tue Dec 21 2021 16:44:01")
    comment1134 = Comment(videoId=238, channelId=29, content="As he looked out the window, he saw a clown walk by.", createdAt="Sun Apr 11 2021 07:05:30", updatedAt="Mon Apr 26 2021 22:25:15")
    comment1135 = Comment(videoId=420, channelId=13, content="Nobody questions who built the pyramids in Mexico.", createdAt="Wed Mar 09 2022 22:11:04", updatedAt="Tue Sep 07 2021 12:26:14")
    comment1136 = Comment(videoId=298, channelId=20, content="I trust everything that's written in purple ink.", createdAt="Sun Jan 09 2022 21:48:46", updatedAt="Wed Feb 23 2022 22:08:34")
    comment1137 = Comment(videoId=312, channelId=34, content="The fact that there's a stairway to heaven and a highway to hell explains life well.", createdAt="Sat Jan 29 2022 16:34:51", updatedAt="Wed Nov 24 2021 08:34:52")
    comment1138 = Comment(videoId=244, channelId=57, content="Her hair was windswept as she rode in the black convertible.", createdAt="Mon May 03 2021 08:00:44", updatedAt="Fri Dec 24 2021 09:42:48")
    comment1139 = Comment(videoId=349, channelId=82, content="He had a hidden stash underneath the floorboards in the back room of the house.", createdAt="Fri Jan 28 2022 11:30:28", updatedAt="Tue Jun 01 2021 11:00:32")
    comment1140 = Comment(videoId=722, channelId=72, content="I've traveled all around Africa and still haven't found the gnu who stole my scarf.", createdAt="Wed Nov 10 2021 00:37:11", updatedAt="Tue Jul 13 2021 06:27:37")
    comment1141 = Comment(videoId=52, channelId=45, content="That was how he came to win $1 million.", createdAt="Sun Jul 04 2021 01:30:07", updatedAt="Wed Mar 16 2022 14:11:20")
    comment1142 = Comment(videoId=18, channelId=93, content="They called out her name time and again, but were met with nothing but silence.", createdAt="Sun May 16 2021 20:14:14", updatedAt="Sun Sep 26 2021 14:50:03")
    comment1143 = Comment(videoId=181, channelId=63, content="Her daily goal was to improve on yesterday.", createdAt="Wed Oct 20 2021 23:59:12", updatedAt="Thu Apr 07 2022 04:04:18")
    comment1144 = Comment(videoId=81, channelId=26, content="The teenage boy was accused of breaking his arm simply to get out of the test.", createdAt="Sat Jun 19 2021 19:18:03", updatedAt="Thu Nov 25 2021 05:39:09")
    comment1145 = Comment(videoId=697, channelId=4, content="Baby wipes are made of chocolate stardust.", createdAt="Fri Oct 01 2021 20:54:54", updatedAt="Tue May 04 2021 19:35:11")
    comment1146 = Comment(videoId=262, channelId=1, content="Trash covered the landscape like sprinkles do a birthday cake.", createdAt="Thu Feb 17 2022 04:09:59", updatedAt="Wed Nov 10 2021 00:26:22")
    comment1147 = Comment(videoId=25, channelId=9, content="Three years later, the coffin was still full of Jello.", createdAt="Thu Mar 31 2022 02:40:26", updatedAt="Sun Nov 07 2021 13:22:36")
    comment1148 = Comment(videoId=257, channelId=35, content="I would be delighted if the sea were full of cucumber juice.", createdAt="Wed Nov 17 2021 22:48:58", updatedAt="Sun Dec 05 2021 00:48:15")
    comment1149 = Comment(videoId=755, channelId=79, content="The elephant didn't want to talk about the person in the room.", createdAt="Thu Mar 17 2022 02:47:48", updatedAt="Sun Oct 31 2021 14:01:14")
    comment1150 = Comment(videoId=756, channelId=96, content="She lived on Monkey Jungle Road and that seemed to explain all of her strangeness.", createdAt="Thu Jul 15 2021 12:11:38", updatedAt="Sat Apr 24 2021 00:24:18")
    comment1151 = Comment(videoId=87, channelId=47, content="I made myself a peanut butter sandwich as I didn't want to subsist on veggie crackers.", createdAt="Sun Jun 06 2021 21:30:16", updatedAt="Mon Aug 02 2021 15:05:11")
    comment1152 = Comment(videoId=243, channelId=24, content="The heat", createdAt="Tue Jul 20 2021 05:52:42", updatedAt="Sun Oct 31 2021 18:46:50")
    comment1153 = Comment(videoId=181, channelId=42, content="Normal activities took extraordinary amounts of concentration at the high altitude.", createdAt="Sun Apr 11 2021 11:30:01", updatedAt="Wed Feb 23 2022 12:51:08")
    comment1155 = Comment(videoId=733, channelId=23, content="There's no reason a hula hoop can't also be a circus ring.", createdAt="Sun Jun 13 2021 12:25:07", updatedAt="Sun Apr 11 2021 21:57:24")
    comment1157 = Comment(videoId=309, channelId=49, content="I've always wanted to go to Tajikistan, but my cat would miss me.", createdAt="Sat Nov 13 2021 13:07:33", updatedAt="Sun Apr 11 2021 15:56:34")
    comment1158 = Comment(videoId=634, channelId=18, content="The irony of the situation wasn't lost on anyone in the room.", createdAt="Wed Mar 09 2022 10:47:25", updatedAt="Wed Dec 01 2021 09:41:44")
    comment1159 = Comment(videoId=748, channelId=64, content="I currently have 4 windows open up… and I don’t know why.", createdAt="Thu Dec 09 2021 21:33:24", updatedAt="Sun May 02 2021 14:20:09")
    comment1160 = Comment(videoId=701, channelId=39, content="Mary realized if her calculator had a history, it would be more embarrassing than her computer browser history.", createdAt="Sat Jul 24 2021 10:45:15", updatedAt="Fri Nov 05 2021 16:49:06")
    comment1161 = Comment(videoId=582, channelId=58, content="Sometimes, all you need to do is completely make an ass of yourself and laugh it off to realise that life isn’t so bad after all.", createdAt="Mon Nov 15 2021 05:19:36", updatedAt="Fri Apr 16 2021 18:44:34")
    comment1162 = Comment(videoId=608, channelId=68, content="The tattered work gloves speak of the many hours of hard labor he endured throughout his life.", createdAt="Sat May 01 2021 16:25:07", updatedAt="Mon Nov 15 2021 10:05:55")
    comment1163 = Comment(videoId=685, channelId=7, content="It dawned on her that others could make her happier, but only she could make herself happy.", createdAt="Fri Oct 01 2021 05:52:12", updatedAt="Fri Dec 03 2021 15:17:30")
    comment1164 = Comment(videoId=636, channelId=21, content="He was surprised that his immense laziness was inspirational to others.", createdAt="Mon Feb 14 2022 05:29:55", updatedAt="Tue Apr 27 2021 20:26:43")
    comment1165 = Comment(videoId=214, channelId=25, content="The tortoise jumped into the lake with dreams of becoming a sea turtle.", createdAt="Tue Aug 10 2021 21:37:01", updatedAt="Thu Jan 13 2022 22:10:37")
    comment1166 = Comment(videoId=626, channelId=31, content="The complicated school homework left the parents trying to help their kids quite confused.", createdAt="Fri May 28 2021 14:29:09", updatedAt="Thu Dec 02 2021 16:00:29")
    comment1167 = Comment(videoId=146, channelId=79, content="If you spin around three times, you'll start to feel melancholy.", createdAt="Sat Sep 11 2021 16:13:57", updatedAt="Wed Jul 28 2021 01:36:07")
    comment1168 = Comment(videoId=293, channelId=32, content="Erin accidentally created a new universe.", createdAt="Fri May 14 2021 22:45:23", updatedAt="Thu Jul 29 2021 13:25:46")
    comment1169 = Comment(videoId=270, channelId=69, content="Sometimes you have to just give up and win by cheating.", createdAt="Thu Oct 21 2021 01:36:35", updatedAt="Thu Oct 14 2021 09:51:33")
    comment1170 = Comment(videoId=235, channelId=95, content="The clock within this blog and the clock on my laptop are 1 hour different from each other.", createdAt="Sat May 01 2021 09:28:04", updatedAt="Sat Aug 21 2021 19:59:27")
    comment1171 = Comment(videoId=105, channelId=73, content="It's not often you find a soggy banana on the street.", createdAt="Sat Aug 21 2021 01:58:05", updatedAt="Thu Mar 24 2022 21:09:29")
    comment1172 = Comment(videoId=74, channelId=71, content="I received a heavy fine but it failed to crush my spirit.", createdAt="Fri May 07 2021 13:19:20", updatedAt="Fri Jun 11 2021 04:41:47")
    comment1173 = Comment(videoId=248, channelId=13, content="Toddlers feeding raccoons surprised even the seasoned park ranger.", createdAt="Mon Nov 08 2021 13:09:23", updatedAt="Fri Mar 11 2022 14:12:56")
    comment1174 = Comment(videoId=640, channelId=47, content="I can't believe this is the eighth time I'm smashing open my piggy bank on the same day!", createdAt="Fri Jun 04 2021 01:25:52", updatedAt="Tue Nov 09 2021 09:40:44")
    comment1175 = Comment(videoId=386, channelId=38, content="He put heat on the wound to see what would grow.", createdAt="Wed Jun 16 2021 20:20:59", updatedAt="Fri Nov 26 2021 10:51:09")
    comment1176 = Comment(videoId=434, channelId=82, content="100 years old is such a young age if you happen to be a bristlecone pine.", createdAt="Sun Mar 06 2022 01:19:13", updatedAt="Thu Jun 10 2021 00:32:16")
    comment1178 = Comment(videoId=315, channelId=82, content="He waited for the stop sign to turn to a go sign.", createdAt="Mon Jun 28 2021 05:24:19", updatedAt="Mon Sep 13 2021 18:22:38")
    comment1179 = Comment(videoId=93, channelId=48, content="He didn't heed the warning and it had turned out surprisingly well.", createdAt="Fri Feb 25 2022 08:10:22", updatedAt="Fri May 14 2021 05:19:29")
    comment1180 = Comment(videoId=622, channelId=86, content="They say people remember important moments in their life well, yet no one even remembers their own birth.", createdAt="Wed Jun 02 2021 07:50:09", updatedAt="Thu Jul 22 2021 04:51:10")
    comment1181 = Comment(videoId=674, channelId=69, content="For the 216th time, he said he would quit drinking soda after this last Coke.", createdAt="Sun Aug 15 2021 15:34:29", updatedAt="Fri Aug 27 2021 06:39:32")
    comment1182 = Comment(videoId=649, channelId=44, content="When he asked her favorite number, she answered without hesitation that it was diamonds.", createdAt="Mon Aug 16 2021 15:51:05", updatedAt="Thu Apr 22 2021 14:39:21")
    comment1183 = Comment(videoId=729, channelId=72, content="The family’s excitement over going to Disneyland was crazier than she anticipated.", createdAt="Wed Sep 22 2021 00:04:29", updatedAt="Fri Dec 31 2021 03:40:02")
    comment1184 = Comment(videoId=367, channelId=64, content="It was the scarcity that fueled his creativity.", createdAt="Sun Aug 29 2021 02:45:46", updatedAt="Sat Apr 09 2022 01:12:28")
    comment1185 = Comment(videoId=738, channelId=99, content="Before he moved to the inner city, he had always believed that security complexes were psychological.", createdAt="Wed Dec 22 2021 23:39:34", updatedAt="Wed Nov 24 2021 07:16:17")
    comment1186 = Comment(videoId=192, channelId=23, content="If any cop asks you where you were, just say you were visiting Kansas.", createdAt="Tue Feb 15 2022 16:26:05", updatedAt="Sun May 09 2021 03:13:33")
    comment1187 = Comment(videoId=554, channelId=79, content="The sky is clear; the stars are twinkling.", createdAt="Sat Jun 19 2021 04:40:23", updatedAt="Wed Dec 15 2021 21:38:29")
    comment1188 = Comment(videoId=565, channelId=93, content="It was obvious she was hot, sweaty, and tired.", createdAt="Mon Aug 02 2021 15:02:26", updatedAt="Sat Aug 07 2021 19:00:53")
    comment1189 = Comment(videoId=102, channelId=11, content="The busker hoped that the people passing by would throw money, but they threw tomatoes instead, so he exchanged his hat for a juicer.", createdAt="Thu May 20 2021 12:03:58", updatedAt="Wed Jun 09 2021 15:14:05")
    comment1190 = Comment(videoId=619, channelId=2, content="It's important to remember to be aware of rampaging grizzly bears.", createdAt="Mon Dec 27 2021 04:32:44", updatedAt="Sat Apr 17 2021 01:22:44")
    comment1191 = Comment(videoId=88, channelId=91, content="Cursive writing is the best way to build a race track.", createdAt="Thu Aug 26 2021 01:01:47", updatedAt="Mon May 24 2021 02:50:04")
    comment1192 = Comment(videoId=16, channelId=16, content="I cheated while playing the darts tournament by using a longbow.", createdAt="Mon Sep 27 2021 09:26:18", updatedAt="Fri Jun 25 2021 00:48:39")
    comment1194 = Comment(videoId=327, channelId=72, content="He appeared to be confusingly perplexed.", createdAt="Sat May 15 2021 21:24:12", updatedAt="Wed Oct 06 2021 13:07:06")
    comment1195 = Comment(videoId=764, channelId=11, content="Two seats were vacant.", createdAt="Sun Feb 27 2022 05:07:44", updatedAt="Sat Jul 03 2021 02:27:14")
    comment1196 = Comment(videoId=246, channelId=44, content="I'm a great listener, really good with empathy vs sympathy and all that, but I hate people.", createdAt="Tue May 11 2021 07:48:46", updatedAt="Sat Oct 09 2021 02:09:49")
    comment1197 = Comment(videoId=637, channelId=80, content="The virus had powers none of us knew existed.", createdAt="Sat Sep 18 2021 20:50:00", updatedAt="Sat Jan 15 2022 17:11:34")
    comment1198 = Comment(videoId=151, channelId=18, content="Nancy was proud that she ran a tight shipwreck.", createdAt="Wed Apr 06 2022 20:20:23", updatedAt="Thu May 13 2021 07:48:45")
    comment1199 = Comment(videoId=654, channelId=99, content="She was amazed by the large chunks of ice washing up on the beach.", createdAt="Wed Mar 30 2022 10:13:46", updatedAt="Sat Jun 19 2021 03:23:11")
    comment1200 = Comment(videoId=549, channelId=24, content="People keep telling me \"orange\" but I still prefer \"pink\".", createdAt="Fri Oct 22 2021 10:17:40", updatedAt="Mon Jun 21 2021 12:20:21")
    comment1201 = Comment(videoId=489, channelId=40, content="A song can make or ruin a person’s day if they let it get to them.", createdAt="Mon Sep 27 2021 22:50:41", updatedAt="Fri Dec 10 2021 16:50:43")
    comment1202 = Comment(videoId=327, channelId=27, content="I just wanted to tell you I could see the love you have for your child by the way you look at her.", createdAt="Fri Jan 07 2022 23:56:56", updatedAt="Tue Apr 05 2022 10:01:30")
    comment1204 = Comment(videoId=405, channelId=16, content="The father handed each child a roadmap at the beginning of the 2-day road trip and explained it was so they could find their way home.", createdAt="Wed Dec 01 2021 10:06:07", updatedAt="Wed Oct 20 2021 04:20:02")
    comment1205 = Comment(videoId=284, channelId=17, content="Various sea birds are elegant, but nothing is as elegant as a gliding pelican.", createdAt="Mon Apr 12 2021 00:08:22", updatedAt="Wed Mar 02 2022 11:47:15")
    comment1206 = Comment(videoId=72, channelId=77, content="The bird had a belief that it was really a groundhog.", createdAt="Sat Nov 20 2021 06:07:22", updatedAt="Wed May 12 2021 23:02:50")
    comment1207 = Comment(videoId=356, channelId=54, content="There's no reason a hula hoop can't also be a circus ring.", createdAt="Wed Apr 28 2021 13:22:05", updatedAt="Mon Aug 09 2021 02:13:49")
    comment1208 = Comment(videoId=61, channelId=71, content="Truth in advertising and dinosaurs with skateboards have much in common.", createdAt="Sun Oct 17 2021 20:39:24", updatedAt="Tue Aug 17 2021 03:40:22")
    comment1209 = Comment(videoId=770, channelId=44, content="She used her own hair in the soup to give it more flavor.", createdAt="Sun Oct 03 2021 09:51:09", updatedAt="Tue Jan 25 2022 03:03:20")
    comment1210 = Comment(videoId=303, channelId=51, content="The toy brought back fond memories of being lost in the rain forest.", createdAt="Thu Jan 06 2022 01:08:08", updatedAt="Tue May 11 2021 22:34:32")
    comment1211 = Comment(videoId=266, channelId=89, content="The furnace repairman indicated the heating system was acting as an air conditioner.", createdAt="Fri Mar 04 2022 02:17:35", updatedAt="Sat Dec 04 2021 12:47:49")
    comment1212 = Comment(videoId=138, channelId=35, content="Carol drank the blood as if she were a vampire.", createdAt="Fri Jul 30 2021 20:09:41", updatedAt="Tue Oct 19 2021 03:53:10")
    comment1213 = Comment(videoId=735, channelId=46, content="Karen believed all traffic laws should be obeyed by all except herself.", createdAt="Mon Nov 15 2021 10:27:12", updatedAt="Wed Sep 29 2021 16:52:38")
    comment1214 = Comment(videoId=193, channelId=48, content="She can live her life however she wants as long as she listens to what I have to say.", createdAt="Tue Oct 19 2021 15:16:28", updatedAt="Fri Dec 03 2021 01:02:59")
    comment1215 = Comment(videoId=569, channelId=63, content="He learned the hardest lesson of his life and had the scars, both physical and mental, to prove it.", createdAt="Wed Aug 04 2021 17:06:45", updatedAt="Sat Dec 11 2021 17:18:54")
    comment1216 = Comment(videoId=177, channelId=76, content="It had been sixteen days since the zombies first attacked.", createdAt="Wed Nov 03 2021 00:35:04", updatedAt="Sun Jan 23 2022 07:54:17")
    comment1217 = Comment(videoId=724, channelId=41, content="He was disappointed when he found the beach to be so sandy and the sun so sunny.", createdAt="Sat Oct 09 2021 04:23:11", updatedAt="Sat Mar 26 2022 10:50:22")
    comment1218 = Comment(videoId=491, channelId=60, content="Jenny made the announcement that her baby was an alien.", createdAt="Wed Aug 25 2021 06:20:56", updatedAt="Fri Feb 25 2022 11:27:04")
    comment1219 = Comment(videoId=500, channelId=93, content="Nudist colonies shun fig-leaf couture.", createdAt="Wed Mar 02 2022 15:17:09", updatedAt="Mon Jan 03 2022 17:42:35")
    comment1220 = Comment(videoId=505, channelId=10, content="Flash photography is best used in full sunlight.", createdAt="Mon Sep 13 2021 03:08:29", updatedAt="Sat Jun 12 2021 01:25:16")
    comment1221 = Comment(videoId=412, channelId=57, content="Homesickness became contagious in the young campers' cabin.", createdAt="Thu May 20 2021 08:31:04", updatedAt="Sun Jul 18 2021 17:27:24")
    comment1222 = Comment(videoId=548, channelId=50, content="I liked their first two albums but changed my mind after that charity gig.", createdAt="Tue Nov 02 2021 02:46:07", updatedAt="Thu Oct 07 2021 05:44:22")
    comment1223 = Comment(videoId=677, channelId=36, content="She had some amazing news to share but nobody to share it with.", createdAt="Tue Nov 02 2021 16:43:34", updatedAt="Sat May 15 2021 01:28:51")
    comment1224 = Comment(videoId=501, channelId=21, content="He colored deep space a soft yellow.", createdAt="Sun Feb 20 2022 04:02:42", updatedAt="Sun Dec 26 2021 02:34:49")
    comment1225 = Comment(videoId=220, channelId=86, content="As he entered the church he could hear the soft voice of someone whispering into a cell phone.", createdAt="Sat Oct 02 2021 22:23:45", updatedAt="Mon May 03 2021 21:37:23")
    comment1226 = Comment(videoId=530, channelId=3, content="I don’t respect anybody who can’t tell the difference between Pepsi and Coke.", createdAt="Sun Mar 27 2022 09:59:14", updatedAt="Sat Mar 12 2022 02:21:05")
    comment1228 = Comment(videoId=283, channelId=80, content="Separation anxiety is what happens when you can't find your phone.", createdAt="Fri Feb 04 2022 10:29:22", updatedAt="Mon Aug 09 2021 09:17:25")
    comment1229 = Comment(videoId=707, channelId=51, content="The toddler’s endless tantrum caused the entire plane anxiety.", createdAt="Fri Jan 14 2022 20:42:35", updatedAt="Mon Mar 21 2022 17:51:11")
    comment1230 = Comment(videoId=261, channelId=21, content="More RVs were seen in the storage lot than at the campground.", createdAt="Sat Jan 22 2022 18:28:36", updatedAt="Fri May 21 2021 23:06:18")
    comment1231 = Comment(videoId=138, channelId=51, content="The three-year-old girl ran down the beach as the kite flew behind her.", createdAt="Thu Jul 22 2021 06:25:42", updatedAt="Fri Nov 12 2021 18:54:00")
    comment1232 = Comment(videoId=669, channelId=52, content="The waitress was not amused when he ordered green eggs and ham.", createdAt="Mon Nov 01 2021 04:29:06", updatedAt="Wed Mar 16 2022 03:14:07")
    comment1233 = Comment(videoId=87, channelId=45, content="She wasn't sure whether to be impressed or concerned that he folded underwear in neat little packages.", createdAt="Tue Sep 21 2021 00:36:15", updatedAt="Wed Apr 14 2021 15:45:20")
    comment1234 = Comment(videoId=498, channelId=26, content="Kevin embraced his ability to be at the wrong place at the wrong time.", createdAt="Thu May 20 2021 20:00:16", updatedAt="Mon Dec 20 2021 02:26:46")
    comment1235 = Comment(videoId=203, channelId=56, content="I want more detailed information.", createdAt="Sun Dec 12 2021 01:42:23", updatedAt="Sun Oct 24 2021 23:28:28")
    comment1236 = Comment(videoId=653, channelId=1, content="She tilted her head back and let whip cream stream into her mouth while taking a bath.", createdAt="Tue Jan 18 2022 12:17:20", updatedAt="Thu Dec 02 2021 05:00:40")
    comment1237 = Comment(videoId=410, channelId=15, content="My Mum tries to be cool by saying that she likes all the same things that I do.", createdAt="Sun Jan 23 2022 13:37:57", updatedAt="Sat Mar 12 2022 07:58:02")
    comment1238 = Comment(videoId=206, channelId=53, content="I'm worried by the fact that my daughter looks to the local carpet seller as a role model.", createdAt="Mon Jan 10 2022 23:31:16", updatedAt="Wed Sep 01 2021 23:11:24")
    comment1239 = Comment(videoId=737, channelId=52, content="My biggest joy is roasting almonds while stalking prey.", createdAt="Mon May 10 2021 18:11:34", updatedAt="Mon Aug 16 2021 18:06:30")
    comment1240 = Comment(videoId=335, channelId=34, content="Nancy thought the best way to create a welcoming home was to line it with barbed wire.", createdAt="Tue May 18 2021 15:09:53", updatedAt="Mon Jun 28 2021 09:20:33")
    comment1241 = Comment(videoId=29, channelId=67, content="I cheated while playing the darts tournament by using a longbow.", createdAt="Thu May 06 2021 17:06:29", updatedAt="Tue Aug 31 2021 05:25:49")
    comment1242 = Comment(videoId=385, channelId=53, content="The efficiency with which he paired the socks in the drawer was quite admirable.", createdAt="Wed Jul 28 2021 05:11:34", updatedAt="Thu Jul 15 2021 20:10:08")
    comment1243 = Comment(videoId=718, channelId=7, content="Cursive writing is the best way to build a race track.", createdAt="Fri Jan 28 2022 02:17:06", updatedAt="Fri Aug 27 2021 05:39:53")
    comment1244 = Comment(videoId=357, channelId=29, content="I'll have you know I've written over fifty novels", createdAt="Wed Mar 16 2022 03:11:24", updatedAt="Wed Apr 28 2021 00:04:31")
    comment1245 = Comment(videoId=28, channelId=54, content="The light in his life was actually a fire burning all around him.", createdAt="Wed Nov 24 2021 15:09:28", updatedAt="Thu Sep 09 2021 12:06:13")
    comment1246 = Comment(videoId=311, channelId=9, content="The two walked down the slot canyon oblivious to the sound of thunder in the distance.", createdAt="Sat Jul 17 2021 09:16:07", updatedAt="Tue Dec 14 2021 06:37:26")
    comment1247 = Comment(videoId=591, channelId=5, content="When transplanting seedlings, candied teapots will make the task easier.", createdAt="Sat Apr 02 2022 22:22:18", updatedAt="Mon Sep 20 2021 20:15:02")
    comment1248 = Comment(videoId=118, channelId=49, content="With a single flip of the coin, his life changed forever.", createdAt="Tue Jan 25 2022 16:39:53", updatedAt="Sun Aug 15 2021 12:30:33")
    comment1249 = Comment(videoId=626, channelId=57, content="The beach was crowded with snow leopards.", createdAt="Fri Jul 30 2021 14:58:12", updatedAt="Thu May 27 2021 06:46:55")
    comment1250 = Comment(videoId=418, channelId=89, content="The lake is a long way from here.", createdAt="Fri May 28 2021 11:11:03", updatedAt="Tue Apr 27 2021 09:45:14")
    comment1251 = Comment(videoId=557, channelId=86, content="Jerry liked to look at paintings while eating garlic ice cream.", createdAt="Sun Jul 04 2021 22:33:16", updatedAt="Mon Jul 05 2021 12:05:07")
    comment1252 = Comment(videoId=138, channelId=6, content="He is good at eating pickles and telling women about his emotional problems.", createdAt="Sat Aug 28 2021 14:16:08", updatedAt="Thu Oct 21 2021 15:53:37")
    comment1253 = Comment(videoId=414, channelId=51, content="He created a pig burger out of beef.", createdAt="Tue Oct 19 2021 14:24:32", updatedAt="Mon Aug 02 2021 23:25:35")
    comment1254 = Comment(videoId=288, channelId=34, content="He watched the dancing piglets with panda bear tummies in the swimming pool.", createdAt="Sat Feb 12 2022 22:49:47", updatedAt="Mon May 10 2021 22:48:56")
    comment1255 = Comment(videoId=512, channelId=96, content="He played the game as if his life depended on it and the truth was that it did.", createdAt="Mon May 24 2021 09:28:37", updatedAt="Fri Mar 11 2022 14:45:23")
    comment1256 = Comment(videoId=21, channelId=11, content="He excelled at firing people nicely.", createdAt="Mon Dec 27 2021 21:16:56", updatedAt="Wed Nov 17 2021 20:40:14")
    comment1257 = Comment(videoId=276, channelId=32, content="She tilted her head back and let whip cream stream into her mouth while taking a bath.", createdAt="Wed Dec 29 2021 15:11:52", updatedAt="Tue Nov 30 2021 06:42:54")
    comment1258 = Comment(videoId=109, channelId=91, content="He dreamed of eating green apples with worms.", createdAt="Fri Mar 04 2022 08:25:49", updatedAt="Sun Oct 31 2021 21:57:00")
    comment1259 = Comment(videoId=575, channelId=78, content="Whenever he saw a red flag warning at the beach he grabbed his surfboard.", createdAt="Tue Nov 02 2021 17:15:31", updatedAt="Sun Apr 25 2021 11:04:38")
    comment1260 = Comment(videoId=452, channelId=48, content="The waitress was not amused when he ordered green eggs and ham.", createdAt="Thu Nov 04 2021 02:11:33", updatedAt="Tue Aug 17 2021 11:55:06")
    comment1261 = Comment(videoId=60, channelId=80, content="After fighting off the alligator, Brian still had to face the anaconda.", createdAt="Tue Nov 09 2021 07:53:44", updatedAt="Sun Jan 16 2022 10:47:49")
    comment1262 = Comment(videoId=401, channelId=86, content="Everybody should read Chaucer to improve their everyday vocabulary.", createdAt="Fri Oct 29 2021 13:38:23", updatedAt="Fri May 14 2021 07:54:56")
    comment1263 = Comment(videoId=608, channelId=49, content="Don't put peanut butter on the dog's nose.", createdAt="Mon Jul 26 2021 21:30:37", updatedAt="Sun Nov 07 2021 01:51:38")
    comment1264 = Comment(videoId=123, channelId=8, content="I made myself a peanut butter sandwich as I didn't want to subsist on veggie crackers.", createdAt="Thu Feb 24 2022 01:33:41", updatedAt="Fri Sep 17 2021 20:52:25")
    comment1265 = Comment(videoId=451, channelId=56, content="He was so preoccupied with whether or not he could that he failed to stop to consider if he should.", createdAt="Sun Jun 06 2021 15:30:42", updatedAt="Wed Feb 02 2022 14:56:38")
    comment1266 = Comment(videoId=570, channelId=92, content="I'm not a party animal, but I do like animal parties.", createdAt="Mon Dec 06 2021 19:59:59", updatedAt="Fri Aug 27 2021 14:58:03")
    comment1267 = Comment(videoId=748, channelId=56, content="I was fishing for compliments and accidentally caught a trout.", createdAt="Wed Mar 09 2022 21:19:31", updatedAt="Wed Feb 02 2022 02:15:14")
    comment1268 = Comment(videoId=273, channelId=35, content="We have never been to Asia, nor have we visited Africa.", createdAt="Sat Jun 19 2021 10:07:25", updatedAt="Fri Dec 17 2021 10:55:11")
    comment1269 = Comment(videoId=137, channelId=49, content="Today I bought a raincoat and wore it on a sunny day.", createdAt="Sat Jul 24 2021 04:21:21", updatedAt="Wed May 19 2021 14:59:13")
    comment1270 = Comment(videoId=27, channelId=46, content="He is no James Bond; his name is Roger Moore.", createdAt="Thu Feb 24 2022 14:06:31", updatedAt="Thu Jul 15 2021 04:01:03")
    comment1271 = Comment(videoId=520, channelId=61, content="The old rusted farm equipment surrounded the house predicting its demise.", createdAt="Tue Apr 27 2021 16:31:39", updatedAt="Thu Oct 07 2021 10:58:25")
    comment1272 = Comment(videoId=329, channelId=44, content="While on the first date he accidentally hit his head on the beam.", createdAt="Tue May 11 2021 19:01:12", updatedAt="Fri Feb 25 2022 16:07:48")
    comment1273 = Comment(videoId=522, channelId=89, content="She works two jobs to make ends meet; at least, that was her reason for not having time to join us.", createdAt="Sat Jul 10 2021 22:08:22", updatedAt="Sat Aug 21 2021 14:57:58")
    comment1274 = Comment(videoId=33, channelId=97, content="It's much more difficult to play tennis with a bowling ball than it is to bowl with a tennis ball.", createdAt="Tue Sep 21 2021 00:40:56", updatedAt="Thu May 27 2021 16:09:34")
    comment1275 = Comment(videoId=293, channelId=93, content="The door swung open to reveal pink giraffes and red elephants.", createdAt="Mon Dec 06 2021 10:31:24", updatedAt="Fri Jun 25 2021 06:20:01")
    comment1276 = Comment(videoId=636, channelId=35, content="He looked behind the door and didn't like what he saw.", createdAt="Sun Mar 20 2022 05:40:05", updatedAt="Sat Aug 07 2021 19:45:04")
    comment1277 = Comment(videoId=701, channelId=67, content="He never understood why what, when, and where left out who.", createdAt="Sun Jul 04 2021 03:50:38", updatedAt="Mon Jan 17 2022 11:47:43")
    comment1278 = Comment(videoId=107, channelId=70, content="They called out her name time and again, but were met with nothing but silence.", createdAt="Wed Apr 14 2021 01:26:29", updatedAt="Tue Jun 08 2021 14:01:09")
    comment1279 = Comment(videoId=359, channelId=2, content="The llama couldn't resist trying the lemonade.", createdAt="Mon Jan 17 2022 08:08:43", updatedAt="Sun Jul 04 2021 08:24:26")
    comment1280 = Comment(videoId=335, channelId=84, content="The random sentence generator generated a random sentence about a random sentence.", createdAt="Fri Feb 18 2022 21:22:21", updatedAt="Tue Mar 08 2022 22:29:50")
    comment1281 = Comment(videoId=422, channelId=7, content="There was coal in his stocking and he was thrilled.", createdAt="Tue Jun 15 2021 19:00:10", updatedAt="Tue Oct 19 2021 20:33:34")
    comment1282 = Comment(videoId=763, channelId=66, content="Sarah ran from the serial killer holding a jug of milk.", createdAt="Thu Dec 09 2021 10:36:24", updatedAt="Fri May 21 2021 20:30:29")
    comment1283 = Comment(videoId=228, channelId=4, content="The elephant didn't want to talk about the person in the room.", createdAt="Sat Oct 09 2021 10:31:25", updatedAt="Sun Jul 18 2021 03:07:39")
    comment1284 = Comment(videoId=347, channelId=64, content="The child’s favorite Christmas gift was the large box her father’s lawnmower came in.", createdAt="Thu Dec 09 2021 02:04:04", updatedAt="Sat Jan 08 2022 04:30:40")
    comment1285 = Comment(videoId=192, channelId=44, content="Today we gathered moss for my uncle's wedding.", createdAt="Mon Jan 03 2022 07:06:56", updatedAt="Mon Apr 19 2021 16:45:18")
    comment1287 = Comment(videoId=194, channelId=72, content="Watching the geriatric men’s softball team brought back memories of 3 yr olds playing t-ball.", createdAt="Fri Feb 04 2022 03:15:33", updatedAt="Sun Nov 14 2021 17:29:40")
    comment1288 = Comment(videoId=128, channelId=47, content="The elderly neighborhood became enraged over the coyotes who had been blamed for the poodle’s disappearance.", createdAt="Thu Jul 15 2021 01:50:08", updatedAt="Fri Apr 08 2022 15:56:10")
    comment1289 = Comment(videoId=113, channelId=10, content="As he entered the church he could hear the soft voice of someone whispering into a cell phone.", createdAt="Sat Jul 24 2021 07:12:44", updatedAt="Wed Oct 20 2021 22:01:41")
    comment1290 = Comment(videoId=597, channelId=76, content="When nobody is around, the trees gossip about the people who have walked under them.", createdAt="Fri Jul 02 2021 14:00:15", updatedAt="Thu Dec 30 2021 19:13:21")
    comment1291 = Comment(videoId=405, channelId=59, content="It was at that moment that he learned there are certain parts of the body that you should never Nair.", createdAt="Sat Apr 09 2022 06:49:52", updatedAt="Mon Feb 28 2022 09:25:47")
    comment1292 = Comment(videoId=717, channelId=89, content="He decided to live his life by the big beats manifesto.", createdAt="Tue Oct 19 2021 09:06:31", updatedAt="Fri Dec 31 2021 01:48:54")
    comment1293 = Comment(videoId=4, channelId=3, content="Grape jelly was leaking out the hole in the roof.", createdAt="Tue Jun 22 2021 23:08:37", updatedAt="Wed Dec 08 2021 14:00:37")
    comment1294 = Comment(videoId=464, channelId=48, content="The blue parrot drove by the hitchhiking mongoose.", createdAt="Sat Nov 27 2021 08:30:51", updatedAt="Mon Aug 23 2021 14:17:15")
    comment1295 = Comment(videoId=702, channelId=34, content="He would only survive if he kept the fire going and he could hear thunder in the distance.", createdAt="Wed Jan 26 2022 02:48:32", updatedAt="Sun Dec 19 2021 16:18:21")
    comment1296 = Comment(videoId=728, channelId=4, content="As the years pass by, we all know owners look more and more like their dogs.", createdAt="Thu Apr 22 2021 18:50:40", updatedAt="Sat May 22 2021 01:54:50")
    comment1297 = Comment(videoId=653, channelId=5, content="It's difficult to understand the lengths he'd go to remain short.", createdAt="Mon Feb 21 2022 06:58:31", updatedAt="Wed Jan 05 2022 12:32:50")
    comment1298 = Comment(videoId=628, channelId=87, content="Check back tomorrow; I will see if the book has arrived.", createdAt="Thu Jul 29 2021 21:05:22", updatedAt="Wed Apr 21 2021 09:50:59")
    comment1299 = Comment(videoId=774, channelId=67, content="I liked their first two albums but changed my mind after that charity gig.", createdAt="Sat Feb 26 2022 19:38:56", updatedAt="Sun Sep 19 2021 19:05:18")
    comment1300 = Comment(videoId=213, channelId=30, content="For some unfathomable reason, the response team didn't consider a lack of milk for my cereal as a proper emergency.", createdAt="Tue May 04 2021 12:04:21", updatedAt="Mon May 24 2021 13:04:55")
    comment1301 = Comment(videoId=214, channelId=86, content="The gruff old man sat in the back of the bait shop grumbling to himself as he scooped out a handful of worms.", createdAt="Wed Aug 04 2021 17:06:05", updatedAt="Sat Jul 24 2021 06:31:24")
    comment1302 = Comment(videoId=128, channelId=77, content="You've been eyeing me all day and waiting for your move like a lion stalking a gazelle in a savannah.", createdAt="Fri Jun 18 2021 15:58:13", updatedAt="Mon Sep 13 2021 03:34:13")
    comment1303 = Comment(videoId=742, channelId=10, content="There were white out conditions in the town; subsequently, the roads were impassable.", createdAt="Sun Oct 03 2021 04:45:26", updatedAt="Mon Oct 11 2021 22:58:33")
    comment1304 = Comment(videoId=338, channelId=48, content="People who insist on picking their teeth with their elbows are so annoying!", createdAt="Thu Dec 23 2021 12:30:44", updatedAt="Sat Dec 25 2021 18:53:13")
    comment1305 = Comment(videoId=487, channelId=35, content="He told us a very exciting adventure story.", createdAt="Wed Sep 29 2021 21:28:28", updatedAt="Sun Jul 11 2021 21:25:46")
    comment1306 = Comment(videoId=696, channelId=28, content="She finally understood that grief was her love with no place for it to go.", createdAt="Mon Jan 10 2022 08:55:34", updatedAt="Tue Jun 22 2021 10:53:44")
    comment1307 = Comment(videoId=213, channelId=89, content="You're unsure whether or not to trust him, but very thankful that you wore a turtle neck.", createdAt="Sun Mar 06 2022 03:29:18", updatedAt="Sat Dec 04 2021 17:50:57")
    comment1308 = Comment(videoId=211, channelId=61, content="The stench from the feedlot permeated the car despite having the air conditioning on recycled air.", createdAt="Wed Jan 05 2022 15:37:21", updatedAt="Thu Apr 07 2022 06:54:31")
    comment1309 = Comment(videoId=410, channelId=47, content="Pair your designer cowboy hat with scuba gear for a memorable occasion.", createdAt="Fri Apr 23 2021 12:32:46", updatedAt="Tue Jan 04 2022 10:46:34")
    comment1310 = Comment(videoId=653, channelId=73, content="When nobody is around, the trees gossip about the people who have walked under them.", createdAt="Sun Sep 05 2021 19:17:26", updatedAt="Sun Nov 28 2021 22:50:27")
    comment1311 = Comment(videoId=581, channelId=68, content="The reservoir water level continued to lower while we enjoyed our long shower.", createdAt="Thu May 27 2021 12:17:53", updatedAt="Fri Feb 18 2022 06:42:48")
    comment1312 = Comment(videoId=677, channelId=69, content="25 years later, she still regretted that specific moment.", createdAt="Sun Feb 20 2022 18:08:19", updatedAt="Sat Jul 03 2021 10:08:43")
    comment1313 = Comment(videoId=474, channelId=6, content="If you don't like toenails, you probably shouldn't look at your feet.", createdAt="Sat Oct 16 2021 23:27:53", updatedAt="Sun May 23 2021 10:11:07")
    comment1314 = Comment(videoId=418, channelId=98, content="Blue sounded too cold at the time and yet it seemed to work for gin.", createdAt="Fri Aug 27 2021 08:33:12", updatedAt="Tue Sep 07 2021 04:28:04")
    comment1315 = Comment(videoId=704, channelId=79, content="For some unfathomable reason, the response team didn't consider a lack of milk for my cereal as a proper emergency.", createdAt="Wed Oct 20 2021 05:11:21", updatedAt="Mon Sep 20 2021 03:56:32")
    comment1316 = Comment(videoId=454, channelId=62, content="The fish listened intently to what the frogs had to say.", createdAt="Wed Sep 01 2021 14:42:48", updatedAt="Sat Feb 12 2022 01:07:47")
    comment1317 = Comment(videoId=29, channelId=48, content="It's never been my responsibility to glaze the donuts.", createdAt="Sat May 01 2021 00:51:25", updatedAt="Sat Jun 05 2021 15:49:43")
    comment1318 = Comment(videoId=56, channelId=83, content="Greetings from the galaxy MACS0647-JD, or what we call home.", createdAt="Wed Oct 27 2021 00:27:28", updatedAt="Tue Oct 19 2021 22:27:03")
    comment1319 = Comment(videoId=705, channelId=81, content="Sixty-Four comes asking for bread.", createdAt="Sat Jun 26 2021 02:14:49", updatedAt="Mon Apr 26 2021 17:09:25")
    comment1320 = Comment(videoId=98, channelId=54, content="He is no James Bond; his name is Roger Moore.", createdAt="Sun Jan 23 2022 02:35:57", updatedAt="Wed Mar 23 2022 14:55:52")
    comment1321 = Comment(videoId=552, channelId=67, content="The teens wondered what was kept in the red shed on the far edge of the school grounds.", createdAt="Tue Oct 05 2021 21:05:14", updatedAt="Tue Sep 28 2021 12:06:50")
    comment1322 = Comment(videoId=483, channelId=94, content="I'm a great listener, really good with empathy vs sympathy and all that, but I hate people.", createdAt="Thu Jan 20 2022 20:53:51", updatedAt="Thu Jun 03 2021 02:47:47")
    comment1323 = Comment(videoId=64, channelId=97, content="She wrote him a long letter, but he didn't read it.", createdAt="Sat Jul 31 2021 09:52:08", updatedAt="Sun Jul 04 2021 16:23:17")
    comment1324 = Comment(videoId=748, channelId=36, content="I think I will buy the red car, or I will lease the blue one.", createdAt="Tue Feb 08 2022 07:48:52", updatedAt="Thu Jul 22 2021 15:59:44")
    comment1325 = Comment(videoId=530, channelId=83, content="There was coal in his stocking and he was thrilled.", createdAt="Sat Jun 19 2021 05:38:24", updatedAt="Sat Oct 30 2021 18:08:34")
    comment1326 = Comment(videoId=162, channelId=71, content="Nancy decided to make the porta-potty her home.", createdAt="Sat Jan 15 2022 09:18:09", updatedAt="Tue Aug 17 2021 11:49:56")
    comment1327 = Comment(videoId=35, channelId=93, content="It was her first experience training a rainbow unicorn.", createdAt="Sat Apr 02 2022 13:45:01", updatedAt="Thu Aug 19 2021 10:34:48")
    comment1329 = Comment(videoId=224, channelId=34, content="All she wanted was the answer, but she had no idea how much she would hate it.", createdAt="Sun Jul 11 2021 15:49:34", updatedAt="Thu Dec 23 2021 15:53:15")
    comment1330 = Comment(videoId=215, channelId=80, content="I’m working on a sweet potato farm.", createdAt="Wed Jan 05 2022 12:56:16", updatedAt="Thu Mar 17 2022 23:20:59")
    comment1331 = Comment(videoId=759, channelId=93, content="Always bring cinnamon buns on a deep-sea diving expedition.", createdAt="Mon May 03 2021 23:54:33", updatedAt="Sun Sep 19 2021 09:55:57")
    comment1332 = Comment(videoId=205, channelId=41, content="David subscribes to the \"stuff your tent into the bag\" strategy over nicely folding it.", createdAt="Sun Oct 31 2021 05:25:11", updatedAt="Thu Jul 01 2021 16:18:06")
    comment1333 = Comment(videoId=420, channelId=60, content="Shakespeare was a famous 17th-century diesel mechanic.", createdAt="Mon Jan 17 2022 14:58:54", updatedAt="Wed May 12 2021 09:47:08")
    comment1334 = Comment(videoId=464, channelId=18, content="He didn't understand why the bird wanted to ride the bicycle.", createdAt="Sun Oct 31 2021 17:54:01", updatedAt="Sat Nov 27 2021 14:03:08")
    comment1335 = Comment(videoId=593, channelId=74, content="The manager of the fruit stand always sat and only sold vegetables.", createdAt="Sun Jan 09 2022 09:51:20", updatedAt="Thu Dec 16 2021 05:07:16")
    comment1336 = Comment(videoId=461, channelId=20, content="It's not often you find a soggy banana on the street.", createdAt="Fri Oct 15 2021 09:56:44", updatedAt="Sat Nov 13 2021 02:44:27")
    comment1337 = Comment(videoId=296, channelId=30, content="Swim at your own risk was taken as a challenge for the group of Kansas City college students.", createdAt="Sat Jan 08 2022 13:24:50", updatedAt="Mon Feb 07 2022 18:19:09")
    comment1338 = Comment(videoId=172, channelId=96, content="Martha came to the conclusion that shake weights are a great gift for any occasion.", createdAt="Thu Apr 15 2021 10:35:20", updatedAt="Sat Aug 21 2021 13:05:22")
    comment1339 = Comment(videoId=154, channelId=66, content="Hit me with your pet shark!", createdAt="Tue Mar 01 2022 11:36:51", updatedAt="Mon Dec 20 2021 18:06:46")
    comment1340 = Comment(videoId=677, channelId=77, content="More RVs were seen in the storage lot than at the campground.", createdAt="Tue Jun 22 2021 06:41:41", updatedAt="Sun Jul 04 2021 02:31:15")
    comment1341 = Comment(videoId=291, channelId=30, content="He fumbled in the darkness looking for the light switch, but when he finally found it there was someone already there.", createdAt="Mon Jan 24 2022 00:39:15", updatedAt="Tue May 04 2021 14:10:33")
    comment1342 = Comment(videoId=617, channelId=23, content="He wondered if she would appreciate his toenail collection.", createdAt="Fri Aug 06 2021 01:27:12", updatedAt="Wed Feb 16 2022 20:11:22")
    comment1343 = Comment(videoId=25, channelId=3, content="All they could see was the blue water surrounding their sailboat.", createdAt="Thu Apr 22 2021 17:06:05", updatedAt="Fri May 21 2021 09:34:22")
    comment1344 = Comment(videoId=228, channelId=57, content="Don't step on the broken glass.", createdAt="Mon Oct 18 2021 15:04:42", updatedAt="Wed Oct 27 2021 23:01:36")
    comment1345 = Comment(videoId=753, channelId=87, content="Just go ahead and press that button.", createdAt="Fri Aug 27 2021 13:41:59", updatedAt="Sat May 01 2021 09:22:28")
    comment1346 = Comment(videoId=196, channelId=71, content="Jim liked driving around town with his hazard lights on.", createdAt="Mon May 17 2021 15:32:50", updatedAt="Mon Dec 06 2021 15:19:36")
    comment1347 = Comment(videoId=603, channelId=17, content="Flying fish flew by the space station.", createdAt="Wed Dec 29 2021 06:05:51", updatedAt="Sun Aug 29 2021 15:44:39")
    comment1348 = Comment(videoId=686, channelId=91, content="The irony of the situation wasn't lost on anyone in the room.", createdAt="Fri Apr 23 2021 08:38:54", updatedAt="Sun Jan 16 2022 09:14:35")
    comment1349 = Comment(videoId=466, channelId=31, content="A glittering gem is not enough.", createdAt="Fri Jun 18 2021 10:58:22", updatedAt="Mon Jun 14 2021 04:30:33")
    comment1350 = Comment(videoId=764, channelId=14, content="He wondered if it could be called a beach if there was no sand.", createdAt="Fri Dec 24 2021 13:14:57", updatedAt="Sat Jun 12 2021 23:12:24")
    comment1351 = Comment(videoId=202, channelId=2, content="Two more days and all his problems would be solved.", createdAt="Wed Jul 14 2021 11:44:29", updatedAt="Wed Mar 09 2022 03:40:10")
    comment1352 = Comment(videoId=749, channelId=5, content="Nobody loves a pig wearing lipstick.", createdAt="Sun Aug 22 2021 22:42:53", updatedAt="Mon Jun 14 2021 19:18:47")
    comment1353 = Comment(videoId=63, channelId=4, content="Jason didn’t understand why his parents wouldn’t let him sell his little sister at the garage sale.", createdAt="Tue Nov 16 2021 13:59:13", updatedAt="Fri Jun 25 2021 07:39:10")
    comment1354 = Comment(videoId=629, channelId=18, content="As he looked out the window, he saw a clown walk by.", createdAt="Thu Mar 31 2022 05:25:23", updatedAt="Wed Nov 03 2021 03:13:26")
    comment1355 = Comment(videoId=708, channelId=36, content="The fog was so dense even a laser decided it wasn't worth the effort.", createdAt="Mon May 17 2021 03:13:30", updatedAt="Tue Jul 13 2021 15:55:28")
    comment1356 = Comment(videoId=439, channelId=12, content="Eating eggs on Thursday for choir practice was recommended.", createdAt="Sun Aug 29 2021 08:16:51", updatedAt="Mon Feb 28 2022 11:20:32")
    comment1357 = Comment(videoId=606, channelId=38, content="He is good at eating pickles and telling women about his emotional problems.", createdAt="Thu Nov 11 2021 22:57:41", updatedAt="Fri Sep 10 2021 21:03:56")
    comment1358 = Comment(videoId=451, channelId=15, content="It's never been my responsibility to glaze the donuts.", createdAt="Tue May 18 2021 03:11:44", updatedAt="Thu Nov 04 2021 01:12:37")
    comment1359 = Comment(videoId=35, channelId=25, content="Joe made the sugar cookies; Susan decorated them.", createdAt="Mon Apr 19 2021 18:02:54", updatedAt="Fri Jan 07 2022 11:51:46")
    comment1360 = Comment(videoId=290, channelId=20, content="Nobody has encountered an explosive daisy and lived to tell the tale.", createdAt="Tue Aug 03 2021 01:30:40", updatedAt="Wed Sep 22 2021 12:13:50")
    comment1361 = Comment(videoId=503, channelId=41, content="The group quickly understood that toxic waste was the most effective barrier to use against the zombies.", createdAt="Sun Sep 26 2021 22:32:56", updatedAt="Sat Apr 24 2021 20:57:18")
    comment1362 = Comment(videoId=375, channelId=15, content="The secret ingredient to his wonderful life was crime.", createdAt="Sat Jun 19 2021 08:21:20", updatedAt="Tue Feb 01 2022 10:10:19")
    comment1364 = Comment(videoId=136, channelId=59, content="I honestly find her about as intimidating as a basket of kittens.", createdAt="Tue Apr 27 2021 12:55:11", updatedAt="Fri Apr 23 2021 07:53:00")
    comment1365 = Comment(videoId=105, channelId=33, content="Shingle color was not something the couple had ever talked about.", createdAt="Thu Jun 10 2021 21:12:47", updatedAt="Fri Jan 07 2022 06:49:33")
    comment1366 = Comment(videoId=77, channelId=19, content="The virus had powers none of us knew existed.", createdAt="Thu Apr 29 2021 03:51:24", updatedAt="Wed Oct 20 2021 05:41:02")
    comment1367 = Comment(videoId=20, channelId=76, content="All you need to do is pick up the pen and begin.", createdAt="Tue Nov 02 2021 17:26:14", updatedAt="Sat Dec 11 2021 15:20:55")
    comment1368 = Comment(videoId=552, channelId=70, content="He had decided to accept his fate of accepting his fate.", createdAt="Tue Nov 23 2021 09:30:10", updatedAt="Sun Jul 25 2021 18:31:05")
    comment1369 = Comment(videoId=723, channelId=12, content="It isn't difficult to do a handstand if you just stand on your hands.", createdAt="Mon May 31 2021 11:00:38", updatedAt="Sat Oct 09 2021 06:13:57")
    comment1370 = Comment(videoId=624, channelId=39, content="She looked at the masterpiece hanging in the museum but all she could think is that her five-year-old could do better.", createdAt="Sun May 09 2021 16:14:41", updatedAt="Thu Apr 29 2021 20:19:08")
    comment1371 = Comment(videoId=254, channelId=7, content="Today arrived with a crash of my car through the garage door.", createdAt="Sat Jan 22 2022 03:07:08", updatedAt="Mon Feb 21 2022 17:16:33")
    comment1372 = Comment(videoId=486, channelId=54, content="Various sea birds are elegant, but nothing is as elegant as a gliding pelican.", createdAt="Fri May 07 2021 02:03:18", updatedAt="Thu Jul 01 2021 03:00:37")
    comment1373 = Comment(videoId=490, channelId=15, content="He always wore his sunglasses at night.", createdAt="Tue Apr 13 2021 15:52:03", updatedAt="Mon Aug 09 2021 10:07:29")
    comment1374 = Comment(videoId=427, channelId=86, content="Greetings from the real universe.", createdAt="Mon Jun 21 2021 22:02:32", updatedAt="Thu Apr 15 2021 19:45:22")
    comment1375 = Comment(videoId=32, channelId=31, content="The fifty mannequin heads floating in the pool kind of freaked them out.", createdAt="Fri Apr 23 2021 15:54:50", updatedAt="Wed Dec 15 2021 22:45:23")
    comment1376 = Comment(videoId=369, channelId=82, content="The efficiency with which he paired the socks in the drawer was quite admirable.", createdAt="Thu Apr 22 2021 12:56:04", updatedAt="Sun Oct 03 2021 04:37:31")
    comment1377 = Comment(videoId=504, channelId=68, content="Sometimes I stare at a door or a wall and I wonder what is this reality, why am I alive, and what is this all about?", createdAt="Tue Sep 21 2021 13:00:44", updatedAt="Thu Aug 05 2021 20:40:56")
    comment1378 = Comment(videoId=45, channelId=6, content="She was too busy always talking about what she wanted to do to actually do any of it.", createdAt="Sat Nov 20 2021 00:37:17", updatedAt="Thu Aug 05 2021 16:25:27")
    comment1380 = Comment(videoId=580, channelId=74, content="He turned in the research paper on Friday; otherwise, he would have not passed the class.", createdAt="Mon Aug 09 2021 15:11:14", updatedAt="Sat Apr 02 2022 03:27:56")
    comment1381 = Comment(videoId=429, channelId=67, content="I had a friend in high school named Rick Shaw, but he was fairly useless as a mode of transport.", createdAt="Thu Mar 31 2022 09:37:45", updatedAt="Mon Aug 09 2021 08:54:02")
    comment1382 = Comment(videoId=271, channelId=5, content="There should have been a time and a place, but this wasn't it.", createdAt="Sun Jun 20 2021 07:14:57", updatedAt="Wed Oct 27 2021 23:25:27")
    comment1384 = Comment(videoId=140, channelId=23, content="He poured rocks in the dungeon of his mind.", createdAt="Sat Jul 17 2021 23:25:27", updatedAt="Tue May 18 2021 11:45:13")
    comment1385 = Comment(videoId=118, channelId=74, content="People keep telling me \"orange\" but I still prefer \"pink\".", createdAt="Fri Jul 30 2021 16:02:16", updatedAt="Wed Mar 02 2022 15:04:27")
    comment1386 = Comment(videoId=467, channelId=55, content="Patricia found the meaning of life in a bowl of Cheerios.", createdAt="Fri Jun 25 2021 09:25:01", updatedAt="Thu Nov 04 2021 14:11:26")
    comment1387 = Comment(videoId=714, channelId=77, content="Gwen had her best sleep ever on her new bed of nails.", createdAt="Thu Oct 21 2021 20:48:56", updatedAt="Wed Dec 01 2021 09:53:09")
    comment1388 = Comment(videoId=7, channelId=48, content="It caught him off guard that space smelled of seared steak.", createdAt="Fri May 14 2021 20:27:42", updatedAt="Mon May 31 2021 07:07:11")
    comment1389 = Comment(videoId=169, channelId=73, content="The clock within this blog and the clock on my laptop are 1 hour different from each other.", createdAt="Mon Mar 07 2022 16:10:42", updatedAt="Sat May 22 2021 06:08:23")
    comment1390 = Comment(videoId=290, channelId=16, content="More RVs were seen in the storage lot than at the campground.", createdAt="Fri Dec 31 2021 23:08:14", updatedAt="Sat Nov 27 2021 08:59:52")
    comment1391 = Comment(videoId=133, channelId=89, content="He was an introvert that extroverts seemed to love.", createdAt="Tue Jul 20 2021 12:00:40", updatedAt="Mon Jun 21 2021 13:36:45")
    comment1392 = Comment(videoId=380, channelId=95, content="In hopes of finding out the truth, he entered the one-room library.", createdAt="Sun Jan 02 2022 01:55:29", updatedAt="Tue Jun 01 2021 16:38:49")
    comment1393 = Comment(videoId=622, channelId=6, content="Last Friday I saw a spotted striped blue worm shake hands with a legless lizard.", createdAt="Mon Nov 29 2021 17:14:02", updatedAt="Mon Jan 10 2022 14:37:57")
    comment1394 = Comment(videoId=494, channelId=19, content="It was the first time he had ever seen someone cook dinner on an elephant.", createdAt="Thu Jul 29 2021 19:03:42", updatedAt="Tue Oct 05 2021 18:45:53")
    comment1395 = Comment(videoId=352, channelId=9, content="The wake behind the boat told of the past while the open sea for told life in the unknown future.", createdAt="Thu Feb 10 2022 19:12:34", updatedAt="Sun Oct 10 2021 12:56:00")
    comment1396 = Comment(videoId=669, channelId=45, content="He decided to live his life by the big beats manifesto.", createdAt="Sun Mar 27 2022 15:12:46", updatedAt="Fri Jan 28 2022 10:27:49")
    comment1397 = Comment(videoId=595, channelId=13, content="Today I heard something new and unmemorable.", createdAt="Sat Jan 29 2022 07:44:34", updatedAt="Fri Apr 16 2021 19:42:14")
    comment1398 = Comment(videoId=57, channelId=38, content="Blue sounded too cold at the time and yet it seemed to work for gin.", createdAt="Mon Jan 10 2022 02:22:52", updatedAt="Sat Jun 05 2021 19:55:52")
    comment1399 = Comment(videoId=57, channelId=95, content="Before he moved to the inner city, he had always believed that security complexes were psychological.", createdAt="Wed Jan 12 2022 04:51:19", updatedAt="Mon Jun 07 2021 03:45:40")
    comment1400 = Comment(videoId=758, channelId=62, content="There can never be too many cherries on an ice cream sundae.", createdAt="Fri Mar 11 2022 00:42:47", updatedAt="Fri Feb 25 2022 00:53:05")
    comment1401 = Comment(videoId=569, channelId=39, content="All she wanted was the answer, but she had no idea how much she would hate it.", createdAt="Sun Jul 04 2021 14:31:29", updatedAt="Thu Dec 02 2021 01:56:22")
    comment1402 = Comment(videoId=82, channelId=60, content="She hadn't had her cup of coffee, and that made things all the worse.", createdAt="Sun Sep 26 2021 13:14:17", updatedAt="Thu Feb 03 2022 22:45:56")
    comment1403 = Comment(videoId=346, channelId=59, content="I am my aunt's sister's daughter.", createdAt="Thu Jan 20 2022 08:57:42", updatedAt="Sat May 15 2021 04:29:25")
    comment1404 = Comment(videoId=266, channelId=45, content="Her scream silenced the rowdy teenagers.", createdAt="Thu Feb 24 2022 20:21:36", updatedAt="Tue Aug 17 2021 06:34:20")
    comment1406 = Comment(videoId=361, channelId=23, content="He picked up trash in his spare time to dump in his neighbor's yard.", createdAt="Wed Jan 26 2022 21:30:49", updatedAt="Thu Oct 28 2021 11:28:50")
    comment1407 = Comment(videoId=412, channelId=13, content="The gruff old man sat in the back of the bait shop grumbling to himself as he scooped out a handful of worms.", createdAt="Sat May 01 2021 21:02:55", updatedAt="Sat Apr 09 2022 08:50:31")
    comment1408 = Comment(videoId=487, channelId=13, content="It's important to remember to be aware of rampaging grizzly bears.", createdAt="Mon Jan 31 2022 19:25:13", updatedAt="Fri Jun 11 2021 04:37:18")
    comment1409 = Comment(videoId=643, channelId=97, content="The light that burns twice as bright burns half as long.", createdAt="Fri Jan 28 2022 03:32:28", updatedAt="Sat Feb 05 2022 01:18:30")
    comment1410 = Comment(videoId=146, channelId=23, content="It dawned on her that others could make her happier, but only she could make herself happy.", createdAt="Mon Apr 12 2021 20:51:34", updatedAt="Fri May 28 2021 20:10:23")
    comment1411 = Comment(videoId=511, channelId=88, content="I love bacon, beer, birds, and baboons.", createdAt="Wed Apr 21 2021 12:14:35", updatedAt="Wed May 26 2021 17:02:10")
    comment1412 = Comment(videoId=549, channelId=17, content="Today I bought a raincoat and wore it on a sunny day.", createdAt="Thu Oct 14 2021 23:58:14", updatedAt="Sun Jul 11 2021 11:28:39")
    comment1413 = Comment(videoId=765, channelId=70, content="She traveled because it cost the same as therapy and was a lot more enjoyable.", createdAt="Sun Jan 23 2022 22:25:10", updatedAt="Thu Feb 24 2022 12:23:00")
    comment1414 = Comment(videoId=449, channelId=54, content="He went back to the video to see what had been recorded and was shocked at what he saw.", createdAt="Tue Nov 16 2021 12:47:12", updatedAt="Sat Mar 19 2022 02:15:03")
    comment1415 = Comment(videoId=545, channelId=61, content="Gary didn't understand why Doug went upstairs to get one dollar bills when he invited him to go cow tipping.", createdAt="Sun Oct 10 2021 06:43:29", updatedAt="Sat Dec 25 2021 15:39:17")
    comment1416 = Comment(videoId=151, channelId=49, content="We should play with legos at camp.", createdAt="Sun Feb 06 2022 18:15:21", updatedAt="Thu Oct 14 2021 06:58:08")
    comment1417 = Comment(videoId=275, channelId=20, content="It was getting dark, and we weren’t there yet.", createdAt="Wed Jun 23 2021 23:24:11", updatedAt="Mon May 24 2021 09:20:52")
    comment1418 = Comment(videoId=177, channelId=12, content="He stepped gingerly onto the bridge knowing that enchantment awaited on the other side.", createdAt="Thu Mar 10 2022 07:03:29", updatedAt="Sun Jun 27 2021 14:51:44")
    comment1419 = Comment(videoId=673, channelId=75, content="Shakespeare was a famous 17th-century diesel mechanic.", createdAt="Wed Jan 05 2022 05:54:26", updatedAt="Wed Dec 15 2021 18:55:06")
    comment1420 = Comment(videoId=773, channelId=27, content="Three years later, the coffin was still full of Jello.", createdAt="Fri Nov 05 2021 19:17:13", updatedAt="Fri Oct 29 2021 04:11:22")
    comment1421 = Comment(videoId=368, channelId=48, content="Every manager should be able to recite at least ten nursery rhymes backward.", createdAt="Tue Aug 03 2021 21:42:39", updatedAt="Fri Jul 16 2021 20:08:23")
    comment1422 = Comment(videoId=736, channelId=93, content="The fence was confused about whether it was supposed to keep things in or keep things out.", createdAt="Sun Jun 13 2021 23:23:36", updatedAt="Thu Feb 03 2022 19:04:24")
    comment1423 = Comment(videoId=665, channelId=2, content="Warm beer on a cold day isn't my idea of fun.", createdAt="Tue Jan 18 2022 15:57:01", updatedAt="Thu Mar 03 2022 03:40:53")
    comment1424 = Comment(videoId=533, channelId=10, content="The fish listened intently to what the frogs had to say.", createdAt="Tue Mar 22 2022 23:49:42", updatedAt="Sat Oct 23 2021 22:10:50")
    comment1425 = Comment(videoId=96, channelId=25, content="Jenny made the announcement that her baby was an alien.", createdAt="Sun Mar 20 2022 17:23:33", updatedAt="Sat Jul 17 2021 22:17:41")
    comment1426 = Comment(videoId=223, channelId=58, content="The lake is a long way from here.", createdAt="Sat Apr 24 2021 04:55:14", updatedAt="Tue Apr 13 2021 22:16:40")
    comment1427 = Comment(videoId=481, channelId=60, content="They throw cabbage that turns your brain into emotional baggage.", createdAt="Fri Feb 04 2022 15:23:07", updatedAt="Sat Mar 12 2022 01:33:28")
    comment1428 = Comment(videoId=323, channelId=42, content="It's never comforting to know that your fate depends on something as unpredictable as the popping of corn.", createdAt="Mon Jul 26 2021 19:15:37", updatedAt="Tue Nov 23 2021 06:37:37")
    comment1429 = Comment(videoId=510, channelId=27, content="If my calculator had a history, it would be more embarrassing than my browser history.", createdAt="Sun May 02 2021 02:15:16", updatedAt="Tue Aug 10 2021 17:57:48")
    comment1430 = Comment(videoId=559, channelId=52, content="Doris enjoyed tapping her nails on the table to annoy everyone.", createdAt="Mon Sep 06 2021 07:08:14", updatedAt="Thu Oct 28 2021 09:40:14")
    comment1431 = Comment(videoId=388, channelId=91, content="I know many children ask for a pony, but I wanted a bicycle with rockets strapped to it.", createdAt="Thu Jul 08 2021 05:35:19", updatedAt="Sat Apr 09 2022 00:58:49")
    comment1432 = Comment(videoId=442, channelId=89, content="Lucifer was surprised at the amount of life at Death Valley.", createdAt="Fri Dec 10 2021 04:59:54", updatedAt="Tue Oct 05 2021 18:23:23")
    comment1433 = Comment(videoId=480, channelId=67, content="Martha came to the conclusion that shake weights are a great gift for any occasion.", createdAt="Sun May 09 2021 03:49:21", updatedAt="Sat Aug 07 2021 14:22:07")
    comment1434 = Comment(videoId=590, channelId=88, content="Kevin embraced his ability to be at the wrong place at the wrong time.", createdAt="Wed Mar 23 2022 17:25:35", updatedAt="Tue Jun 29 2021 12:14:05")
    comment1435 = Comment(videoId=566, channelId=81, content="She only paints with bold colors; she does not like pastels.", createdAt="Tue May 11 2021 03:30:43", updatedAt="Wed Mar 23 2022 15:31:04")
    comment1436 = Comment(videoId=293, channelId=98, content="Sometimes I stare at a door or a wall and I wonder what is this reality, why am I alive, and what is this all about?", createdAt="Wed Jun 02 2021 08:45:36", updatedAt="Wed Feb 09 2022 07:30:11")
    comment1437 = Comment(videoId=420, channelId=90, content="Pair your designer cowboy hat with scuba gear for a memorable occasion.", createdAt="Sat Nov 27 2021 05:21:11", updatedAt="Sun Mar 20 2022 22:45:18")
    comment1438 = Comment(videoId=362, channelId=91, content="Green should have smelled more tranquil, but somehow it just tasted rotten.", createdAt="Wed Nov 24 2021 08:44:01", updatedAt="Sat Sep 11 2021 21:29:09")
    comment1439 = Comment(videoId=696, channelId=94, content="I was starting to worry that my pet turtle could tell what I was thinking.", createdAt="Wed May 12 2021 15:30:58", updatedAt="Mon Dec 13 2021 17:26:29")
    comment1440 = Comment(videoId=104, channelId=3, content="Jim liked driving around town with his hazard lights on.", createdAt="Tue Oct 26 2021 21:12:21", updatedAt="Thu May 20 2021 03:53:44")
    comment1441 = Comment(videoId=779, channelId=93, content="The heat", createdAt="Tue May 11 2021 11:31:10", updatedAt="Sun Feb 20 2022 12:06:22")
    comment1442 = Comment(videoId=54, channelId=74, content="He hated that he loved what she hated about hate.", createdAt="Thu Dec 16 2021 00:02:42", updatedAt="Wed Dec 29 2021 01:12:07")
    comment1444 = Comment(videoId=562, channelId=45, content="If you like tuna and tomato sauce, try combining the two, it’s really not as bad as it sounds.", createdAt="Fri Jun 18 2021 02:35:24", updatedAt="Tue Jun 29 2021 07:02:46")
    comment1445 = Comment(videoId=674, channelId=86, content="Having no hair made him look even hairier.", createdAt="Fri Jul 02 2021 13:25:49", updatedAt="Sat Nov 06 2021 12:14:46")
    comment1446 = Comment(videoId=180, channelId=14, content="Let me help you with your baggage.", createdAt="Thu Dec 09 2021 11:37:03", updatedAt="Fri Jan 14 2022 06:21:21")
    comment1447 = Comment(videoId=123, channelId=58, content="Please put on these earmuffs because I can't you hear.", createdAt="Wed Jun 09 2021 06:37:16", updatedAt="Wed Mar 16 2022 19:57:17")
    comment1448 = Comment(videoId=17, channelId=57, content="He dreamed of eating green apples with worms.", createdAt="Tue Jul 06 2021 01:25:25", updatedAt="Tue Oct 19 2021 18:18:04")
    comment1449 = Comment(videoId=768, channelId=81, content="Nancy thought the best way to create a welcoming home was to line it with barbed wire.", createdAt="Sat Mar 12 2022 04:31:02", updatedAt="Wed Oct 13 2021 05:47:56")
    comment1450 = Comment(videoId=22, channelId=93, content="As he waited for the shower to warm, he noticed that he could hear water change temperature.", createdAt="Tue Jan 18 2022 04:10:54", updatedAt="Wed Jun 02 2021 15:32:36")
    comment1451 = Comment(videoId=328, channelId=85, content="They looked up at the sky and saw a million stars.", createdAt="Sun Sep 26 2021 08:42:20", updatedAt="Tue Jun 15 2021 23:43:55")
    comment1452 = Comment(videoId=429, channelId=34, content="Nancy decided to make the porta-potty her home.", createdAt="Sat Nov 20 2021 21:07:39", updatedAt="Sat Feb 05 2022 13:43:52")
    comment1453 = Comment(videoId=312, channelId=69, content="Each person who knows you has a different perception of who you are.", createdAt="Thu Aug 19 2021 17:32:04", updatedAt="Mon Aug 16 2021 10:00:41")
    comment1454 = Comment(videoId=149, channelId=79, content="I just wanted to tell you I could see the love you have for your child by the way you look at her.", createdAt="Sat Sep 11 2021 18:47:48", updatedAt="Tue Jun 01 2021 16:28:27")
    comment1455 = Comment(videoId=186, channelId=47, content="This is a Japanese doll.", createdAt="Wed Oct 13 2021 19:52:39", updatedAt="Wed Feb 09 2022 17:54:20")
    comment1457 = Comment(videoId=301, channelId=60, content="Number of Sentences:", createdAt="Wed Aug 11 2021 09:35:28", updatedAt="Tue Jan 04 2022 05:39:47")
    comment1458 = Comment(videoId=714, channelId=24, content="50", createdAt="Thu Mar 03 2022 18:47:28", updatedAt="Tue Nov 30 2021 16:51:21")
    comment1459 = Comment(videoId=5, channelId=89, content="The father handed each child a roadmap at the beginning of the 2-day road trip and explained it was so they could find their way home.", createdAt="Sun May 16 2021 09:31:40", updatedAt="Sun Nov 14 2021 01:54:20")
    comment1460 = Comment(videoId=340, channelId=31, content="She had convinced her kids that any mushroom found on the ground would kill them if they touched it.", createdAt="Fri May 07 2021 06:15:02", updatedAt="Mon Aug 16 2021 04:00:04")
    comment1461 = Comment(videoId=397, channelId=92, content="When money was tight, he'd get his lunch money from the local wishing well.", createdAt="Wed Sep 01 2021 23:05:35", updatedAt="Fri Oct 08 2021 00:12:22")
    comment1462 = Comment(videoId=559, channelId=42, content="He invested some skill points in Charisma and Strength.", createdAt="Fri Oct 29 2021 11:49:19", updatedAt="Fri Aug 13 2021 18:53:51")
    comment1463 = Comment(videoId=463, channelId=48, content="Jenny made the announcement that her baby was an alien.", createdAt="Mon Jan 31 2022 19:45:04", updatedAt="Mon Feb 21 2022 00:50:51")
    comment1464 = Comment(videoId=3, channelId=96, content="On each full moon", createdAt="Mon Nov 15 2021 10:31:44", updatedAt="Sat Oct 16 2021 19:03:12")
    comment1465 = Comment(videoId=766, channelId=35, content="Situps are a terrible way to end your day.", createdAt="Sun Jan 16 2022 13:44:35", updatedAt="Mon Jun 07 2021 07:30:56")
    comment1466 = Comment(videoId=472, channelId=14, content="At that moment he wasn't listening to music, he was living an experience.", createdAt="Wed Jun 23 2021 01:53:20", updatedAt="Mon May 24 2021 11:00:02")
    comment1467 = Comment(videoId=441, channelId=43, content="I never knew what hardship looked like until it started raining bowling balls.", createdAt="Mon Feb 21 2022 14:57:21", updatedAt="Wed Apr 21 2021 09:35:31")
    comment1468 = Comment(videoId=717, channelId=53, content="The door slammed on the watermelon.", createdAt="Tue Dec 21 2021 21:40:35", updatedAt="Mon Jun 21 2021 10:14:15")
    comment1469 = Comment(videoId=28, channelId=33, content="That was how he came to win $1 million.", createdAt="Wed Aug 11 2021 17:21:19", updatedAt="Wed Feb 16 2022 15:51:44")
    comment1470 = Comment(videoId=58, channelId=13, content="People who insist on picking their teeth with their elbows are so annoying!", createdAt="Tue Sep 21 2021 08:22:25", updatedAt="Fri Aug 13 2021 23:24:41")
    comment1471 = Comment(videoId=544, channelId=27, content="He had a vague sense that trees gave birth to dinosaurs.", createdAt="Sun Apr 18 2021 10:31:22", updatedAt="Wed Feb 09 2022 06:15:16")
    comment1472 = Comment(videoId=48, channelId=1, content="Pink horses galloped across the sea.", createdAt="Mon Oct 25 2021 05:16:10", updatedAt="Sat Oct 23 2021 20:57:49")
    comment1473 = Comment(videoId=30, channelId=16, content="Everyone says they love nature until they realize how dangerous she can be.", createdAt="Sat Jun 12 2021 22:17:51", updatedAt="Wed Dec 15 2021 01:25:32")
    comment1475 = Comment(videoId=560, channelId=53, content="He kept telling himself that one day it would all somehow make sense.", createdAt="Tue Sep 14 2021 03:39:31", updatedAt="Sun Feb 20 2022 15:08:34")
    comment1476 = Comment(videoId=77, channelId=83, content="Peanuts don't grow on trees, but cashews do.", createdAt="Mon Jan 31 2022 22:48:32", updatedAt="Fri Oct 01 2021 06:05:34")
    comment1477 = Comment(videoId=750, channelId=42, content="The lake is a long way from here.", createdAt="Mon Jun 07 2021 21:00:05", updatedAt="Sun May 02 2021 17:48:02")
    comment1478 = Comment(videoId=548, channelId=54, content="There are few things better in life than a slice of pie.", createdAt="Thu Aug 19 2021 22:38:51", updatedAt="Sun Nov 21 2021 08:49:28")
    comment1479 = Comment(videoId=475, channelId=34, content="He found the end of the rainbow and was surprised at what he found there.", createdAt="Fri Nov 05 2021 02:16:16", updatedAt="Thu Mar 24 2022 22:34:50")
    comment1480 = Comment(videoId=486, channelId=23, content="A kangaroo is really just a rabbit on steroids.", createdAt="Tue May 25 2021 18:35:28", updatedAt="Sat Jan 08 2022 22:00:09")
    comment1481 = Comment(videoId=192, channelId=79, content="I was very proud of my nickname throughout high school but today- I couldn’t be any different to what my nickname was.", createdAt="Thu Nov 11 2021 09:07:39", updatedAt="Sun Jan 09 2022 17:09:26")
    comment1482 = Comment(videoId=302, channelId=43, content="The thunderous roar of the jet overhead confirmed her worst fears.", createdAt="Sat May 08 2021 00:58:22", updatedAt="Fri Apr 08 2022 09:05:31")
    comment1483 = Comment(videoId=483, channelId=40, content="Homesickness became contagious in the young campers' cabin.", createdAt="Thu Dec 02 2021 07:42:13", updatedAt="Sat Sep 18 2021 06:08:09")
    comment1484 = Comment(videoId=196, channelId=97, content="She hadn't had her cup of coffee, and that made things all the worse.", createdAt="Thu Apr 22 2021 13:35:33", updatedAt="Wed Jun 16 2021 18:37:20")
    comment1485 = Comment(videoId=85, channelId=75, content="She can live her life however she wants as long as she listens to what I have to say.", createdAt="Tue Mar 08 2022 03:12:02", updatedAt="Tue Sep 14 2021 12:40:30")
    comment1486 = Comment(videoId=87, channelId=79, content="In that instant, everything changed.", createdAt="Thu Jun 10 2021 23:17:00", updatedAt="Wed Jul 07 2021 08:25:00")
    comment1487 = Comment(videoId=213, channelId=92, content="He learned the important lesson that a picnic at the beach on a windy day is a bad idea.", createdAt="Fri Dec 24 2021 16:21:17", updatedAt="Sat Sep 04 2021 20:56:23")
    comment1488 = Comment(videoId=531, channelId=51, content="He's in a boy band which doesn't make much sense for a snake.", createdAt="Tue Mar 15 2022 04:15:14", updatedAt="Tue Nov 23 2021 18:59:12")
    comment1489 = Comment(videoId=427, channelId=85, content="She did not cheat on the test, for it was not the right thing to do.", createdAt="Tue Nov 30 2021 06:08:47", updatedAt="Sun Aug 01 2021 02:54:05")
    comment1490 = Comment(videoId=617, channelId=70, content="The beauty of the sunset was obscured by the industrial cranes.", createdAt="Sat Jan 08 2022 21:21:34", updatedAt="Wed Apr 14 2021 03:24:32")
    comment1491 = Comment(videoId=297, channelId=58, content="The secret ingredient to his wonderful life was crime.", createdAt="Fri Mar 25 2022 04:06:18", updatedAt="Tue Jan 11 2022 02:50:16")
    comment1492 = Comment(videoId=389, channelId=60, content="They got there early, and they got really good seats.", createdAt="Tue Sep 28 2021 19:35:17", updatedAt="Fri Aug 06 2021 23:59:34")
    comment1493 = Comment(videoId=172, channelId=20, content="The tart lemonade quenched her thirst, but not her longing.", createdAt="Sun Nov 28 2021 16:16:02", updatedAt="Fri Mar 04 2022 20:03:02")
    comment1494 = Comment(videoId=682, channelId=92, content="Pat ordered a ghost pepper pie.", createdAt="Sun Dec 19 2021 16:58:24", updatedAt="Fri Dec 03 2021 08:10:46")
    comment1495 = Comment(videoId=335, channelId=88, content="He fumbled in the darkness looking for the light switch, but when he finally found it there was someone already there.", createdAt="Fri May 28 2021 12:28:15", updatedAt="Sat Jun 12 2021 22:28:33")
    comment1496 = Comment(videoId=600, channelId=47, content="Every manager should be able to recite at least ten nursery rhymes backward.", createdAt="Tue Jul 13 2021 20:19:35", updatedAt="Thu Feb 10 2022 17:16:23")
    comment1497 = Comment(videoId=621, channelId=69, content="At that moment I was the most fearsome weasel in the entire swamp.", createdAt="Mon Jan 17 2022 16:39:42", updatedAt="Fri Sep 10 2021 09:27:52")
    comment1498 = Comment(videoId=687, channelId=25, content="The skeleton had skeletons of his own in the closet.", createdAt="Sun Dec 19 2021 11:23:13", updatedAt="Wed May 26 2021 23:58:29")
    comment1499 = Comment(videoId=667, channelId=60, content="The team members were hard to tell apart since they all wore their hair in a ponytail.", createdAt="Mon Jul 19 2021 13:08:15", updatedAt="Wed Feb 16 2022 16:53:33")
    comment1500 = Comment(videoId=538, channelId=91, content="The fish dreamed of escaping the fishbowl and into the toilet where he saw his friend go.", createdAt="Sat Jul 17 2021 18:18:36", updatedAt="Thu Sep 09 2021 06:16:06")
    comment1501 = Comment(videoId=746, channelId=38, content="Jason didn’t understand why his parents wouldn’t let him sell his little sister at the garage sale.", createdAt="Sat Jul 24 2021 20:03:03", updatedAt="Thu Jul 22 2021 07:59:25")
    comment1502 = Comment(videoId=222, channelId=67, content="We have young kids who often walk into our room at night for various reasons including clowns in the closet.", createdAt="Sun Oct 17 2021 11:17:34", updatedAt="Fri Nov 12 2021 22:51:52")
    comment1503 = Comment(videoId=399, channelId=99, content="He drank life before spitting it out.", createdAt="Mon Aug 02 2021 08:14:05", updatedAt="Sat Mar 19 2022 15:54:34")
    comment1504 = Comment(videoId=558, channelId=90, content="He never understood why what, when, and where left out who.", createdAt="Fri May 28 2021 09:36:44", updatedAt="Sat Oct 16 2021 21:11:19")
    comment1505 = Comment(videoId=224, channelId=55, content="Being unacquainted with the chief raccoon was harming his prospects for promotion.", createdAt="Sat Nov 27 2021 23:11:29", updatedAt="Mon May 31 2021 03:23:02")
    comment1506 = Comment(videoId=228, channelId=98, content="Nothing is as cautiously cuddly as a pet porcupine.", createdAt="Fri Jul 23 2021 04:48:46", updatedAt="Sat Apr 02 2022 09:31:02")
    comment1507 = Comment(videoId=646, channelId=38, content="She was disgusted he couldn’t tell the difference between lemonade and limeade.", createdAt="Mon May 03 2021 17:57:57", updatedAt="Mon Jul 05 2021 08:46:32")
    comment1508 = Comment(videoId=531, channelId=5, content="There are over 500 starfish in the bathroom drawer.", createdAt="Fri Oct 22 2021 07:20:44", updatedAt="Thu Jan 20 2022 09:35:23")
    comment1509 = Comment(videoId=302, channelId=3, content="The light in his life was actually a fire burning all around him.", createdAt="Thu Jan 13 2022 02:21:45", updatedAt="Thu Sep 16 2021 14:54:53")
    comment1510 = Comment(videoId=152, channelId=21, content="Everyone was busy, so I went to the movie alone.", createdAt="Tue Aug 31 2021 05:30:58", updatedAt="Wed Oct 27 2021 00:25:56")
    comment1511 = Comment(videoId=31, channelId=96, content="He had a wall full of masks so she could wear a different face every day.", createdAt="Wed Feb 23 2022 08:33:51", updatedAt="Mon Aug 09 2021 16:03:45")
    comment1512 = Comment(videoId=360, channelId=33, content="My biggest joy is roasting almonds while stalking prey.", createdAt="Thu Jul 22 2021 09:09:36", updatedAt="Sun Feb 13 2022 20:13:41")
    comment1513 = Comment(videoId=87, channelId=13, content="The busker hoped that the people passing by would throw money, but they threw tomatoes instead, so he exchanged his hat for a juicer.", createdAt="Sat Jul 03 2021 17:25:51", updatedAt="Fri Jan 07 2022 05:14:37")
    comment1514 = Comment(videoId=244, channelId=58, content="The clouds formed beautiful animals in the sky that eventually created a tornado to wreak havoc.", createdAt="Wed Jun 23 2021 08:21:44", updatedAt="Sat Sep 11 2021 21:21:48")
    comment1515 = Comment(videoId=423, channelId=19, content="She used her own hair in the soup to give it more flavor.", createdAt="Mon Jan 17 2022 01:24:22", updatedAt="Sun Aug 15 2021 04:38:45")
    comment1516 = Comment(videoId=363, channelId=98, content="It's difficult to understand the lengths he'd go to remain short.", createdAt="Mon May 03 2021 14:02:02", updatedAt="Wed Sep 08 2021 00:51:38")
    comment1517 = Comment(videoId=121, channelId=25, content="I would be delighted if the sea were full of cucumber juice.", createdAt="Wed Dec 22 2021 15:50:19", updatedAt="Sun Oct 17 2021 15:47:06")
    comment1518 = Comment(videoId=687, channelId=83, content="The tattered work gloves speak of the many hours of hard labor he endured throughout his life.", createdAt="Mon May 03 2021 06:36:03", updatedAt="Mon May 03 2021 17:41:24")
    comment1519 = Comment(videoId=678, channelId=73, content="The trick to getting kids to eat anything is to put catchup on it.", createdAt="Fri Aug 27 2021 17:24:51", updatedAt="Sun Sep 05 2021 14:39:13")
    comment1520 = Comment(videoId=406, channelId=82, content="At that moment she realized she had a sixth sense.", createdAt="Sun Mar 27 2022 11:56:31", updatedAt="Tue Aug 31 2021 07:57:30")
    comment1521 = Comment(videoId=468, channelId=93, content="The random sentence generator generated a random sentence about a random sentence.", createdAt="Wed Jun 16 2021 02:06:14", updatedAt="Fri Jun 11 2021 09:06:13")
    comment1522 = Comment(videoId=227, channelId=15, content="Patricia found the meaning of life in a bowl of Cheerios.", createdAt="Tue Mar 22 2022 15:23:51", updatedAt="Thu May 06 2021 15:34:47")
    comment1523 = Comment(videoId=115, channelId=42, content="The llama couldn't resist trying the lemonade.", createdAt="Wed Nov 03 2021 02:40:17", updatedAt="Fri Apr 01 2022 17:45:24")
    comment1524 = Comment(videoId=682, channelId=15, content="Wisdom is easily acquired when hiding under the bed with a saucepan on your head.", createdAt="Tue Jul 06 2021 23:31:24", updatedAt="Wed Jan 05 2022 12:03:15")
    comment1525 = Comment(videoId=535, channelId=39, content="The beauty of the sunset was obscured by the industrial cranes.", createdAt="Tue May 18 2021 07:00:34", updatedAt="Mon Apr 04 2022 14:16:27")
    comment1526 = Comment(videoId=637, channelId=8, content="It was a really good Monday for being a Saturday.", createdAt="Tue Oct 05 2021 04:50:43", updatedAt="Mon Jan 03 2022 09:08:41")
    comment1527 = Comment(videoId=695, channelId=60, content="Two seats were vacant.", createdAt="Tue Nov 09 2021 08:40:54", updatedAt="Fri Aug 13 2021 15:10:00")
    comment1528 = Comment(videoId=160, channelId=69, content="The teens wondered what was kept in the red shed on the far edge of the school grounds.", createdAt="Thu Jan 06 2022 23:15:43", updatedAt="Sun Aug 22 2021 23:55:45")
    comment1529 = Comment(videoId=182, channelId=90, content="The fence was confused about whether it was supposed to keep things in or keep things out.", createdAt="Sat Jan 15 2022 08:22:14", updatedAt="Wed May 05 2021 11:48:24")
    comment1530 = Comment(videoId=243, channelId=25, content="The newly planted trees were held up by wooden frames in hopes they could survive the next storm.", createdAt="Sun Jul 25 2021 11:47:07", updatedAt="Mon Dec 13 2021 13:27:19")
    comment1531 = Comment(videoId=494, channelId=97, content="Situps are a terrible way to end your day.", createdAt="Wed Apr 14 2021 08:50:56", updatedAt="Wed Sep 22 2021 22:40:47")
    comment1532 = Comment(videoId=13, channelId=6, content="She always had an interesting perspective on why the world must be flat.", createdAt="Thu Jun 17 2021 16:16:09", updatedAt="Wed Aug 11 2021 14:17:15")
    comment1533 = Comment(videoId=168, channelId=82, content="He loved eating his bananas in hot dog buns.", createdAt="Sat Oct 23 2021 12:19:53", updatedAt="Thu Sep 16 2021 06:40:18")
    comment1534 = Comment(videoId=719, channelId=13, content="He was the only member of the club who didn't like plum pudding.", createdAt="Wed May 12 2021 20:22:47", updatedAt="Fri Nov 05 2021 05:11:37")
    comment1535 = Comment(videoId=205, channelId=98, content="Plans for this weekend include turning wine into water.", createdAt="Mon Feb 14 2022 12:18:48", updatedAt="Wed Apr 28 2021 04:48:40")
    comment1536 = Comment(videoId=11, channelId=90, content="When money was tight, he'd get his lunch money from the local wishing well.", createdAt="Wed Apr 14 2021 19:05:44", updatedAt="Thu Mar 17 2022 02:20:28")
    comment1537 = Comment(videoId=104, channelId=24, content="The lyrics of the song sounded like fingernails on a chalkboard.", createdAt="Tue May 25 2021 08:09:02", updatedAt="Fri Jul 23 2021 15:13:53")
    comment1538 = Comment(videoId=129, channelId=5, content="He had concluded that pigs must be able to fly in Hog Heaven.", createdAt="Mon May 24 2021 10:49:13", updatedAt="Mon May 31 2021 12:06:52")
    comment1539 = Comment(videoId=180, channelId=85, content="She cried diamonds.", createdAt="Sun May 23 2021 02:57:04", updatedAt="Wed Mar 16 2022 07:49:24")
    comment1540 = Comment(videoId=456, channelId=14, content="You'll see the rainbow bridge after it rains cats and dogs.", createdAt="Sat Oct 16 2021 17:38:11", updatedAt="Mon Feb 28 2022 23:58:53")
    comment1541 = Comment(videoId=359, channelId=47, content="The rusty nail stood erect, angled at a 45-degree angle, just waiting for the perfect barefoot to come along.", createdAt="Mon Sep 06 2021 18:26:51", updatedAt="Fri May 21 2021 19:30:55")
    comment1542 = Comment(videoId=716, channelId=18, content="The old apple revels in its authority.", createdAt="Wed Sep 29 2021 13:54:53", updatedAt="Tue Jul 20 2021 11:30:36")
    comment1543 = Comment(videoId=442, channelId=54, content="25 years later, she still regretted that specific moment.", createdAt="Mon May 31 2021 12:52:35", updatedAt="Fri Apr 16 2021 20:32:36")
    comment1544 = Comment(videoId=305, channelId=45, content="Most shark attacks occur about 10 feet from the beach since that's where the people are.", createdAt="Fri Jun 11 2021 15:08:59", updatedAt="Wed Sep 15 2021 02:11:41")
    comment1545 = Comment(videoId=104, channelId=19, content="As time wore on, simple dog commands turned into full paragraphs explaining why the dog couldn’t do something.", createdAt="Sun Apr 18 2021 04:28:50", updatedAt="Thu Feb 03 2022 00:09:44")
    comment1546 = Comment(videoId=273, channelId=62, content="Getting up at dawn is for the birds.", createdAt="Wed Jul 14 2021 11:00:11", updatedAt="Sun Jul 11 2021 22:28:55")
    comment1547 = Comment(videoId=216, channelId=6, content="More RVs were seen in the storage lot than at the campground.", createdAt="Fri Oct 15 2021 00:15:37", updatedAt="Sat May 22 2021 01:36:13")
    comment1548 = Comment(videoId=747, channelId=69, content="Car safety systems have come a long way, but he was out to prove they could be outsmarted.", createdAt="Mon Oct 25 2021 12:25:14", updatedAt="Sun May 16 2021 03:51:40")
    comment1549 = Comment(videoId=401, channelId=31, content="As the asteroid hurtled toward earth, Becky was upset her dentist appointment had been canceled.", createdAt="Tue Mar 08 2022 20:26:21", updatedAt="Sat Jan 22 2022 08:27:16")
    comment1550 = Comment(videoId=553, channelId=16, content="Despite multiple complications and her near-death experience", createdAt="Fri Aug 27 2021 09:27:51", updatedAt="Wed Feb 23 2022 06:32:55")
    comment1551 = Comment(videoId=337, channelId=52, content="The sign said there was road work ahead so he decided to speed up.", createdAt="Thu Jul 08 2021 23:46:23", updatedAt="Sun Oct 31 2021 05:03:34")
    comment1552 = Comment(videoId=604, channelId=73, content="His son quipped that power bars were nothing more than adult candy bars.", createdAt="Mon Oct 25 2021 07:08:47", updatedAt="Wed Dec 15 2021 20:41:22")
    comment1553 = Comment(videoId=183, channelId=64, content="The mysterious diary records the voice.", createdAt="Tue Jul 20 2021 01:41:31", updatedAt="Mon Mar 07 2022 18:01:32")
    comment1554 = Comment(videoId=484, channelId=9, content="Mary realized if her calculator had a history, it would be more embarrassing than her computer browser history.", createdAt="Wed Feb 02 2022 09:29:27", updatedAt="Sat Jul 03 2021 03:22:47")
    comment1556 = Comment(videoId=167, channelId=89, content="He used to get confused between soldiers and shoulders, but as a military man, he now soldiers responsibility.", createdAt="Sun Aug 01 2021 12:23:18", updatedAt="Fri Aug 06 2021 21:15:57")
    comment1557 = Comment(videoId=393, channelId=12, content="Mom didn’t understand why no one else wanted a hot tub full of jello.", createdAt="Sat Jul 03 2021 09:55:46", updatedAt="Wed May 05 2021 22:16:57")
    comment1558 = Comment(videoId=594, channelId=74, content="I would have gotten the promotion, but my attendance wasn’t good enough.", createdAt="Tue Feb 08 2022 10:04:07", updatedAt="Tue May 04 2021 02:41:49")
    comment1560 = Comment(videoId=171, channelId=58, content="She did not cheat on the test, for it was not the right thing to do.", createdAt="Sat Sep 11 2021 12:50:35", updatedAt="Thu Jan 27 2022 21:23:41")
    comment1561 = Comment(videoId=134, channelId=3, content="The fifty mannequin heads floating in the pool kind of freaked them out.", createdAt="Fri Dec 10 2021 01:39:44", updatedAt="Fri Jun 04 2021 14:58:00")
    comment1562 = Comment(videoId=164, channelId=42, content="Various sea birds are elegant, but nothing is as elegant as a gliding pelican.", createdAt="Fri Aug 27 2021 10:46:09", updatedAt="Wed Oct 27 2021 06:43:52")
    comment1563 = Comment(videoId=117, channelId=8, content="They got there early, and they got really good seats.", createdAt="Fri Nov 26 2021 08:47:00", updatedAt="Tue Nov 23 2021 04:35:21")
    comment1564 = Comment(videoId=94, channelId=5, content="Tom got a small piece of pie.", createdAt="Thu Jan 20 2022 20:02:34", updatedAt="Tue Mar 01 2022 13:51:29")
    comment1565 = Comment(videoId=198, channelId=11, content="Excitement replaced fear until the final moment.", createdAt="Mon Sep 20 2021 05:28:05", updatedAt="Mon Mar 21 2022 15:09:16")
    comment1566 = Comment(videoId=172, channelId=9, content="I love eating toasted cheese and tuna sandwiches.", createdAt="Sun Feb 27 2022 21:13:30", updatedAt="Tue Nov 09 2021 19:38:55")
    comment1567 = Comment(videoId=531, channelId=6, content="She folded her handkerchief neatly.", createdAt="Fri Nov 26 2021 04:28:32", updatedAt="Tue Feb 01 2022 13:23:20")
    comment1568 = Comment(videoId=155, channelId=13, content="She wore green lipstick like a fashion icon.", createdAt="Sat Sep 11 2021 12:32:33", updatedAt="Wed Oct 13 2021 19:22:36")
    comment1569 = Comment(videoId=354, channelId=15, content="I liked their first two albums but changed my mind after that charity gig.", createdAt="Tue Apr 27 2021 14:46:11", updatedAt="Wed Apr 21 2021 13:21:29")
    comment1570 = Comment(videoId=203, channelId=95, content="Everyone was curious about the large white blimp that appeared overnight.", createdAt="Thu Feb 10 2022 16:23:00", updatedAt="Wed Dec 22 2021 00:52:52")
    comment1571 = Comment(videoId=211, channelId=91, content="That is an appealing treasure map that I can't read.", createdAt="Tue Dec 28 2021 01:43:52", updatedAt="Sat Feb 05 2022 13:25:55")
    comment1573 = Comment(videoId=485, channelId=96, content="Cursive writing is the best way to build a race track.", createdAt="Tue Dec 21 2021 15:15:15", updatedAt="Wed Dec 22 2021 09:47:47")
    comment1574 = Comment(videoId=303, channelId=75, content="The father died during childbirth.", createdAt="Mon Nov 22 2021 04:02:52", updatedAt="Wed Aug 25 2021 12:12:03")
    comment1575 = Comment(videoId=567, channelId=12, content="The bullet pierced the window shattering it before missing Danny's head by mere millimeters.", createdAt="Fri May 28 2021 21:17:02", updatedAt="Sun Oct 10 2021 14:47:41")
    comment1576 = Comment(videoId=678, channelId=48, content="Don't step on the broken glass.", createdAt="Sat Aug 21 2021 01:17:23", updatedAt="Fri Dec 03 2021 18:23:40")
    comment1577 = Comment(videoId=516, channelId=2, content="She opened up her third bottle of wine of the night.", createdAt="Tue Oct 05 2021 23:22:01", updatedAt="Fri Nov 19 2021 04:56:05")
    comment1578 = Comment(videoId=516, channelId=82, content="My biggest joy is roasting almonds while stalking prey.", createdAt="Wed Sep 01 2021 14:53:57", updatedAt="Wed Mar 16 2022 01:33:35")
    comment1579 = Comment(videoId=592, channelId=25, content="She saw the brake lights, but not in time.", createdAt="Fri Oct 15 2021 23:32:51", updatedAt="Thu Jul 01 2021 00:08:25")
    comment1580 = Comment(videoId=691, channelId=4, content="Today I heard something new and unmemorable.", createdAt="Sat Apr 17 2021 08:18:08", updatedAt="Fri Jun 25 2021 10:54:05")
    comment1581 = Comment(videoId=385, channelId=54, content="Baby wipes are made of chocolate stardust.", createdAt="Mon Jul 12 2021 06:37:59", updatedAt="Sun May 09 2021 04:32:00")
    comment1582 = Comment(videoId=418, channelId=46, content="Normal activities took extraordinary amounts of concentration at the high altitude.", createdAt="Tue Jun 22 2021 11:53:50", updatedAt="Mon Aug 02 2021 17:51:21")
    comment1583 = Comment(videoId=587, channelId=30, content="There was no ice cream in the freezer, nor did they have money to go to the store.", createdAt="Mon Apr 04 2022 14:42:31", updatedAt="Wed Jun 02 2021 10:13:30")
    comment1584 = Comment(videoId=262, channelId=62, content="He was disappointed when he found the beach to be so sandy and the sun so sunny.", createdAt="Sat Mar 05 2022 18:49:24", updatedAt="Thu Dec 16 2021 03:57:23")
    comment1585 = Comment(videoId=8, channelId=85, content="The dead trees waited to be ignited by the smallest spark and seek their revenge.", createdAt="Sun Nov 14 2021 09:28:36", updatedAt="Tue Oct 26 2021 11:16:59")
    comment1586 = Comment(videoId=779, channelId=34, content="Happiness can be found in the depths of chocolate pudding.", createdAt="Sat May 15 2021 16:06:33", updatedAt="Sun Feb 27 2022 15:41:07")
    comment1587 = Comment(videoId=17, channelId=93, content="He fumbled in the darkness looking for the light switch, but when he finally found it there was someone already there.", createdAt="Wed Oct 20 2021 14:20:55", updatedAt="Sun May 09 2021 22:35:51")
    comment1588 = Comment(videoId=56, channelId=57, content="Three years later, the coffin was still full of Jello.", createdAt="Sat Feb 19 2022 09:35:41", updatedAt="Sat Sep 11 2021 01:43:40")
    comment1589 = Comment(videoId=757, channelId=44, content="The trick to getting kids to eat anything is to put catchup on it.", createdAt="Tue Feb 08 2022 01:57:19", updatedAt="Tue Sep 14 2021 01:53:12")
    comment1590 = Comment(videoId=25, channelId=12, content="The three-year-old girl ran down the beach as the kite flew behind her.", createdAt="Thu Oct 28 2021 12:38:46", updatedAt="Sun Dec 19 2021 05:58:35")
    comment1591 = Comment(videoId=55, channelId=42, content="When nobody is around, the trees gossip about the people who have walked under them.", createdAt="Tue Jun 08 2021 10:43:22", updatedAt="Wed Apr 06 2022 02:31:01")
    comment1592 = Comment(videoId=130, channelId=74, content="Poison ivy grew through the fence they said was impenetrable.", createdAt="Sun Aug 15 2021 23:36:39", updatedAt="Wed Oct 13 2021 07:15:48")
    comment1593 = Comment(videoId=518, channelId=67, content="David subscribes to the \"stuff your tent into the bag\" strategy over nicely folding it.", createdAt="Sat Mar 19 2022 05:25:08", updatedAt="Fri Oct 15 2021 00:16:18")
    comment1594 = Comment(videoId=176, channelId=81, content="It's never been my responsibility to glaze the donuts.", createdAt="Fri May 28 2021 12:16:30", updatedAt="Tue Apr 27 2021 12:30:09")
    comment1595 = Comment(videoId=51, channelId=91, content="He strives to keep the best lawn in the neighborhood.", createdAt="Sun Apr 18 2021 09:23:03", updatedAt="Thu Sep 16 2021 04:56:05")
    comment1596 = Comment(videoId=300, channelId=7, content="He wondered why at 18 he was old enough to go to war, but not old enough to buy cigarettes.", createdAt="Fri Feb 18 2022 06:24:31", updatedAt="Tue Nov 09 2021 20:29:12")
    comment1597 = Comment(videoId=742, channelId=84, content="He didn't understand why the bird wanted to ride the bicycle.", createdAt="Wed Dec 01 2021 14:17:06", updatedAt="Wed Apr 28 2021 09:30:52")
    comment1598 = Comment(videoId=242, channelId=57, content="As time wore on, simple dog commands turned into full paragraphs explaining why the dog couldn’t do something.", createdAt="Mon Feb 21 2022 22:57:39", updatedAt="Wed May 26 2021 16:58:24")
    comment1600 = Comment(videoId=506, channelId=50, content="The external scars tell only part of the story.", createdAt="Fri Apr 30 2021 08:58:23", updatedAt="Wed Jan 05 2022 08:35:11")
    comment1601 = Comment(videoId=615, channelId=23, content="Homesickness became contagious in the young campers' cabin.", createdAt="Sat Oct 16 2021 07:30:02", updatedAt="Wed Jan 26 2022 13:29:30")
    comment1602 = Comment(videoId=515, channelId=53, content="Best friends are like old tomatoes and shoelaces.", createdAt="Sun Jul 04 2021 19:36:19", updatedAt="Thu Aug 05 2021 10:53:13")
    comment1603 = Comment(videoId=369, channelId=45, content="He walked into the basement with the horror movie from the night before playing in his head.", createdAt="Sat Jul 03 2021 06:33:03", updatedAt="Mon May 17 2021 02:54:31")
    comment1604 = Comment(videoId=50, channelId=33, content="She borrowed the book from him many years ago and hasn't yet returned it.", createdAt="Mon Oct 11 2021 07:02:17", updatedAt="Sat Oct 23 2021 09:33:53")
    comment1605 = Comment(videoId=417, channelId=10, content="The fog was so dense even a laser decided it wasn't worth the effort.", createdAt="Tue Jan 11 2022 17:30:08", updatedAt="Fri Nov 12 2021 00:53:12")
    comment1606 = Comment(videoId=455, channelId=5, content="I had a friend in high school named Rick Shaw, but he was fairly useless as a mode of transport.", createdAt="Tue Sep 07 2021 04:21:27", updatedAt="Tue May 18 2021 13:55:58")
    comment1607 = Comment(videoId=345, channelId=71, content="In hopes of finding out the truth, he entered the one-room library.", createdAt="Fri Jun 25 2021 15:19:54", updatedAt="Sun Sep 12 2021 22:06:50")
    comment1608 = Comment(videoId=239, channelId=1, content="He had a hidden stash underneath the floorboards in the back room of the house.", createdAt="Fri Sep 24 2021 01:53:21", updatedAt="Wed Apr 06 2022 07:50:12")
    comment1609 = Comment(videoId=98, channelId=81, content="That must be the tenth time I've been arrested for selling deep-fried cigars.", createdAt="Thu Feb 03 2022 18:29:27", updatedAt="Sat Feb 26 2022 06:42:22")
    comment1610 = Comment(videoId=722, channelId=26, content="Her scream silenced the rowdy teenagers.", createdAt="Sat Apr 02 2022 05:41:42", updatedAt="Wed Nov 17 2021 07:31:03")
    comment1611 = Comment(videoId=643, channelId=84, content="It was a really good Monday for being a Saturday.", createdAt="Wed Jun 16 2021 02:11:41", updatedAt="Thu Jun 17 2021 18:35:25")
    comment1612 = Comment(videoId=126, channelId=27, content="Standing on one's head at job interviews forms a lasting impression.", createdAt="Fri Sep 24 2021 10:09:05", updatedAt="Sat Jan 01 2022 16:50:44")
    comment1613 = Comment(videoId=302, channelId=5, content="They were excited to see their first sloth.", createdAt="Wed Mar 23 2022 08:52:30", updatedAt="Tue Apr 05 2022 17:54:13")
    comment1614 = Comment(videoId=682, channelId=9, content="Barking dogs and screaming toddlers have the unique ability to turn friendly neighbors into cranky enemies.", createdAt="Sun Mar 27 2022 18:34:01", updatedAt="Tue Feb 15 2022 21:50:43")
    comment1615 = Comment(videoId=344, channelId=30, content="He would only survive if he kept the fire going and he could hear thunder in the distance.", createdAt="Fri Jan 21 2022 21:10:27", updatedAt="Sat Jul 03 2021 14:50:01")
    comment1616 = Comment(videoId=721, channelId=75, content="I hear that Nancy is very pretty.", createdAt="Sun Aug 01 2021 02:00:41", updatedAt="Tue Aug 17 2021 19:10:46")
    comment1617 = Comment(videoId=537, channelId=15, content="She wasn't sure whether to be impressed or concerned that he folded underwear in neat little packages.", createdAt="Mon Nov 08 2021 16:13:40", updatedAt="Sat Jun 12 2021 16:23:25")
    comment1618 = Comment(videoId=231, channelId=61, content="Garlic ice-cream was her favorite.", createdAt="Sun Sep 12 2021 23:39:03", updatedAt="Tue Mar 29 2022 06:34:50")
    comment1619 = Comment(videoId=249, channelId=80, content="The fish listened intently to what the frogs had to say.", createdAt="Sat Aug 14 2021 08:13:55", updatedAt="Fri Jul 30 2021 07:26:58")
    comment1620 = Comment(videoId=641, channelId=24, content="Nancy was proud that she ran a tight shipwreck.", createdAt="Fri Jan 28 2022 01:54:22", updatedAt="Mon Jan 03 2022 22:51:56")
    comment1621 = Comment(videoId=452, channelId=79, content="The beauty of the sunset was obscured by the industrial cranes.", createdAt="Tue Sep 28 2021 21:55:51", updatedAt="Thu Nov 04 2021 00:29:54")
    comment1622 = Comment(videoId=204, channelId=80, content="They decided to plant an orchard of cotton candy.", createdAt="Tue Feb 01 2022 22:58:32", updatedAt="Sun Apr 11 2021 11:33:38")
    comment1623 = Comment(videoId=44, channelId=2, content="Fluffy pink unicorns are a popular status symbol among macho men.", createdAt="Thu Mar 31 2022 06:30:40", updatedAt="Thu Nov 04 2021 11:50:37")
    comment1624 = Comment(videoId=427, channelId=7, content="The sky is clear; the stars are twinkling.", createdAt="Wed Mar 23 2022 05:13:38", updatedAt="Tue Jul 20 2021 07:25:38")
    comment1625 = Comment(videoId=41, channelId=91, content="Lightning Paradise was the local hangout joint where the group usually ended up spending the night.", createdAt="Sun Jul 18 2021 14:09:45", updatedAt="Thu Sep 23 2021 15:10:47")
    comment1626 = Comment(videoId=307, channelId=15, content="As the asteroid hurtled toward earth, Becky was upset her dentist appointment had been canceled.", createdAt="Sun Nov 28 2021 14:40:23", updatedAt="Thu Sep 09 2021 01:04:55")
    comment1627 = Comment(videoId=605, channelId=7, content="To the surprise of everyone, the Rapture happened yesterday but it didn't quite go as expected.", createdAt="Fri Feb 04 2022 20:21:17", updatedAt="Sat Feb 26 2022 17:47:42")
    comment1628 = Comment(videoId=725, channelId=48, content="He appeared to be confusingly perplexed.", createdAt="Tue Mar 29 2022 04:33:52", updatedAt="Sat Mar 26 2022 22:56:00")
    comment1629 = Comment(videoId=470, channelId=58, content="The murder hornet was disappointed by the preconceived ideas people had of him.", createdAt="Sun Jan 16 2022 13:39:59", updatedAt="Tue Feb 01 2022 08:01:18")
    comment1631 = Comment(videoId=129, channelId=98, content="She works two jobs to make ends meet; at least, that was her reason for not having time to join us.", createdAt="Sat May 15 2021 21:06:02", updatedAt="Fri Apr 23 2021 14:13:32")
    comment1632 = Comment(videoId=209, channelId=68, content="She had some amazing news to share but nobody to share it with.", createdAt="Wed Jan 26 2022 03:47:42", updatedAt="Sun Dec 05 2021 18:27:58")
    comment1633 = Comment(videoId=109, channelId=49, content="It must be five o'clock somewhere.", createdAt="Tue Nov 23 2021 01:21:39", updatedAt="Tue Feb 08 2022 17:11:40")
    comment1634 = Comment(videoId=135, channelId=48, content="Swim at your own risk was taken as a challenge for the group of Kansas City college students.", createdAt="Tue Nov 16 2021 02:06:44", updatedAt="Mon Mar 07 2022 06:33:46")
    comment1635 = Comment(videoId=58, channelId=96, content="Jenny made the announcement that her baby was an alien.", createdAt="Mon Sep 13 2021 10:59:09", updatedAt="Thu Sep 30 2021 01:56:03")
    comment1636 = Comment(videoId=107, channelId=27, content="Today I heard something new and unmemorable.", createdAt="Sun Mar 20 2022 14:20:16", updatedAt="Sun Apr 10 2022 03:14:06")
    comment1637 = Comment(videoId=472, channelId=78, content="Written warnings in instruction manuals are worthless since rabbits can't read.", createdAt="Mon Mar 14 2022 04:42:57", updatedAt="Sat Mar 19 2022 07:42:25")
    comment1638 = Comment(videoId=724, channelId=27, content="A glittering gem is not enough.", createdAt="Tue Dec 14 2021 01:28:35", updatedAt="Wed Feb 23 2022 05:24:04")
    comment1639 = Comment(videoId=76, channelId=35, content="Hit me with your pet shark!", createdAt="Fri Oct 01 2021 02:41:14", updatedAt="Sat Jun 19 2021 19:51:45")
    comment1640 = Comment(videoId=198, channelId=19, content="That was how he came to win $1 million.", createdAt="Wed Feb 23 2022 03:34:22", updatedAt="Fri Oct 15 2021 14:06:16")
    comment1641 = Comment(videoId=172, channelId=46, content="Little Red Riding Hood decided to wear orange today.", createdAt="Sun Jan 23 2022 23:56:13", updatedAt="Mon May 31 2021 08:30:46")
    comment1642 = Comment(videoId=382, channelId=6, content="He didn't understand why the bird wanted to ride the bicycle.", createdAt="Thu Oct 14 2021 18:49:38", updatedAt="Sun Oct 24 2021 14:57:58")
    comment1643 = Comment(videoId=318, channelId=35, content="Today we gathered moss for my uncle's wedding.", createdAt="Tue Mar 15 2022 05:30:40", updatedAt="Tue Jan 11 2022 16:23:44")
    comment1644 = Comment(videoId=57, channelId=6, content="Don't put peanut butter on the dog's nose.", createdAt="Sat Aug 21 2021 21:54:35", updatedAt="Sun Oct 31 2021 17:05:43")
    comment1645 = Comment(videoId=583, channelId=86, content="There's a growing trend among teenagers of using frisbees as go-cart wheels.", createdAt="Thu Dec 02 2021 22:40:24", updatedAt="Fri Jan 21 2022 02:50:28")
    comment1646 = Comment(videoId=509, channelId=98, content="He enjoys practicing his ballet in the bathroom.", createdAt="Mon Jun 28 2021 03:36:25", updatedAt="Thu Oct 28 2021 13:31:55")
    comment1647 = Comment(videoId=494, channelId=53, content="The small white buoys marked the location of hundreds of crab pots.", createdAt="Sun Jun 06 2021 04:02:09", updatedAt="Fri Apr 30 2021 04:43:02")
    comment1648 = Comment(videoId=274, channelId=47, content="Despite what your teacher may have told you, there is a wrong way to wield a lasso.", createdAt="Sun May 30 2021 09:37:27", updatedAt="Mon May 03 2021 21:22:34")
    comment1649 = Comment(videoId=278, channelId=64, content="Too many prisons have become early coffins.", createdAt="Tue Jan 11 2022 05:39:18", updatedAt="Sun Jun 20 2021 00:29:20")
    comment1650 = Comment(videoId=508, channelId=83, content="The fox in the tophat whispered into the ear of the rabbit.", createdAt="Fri Jul 16 2021 01:38:01", updatedAt="Wed Dec 29 2021 15:51:28")
    comment1651 = Comment(videoId=237, channelId=37, content="The green tea and avocado smoothie turned out exactly as would be expected.", createdAt="Thu Nov 11 2021 09:21:21", updatedAt="Sun Nov 28 2021 07:28:04")
    comment1652 = Comment(videoId=47, channelId=78, content="She can live her life however she wants as long as she listens to what I have to say.", createdAt="Fri Jul 02 2021 12:39:24", updatedAt="Tue Dec 28 2021 09:24:30")
    comment1653 = Comment(videoId=40, channelId=58, content="Instead of a bachelorette party", createdAt="Mon Jan 17 2022 11:32:13", updatedAt="Wed Jul 28 2021 21:05:18")
    comment1654 = Comment(videoId=408, channelId=55, content="Red is greener than purple, for sure.", createdAt="Thu Jul 29 2021 08:01:56", updatedAt="Fri Feb 25 2022 09:48:37")
    comment1655 = Comment(videoId=432, channelId=98, content="Grape jelly was leaking out the hole in the roof.", createdAt="Sat Jan 01 2022 09:37:35", updatedAt="Sat Sep 18 2021 07:36:37")
    comment1656 = Comment(videoId=607, channelId=21, content="The sun had set and so had his dreams.", createdAt="Mon Dec 20 2021 20:02:00", updatedAt="Thu Oct 14 2021 03:19:20")
    comment1657 = Comment(videoId=322, channelId=28, content="She cried diamonds.", createdAt="Fri Mar 25 2022 15:28:19", updatedAt="Sun Jul 11 2021 13:24:23")
    comment1658 = Comment(videoId=387, channelId=95, content="Poison ivy grew through the fence they said was impenetrable.", createdAt="Thu Apr 29 2021 15:43:58", updatedAt="Tue Dec 28 2021 21:04:10")
    comment1659 = Comment(videoId=141, channelId=41, content="They say that dogs are man's best friend, but this cat was setting out to sabotage that theory.", createdAt="Sat Mar 26 2022 13:51:58", updatedAt="Thu Feb 10 2022 06:28:49")
    comment1660 = Comment(videoId=160, channelId=32, content="Art doesn't have to be intentional.", createdAt="Thu Sep 23 2021 21:30:02", updatedAt="Tue Feb 15 2022 17:26:12")
    comment1661 = Comment(videoId=247, channelId=92, content="He stomped on his fruit loops and thus became a cereal killer.", createdAt="Sat Sep 18 2021 10:15:40", updatedAt="Thu Jul 01 2021 06:20:05")
    comment1662 = Comment(videoId=753, channelId=98, content="Her scream silenced the rowdy teenagers.", createdAt="Sat Oct 30 2021 02:10:38", updatedAt="Tue Mar 01 2022 23:23:43")
    comment1663 = Comment(videoId=347, channelId=32, content="She folded her handkerchief neatly.", createdAt="Thu Dec 09 2021 10:31:08", updatedAt="Thu Nov 18 2021 06:56:16")
    comment1664 = Comment(videoId=648, channelId=34, content="She only paints with bold colors; she does not like pastels.", createdAt="Mon Feb 28 2022 09:28:39", updatedAt="Wed Dec 01 2021 16:58:58")
    comment1665 = Comment(videoId=537, channelId=36, content="If you like tuna and tomato sauce, try combining the two, it’s really not as bad as it sounds.", createdAt="Fri Jan 21 2022 20:58:19", updatedAt="Sun Feb 13 2022 06:05:22")
    comment1666 = Comment(videoId=442, channelId=54, content="The wake behind the boat told of the past while the open sea for told life in the unknown future.", createdAt="Thu Feb 10 2022 10:06:30", updatedAt="Thu Jul 22 2021 08:52:02")
    comment1667 = Comment(videoId=364, channelId=17, content="There aren't enough towels in the world to stop the sewage flowing from his mouth.", createdAt="Fri May 14 2021 18:37:33", updatedAt="Thu Jun 17 2021 17:59:30")
    comment1668 = Comment(videoId=144, channelId=75, content="Someone I know recently combined Maple Syrup & buttered Popcorn thinking it would taste like caramel popcorn. It didn’t and they don’t recommend anyone else do it either.", createdAt="Sat Sep 18 2021 01:32:11", updatedAt="Fri Feb 04 2022 19:31:15")
    comment1669 = Comment(videoId=531, channelId=58, content="He dreamed of eating green apples with worms.", createdAt="Sat Oct 23 2021 23:50:15", updatedAt="Tue Apr 05 2022 07:03:56")
    comment1670 = Comment(videoId=170, channelId=20, content="As the asteroid hurtled toward earth, Becky was upset her dentist appointment had been canceled.", createdAt="Mon Mar 07 2022 00:58:53", updatedAt="Sun Mar 06 2022 03:10:00")
    comment1671 = Comment(videoId=292, channelId=15, content="I've never seen a more beautiful brandy glass filled with wine.", createdAt="Fri Oct 22 2021 20:42:32", updatedAt="Fri Oct 22 2021 20:29:52")
    comment1672 = Comment(videoId=309, channelId=31, content="Iron pyrite is the most foolish of all minerals.", createdAt="Tue Jul 27 2021 20:04:59", updatedAt="Sun Apr 11 2021 02:27:28")
    comment1673 = Comment(videoId=693, channelId=62, content="A suit of armor provides excellent sun protection on hot days.", createdAt="Tue Jul 13 2021 19:32:39", updatedAt="Sun Jul 25 2021 04:18:07")
    comment1674 = Comment(videoId=685, channelId=64, content="I hear that Nancy is very pretty.", createdAt="Sat Jul 31 2021 18:34:09", updatedAt="Tue Jul 20 2021 10:23:46")
    comment1675 = Comment(videoId=18, channelId=68, content="That was how he came to win $1 million.", createdAt="Mon Aug 16 2021 00:26:44", updatedAt="Thu Jul 01 2021 12:09:58")
    comment1676 = Comment(videoId=351, channelId=21, content="Everyone says they love nature until they realize how dangerous she can be.", createdAt="Sun Jul 04 2021 11:21:51", updatedAt="Tue Nov 16 2021 13:57:04")
    comment1677 = Comment(videoId=582, channelId=23, content="The hand sanitizer was actually clear glue.", createdAt="Wed Jun 02 2021 03:04:47", updatedAt="Tue Apr 13 2021 12:51:52")
    comment1678 = Comment(videoId=533, channelId=38, content="The Guinea fowl flies through the air with all the grace of a turtle.", createdAt="Wed Sep 01 2021 03:24:43", updatedAt="Sun Jun 20 2021 05:30:08")
    comment1679 = Comment(videoId=638, channelId=96, content="As she walked along the street and looked in the gutter, she realized facemasks had become the new cigarette butts.", createdAt="Mon Mar 28 2022 11:53:34", updatedAt="Wed May 26 2021 15:25:38")
    comment1680 = Comment(videoId=213, channelId=14, content="That must be the tenth time I've been arrested for selling deep-fried cigars.", createdAt="Fri Jun 04 2021 10:53:48", updatedAt="Fri Jun 04 2021 05:38:35")
    comment1681 = Comment(videoId=481, channelId=89, content="She had a difficult time owning up to her own crazy self.", createdAt="Sat Oct 09 2021 06:21:58", updatedAt="Sat May 15 2021 01:39:51")
    comment1682 = Comment(videoId=527, channelId=26, content="Please put on these earmuffs because I can't you hear.", createdAt="Sat Oct 23 2021 21:18:24", updatedAt="Tue Feb 15 2022 13:21:00")
    comment1683 = Comment(videoId=321, channelId=90, content="It's important to remember to be aware of rampaging grizzly bears.", createdAt="Mon Jun 28 2021 01:41:07", updatedAt="Tue Aug 17 2021 00:57:07")
    comment1684 = Comment(videoId=11, channelId=69, content="I was offended by the suggestion that my baby brother was a jewel thief.", createdAt="Wed Jan 19 2022 13:17:25", updatedAt="Sun May 23 2021 00:21:15")
    comment1685 = Comment(videoId=378, channelId=17, content="The bug was having an excellent day until he hit the windshield.", createdAt="Wed Jun 30 2021 10:30:01", updatedAt="Tue Jun 08 2021 03:43:48")
    comment1686 = Comment(videoId=691, channelId=82, content="She had that tint of craziness in her soul that made her believe she could actually make a difference.", createdAt="Fri Aug 13 2021 20:48:20", updatedAt="Sat Jan 15 2022 20:59:03")
    comment1687 = Comment(videoId=572, channelId=68, content="He fumbled in the darkness looking for the light switch, but when he finally found it there was someone already there.", createdAt="Mon Nov 29 2021 19:43:43", updatedAt="Sat Sep 25 2021 02:53:23")
    comment1688 = Comment(videoId=202, channelId=99, content="The Great Dane looked more like a horse than a dog.", createdAt="Sun Mar 20 2022 16:21:33", updatedAt="Wed Apr 21 2021 12:31:04")
    comment1689 = Comment(videoId=745, channelId=38, content="The busker hoped that the people passing by would throw money, but they threw tomatoes instead, so he exchanged his hat for a juicer.", createdAt="Fri Oct 01 2021 02:55:19", updatedAt="Mon Oct 18 2021 13:46:56")
    comment1690 = Comment(videoId=273, channelId=23, content="I am happy to take your donation; any amount will be greatly appreciated.", createdAt="Sun Oct 31 2021 10:59:43", updatedAt="Wed Dec 15 2021 16:17:14")
    comment1691 = Comment(videoId=632, channelId=87, content="Everybody should read Chaucer to improve their everyday vocabulary.", createdAt="Thu Mar 31 2022 20:50:28", updatedAt="Sun Oct 10 2021 12:56:36")
    comment1692 = Comment(videoId=474, channelId=35, content="Honestly, I didn't care much for the first season, so I didn't bother with the second.", createdAt="Wed Oct 13 2021 02:10:22", updatedAt="Mon Feb 28 2022 01:54:25")
    comment1693 = Comment(videoId=279, channelId=80, content="Today arrived with a crash of my car through the garage door.", createdAt="Sat Nov 20 2021 12:47:27", updatedAt="Fri Nov 12 2021 07:58:47")
    comment1694 = Comment(videoId=663, channelId=19, content="Potato wedges probably are not best for relationships.", createdAt="Mon Dec 13 2021 14:16:19", updatedAt="Sun Oct 03 2021 02:05:46")
    comment1695 = Comment(videoId=675, channelId=94, content="He swore he just saw his sushi move.", createdAt="Mon Dec 20 2021 23:20:09", updatedAt="Tue Dec 28 2021 20:10:10")
    comment1696 = Comment(videoId=337, channelId=68, content="The Japanese yen for commerce is still well-known.", createdAt="Sat Dec 04 2021 07:32:22", updatedAt="Thu Jul 08 2021 11:37:53")
    comment1697 = Comment(videoId=318, channelId=24, content="She traveled because it cost the same as therapy and was a lot more enjoyable.", createdAt="Mon Apr 04 2022 01:53:03", updatedAt="Tue Nov 30 2021 03:26:52")
    comment1698 = Comment(videoId=125, channelId=100, content="Her life in the confines of the house became her new normal.", createdAt="Mon Aug 09 2021 09:18:48", updatedAt="Thu Jan 20 2022 06:32:01")
    comment1699 = Comment(videoId=329, channelId=73, content="I can't believe this is the eighth time I'm smashing open my piggy bank on the same day!", createdAt="Sun Sep 26 2021 04:01:38", updatedAt="Mon Aug 02 2021 06:20:42")
    comment1700 = Comment(videoId=440, channelId=86, content="He walked into the basement with the horror movie from the night before playing in his head.", createdAt="Wed Jul 28 2021 23:33:40", updatedAt="Tue Mar 29 2022 08:08:03")
    comment1701 = Comment(videoId=737, channelId=14, content="Cats are good pets, for they are clean and are not noisy.", createdAt="Mon Jun 14 2021 04:00:32", updatedAt="Thu Dec 16 2021 15:31:16")
    comment1702 = Comment(videoId=702, channelId=68, content="Boulders lined the side of the road foretelling what could come next.", createdAt="Mon May 03 2021 13:08:28", updatedAt="Thu Dec 23 2021 05:01:30")
    comment1703 = Comment(videoId=726, channelId=28, content="Random words in front of other random words create a random sentence.", createdAt="Mon Jul 12 2021 14:33:59", updatedAt="Thu Feb 03 2022 02:49:44")
    comment1704 = Comment(videoId=763, channelId=4, content="He wore the surgical mask in public not to keep from catching a virus, but to keep people away from him.", createdAt="Wed Jul 21 2021 23:14:46", updatedAt="Fri Nov 19 2021 21:57:48")
    comment1705 = Comment(videoId=171, channelId=90, content="She looked into the mirror and saw another person.", createdAt="Wed Feb 16 2022 13:12:42", updatedAt="Thu Mar 31 2022 01:41:41")
    comment1706 = Comment(videoId=93, channelId=82, content="Patricia found the meaning of life in a bowl of Cheerios.", createdAt="Sat Jun 12 2021 08:06:20", updatedAt="Sun Feb 06 2022 18:57:56")
    comment1707 = Comment(videoId=312, channelId=81, content="A good example of a useful vegetable is medicinal rhubarb.", createdAt="Sat Dec 11 2021 01:29:57", updatedAt="Tue Dec 07 2021 21:51:26")
    comment1708 = Comment(videoId=10, channelId=25, content="The shark-infested South Pine channel was the only way in or out.", createdAt="Tue Mar 01 2022 23:41:26", updatedAt="Sat Jul 03 2021 05:48:24")
    comment1709 = Comment(videoId=574, channelId=1, content="The waves were crashing on the shore; it was a lovely sight.", createdAt="Thu May 13 2021 22:42:33", updatedAt="Sun Jan 23 2022 11:52:26")
    comment1710 = Comment(videoId=448, channelId=54, content="He went back to the video to see what had been recorded and was shocked at what he saw.", createdAt="Tue Apr 27 2021 13:18:03", updatedAt="Thu Mar 17 2022 21:02:28")
    comment1711 = Comment(videoId=698, channelId=14, content="He fumbled in the darkness looking for the light switch, but when he finally found it there was someone already there.", createdAt="Tue Sep 21 2021 17:32:54", updatedAt="Sat Aug 07 2021 00:54:06")
    comment1712 = Comment(videoId=462, channelId=32, content="She had a difficult time owning up to her own crazy self.", createdAt="Fri Dec 10 2021 06:29:29", updatedAt="Thu Mar 24 2022 19:11:51")
    comment1713 = Comment(videoId=40, channelId=2, content="He didn’t want to go to the dentist, yet he went anyway.", createdAt="Fri Dec 10 2021 00:10:45", updatedAt="Wed Nov 03 2021 06:00:54")
    comment1714 = Comment(videoId=779, channelId=70, content="Plans for this weekend include turning wine into water.", createdAt="Mon Sep 13 2021 21:30:12", updatedAt="Mon Dec 06 2021 20:50:30")
    comment1715 = Comment(videoId=296, channelId=34, content="The clock within this blog and the clock on my laptop are 1 hour different from each other.", createdAt="Fri Oct 29 2021 23:10:45", updatedAt="Tue Sep 28 2021 18:37:11")
    comment1716 = Comment(videoId=723, channelId=51, content="He was an introvert that extroverts seemed to love.", createdAt="Tue Sep 21 2021 21:11:24", updatedAt="Mon Jan 10 2022 01:04:04")
    comment1717 = Comment(videoId=36, channelId=48, content="The sign said there was road work ahead so he decided to speed up.", createdAt="Mon Apr 12 2021 17:06:24", updatedAt="Mon Jan 31 2022 09:49:17")
    comment1718 = Comment(videoId=173, channelId=1, content="The shooter says goodbye to his love.", createdAt="Mon Mar 14 2022 08:12:25", updatedAt="Wed Dec 22 2021 02:17:14")
    comment1719 = Comment(videoId=735, channelId=44, content="She insisted that cleaning out your closet was the key to good driving.", createdAt="Tue May 04 2021 21:52:30", updatedAt="Sun Aug 29 2021 23:38:50")
    comment1720 = Comment(videoId=65, channelId=67, content="She was too short to see over the fence.", createdAt="Wed Nov 24 2021 23:39:48", updatedAt="Wed Jun 02 2021 21:43:08")
    comment1721 = Comment(videoId=537, channelId=41, content="The fog was so dense even a laser decided it wasn't worth the effort.", createdAt="Mon Nov 22 2021 16:31:41", updatedAt="Mon Jul 26 2021 02:41:00")
    comment1722 = Comment(videoId=638, channelId=19, content="The best key lime pie is still up for debate.", createdAt="Thu May 13 2021 18:15:45", updatedAt="Sun Oct 24 2021 11:20:21")
    comment1723 = Comment(videoId=417, channelId=12, content="I am happy to take your donation; any amount will be greatly appreciated.", createdAt="Thu Dec 23 2021 23:45:20", updatedAt="Thu Feb 17 2022 12:49:19")
    comment1724 = Comment(videoId=295, channelId=9, content="The golden retriever loved the fireworks each Fourth of July.", createdAt="Wed Jan 05 2022 05:23:17", updatedAt="Fri Jul 16 2021 23:00:55")
    comment1725 = Comment(videoId=428, channelId=1, content="The rusty nail stood erect, angled at a 45-degree angle, just waiting for the perfect barefoot to come along.", createdAt="Sat Jan 22 2022 06:19:27", updatedAt="Wed Apr 14 2021 20:45:57")
    comment1726 = Comment(videoId=299, channelId=3, content="The virus had powers none of us knew existed.", createdAt="Fri Jan 28 2022 12:53:52", updatedAt="Sat Feb 19 2022 06:51:56")
    comment1727 = Comment(videoId=215, channelId=66, content="Tomatoes make great weapons when water balloons aren’t available.", createdAt="Wed Jul 21 2021 17:33:42", updatedAt="Sat Feb 19 2022 03:40:51")
    comment1728 = Comment(videoId=655, channelId=25, content="Douglas figured the best way to succeed was to do the opposite of what he'd been doing all his life.", createdAt="Tue Jan 25 2022 13:15:28", updatedAt="Fri Aug 20 2021 16:09:16")
    comment1729 = Comment(videoId=36, channelId=1, content="Swim at your own risk was taken as a challenge for the group of Kansas City college students.", createdAt="Tue May 11 2021 20:51:31", updatedAt="Wed Jul 07 2021 17:55:07")
    comment1730 = Comment(videoId=187, channelId=68, content="The glacier came alive as the climbers hiked closer.", createdAt="Sat Jul 31 2021 07:37:07", updatedAt="Sat Feb 19 2022 08:27:02")
    comment1731 = Comment(videoId=123, channelId=52, content="It caught him off guard that space smelled of seared steak.", createdAt="Thu Jul 29 2021 03:36:24", updatedAt="Tue Dec 07 2021 18:16:16")
    comment1732 = Comment(videoId=578, channelId=34, content="The delicious aroma from the kitchen was ruined by cigarette smoke.", createdAt="Thu Mar 24 2022 01:25:11", updatedAt="Wed Apr 21 2021 05:44:08")
    comment1733 = Comment(videoId=520, channelId=66, content="I've always wanted to go to Tajikistan, but my cat would miss me.", createdAt="Thu Feb 03 2022 08:28:16", updatedAt="Sun Oct 24 2021 08:04:58")
    comment1734 = Comment(videoId=346, channelId=9, content="You bite up because of your lower jaw.", createdAt="Sun Jan 23 2022 05:47:05", updatedAt="Mon Aug 09 2021 08:26:04")
    comment1735 = Comment(videoId=337, channelId=33, content="She is never happy until she finds something to be unhappy about; then, she is overjoyed.", createdAt="Fri Oct 08 2021 15:34:58", updatedAt="Thu Mar 24 2022 20:23:14")
    comment1736 = Comment(videoId=662, channelId=93, content="The swirled lollipop had issues with the pop rock candy.", createdAt="Mon Nov 29 2021 03:04:13", updatedAt="Wed Sep 15 2021 20:09:05")
    comment1737 = Comment(videoId=519, channelId=89, content="Although it wasn't a pot of gold, Nancy was still enthralled at what she found at the end of the rainbow.", createdAt="Wed Feb 16 2022 16:52:07", updatedAt="Mon Apr 19 2021 17:16:33")
    comment1738 = Comment(videoId=365, channelId=21, content="Charles ate the french fries knowing they would be his last meal.", createdAt="Thu Mar 03 2022 21:42:34", updatedAt="Tue Dec 14 2021 06:10:20")
    comment1739 = Comment(videoId=330, channelId=37, content="She had a habit of taking showers in lemonade.", createdAt="Mon Jul 12 2021 16:56:18", updatedAt="Mon Oct 25 2021 13:15:18")
    comment1740 = Comment(videoId=556, channelId=23, content="The truth is that you pay for your lifestyle in hours.", createdAt="Fri Apr 30 2021 21:42:11", updatedAt="Wed Feb 23 2022 08:38:16")
    comment1741 = Comment(videoId=407, channelId=93, content="Nancy thought the best way to create a welcoming home was to line it with barbed wire.", createdAt="Thu Sep 02 2021 02:01:57", updatedAt="Fri Sep 24 2021 01:13:43")
    comment1742 = Comment(videoId=28, channelId=95, content="Happiness can be found in the depths of chocolate pudding.", createdAt="Tue Nov 16 2021 17:40:54", updatedAt="Sat Jan 15 2022 15:09:07")
    comment1743 = Comment(videoId=315, channelId=44, content="It's never been my responsibility to glaze the donuts.", createdAt="Sun Mar 06 2022 07:37:18", updatedAt="Mon Oct 18 2021 07:23:57")
    comment1744 = Comment(videoId=188, channelId=62, content="She was too busy always talking about what she wanted to do to actually do any of it.", createdAt="Sat Oct 30 2021 15:00:58", updatedAt="Fri Mar 11 2022 03:57:20")
    comment1745 = Comment(videoId=617, channelId=2, content="Her fragrance of choice was fresh garlic.", createdAt="Mon Jun 14 2021 09:59:25", updatedAt="Fri Aug 27 2021 11:48:16")
    comment1746 = Comment(videoId=377, channelId=48, content="Even though he thought the world was flat he didn’t see the irony of wanting to travel around the world.", createdAt="Mon Jan 03 2022 23:38:51", updatedAt="Tue Mar 29 2022 07:09:57")
    comment1747 = Comment(videoId=586, channelId=57, content="It was a slippery slope and he was willing to slide all the way to the deepest depths.", createdAt="Sat Jan 29 2022 17:12:28", updatedAt="Sun Oct 17 2021 07:04:14")
    comment1748 = Comment(videoId=412, channelId=93, content="She works two jobs to make ends meet; at least, that was her reason for not having time to join us.", createdAt="Tue Oct 05 2021 11:43:27", updatedAt="Tue Nov 30 2021 03:52:41")
    comment1749 = Comment(videoId=434, channelId=39, content="While on the first date he accidentally hit his head on the beam.", createdAt="Tue Dec 07 2021 13:19:07", updatedAt="Mon Mar 07 2022 01:47:20")
    comment1750 = Comment(videoId=440, channelId=4, content="When he asked her favorite number, she answered without hesitation that it was diamonds.", createdAt="Wed Feb 16 2022 08:45:10", updatedAt="Sat May 29 2021 06:25:55")
    comment1751 = Comment(videoId=478, channelId=69, content="Iguanas were falling out of the trees.", createdAt="Sat Sep 11 2021 21:10:03", updatedAt="Thu Dec 02 2021 13:28:54")
    comment1752 = Comment(videoId=120, channelId=2, content="Please put on these earmuffs because I can't you hear.", createdAt="Sun Jun 06 2021 06:51:33", updatedAt="Sat Mar 26 2022 01:20:15")
    comment1753 = Comment(videoId=296, channelId=47, content="He loved eating his bananas in hot dog buns.", createdAt="Thu Feb 24 2022 23:15:09", updatedAt="Fri Jun 11 2021 13:16:43")
    comment1754 = Comment(videoId=426, channelId=10, content="The heat", createdAt="Sun Jan 02 2022 10:16:54", updatedAt="Mon Jan 03 2022 08:23:11")
    comment1755 = Comment(videoId=602, channelId=4, content="It's always a good idea to seek shelter from the evil gaze of the sun.", createdAt="Sun Jul 11 2021 18:17:52", updatedAt="Mon Dec 06 2021 21:52:12")
    comment1756 = Comment(videoId=777, channelId=88, content="As he looked out the window, he saw a clown walk by.", createdAt="Sun Nov 28 2021 22:49:10", updatedAt="Mon Sep 06 2021 07:29:18")
    comment1757 = Comment(videoId=611, channelId=6, content="We have a lot of rain in June.", createdAt="Sat Jan 15 2022 18:55:55", updatedAt="Thu Jan 27 2022 09:22:17")
    comment1758 = Comment(videoId=683, channelId=61, content="It's much more difficult to play tennis with a bowling ball than it is to bowl with a tennis ball.", createdAt="Tue Mar 29 2022 02:09:43", updatedAt="Thu Nov 04 2021 08:37:48")
    comment1759 = Comment(videoId=388, channelId=34, content="Writing a list of random sentences is harder than I initially thought it would be.", createdAt="Mon Apr 26 2021 13:18:41", updatedAt="Sat May 08 2021 04:54:51")
    comment1760 = Comment(videoId=525, channelId=96, content="The crowd yells and screams for more memes.", createdAt="Fri Jun 25 2021 05:30:22", updatedAt="Thu Feb 24 2022 20:55:25")
    comment1761 = Comment(videoId=330, channelId=7, content="You're unsure whether or not to trust him, but very thankful that you wore a turtle neck.", createdAt="Sat Sep 18 2021 21:17:42", updatedAt="Sat Jan 08 2022 00:55:39")
    comment1762 = Comment(videoId=583, channelId=7, content="The father handed each child a roadmap at the beginning of the 2-day road trip and explained it was so they could find their way home.", createdAt="Mon Oct 11 2021 03:03:38", updatedAt="Thu Oct 07 2021 18:32:06")
    comment1763 = Comment(videoId=565, channelId=52, content="I always dreamed about being stranded on a desert island until it actually happened.", createdAt="Wed Oct 06 2021 04:34:36", updatedAt="Wed Nov 24 2021 08:02:14")
    comment1764 = Comment(videoId=700, channelId=5, content="People generally approve of dogs eating cat food but not cats eating dog food.", createdAt="Mon Nov 15 2021 09:55:42", updatedAt="Thu Nov 25 2021 17:19:08")
    comment1765 = Comment(videoId=249, channelId=97, content="The tree fell unexpectedly short.", createdAt="Sun Feb 20 2022 14:46:01", updatedAt="Sat Jan 22 2022 08:07:44")
    comment1766 = Comment(videoId=506, channelId=47, content="As he dangled from the rope deep inside the crevasse", createdAt="Tue Jan 04 2022 17:09:17", updatedAt="Mon Oct 25 2021 11:43:12")
    comment1767 = Comment(videoId=454, channelId=41, content="When transplanting seedlings, candied teapots will make the task easier.", createdAt="Sun Oct 10 2021 08:34:36", updatedAt="Fri Jul 23 2021 06:37:28")
    comment1768 = Comment(videoId=589, channelId=63, content="As you consider all the possible ways to improve yourself and the world, you notice John Travolta seems fairly unhappy.", createdAt="Sun Oct 10 2021 03:12:55", updatedAt="Sat Mar 05 2022 11:34:16")
    comment1769 = Comment(videoId=557, channelId=16, content="She couldn't understand why nobody else could see that the sky is full of cotton candy.", createdAt="Fri Jun 18 2021 18:04:12", updatedAt="Tue Mar 01 2022 15:47:02")
    comment1770 = Comment(videoId=310, channelId=21, content="He had a vague sense that trees gave birth to dinosaurs.", createdAt="Thu Mar 10 2022 18:02:46", updatedAt="Fri Dec 24 2021 05:36:24")
    comment1771 = Comment(videoId=377, channelId=83, content="Truth in advertising and dinosaurs with skateboards have much in common.", createdAt="Wed Mar 30 2022 00:54:32", updatedAt="Mon Aug 16 2021 03:06:51")
    comment1772 = Comment(videoId=112, channelId=38, content="The two walked down the slot canyon oblivious to the sound of thunder in the distance.", createdAt="Sat Mar 26 2022 03:15:54", updatedAt="Thu Mar 03 2022 14:10:57")
    comment1773 = Comment(videoId=515, channelId=62, content="It's a skateboarding penguin with a sunhat!", createdAt="Fri Jan 28 2022 05:45:14", updatedAt="Tue Jan 04 2022 11:12:09")
    comment1774 = Comment(videoId=634, channelId=61, content="He embraced his new life as an eggplant.", createdAt="Wed Nov 10 2021 07:00:05", updatedAt="Wed May 26 2021 13:19:24")
    comment1775 = Comment(videoId=653, channelId=78, content="He found the end of the rainbow and was surprised at what he found there.", createdAt="Thu May 27 2021 05:50:17", updatedAt="Thu Jul 01 2021 01:59:16")
    comment1776 = Comment(videoId=435, channelId=28, content="Doris enjoyed tapping her nails on the table to annoy everyone.", createdAt="Tue Nov 30 2021 16:36:14", updatedAt="Sat Jul 10 2021 06:30:53")
    comment1777 = Comment(videoId=468, channelId=67, content="His son quipped that power bars were nothing more than adult candy bars.", createdAt="Sun Sep 26 2021 02:57:55", updatedAt="Sat Oct 09 2021 16:41:04")
    comment1778 = Comment(videoId=162, channelId=69, content="He used to get confused between soldiers and shoulders, but as a military man, he now soldiers responsibility.", createdAt="Wed Feb 23 2022 20:58:43", updatedAt="Mon May 31 2021 19:58:43")
    comment1779 = Comment(videoId=25, channelId=82, content="Little Red Riding Hood decided to wear orange today.", createdAt="Wed Aug 11 2021 18:21:59", updatedAt="Sat Feb 12 2022 12:34:31")
    comment1780 = Comment(videoId=358, channelId=62, content="It was her first experience training a rainbow unicorn.", createdAt="Sat Oct 09 2021 09:00:17", updatedAt="Fri May 21 2021 20:23:44")
    comment1781 = Comment(videoId=687, channelId=28, content="She couldn't decide of the glass was half empty or half full so she drank it.", createdAt="Thu Feb 03 2022 17:55:04", updatedAt="Thu Mar 31 2022 23:41:06")
    comment1782 = Comment(videoId=448, channelId=33, content="I liked their first two albums but changed my mind after that charity gig.", createdAt="Mon Sep 13 2021 05:43:21", updatedAt="Sat Apr 24 2021 14:04:50")
    comment1783 = Comment(videoId=628, channelId=76, content="They got there early, and they got really good seats.", createdAt="Sun Apr 11 2021 08:52:45", updatedAt="Sun Nov 21 2021 13:13:36")
    comment1784 = Comment(videoId=545, channelId=76, content="Joe made the sugar cookies; Susan decorated them.", createdAt="Fri Jan 28 2022 06:35:06", updatedAt="Sun Feb 13 2022 10:19:42")
    comment1785 = Comment(videoId=772, channelId=42, content="Flying fish flew by the space station.", createdAt="Wed Mar 30 2022 18:07:17", updatedAt="Fri Aug 06 2021 11:29:31")
    comment1786 = Comment(videoId=62, channelId=23, content="The heat", createdAt="Wed Feb 23 2022 18:41:07", updatedAt="Wed Sep 15 2021 06:21:53")
    comment1787 = Comment(videoId=301, channelId=22, content="We have young kids who often walk into our room at night for various reasons including clowns in the closet.", createdAt="Thu Sep 30 2021 00:38:02", updatedAt="Tue Jun 15 2021 07:35:55")
    comment1788 = Comment(videoId=195, channelId=39, content="His confidence would have bee admirable if it wasn't for his stupidity.", createdAt="Mon Aug 16 2021 16:58:21", updatedAt="Sat Jan 01 2022 14:15:31")
    comment1789 = Comment(videoId=766, channelId=15, content="He went on a whiskey diet and immediately lost three days.", createdAt="Thu Mar 03 2022 01:34:19", updatedAt="Sun Jan 30 2022 14:29:34")
    comment1790 = Comment(videoId=312, channelId=81, content="He watched the dancing piglets with panda bear tummies in the swimming pool.", createdAt="Wed Mar 09 2022 09:19:00", updatedAt="Tue Aug 31 2021 16:29:44")
    comment1791 = Comment(videoId=15, channelId=34, content="It was at that moment that he learned there are certain parts of the body that you should never Nair.", createdAt="Sun Jan 23 2022 02:42:11", updatedAt="Mon Apr 04 2022 03:19:47")
    comment1792 = Comment(videoId=474, channelId=68, content="He poured rocks in the dungeon of his mind.", createdAt="Tue Nov 09 2021 04:07:51", updatedAt="Wed Mar 23 2022 20:43:54")
    comment1793 = Comment(videoId=362, channelId=28, content="She found it strange that people use their cellphones to actually talk to one another.", createdAt="Sat Jan 29 2022 01:10:51", updatedAt="Sun Jul 18 2021 22:29:54")
    comment1794 = Comment(videoId=463, channelId=53, content="He decided that the time had come to be stronger than any of the excuses he'd used until then.", createdAt="Sat Aug 28 2021 22:58:13", updatedAt="Tue Apr 13 2021 22:15:08")
    comment1795 = Comment(videoId=739, channelId=66, content="The worst thing about being at the top of the career ladder is that there's a long way to fall.", createdAt="Wed Mar 16 2022 14:55:26", updatedAt="Sat Mar 05 2022 07:04:56")
    comment1796 = Comment(videoId=398, channelId=61, content="It didn't take long for Gary to detect the robbers were amateurs.", createdAt="Thu Aug 19 2021 09:16:55", updatedAt="Sun Oct 24 2021 03:02:30")
    comment1797 = Comment(videoId=163, channelId=42, content="Garlic ice-cream was her favorite.", createdAt="Wed Dec 01 2021 16:10:53", updatedAt="Wed Jun 30 2021 19:37:18")
    comment1798 = Comment(videoId=380, channelId=71, content="When nobody is around, the trees gossip about the people who have walked under them.", createdAt="Mon Jan 03 2022 18:33:13", updatedAt="Mon Jul 26 2021 06:35:21")
    comment1799 = Comment(videoId=481, channelId=74, content="A dead duck doesn't fly backward.", createdAt="Mon Oct 25 2021 19:45:27", updatedAt="Mon Jan 24 2022 23:08:30")
    comment1800 = Comment(videoId=2, channelId=43, content="I caught my squirrel rustling through my gym bag.", createdAt="Tue Apr 27 2021 09:42:55", updatedAt="Mon Jun 07 2021 17:26:48")
    comment1801 = Comment(videoId=325, channelId=89, content="When he asked her favorite number, she answered without hesitation that it was diamonds.", createdAt="Sat Aug 14 2021 21:29:44", updatedAt="Wed Dec 01 2021 18:24:50")
    comment1802 = Comment(videoId=338, channelId=15, content="It's never been my responsibility to glaze the donuts.", createdAt="Thu Jul 15 2021 00:18:23", updatedAt="Tue May 11 2021 23:45:31")
    comment1803 = Comment(videoId=125, channelId=19, content="Harrold felt confident that nobody would ever suspect his spy pigeon.", createdAt="Fri Oct 15 2021 10:42:45", updatedAt="Thu Jul 08 2021 15:38:14")
    comment1804 = Comment(videoId=506, channelId=1, content="The memory we used to share is no longer coherent.", createdAt="Mon Jul 19 2021 23:21:15", updatedAt="Mon Nov 15 2021 06:54:28")
    comment1805 = Comment(videoId=5, channelId=21, content="She learned that water bottles are no longer just to hold liquid, but they're also status symbols.", createdAt="Sun Oct 17 2021 16:19:53", updatedAt="Sat Jun 26 2021 23:18:47")
    comment1806 = Comment(videoId=432, channelId=24, content="Even with the snow falling outside, she felt it appropriate to wear her bikini.", createdAt="Thu Jun 10 2021 07:29:25", updatedAt="Thu Jun 17 2021 05:13:00")
    comment1807 = Comment(videoId=615, channelId=1, content="I met an interesting turtle while the song on the radio blasted away.", createdAt="Mon Mar 28 2022 08:51:40", updatedAt="Tue Apr 27 2021 22:59:20")
    comment1808 = Comment(videoId=541, channelId=13, content="Lets all be unique together until we realise we are all the same.", createdAt="Tue Mar 29 2022 08:05:11", updatedAt="Sat Dec 18 2021 13:20:10")
    comment1809 = Comment(videoId=4, channelId=62, content="There's a reason that roses have thorns.", createdAt="Sun Mar 13 2022 18:51:29", updatedAt="Tue Dec 07 2021 02:37:27")
    comment1811 = Comment(videoId=83, channelId=38, content="The golden retriever loved the fireworks each Fourth of July.", createdAt="Thu Aug 05 2021 12:38:52", updatedAt="Thu Dec 09 2021 09:37:21")
    comment1812 = Comment(videoId=741, channelId=43, content="Lucifer was surprised at the amount of life at Death Valley.", createdAt="Mon Sep 27 2021 19:14:37", updatedAt="Tue Nov 09 2021 13:17:48")
    comment1813 = Comment(videoId=58, channelId=41, content="He swore he just saw his sushi move.", createdAt="Thu Dec 09 2021 19:30:04", updatedAt="Mon Nov 08 2021 18:50:35")
    comment1814 = Comment(videoId=531, channelId=11, content="She traveled because it cost the same as therapy and was a lot more enjoyable.", createdAt="Mon Jan 31 2022 21:04:39", updatedAt="Sat Feb 12 2022 07:41:46")
    comment1815 = Comment(videoId=630, channelId=54, content="Thirty years later, she still thought it was okay to put the toilet paper roll under rather than over.", createdAt="Mon Oct 18 2021 06:35:19", updatedAt="Sun May 30 2021 00:20:00")
    comment1816 = Comment(videoId=582, channelId=80, content="We're careful about orange ping pong balls because people might think they're fruit.", createdAt="Thu Jun 10 2021 08:12:57", updatedAt="Mon May 17 2021 20:15:59")
    comment1817 = Comment(videoId=422, channelId=58, content="Smoky the Bear secretly started the fires.", createdAt="Thu Sep 09 2021 17:20:40", updatedAt="Fri Jun 25 2021 19:06:08")
    comment1818 = Comment(videoId=432, channelId=35, content="He decided to fake his disappearance to avoid jail.", createdAt="Wed Feb 02 2022 14:12:34", updatedAt="Sun Aug 29 2021 19:03:20")
    comment1819 = Comment(videoId=548, channelId=66, content="There can never be too many cherries on an ice cream sundae.", createdAt="Tue Oct 05 2021 23:15:55", updatedAt="Sun May 09 2021 16:07:56")
    comment1820 = Comment(videoId=352, channelId=22, content="Flying fish flew by the space station.", createdAt="Mon Aug 09 2021 09:42:03", updatedAt="Wed Aug 11 2021 16:07:55")
    comment1821 = Comment(videoId=698, channelId=74, content="Please tell me you don't work in a morgue.", createdAt="Fri Dec 17 2021 18:16:48", updatedAt="Fri Apr 01 2022 19:03:53")
    comment1822 = Comment(videoId=761, channelId=27, content="They were excited to see their first sloth.", createdAt="Thu Apr 22 2021 00:28:10", updatedAt="Fri Mar 18 2022 03:07:28")
    comment1823 = Comment(videoId=714, channelId=41, content="In that instant, everything changed.", createdAt="Fri May 21 2021 02:17:32", updatedAt="Mon Jan 03 2022 00:51:42")
    comment1824 = Comment(videoId=600, channelId=75, content="He was willing to find the depths of the rabbit hole in order to be with her.", createdAt="Sun Nov 07 2021 14:44:43", updatedAt="Tue Aug 17 2021 06:56:23")
    comment1825 = Comment(videoId=219, channelId=35, content="All she wanted was the answer, but she had no idea how much she would hate it.", createdAt="Fri Jan 28 2022 17:34:23", updatedAt="Fri Jun 11 2021 16:30:20")
    comment1826 = Comment(videoId=132, channelId=19, content="The two walked down the slot canyon oblivious to the sound of thunder in the distance.", createdAt="Mon May 03 2021 14:48:34", updatedAt="Wed Feb 16 2022 16:32:44")
    comment1827 = Comment(videoId=587, channelId=59, content="Garlic ice-cream was her favorite.", createdAt="Sat Jan 08 2022 13:35:54", updatedAt="Wed Aug 18 2021 10:28:51")
    comment1828 = Comment(videoId=216, channelId=98, content="She learned that water bottles are no longer just to hold liquid, but they're also status symbols.", createdAt="Sat Oct 09 2021 14:11:28", updatedAt="Fri Dec 31 2021 15:57:44")
    comment1829 = Comment(videoId=512, channelId=76, content="She looked at the masterpiece hanging in the museum but all she could think is that her five-year-old could do better.", createdAt="Sat Oct 23 2021 19:03:26", updatedAt="Thu Feb 24 2022 11:34:06")
    comment1830 = Comment(videoId=232, channelId=85, content="The efficiency we have at removing trash has made creating trash more acceptable.", createdAt="Thu Oct 14 2021 03:02:40", updatedAt="Mon Feb 28 2022 14:02:49")
    comment1832 = Comment(videoId=240, channelId=61, content="I want a giraffe, but I'm a turtle eating waffles.", createdAt="Sun Sep 05 2021 21:47:35", updatedAt="Wed May 12 2021 01:12:24")
    comment1833 = Comment(videoId=141, channelId=30, content="The sudden rainstorm washed crocodiles into the ocean.", createdAt="Sat May 29 2021 06:22:39", updatedAt="Sat Jan 15 2022 05:41:20")
    comment1834 = Comment(videoId=563, channelId=76, content="There aren't enough towels in the world to stop the sewage flowing from his mouth.", createdAt="Tue Jan 04 2022 15:24:03", updatedAt="Tue Feb 01 2022 09:38:38")
    comment1835 = Comment(videoId=739, channelId=21, content="The waitress was not amused when he ordered green eggs and ham.", createdAt="Mon Nov 01 2021 13:57:30", updatedAt="Wed Jun 30 2021 02:20:08")
    comment1836 = Comment(videoId=210, channelId=20, content="Erin accidentally created a new universe.", createdAt="Tue Jul 27 2021 20:12:36", updatedAt="Mon Dec 13 2021 04:16:18")
    comment1837 = Comment(videoId=183, channelId=11, content="The worst thing about being at the top of the career ladder is that there's a long way to fall.", createdAt="Sat Jun 26 2021 01:16:47", updatedAt="Mon Dec 20 2021 03:04:23")
    comment1838 = Comment(videoId=641, channelId=24, content="She saw no irony asking me to change but wanting me to accept her for who she is.", createdAt="Mon Aug 09 2021 03:32:00", updatedAt="Sun Jun 20 2021 16:31:55")
    comment1839 = Comment(videoId=758, channelId=31, content="Kevin embraced his ability to be at the wrong place at the wrong time.", createdAt="Mon Aug 09 2021 21:19:33", updatedAt="Sat Nov 06 2021 15:27:06")
    comment1840 = Comment(videoId=569, channelId=61, content="Random words in front of other random words create a random sentence.", createdAt="Wed Mar 09 2022 12:42:21", updatedAt="Mon Oct 04 2021 18:15:34")
    comment1841 = Comment(videoId=172, channelId=4, content="His get rich quick scheme was to grow a cactus farm.", createdAt="Sat Mar 26 2022 20:46:42", updatedAt="Sat Jun 19 2021 20:00:37")
    comment1842 = Comment(videoId=133, channelId=75, content="The furnace repairman indicated the heating system was acting as an air conditioner.", createdAt="Thu Dec 30 2021 08:08:11", updatedAt="Sat Apr 09 2022 21:43:06")
    comment1843 = Comment(videoId=104, channelId=96, content="The tortoise jumped into the lake with dreams of becoming a sea turtle.", createdAt="Tue Sep 21 2021 00:11:49", updatedAt="Thu Jun 24 2021 19:07:59")
    comment1844 = Comment(videoId=125, channelId=10, content="The chic gangster liked to start the day with a pink scarf.", createdAt="Thu Jul 29 2021 05:43:00", updatedAt="Sat Jul 24 2021 00:59:11")
    comment1845 = Comment(videoId=512, channelId=61, content="He had reached the point where he was paranoid about being paranoid.", createdAt="Sat Aug 21 2021 22:51:01", updatedAt="Wed Sep 01 2021 13:16:28")
    comment1846 = Comment(videoId=759, channelId=10, content="When she didn’t like a guy who was trying to pick her up, she started using sign language.", createdAt="Sat Aug 21 2021 11:17:53", updatedAt="Sun Jul 11 2021 05:54:15")
    comment1847 = Comment(videoId=66, channelId=66, content="He decided to live his life by the big beats manifesto.", createdAt="Mon Apr 19 2021 14:26:29", updatedAt="Thu Apr 29 2021 13:22:13")
    comment1848 = Comment(videoId=362, channelId=62, content="Courage and stupidity were all he had.", createdAt="Tue May 25 2021 22:21:24", updatedAt="Wed Sep 22 2021 18:01:29")
    comment1849 = Comment(videoId=84, channelId=10, content="Peter found road kill an excellent way to save money on dinner.", createdAt="Tue Oct 26 2021 12:30:36", updatedAt="Sun Sep 19 2021 06:26:19")
    comment1850 = Comment(videoId=522, channelId=58, content="I met an interesting turtle while the song on the radio blasted away.", createdAt="Mon Apr 19 2021 23:45:21", updatedAt="Fri Feb 04 2022 17:14:27")
    comment1851 = Comment(videoId=254, channelId=47, content="It caught him off guard that space smelled of seared steak.", createdAt="Sat Jan 22 2022 15:26:46", updatedAt="Wed Oct 13 2021 08:54:57")
    comment1852 = Comment(videoId=759, channelId=35, content="The light in his life was actually a fire burning all around him.", createdAt="Sat Jan 29 2022 14:17:10", updatedAt="Sat Aug 07 2021 18:25:16")
    comment1853 = Comment(videoId=448, channelId=82, content="She insisted that cleaning out your closet was the key to good driving.", createdAt="Sun Nov 07 2021 08:38:32", updatedAt="Wed Jun 09 2021 15:08:58")
    comment1854 = Comment(videoId=379, channelId=82, content="Never underestimate the willingness of the greedy to throw you under the bus.", createdAt="Wed Jul 28 2021 06:37:42", updatedAt="Fri Oct 08 2021 23:54:10")
    comment1855 = Comment(videoId=347, channelId=11, content="He would only survive if he kept the fire going and he could hear thunder in the distance.", createdAt="Sat Sep 25 2021 22:19:07", updatedAt="Sun Oct 03 2021 21:16:26")
    comment1856 = Comment(videoId=172, channelId=5, content="My secretary is the only person who truly understands my stamp-collecting obsession.", createdAt="Wed Apr 14 2021 20:53:48", updatedAt="Fri Nov 19 2021 14:27:01")
    comment1857 = Comment(videoId=167, channelId=24, content="Her hair was windswept as she rode in the black convertible.", createdAt="Thu Nov 18 2021 10:56:05", updatedAt="Sat Feb 12 2022 04:21:19")
    comment1858 = Comment(videoId=194, channelId=56, content="The blinking lights of the antenna tower came into focus just as I heard a loud snap.", createdAt="Sun Oct 31 2021 18:31:31", updatedAt="Thu Mar 10 2022 18:32:54")
    comment1859 = Comment(videoId=389, channelId=71, content="Henry couldn't decide if he was an auto mechanic or a priest.", createdAt="Sat Jul 10 2021 04:47:38", updatedAt="Tue Oct 19 2021 04:37:15")
    comment1860 = Comment(videoId=579, channelId=8, content="She moved forward only because she trusted that the ending she now was going through must be followed by a new beginning.", createdAt="Tue Feb 08 2022 08:00:14", updatedAt="Sat Jul 10 2021 09:59:58")
    comment1862 = Comment(videoId=715, channelId=70, content="Yeah, I think it's a good environment for learning English.", createdAt="Sun Oct 31 2021 00:53:58", updatedAt="Fri Feb 04 2022 06:20:13")
    comment1863 = Comment(videoId=55, channelId=100, content="The Guinea fowl flies through the air with all the grace of a turtle.", createdAt="Mon Aug 16 2021 08:15:09", updatedAt="Mon Sep 13 2021 17:08:57")
    comment1864 = Comment(videoId=122, channelId=23, content="The virus had powers none of us knew existed.", createdAt="Fri Apr 01 2022 22:02:13", updatedAt="Mon Mar 28 2022 01:08:20")
    comment1865 = Comment(videoId=708, channelId=92, content="Buried deep in the snow, he hoped his batteries were fresh in his avalanche beacon.", createdAt="Sun Dec 19 2021 07:31:23", updatedAt="Sat May 08 2021 21:37:05")
    comment1866 = Comment(videoId=542, channelId=6, content="Nobody questions who built the pyramids in Mexico.", createdAt="Tue Jun 01 2021 05:09:26", updatedAt="Fri Apr 23 2021 06:18:53")
    comment1867 = Comment(videoId=683, channelId=46, content="The bullet pierced the window shattering it before missing Danny's head by mere millimeters.", createdAt="Fri Mar 18 2022 15:38:18", updatedAt="Wed Oct 13 2021 20:39:32")
    comment1868 = Comment(videoId=142, channelId=84, content="Her daily goal was to improve on yesterday.", createdAt="Tue Oct 26 2021 05:36:14", updatedAt="Mon Nov 01 2021 04:55:46")
    comment1869 = Comment(videoId=258, channelId=31, content="My dentist tells me that chewing bricks is very bad for your teeth.", createdAt="Sun May 16 2021 22:00:55", updatedAt="Sat Jul 10 2021 19:17:51")
    comment1870 = Comment(videoId=712, channelId=98, content="Behind the window was a reflection that only instilled fear.", createdAt="Fri Jul 09 2021 18:31:19", updatedAt="Fri Dec 17 2021 04:36:22")
    comment1871 = Comment(videoId=267, channelId=59, content="Grape jelly was leaking out the hole in the roof.", createdAt="Sun Dec 26 2021 03:41:00", updatedAt="Sun Dec 19 2021 11:06:59")
    comment1872 = Comment(videoId=702, channelId=58, content="He had a wall full of masks so she could wear a different face every day.", createdAt="Wed Jun 23 2021 13:29:58", updatedAt="Mon Jan 24 2022 19:57:28")
    comment1873 = Comment(videoId=399, channelId=94, content="I was offended by the suggestion that my baby brother was a jewel thief.", createdAt="Fri Feb 04 2022 08:17:51", updatedAt="Wed Apr 14 2021 11:22:49")
    comment1874 = Comment(videoId=395, channelId=3, content="While all her friends were positive that Mary had a sixth sense, she knew she actually had a seventh sense.", createdAt="Mon Nov 08 2021 10:21:24", updatedAt="Mon Mar 07 2022 19:03:46")
    comment1875 = Comment(videoId=327, channelId=40, content="The father handed each child a roadmap at the beginning of the 2-day road trip and explained it was so they could find their way home.", createdAt="Tue Apr 13 2021 14:00:00", updatedAt="Tue Dec 14 2021 09:30:42")
    comment1876 = Comment(videoId=288, channelId=17, content="The Great Dane looked more like a horse than a dog.", createdAt="Mon Oct 18 2021 12:57:50", updatedAt="Wed Feb 16 2022 17:45:29")
    comment1877 = Comment(videoId=470, channelId=5, content="Toddlers feeding raccoons surprised even the seasoned park ranger.", createdAt="Sat Oct 02 2021 03:00:54", updatedAt="Mon Oct 25 2021 11:32:50")
    comment1878 = Comment(videoId=341, channelId=93, content="He wondered if it could be called a beach if there was no sand.", createdAt="Fri Sep 24 2021 20:16:51", updatedAt="Sun Nov 28 2021 04:25:04")
    comment1879 = Comment(videoId=590, channelId=88, content="The tumbleweed refused to tumble but was more than willing to prance.", createdAt="Sat Jun 19 2021 14:24:04", updatedAt="Wed Jan 26 2022 05:23:51")
    comment1880 = Comment(videoId=169, channelId=16, content="They got there early, and they got really good seats.", createdAt="Wed May 19 2021 14:31:14", updatedAt="Sun Jan 23 2022 04:13:57")
    comment1881 = Comment(videoId=418, channelId=79, content="He quietly entered the museum as the super bowl started.", createdAt="Sat Dec 18 2021 01:27:07", updatedAt="Thu Sep 16 2021 22:03:03")
    comment1882 = Comment(videoId=411, channelId=2, content="Lucifer was surprised at the amount of life at Death Valley.", createdAt="Mon Dec 27 2021 20:23:42", updatedAt="Fri Dec 03 2021 12:13:38")
    comment1883 = Comment(videoId=501, channelId=42, content="The delicious aroma from the kitchen was ruined by cigarette smoke.", createdAt="Sun Jul 04 2021 20:46:18", updatedAt="Mon Oct 18 2021 10:22:43")
    comment1885 = Comment(videoId=485, channelId=52, content="Courage and stupidity were all he had.", createdAt="Tue Nov 02 2021 06:22:50", updatedAt="Fri Feb 04 2022 18:35:54")
    comment1886 = Comment(videoId=691, channelId=47, content="It didn't take long for Gary to detect the robbers were amateurs.", createdAt="Thu May 20 2021 07:39:12", updatedAt="Fri Dec 03 2021 07:47:25")
    comment1887 = Comment(videoId=7, channelId=25, content="Bill ran from the giraffe toward the dolphin.", createdAt="Mon Mar 21 2022 12:54:49", updatedAt="Thu Nov 25 2021 12:25:57")
    comment1888 = Comment(videoId=63, channelId=24, content="The efficiency with which he paired the socks in the drawer was quite admirable.", createdAt="Fri Mar 11 2022 18:49:36", updatedAt="Fri Feb 18 2022 06:21:59")
    comment1889 = Comment(videoId=527, channelId=62, content="The toy brought back fond memories of being lost in the rain forest.", createdAt="Sun Oct 17 2021 03:15:43", updatedAt="Fri Sep 24 2021 20:34:06")
    comment1890 = Comment(videoId=354, channelId=95, content="In hopes of finding out the truth, he entered the one-room library.", createdAt="Fri Mar 04 2022 02:26:00", updatedAt="Wed Mar 02 2022 02:45:37")
    comment1891 = Comment(videoId=627, channelId=7, content="I’m working on a sweet potato farm.", createdAt="Sat Feb 05 2022 16:36:52", updatedAt="Wed Sep 01 2021 08:37:14")
    comment1892 = Comment(videoId=387, channelId=92, content="The urgent care center was flooded with patients after the news of a new deadly virus was made public.", createdAt="Mon Nov 29 2021 12:17:58", updatedAt="Fri Oct 01 2021 21:11:13")
    comment1893 = Comment(videoId=306, channelId=88, content="Iron pyrite is the most foolish of all minerals.", createdAt="Sun Sep 19 2021 10:44:18", updatedAt="Fri Nov 19 2021 04:15:38")
    comment1894 = Comment(videoId=524, channelId=15, content="No matter how beautiful the sunset, it saddened her knowing she was one day older.", createdAt="Sun Sep 12 2021 04:11:31", updatedAt="Mon Oct 18 2021 09:22:00")
    comment1895 = Comment(videoId=65, channelId=69, content="Nancy thought the best way to create a welcoming home was to line it with barbed wire.", createdAt="Sat May 01 2021 15:00:10", updatedAt="Sat Nov 27 2021 04:31:00")
    comment1896 = Comment(videoId=159, channelId=68, content="The elderly neighborhood became enraged over the coyotes who had been blamed for the poodle’s disappearance.", createdAt="Tue Dec 28 2021 13:03:23", updatedAt="Wed Apr 21 2021 00:21:35")
    comment1897 = Comment(videoId=443, channelId=38, content="At last", createdAt="Wed Mar 02 2022 21:21:51", updatedAt="Wed Aug 18 2021 06:11:19")
    comment1898 = Comment(videoId=63, channelId=33, content="That must be the tenth time I've been arrested for selling deep-fried cigars.", createdAt="Sun Jul 18 2021 22:58:24", updatedAt="Fri Feb 25 2022 07:03:15")
    comment1899 = Comment(videoId=457, channelId=94, content="When he had to picnic on the beach, he purposely put sand in other people’s food.", createdAt="Sat Jul 17 2021 16:45:17", updatedAt="Fri May 07 2021 13:32:30")
    comment1900 = Comment(videoId=574, channelId=81, content="We have young kids who often walk into our room at night for various reasons including clowns in the closet.", createdAt="Sun Aug 29 2021 04:52:41", updatedAt="Thu Jun 10 2021 04:26:18")
    comment1901 = Comment(videoId=7, channelId=54, content="Dan took the deep dive down the rabbit hole.", createdAt="Thu Sep 09 2021 20:52:06", updatedAt="Mon Oct 25 2021 03:46:55")
    comment1902 = Comment(videoId=356, channelId=87, content="The river stole the gods.", createdAt="Tue Jul 13 2021 21:15:27", updatedAt="Tue Dec 28 2021 17:36:29")
    comment1903 = Comment(videoId=424, channelId=57, content="There's a message for you if you look up.", createdAt="Mon Feb 21 2022 18:24:27", updatedAt="Fri Sep 10 2021 12:24:55")
    comment1904 = Comment(videoId=160, channelId=62, content="He enjoys practicing his ballet in the bathroom.", createdAt="Sun Jun 27 2021 07:05:59", updatedAt="Fri Dec 31 2021 13:14:54")
    comment1905 = Comment(videoId=333, channelId=98, content="Random words in front of other random words create a random sentence.", createdAt="Mon Dec 20 2021 21:21:41", updatedAt="Fri Jan 14 2022 05:46:13")
    comment1906 = Comment(videoId=413, channelId=90, content="She could hear him in the shower singing with a joy she hoped he'd retain after she delivered the news.", createdAt="Sat Aug 28 2021 10:15:23", updatedAt="Fri Oct 08 2021 14:07:19")
    comment1907 = Comment(videoId=314, channelId=92, content="The worst thing about being at the top of the career ladder is that there's a long way to fall.", createdAt="Mon Aug 09 2021 01:10:21", updatedAt="Sun Jul 25 2021 10:52:29")
    comment1908 = Comment(videoId=435, channelId=42, content="He was so preoccupied with whether or not he could that he failed to stop to consider if he should.", createdAt="Sat Oct 16 2021 13:34:23", updatedAt="Mon Mar 07 2022 22:16:04")
    comment1909 = Comment(videoId=319, channelId=2, content="My uncle's favorite pastime was building cars out of noodles.", createdAt="Mon Aug 09 2021 00:43:30", updatedAt="Sat Sep 25 2021 18:12:23")
    comment1910 = Comment(videoId=597, channelId=94, content="Everyone was curious about the large white blimp that appeared overnight.", createdAt="Wed Mar 30 2022 18:13:17", updatedAt="Tue Feb 15 2022 20:46:28")
    comment1911 = Comment(videoId=304, channelId=92, content="I am happy to take your donation; any amount will be greatly appreciated.", createdAt="Fri Jun 25 2021 06:14:41", updatedAt="Thu Jul 08 2021 02:08:42")
    comment1912 = Comment(videoId=763, channelId=25, content="Thigh-high in the water, the fisherman’s hope for dinner soon turned to despair.", createdAt="Fri Nov 05 2021 23:21:11", updatedAt="Sun Mar 13 2022 10:42:05")
    comment1913 = Comment(videoId=77, channelId=90, content="Shakespeare was a famous 17th-century diesel mechanic.", createdAt="Tue Feb 15 2022 05:10:00", updatedAt="Fri Mar 25 2022 04:57:20")
    comment1914 = Comment(videoId=325, channelId=20, content="I would be delighted if the sea were full of cucumber juice.", createdAt="Thu Aug 19 2021 11:53:43", updatedAt="Fri Dec 03 2021 02:22:34")
    comment1915 = Comment(videoId=459, channelId=17, content="They improved dramatically once the lead singer left.", createdAt="Fri Mar 18 2022 03:39:21", updatedAt="Fri Mar 18 2022 14:08:06")
    comment1916 = Comment(videoId=458, channelId=56, content="Watching the geriatric men’s softball team brought back memories of 3 yr olds playing t-ball.", createdAt="Thu Oct 14 2021 15:57:52", updatedAt="Fri Oct 01 2021 00:09:43")
    comment1917 = Comment(videoId=515, channelId=20, content="The lyrics of the song sounded like fingernails on a chalkboard.", createdAt="Wed Dec 22 2021 13:05:10", updatedAt="Sun May 09 2021 08:07:17")
    comment1918 = Comment(videoId=689, channelId=67, content="With a single flip of the coin, his life changed forever.", createdAt="Mon Oct 11 2021 01:42:29", updatedAt="Thu Dec 09 2021 13:25:14")
    comment1919 = Comment(videoId=390, channelId=92, content="I trust everything that's written in purple ink.", createdAt="Sun Jan 09 2022 00:22:20", updatedAt="Fri Feb 25 2022 18:50:20")
    comment1920 = Comment(videoId=659, channelId=61, content="I became paranoid that the school of jellyfish was spying on me.", createdAt="Thu Nov 04 2021 01:01:42", updatedAt="Fri Sep 03 2021 06:39:12")
    comment1921 = Comment(videoId=617, channelId=14, content="It was always dangerous to drive with him since he insisted the safety cones were a slalom course.", createdAt="Fri Jan 28 2022 20:20:00", updatedAt="Thu Dec 02 2021 01:16:06")
    comment1922 = Comment(videoId=239, channelId=76, content="It's never been my responsibility to glaze the donuts.", createdAt="Sun Jan 02 2022 15:45:29", updatedAt="Fri Feb 11 2022 07:08:10")
    comment1924 = Comment(videoId=354, channelId=7, content="The fish dreamed of escaping the fishbowl and into the toilet where he saw his friend go.", createdAt="Sat May 08 2021 15:20:36", updatedAt="Sat Jan 22 2022 15:43:36")
    comment1925 = Comment(videoId=463, channelId=83, content="It didn't make sense unless you had the power to eat colors.", createdAt="Sat Sep 04 2021 21:03:13", updatedAt="Sat Aug 21 2021 16:13:59")
    comment1926 = Comment(videoId=111, channelId=23, content="I hear that Nancy is very pretty.", createdAt="Wed Dec 29 2021 03:43:27", updatedAt="Wed Dec 22 2021 11:57:38")
    comment1927 = Comment(videoId=130, channelId=39, content="Toddlers feeding raccoons surprised even the seasoned park ranger.", createdAt="Tue Dec 28 2021 21:51:51", updatedAt="Sun Jun 27 2021 14:10:06")
    comment1928 = Comment(videoId=623, channelId=81, content="It's important to remember to be aware of rampaging grizzly bears.", createdAt="Tue Jan 11 2022 15:13:55", updatedAt="Mon Jul 19 2021 12:25:55")
    comment1929 = Comment(videoId=712, channelId=81, content="I want more detailed information.", createdAt="Mon May 24 2021 23:46:20", updatedAt="Sun Sep 26 2021 03:32:16")
    comment1930 = Comment(videoId=175, channelId=4, content="Yeah, I think it's a good environment for learning English.", createdAt="Thu Jan 27 2022 03:16:49", updatedAt="Mon Apr 04 2022 13:55:50")
    comment1931 = Comment(videoId=116, channelId=57, content="The chic gangster liked to start the day with a pink scarf.", createdAt="Sun Nov 21 2021 07:30:30", updatedAt="Tue Jun 22 2021 13:10:14")
    comment1932 = Comment(videoId=19, channelId=9, content="He had decided to accept his fate of accepting his fate.", createdAt="Tue Nov 02 2021 21:00:56", updatedAt="Fri Aug 27 2021 18:59:31")
    comment1933 = Comment(videoId=171, channelId=90, content="This is a Japanese doll.", createdAt="Thu Feb 03 2022 07:21:01", updatedAt="Sat Oct 09 2021 18:06:25")
    comment1934 = Comment(videoId=339, channelId=41, content="There is no better feeling than staring at a wall with closed eyes.", createdAt="Fri Jul 09 2021 11:11:46", updatedAt="Sat Oct 02 2021 07:29:00")
    comment1935 = Comment(videoId=438, channelId=11, content="Iron pyrite is the most foolish of all minerals.", createdAt="Thu Apr 15 2021 10:59:30", updatedAt="Thu Feb 17 2022 08:02:19")
    comment1936 = Comment(videoId=34, channelId=59, content="If any cop asks you where you were, just say you were visiting Kansas.", createdAt="Wed May 26 2021 15:51:36", updatedAt="Sat Aug 21 2021 16:53:54")
    comment1937 = Comment(videoId=512, channelId=79, content="Two seats were vacant.", createdAt="Wed May 05 2021 19:27:41", updatedAt="Wed Apr 21 2021 12:28:40")
    comment1938 = Comment(videoId=236, channelId=35, content="If my calculator had a history, it would be more embarrassing than my browser history.", createdAt="Mon Apr 04 2022 05:59:19", updatedAt="Fri Dec 17 2021 05:57:26")
    comment1939 = Comment(videoId=178, channelId=85, content="It took him a while to realize that everything he decided not to change, he was actually choosing.", createdAt="Mon Mar 28 2022 17:49:05", updatedAt="Sat Nov 13 2021 18:33:03")
    comment1940 = Comment(videoId=725, channelId=62, content="The father handed each child a roadmap at the beginning of the 2-day road trip and explained it was so they could find their way home.", createdAt="Fri Dec 03 2021 22:48:02", updatedAt="Thu Aug 05 2021 08:34:58")
    comment1941 = Comment(videoId=34, channelId=34, content="At that moment she realized she had a sixth sense.", createdAt="Sat Apr 24 2021 14:03:47", updatedAt="Fri Jan 14 2022 10:58:56")
    comment1942 = Comment(videoId=577, channelId=15, content="It isn't true that my mattress is made of cotton candy.", createdAt="Mon Jul 05 2021 23:36:20", updatedAt="Wed Jul 21 2021 08:22:00")
    comment1943 = Comment(videoId=749, channelId=53, content="I'm not a party animal, but I do like animal parties.", createdAt="Mon May 17 2021 01:17:43", updatedAt="Fri Apr 16 2021 18:15:40")
    comment1944 = Comment(videoId=477, channelId=67, content="We have never been to Asia, nor have we visited Africa.", createdAt="Tue Mar 22 2022 01:33:47", updatedAt="Sun Aug 22 2021 12:19:12")
    comment1945 = Comment(videoId=344, channelId=96, content="At that moment he wasn't listening to music, he was living an experience.", createdAt="Wed Nov 24 2021 18:57:52", updatedAt="Wed Jan 19 2022 20:15:43")
    comment1946 = Comment(videoId=469, channelId=9, content="I thought red would have felt warmer in summer but I didn't think about the equator.", createdAt="Mon Jan 17 2022 15:26:51", updatedAt="Tue Sep 21 2021 21:50:16")
    comment1947 = Comment(videoId=697, channelId=92, content="After exploring the abandoned building, he started to believe in ghosts.", createdAt="Mon Apr 04 2022 12:27:55", updatedAt="Tue Dec 07 2021 13:18:56")
    comment1948 = Comment(videoId=321, channelId=16, content="Traveling became almost extinct during the pandemic.", createdAt="Mon Feb 21 2022 17:13:49", updatedAt="Tue Aug 10 2021 10:16:23")
    comment1949 = Comment(videoId=185, channelId=99, content="This is the last random sentence I will be writing and I am going to stop mid-sent", createdAt="Sun Sep 12 2021 04:40:52", updatedAt="Sat May 08 2021 07:34:46")
    comment1950 = Comment(videoId=694, channelId=5, content="He stepped gingerly onto the bridge knowing that enchantment awaited on the other side.", createdAt="Sun Sep 05 2021 04:36:11", updatedAt="Sun Dec 05 2021 12:16:07")
    comment1951 = Comment(videoId=436, channelId=46, content="100 years old is such a young age if you happen to be a bristlecone pine.", createdAt="Mon Nov 29 2021 17:47:30", updatedAt="Sat Jul 31 2021 01:15:25")
    comment1952 = Comment(videoId=600, channelId=68, content="They say that dogs are man's best friend, but this cat was setting out to sabotage that theory.", createdAt="Wed Jan 12 2022 03:41:30", updatedAt="Thu Jan 20 2022 05:28:41")
    comment1953 = Comment(videoId=750, channelId=22, content="his seven-layer cake only had six layers.", createdAt="Thu May 27 2021 21:06:43", updatedAt="Tue Jul 20 2021 18:39:25")
    comment1954 = Comment(videoId=487, channelId=25, content="He found rain fascinating yet unpleasant.", createdAt="Fri Dec 17 2021 03:12:04", updatedAt="Fri Sep 03 2021 05:10:10")
    comment1955 = Comment(videoId=95, channelId=38, content="It was her first experience training a rainbow unicorn.", createdAt="Mon Jun 21 2021 03:05:33", updatedAt="Mon Feb 14 2022 13:23:50")
    comment1956 = Comment(videoId=739, channelId=45, content="Nobody has encountered an explosive daisy and lived to tell the tale.", createdAt="Fri Oct 01 2021 12:22:46", updatedAt="Mon Apr 04 2022 08:02:11")
    comment1957 = Comment(videoId=549, channelId=61, content="Don't put peanut butter on the dog's nose.", createdAt="Sun Sep 05 2021 09:07:44", updatedAt="Mon Apr 04 2022 14:44:39")
    comment1958 = Comment(videoId=385, channelId=75, content="He fumbled in the darkness looking for the light switch, but when he finally found it there was someone already there.", createdAt="Mon May 10 2021 04:21:00", updatedAt="Tue Apr 05 2022 09:41:40")
    comment1959 = Comment(videoId=670, channelId=57, content="The pigs were insulted that they were named hamburgers.", createdAt="Fri Oct 08 2021 01:55:54", updatedAt="Fri Jun 11 2021 03:15:26")
    comment1960 = Comment(videoId=702, channelId=94, content="There were three sphered rocks congregating in a cubed room.", createdAt="Sun Oct 31 2021 02:25:25", updatedAt="Mon Jan 24 2022 19:14:04")
    comment1961 = Comment(videoId=25, channelId=82, content="The anaconda was the greatest criminal mastermind in this part of the neighborhood.", createdAt="Thu Sep 02 2021 04:10:37", updatedAt="Thu Oct 14 2021 09:49:04")
    comment1962 = Comment(videoId=714, channelId=94, content="Tom got a small piece of pie.", createdAt="Mon May 17 2021 16:17:12", updatedAt="Fri Sep 10 2021 05:25:18")
    comment1963 = Comment(videoId=385, channelId=5, content="Everybody should read Chaucer to improve their everyday vocabulary.", createdAt="Fri Sep 24 2021 14:48:52", updatedAt="Mon Nov 22 2021 04:30:37")
    comment1964 = Comment(videoId=31, channelId=25, content="The thick foliage and intertwined vines made the hike nearly impossible.", createdAt="Tue Dec 21 2021 20:11:10", updatedAt="Fri Sep 03 2021 05:23:46")
    comment1965 = Comment(videoId=397, channelId=38, content="The crowd yells and screams for more memes.", createdAt="Sun Nov 21 2021 17:01:26", updatedAt="Thu Jun 03 2021 06:28:44")
    comment1966 = Comment(videoId=616, channelId=57, content="He was the only member of the club who didn't like plum pudding.", createdAt="Fri Feb 25 2022 10:10:23", updatedAt="Wed Oct 20 2021 21:51:12")
    comment1968 = Comment(videoId=585, channelId=72, content="The sudden rainstorm washed crocodiles into the ocean.", createdAt="Wed Apr 21 2021 16:54:41", updatedAt="Tue Jan 25 2022 03:28:59")
    comment1969 = Comment(videoId=133, channelId=95, content="There have been days when I wished to be separated from my body, but today wasn’t one of those days.", createdAt="Fri Jun 11 2021 18:07:52", updatedAt="Sun Jul 04 2021 09:54:36")
    comment1970 = Comment(videoId=154, channelId=20, content="Nobody loves a pig wearing lipstick.", createdAt="Thu Oct 14 2021 03:04:00", updatedAt="Mon May 24 2021 03:57:40")
    comment1971 = Comment(videoId=303, channelId=14, content="The estate agent quickly marked out his territory on the dance floor.", createdAt="Thu Jul 22 2021 22:00:31", updatedAt="Thu Oct 28 2021 13:29:07")
    comment1972 = Comment(videoId=534, channelId=67, content="She was too busy always talking about what she wanted to do to actually do any of it.", createdAt="Thu Jun 17 2021 08:29:55", updatedAt="Thu Dec 16 2021 18:24:01")
    comment1973 = Comment(videoId=262, channelId=1, content="Nothing seemed out of place except the washing machine in the bar.", createdAt="Wed Aug 11 2021 23:50:39", updatedAt="Thu Jul 15 2021 04:36:05")
    comment1974 = Comment(videoId=215, channelId=11, content="The paintbrush was angry at the color the artist chose to use.", createdAt="Tue Aug 24 2021 14:30:21", updatedAt="Sun Apr 03 2022 18:47:23")
    comment1975 = Comment(videoId=201, channelId=83, content="A quiet house is nice until you are ordered to stay in it for months.", createdAt="Thu Aug 19 2021 13:41:42", updatedAt="Wed Aug 11 2021 01:50:21")
    comment1976 = Comment(videoId=241, channelId=52, content="He played the game as if his life depended on it and the truth was that it did.", createdAt="Tue Jun 15 2021 12:01:12", updatedAt="Sat Apr 09 2022 20:25:51")
    comment1977 = Comment(videoId=590, channelId=27, content="Giving directions that the mountains are to the west only works when you can see them.", createdAt="Thu Jan 20 2022 00:21:37", updatedAt="Thu Oct 14 2021 23:03:59")
    comment1978 = Comment(videoId=358, channelId=55, content="There were white out conditions in the town; subsequently, the roads were impassable.", createdAt="Sat Aug 21 2021 17:14:02", updatedAt="Thu Dec 09 2021 06:34:21")
    comment1979 = Comment(videoId=294, channelId=47, content="Don't put peanut butter on the dog's nose.", createdAt="Sun Nov 14 2021 23:54:56", updatedAt="Mon Dec 06 2021 19:48:30")
    comment1980 = Comment(videoId=240, channelId=98, content="Be careful with that butter knife.", createdAt="Fri May 28 2021 18:53:03", updatedAt="Fri Dec 10 2021 22:26:06")
    comment1981 = Comment(videoId=430, channelId=7, content="He was surprised that his immense laziness was inspirational to others.", createdAt="Sun Aug 29 2021 14:49:18", updatedAt="Fri Aug 13 2021 18:28:29")
    comment1982 = Comment(videoId=284, channelId=74, content="Everyone was curious about the large white blimp that appeared overnight.", createdAt="Sun Oct 24 2021 21:36:23", updatedAt="Wed Nov 24 2021 08:31:01")
    comment1983 = Comment(videoId=164, channelId=74, content="Please wait outside of the house.", createdAt="Thu Sep 09 2021 07:15:28", updatedAt="Sun Feb 20 2022 02:33:50")
    comment1984 = Comment(videoId=133, channelId=15, content="The toy brought back fond memories of being lost in the rain forest.", createdAt="Tue Apr 20 2021 00:42:01", updatedAt="Tue Apr 27 2021 03:12:36")
    comment1985 = Comment(videoId=201, channelId=59, content="They wandered into a strange Tiki bar on the edge of the small beach town.", createdAt="Mon Nov 15 2021 13:07:49", updatedAt="Wed Mar 02 2022 09:32:02")
    comment1986 = Comment(videoId=751, channelId=58, content="Not all people who wander are lost.", createdAt="Sun Mar 06 2022 16:50:47", updatedAt="Tue Aug 17 2021 23:09:42")
    comment1987 = Comment(videoId=251, channelId=35, content="She discovered van life is difficult with 2 cats and a dog.", createdAt="Sat Apr 24 2021 06:46:40", updatedAt="Thu Sep 30 2021 13:24:49")
    comment1988 = Comment(videoId=145, channelId=80, content="A good example of a useful vegetable is medicinal rhubarb.", createdAt="Thu Feb 24 2022 10:20:08", updatedAt="Sun Aug 29 2021 03:06:27")
    comment1990 = Comment(videoId=216, channelId=47, content="Everyone pretends to like wheat until you mention barley.", createdAt="Fri Oct 15 2021 21:38:13", updatedAt="Thu Sep 30 2021 21:25:44")
    comment1991 = Comment(videoId=283, channelId=70, content="I only enjoy window shopping when the windows are transparent.", createdAt="Sat May 22 2021 14:20:56", updatedAt="Tue Sep 07 2021 09:02:00")
    comment1992 = Comment(videoId=602, channelId=7, content="People who insist on picking their teeth with their elbows are so annoying!", createdAt="Sun Sep 05 2021 06:35:50", updatedAt="Fri Mar 18 2022 23:25:27")
    comment1993 = Comment(videoId=161, channelId=23, content="The sunblock was handed to the girl before practice, but the burned skin was proof she did not apply it.", createdAt="Tue Jun 08 2021 01:16:42", updatedAt="Tue Feb 15 2022 05:12:23")
    comment1994 = Comment(videoId=236, channelId=26, content="It didn't take long for Gary to detect the robbers were amateurs.", createdAt="Tue Apr 20 2021 14:00:52", updatedAt="Wed Feb 09 2022 23:32:00")
    comment1995 = Comment(videoId=554, channelId=32, content="He is good at eating pickles and telling women about his emotional problems.", createdAt="Thu Nov 11 2021 07:02:23", updatedAt="Mon Jun 21 2021 13:32:48")
    comment1996 = Comment(videoId=317, channelId=89, content="The most exciting eureka moment I've had was when I realized that the instructions on food packets were just guidelines.", createdAt="Tue Sep 21 2021 07:55:57", updatedAt="Fri Jul 23 2021 10:13:05")
    comment1997 = Comment(videoId=128, channelId=50, content="The fish dreamed of escaping the fishbowl and into the toilet where he saw his friend go.", createdAt="Sat Feb 26 2022 04:14:15", updatedAt="Wed Mar 09 2022 14:24:39")
    comment1998 = Comment(videoId=61, channelId=79, content="The minute she landed she understood the reason this was a fly-over state.", createdAt="Fri Mar 25 2022 09:03:04", updatedAt="Sat May 01 2021 16:02:01")
    comment1999 = Comment(videoId=18, channelId=39, content="She always speaks to him in a loud voice.", createdAt="Mon Dec 13 2021 06:06:05", updatedAt="Tue Aug 10 2021 20:41:54")
    comment2000 = Comment(videoId=192, channelId=85, content="I was very proud of my nickname throughout high school but today- I couldn’t be any different to what my nickname was.", createdAt="Fri Mar 25 2022 17:26:46", updatedAt="Mon Jan 24 2022 21:50:25")
    comment2001 = Comment(videoId=216, channelId=36, content="She moved forward only because she trusted that the ending she now was going through must be followed by a new beginning.", createdAt="Tue Oct 19 2021 04:58:23", updatedAt="Wed Aug 18 2021 14:50:40")
    comment2002 = Comment(videoId=148, channelId=72, content="Potato wedges probably are not best for relationships.", createdAt="Mon Nov 22 2021 16:17:57", updatedAt="Mon Jul 26 2021 00:07:34")
    comment2003 = Comment(videoId=747, channelId=3, content="The teenage boy was accused of breaking his arm simply to get out of the test.", createdAt="Thu Feb 03 2022 04:56:25", updatedAt="Mon May 03 2021 04:33:57")
    comment2004 = Comment(videoId=208, channelId=9, content="He kept telling himself that one day it would all somehow make sense.", createdAt="Fri Nov 19 2021 20:36:56", updatedAt="Mon Aug 23 2021 09:25:01")
    comment2006 = Comment(videoId=268, channelId=85, content="My secretary is the only person who truly understands my stamp-collecting obsession.", createdAt="Sat Jun 05 2021 16:39:27", updatedAt="Mon Jun 21 2021 23:23:15")
    comment2007 = Comment(videoId=351, channelId=84, content="They say that dogs are man's best friend, but this cat was setting out to sabotage that theory.", createdAt="Mon Jan 10 2022 19:43:29", updatedAt="Thu Jul 15 2021 14:21:22")
    comment2009 = Comment(videoId=419, channelId=95, content="My uncle's favorite pastime was building cars out of noodles.", createdAt="Fri Oct 15 2021 22:16:12", updatedAt="Sat May 01 2021 20:56:14")
    comment2010 = Comment(videoId=473, channelId=31, content="On each full moon", createdAt="Sat Oct 16 2021 05:34:32", updatedAt="Mon Feb 28 2022 18:21:21")
    comment2011 = Comment(videoId=394, channelId=99, content="The teens wondered what was kept in the red shed on the far edge of the school grounds.", createdAt="Sat Jul 17 2021 08:08:48", updatedAt="Fri Nov 26 2021 07:48:37")
    comment2012 = Comment(videoId=778, channelId=17, content="The small white buoys marked the location of hundreds of crab pots.", createdAt="Sun Dec 05 2021 08:01:49", updatedAt="Sun Aug 01 2021 23:38:50")
    comment2013 = Comment(videoId=378, channelId=68, content="Each person who knows you has a different perception of who you are.", createdAt="Wed Jan 05 2022 22:57:08", updatedAt="Sat Apr 09 2022 12:45:07")
    comment2014 = Comment(videoId=129, channelId=85, content="The tree fell unexpectedly short.", createdAt="Mon Apr 04 2022 05:23:29", updatedAt="Thu Dec 23 2021 13:10:04")
    comment2015 = Comment(videoId=446, channelId=63, content="The thick foliage and intertwined vines made the hike nearly impossible.", createdAt="Sat Oct 09 2021 22:22:37", updatedAt="Wed May 05 2021 20:00:54")
    comment2016 = Comment(videoId=95, channelId=30, content="Italy is my favorite country; in fact, I plan to spend two weeks there next year.", createdAt="Sun Oct 10 2021 13:30:21", updatedAt="Mon Jul 26 2021 21:25:27")
    comment2017 = Comment(videoId=729, channelId=43, content="Today we gathered moss for my uncle's wedding.", createdAt="Thu Feb 17 2022 19:29:14", updatedAt="Mon Aug 16 2021 17:36:26")
    comment2018 = Comment(videoId=115, channelId=7, content="She had some amazing news to share but nobody to share it with.", createdAt="Sun Jul 18 2021 20:53:50", updatedAt="Mon May 03 2021 13:30:59")
    comment2019 = Comment(videoId=253, channelId=68, content="He hated that he loved what she hated about hate.", createdAt="Mon Oct 18 2021 01:26:19", updatedAt="Fri Nov 19 2021 10:57:15")
    comment2020 = Comment(videoId=736, channelId=8, content="The dead trees waited to be ignited by the smallest spark and seek their revenge.", createdAt="Mon Apr 04 2022 13:47:00", updatedAt="Tue Nov 09 2021 02:29:46")
    comment2021 = Comment(videoId=680, channelId=14, content="They wandered into a strange Tiki bar on the edge of the small beach town.", createdAt="Sun Jan 16 2022 06:56:21", updatedAt="Mon Apr 12 2021 09:03:20")
    comment2022 = Comment(videoId=429, channelId=27, content="This is a Japanese doll.", createdAt="Sat May 15 2021 21:39:52", updatedAt="Mon Jun 21 2021 14:16:07")
    comment2024 = Comment(videoId=628, channelId=80, content="The rusty nail stood erect, angled at a 45-degree angle, just waiting for the perfect barefoot to come along.", createdAt="Wed May 12 2021 09:31:53", updatedAt="Tue Oct 12 2021 20:13:55")
    comment2025 = Comment(videoId=637, channelId=34, content="Always bring cinnamon buns on a deep-sea diving expedition.", createdAt="Sun Jun 20 2021 10:58:21", updatedAt="Tue Mar 08 2022 09:19:27")
    comment2026 = Comment(videoId=69, channelId=74, content="Kevin embraced his ability to be at the wrong place at the wrong time.", createdAt="Wed Jun 23 2021 05:11:29", updatedAt="Sat Apr 24 2021 10:29:32")
    comment2027 = Comment(videoId=735, channelId=85, content="For some unfathomable reason, the response team didn't consider a lack of milk for my cereal as a proper emergency.", createdAt="Tue Oct 26 2021 11:26:55", updatedAt="Thu Dec 09 2021 15:18:34")
    comment2028 = Comment(videoId=419, channelId=95, content="The pet shop stocks everything you need to keep your anaconda happy.", createdAt="Fri Jan 07 2022 21:15:16", updatedAt="Sun Jan 30 2022 22:21:47")
    comment2029 = Comment(videoId=362, channelId=59, content="I purchased a baby clown from the Russian terrorist black market.", createdAt="Mon May 10 2021 20:04:06", updatedAt="Thu Apr 22 2021 00:30:30")
    comment2030 = Comment(videoId=382, channelId=11, content="The random sentence generator generated a random sentence about a random sentence.", createdAt="Sat Oct 16 2021 02:44:54", updatedAt="Mon Sep 13 2021 00:19:15")
    comment2031 = Comment(videoId=353, channelId=34, content="He wondered if she would appreciate his toenail collection.", createdAt="Tue Apr 13 2021 09:58:35", updatedAt="Sun Jan 02 2022 02:12:58")
    comment2032 = Comment(videoId=15, channelId=92, content="Someone I know recently combined Maple Syrup & buttered Popcorn thinking it would taste like caramel popcorn. It didn’t and they don’t recommend anyone else do it either.", createdAt="Thu May 27 2021 06:31:40", updatedAt="Thu Oct 21 2021 05:02:35")
    comment2033 = Comment(videoId=644, channelId=2, content="The toy brought back fond memories of being lost in the rain forest.", createdAt="Wed Oct 13 2021 05:40:10", updatedAt="Wed Jan 05 2022 09:42:11")
    comment2034 = Comment(videoId=208, channelId=56, content="Nancy thought the best way to create a welcoming home was to line it with barbed wire.", createdAt="Sat Aug 21 2021 23:06:34", updatedAt="Wed Sep 01 2021 16:30:16")
    comment2035 = Comment(videoId=533, channelId=63, content="The two walked down the slot canyon oblivious to the sound of thunder in the distance.", createdAt="Mon Sep 13 2021 11:05:07", updatedAt="Fri Jul 23 2021 19:57:10")
    comment2037 = Comment(videoId=723, channelId=83, content="You can't compare apples and oranges, but what about bananas and plantains?", createdAt="Fri Apr 30 2021 00:58:35", updatedAt="Mon Aug 16 2021 23:00:25")
    comment2038 = Comment(videoId=188, channelId=23, content="The tumbleweed refused to tumble but was more than willing to prance.", createdAt="Tue Jul 06 2021 21:28:29", updatedAt="Mon Oct 04 2021 11:35:22")
    comment2039 = Comment(videoId=769, channelId=85, content="Getting up at dawn is for the birds.", createdAt="Sat Jun 26 2021 18:18:38", updatedAt="Mon Feb 14 2022 18:10:29")
    comment2040 = Comment(videoId=752, channelId=70, content="The irony of the situation wasn't lost on anyone in the room.", createdAt="Mon Aug 02 2021 05:27:40", updatedAt="Sun Oct 03 2021 23:08:47")
    comment2041 = Comment(videoId=417, channelId=20, content="I've traveled all around Africa and still haven't found the gnu who stole my scarf.", createdAt="Tue Jun 22 2021 09:00:41", updatedAt="Thu Mar 03 2022 05:50:14")
    comment2042 = Comment(videoId=710, channelId=53, content="We're careful about orange ping pong balls because people might think they're fruit.", createdAt="Tue Jul 20 2021 12:54:31", updatedAt="Fri Jul 09 2021 06:07:27")
    comment2043 = Comment(videoId=255, channelId=44, content="If my calculator had a history, it would be more embarrassing than my browser history.", createdAt="Sat Sep 18 2021 01:24:35", updatedAt="Thu Mar 31 2022 06:43:03")
    comment2044 = Comment(videoId=239, channelId=15, content="Her hair was windswept as she rode in the black convertible.", createdAt="Mon Jul 19 2021 19:00:44", updatedAt="Wed May 26 2021 16:47:26")
    comment2045 = Comment(videoId=288, channelId=80, content="She insisted that cleaning out your closet was the key to good driving.", createdAt="Thu Dec 30 2021 04:42:24", updatedAt="Tue Apr 20 2021 22:02:27")
    comment2046 = Comment(videoId=404, channelId=89, content="On a scale from one to ten, what's your favorite flavor of random grammar?", createdAt="Mon Jan 10 2022 19:47:10", updatedAt="Sat Dec 04 2021 05:50:58")
    comment2047 = Comment(videoId=589, channelId=76, content="They throw cabbage that turns your brain into emotional baggage.", createdAt="Fri Dec 31 2021 19:15:12", updatedAt="Fri May 07 2021 20:01:43")
    comment2048 = Comment(videoId=32, channelId=46, content="She always had an interesting perspective on why the world must be flat.", createdAt="Tue Apr 13 2021 03:57:11", updatedAt="Tue Jun 01 2021 01:03:56")
    comment2049 = Comment(videoId=588, channelId=62, content="They improved dramatically once the lead singer left.", createdAt="Thu Aug 12 2021 09:42:13", updatedAt="Sun Feb 20 2022 01:43:05")
    comment2050 = Comment(videoId=363, channelId=89, content="I may struggle with geography, but I'm sure I'm somewhere around here.", createdAt="Wed Apr 21 2021 14:08:02", updatedAt="Fri Dec 31 2021 03:53:39")
    comment2051 = Comment(videoId=334, channelId=30, content="There was no ice cream in the freezer, nor did they have money to go to the store.", createdAt="Mon Mar 14 2022 08:48:54", updatedAt="Wed Aug 18 2021 10:42:32")
    comment2052 = Comment(videoId=18, channelId=8, content="His get rich quick scheme was to grow a cactus farm.", createdAt="Thu Feb 24 2022 21:10:49", updatedAt="Mon Oct 04 2021 14:20:48")
    comment2053 = Comment(videoId=503, channelId=90, content="Her daily goal was to improve on yesterday.", createdAt="Sat May 15 2021 13:05:23", updatedAt="Sun Apr 10 2022 15:54:18")
    comment2054 = Comment(videoId=124, channelId=100, content="He poured rocks in the dungeon of his mind.", createdAt="Wed Nov 10 2021 13:27:06", updatedAt="Fri Jun 04 2021 05:09:45")
    comment2055 = Comment(videoId=772, channelId=98, content="It's never been my responsibility to glaze the donuts.", createdAt="Mon Jul 12 2021 15:12:37", updatedAt="Wed May 19 2021 10:48:37")
    comment2056 = Comment(videoId=37, channelId=32, content="The snow-covered path was no help in finding his way out of the back-country.", createdAt="Fri May 14 2021 02:25:53", updatedAt="Wed Feb 16 2022 01:18:29")
    comment2058 = Comment(videoId=388, channelId=64, content="I've always wanted to go to Tajikistan, but my cat would miss me.", createdAt="Wed Sep 01 2021 03:32:13", updatedAt="Thu Sep 30 2021 11:40:20")
    comment2059 = Comment(videoId=179, channelId=72, content="Beach-combing replaced wine tasting as his new obsession.", createdAt="Sat Apr 17 2021 11:36:31", updatedAt="Tue Oct 12 2021 09:41:33")
    comment2060 = Comment(videoId=277, channelId=92, content="The elephant didn't want to talk about the person in the room.", createdAt="Tue Jul 27 2021 06:21:00", updatedAt="Fri Oct 15 2021 03:37:53")
    comment2061 = Comment(videoId=558, channelId=30, content="The waves were crashing on the shore; it was a lovely sight.", createdAt="Tue Oct 12 2021 04:30:49", updatedAt="Mon Nov 15 2021 21:21:41")

    ##############################################################################################
    ##############################################################################################
    ##############################################################################################
    ##############################################################################################
    ##############################################################################################
    ##############################################################################################
    ##############################################################################################
    
    comment1b = Comment(videoId=611, channelId=23, content="It was a really good Monday for being a Saturday.", createdAt="Mon Mar 14 2022 17:56:29", updatedAt="Wed Jul 21 2021 12:05:56")
    comment2b = Comment(videoId=151, channelId=5, content="It's not often you find a soggy banana on the street.", createdAt="Sat Jan 01 2022 23:08:06", updatedAt="Mon Aug 09 2021 23:54:22")
    comment3b = Comment(videoId=93, channelId=39, content="Abstraction is often one floor above you.", createdAt="Thu Jul 22 2021 07:48:18", updatedAt="Mon Oct 18 2021 16:31:18")
    comment4b = Comment(videoId=47, channelId=87, content="Warm beer on a cold day isn't my idea of fun.", createdAt="Sat Oct 02 2021 20:49:23", updatedAt="Fri Nov 19 2021 21:42:27")
    comment5b = Comment(videoId=114, channelId=81, content="It's never comforting to know that your fate depends on something as unpredictable as the popping of corn.", createdAt="Fri Apr 08 2022 18:59:10", updatedAt="Tue Jan 04 2022 00:03:11")
    comment6b = Comment(videoId=634, channelId=8, content="Bill ran from the giraffe toward the dolphin.", createdAt="Fri Jul 30 2021 10:08:49", updatedAt="Wed Jan 26 2022 07:25:44")
    comment7b = Comment(videoId=718, channelId=84, content="Giving directions that the mountains are to the west only works when you can see them.", createdAt="Wed May 19 2021 18:01:14", updatedAt="Thu Oct 14 2021 05:48:40")
    comment8b = Comment(videoId=264, channelId=2, content="I often see the time 11:11 or 12:34 on clocks.", createdAt="Wed Dec 08 2021 15:56:12", updatedAt="Wed Sep 22 2021 19:36:52")
    comment9b = Comment(videoId=720, channelId=55, content="Their argument could be heard across the parking lot.", createdAt="Wed Oct 27 2021 17:53:15", updatedAt="Thu May 13 2021 03:17:48")
    comment10b = Comment(videoId=617, channelId=66, content="I want to buy a onesie… but know it won’t suit me.", createdAt="Wed Apr 14 2021 06:18:21", updatedAt="Thu Jul 01 2021 22:29:01")
    comment11b = Comment(videoId=760, channelId=80, content="Buried deep in the snow, he hoped his batteries were fresh in his avalanche beacon.", createdAt="Sun Dec 26 2021 22:28:55", updatedAt="Thu Oct 21 2021 10:58:27")
    comment12b = Comment(videoId=518, channelId=32, content="Three years later, the coffin was still full of Jello.", createdAt="Mon Aug 16 2021 03:37:08", updatedAt="Sun Apr 03 2022 05:59:56")
    comment13b = Comment(videoId=61, channelId=43, content="If you spin around three times, you'll start to feel melancholy.", createdAt="Thu Jul 29 2021 01:19:38", updatedAt="Thu Aug 26 2021 10:46:20")
    comment14b = Comment(videoId=315, channelId=96, content="I really want to go to work, but I am too sick to drive.", createdAt="Mon Nov 08 2021 19:40:05", updatedAt="Sun Oct 17 2021 23:42:37")
    comment15b = Comment(videoId=326, channelId=71, content="Let me help you with your baggage.", createdAt="Mon Jul 12 2021 04:42:16", updatedAt="Wed Jul 21 2021 05:12:54")
    comment16b = Comment(videoId=751, channelId=74, content="Some bathing suits just shouldn’t be worn by some people.", createdAt="Mon Jan 24 2022 02:53:03", updatedAt="Fri Aug 27 2021 01:47:54")
    comment17b = Comment(videoId=191, channelId=47, content="Mary plays the piano.", createdAt="Tue Jan 25 2022 14:41:46", updatedAt="Thu Mar 17 2022 20:08:02")
    comment18b = Comment(videoId=700, channelId=69, content="Erin accidentally created a new universe.", createdAt="Tue Oct 26 2021 18:36:23", updatedAt="Tue May 18 2021 22:20:51")
    comment19b = Comment(videoId=605, channelId=94, content="Peanuts don't grow on trees, but cashews do.", createdAt="Wed Jun 16 2021 17:46:11", updatedAt="Fri Nov 19 2021 11:05:49")
    comment20b = Comment(videoId=658, channelId=19, content="At that moment I was the most fearsome weasel in the entire swamp.", createdAt="Tue May 18 2021 21:18:32", updatedAt="Wed Apr 21 2021 03:17:47")
    comment21b = Comment(videoId=157, channelId=75, content="She had some amazing news to share but nobody to share it with.", createdAt="Wed Jan 19 2022 07:49:28", updatedAt="Thu Apr 22 2021 06:19:01")
    comment22b = Comment(videoId=528, channelId=4, content="As the years pass by, we all know owners look more and more like their dogs.", createdAt="Fri Apr 16 2021 17:10:46", updatedAt="Mon Feb 28 2022 17:23:13")
    comment23b = Comment(videoId=671, channelId=56, content="Being unacquainted with the chief raccoon was harming his prospects for promotion.", createdAt="Sat May 15 2021 01:27:38", updatedAt="Mon Nov 15 2021 20:35:48")
    comment24b = Comment(videoId=440, channelId=64, content="Having no hair made him look even hairier.", createdAt="Thu Sep 16 2021 12:07:05", updatedAt="Thu Nov 25 2021 01:06:56")
    comment25b = Comment(videoId=454, channelId=8, content="As he dangled from the rope deep inside the crevasse", createdAt="Mon Apr 26 2021 15:26:14", updatedAt="Tue Aug 03 2021 04:08:14")
    comment26b = Comment(videoId=548, channelId=97, content="She always speaks to him in a loud voice.", createdAt="Wed Nov 10 2021 12:59:50", updatedAt="Fri Feb 11 2022 14:39:59")
    comment27b = Comment(videoId=774, channelId=49, content="I never knew what hardship looked like until it started raining bowling balls.", createdAt="Tue Jan 04 2022 23:08:05", updatedAt="Mon Jan 24 2022 23:52:18")
    comment28b = Comment(videoId=270, channelId=89, content="The door slammed on the watermelon.", createdAt="Sun Dec 19 2021 06:18:02", updatedAt="Sun Mar 27 2022 00:12:43")
    comment29b = Comment(videoId=556, channelId=93, content="Greetings from the real universe.", createdAt="Sun Jul 18 2021 21:12:49", updatedAt="Sun Jun 13 2021 06:05:44")
    comment30b = Comment(videoId=741, channelId=84, content="Everyone was curious about the large white blimp that appeared overnight.", createdAt="Tue Sep 07 2021 01:00:26", updatedAt="Wed Oct 20 2021 03:46:12")
    comment31b = Comment(videoId=778, channelId=50, content="Today arrived with a crash of my car through the garage door.", createdAt="Mon Nov 15 2021 22:20:56", updatedAt="Fri Oct 01 2021 02:41:12")
    comment32b = Comment(videoId=236, channelId=3, content="After coating myself in vegetable oil I found my success rate skyrocketed.", createdAt="Tue Nov 09 2021 05:01:25", updatedAt="Wed Dec 08 2021 09:54:17")
    comment33b = Comment(videoId=442, channelId=38, content="I know many children ask for a pony, but I wanted a bicycle with rockets strapped to it.", createdAt="Wed May 05 2021 02:20:30", updatedAt="Mon Jun 07 2021 17:23:25")
    comment34b = Comment(videoId=700, channelId=94, content="The balloons floated away along with all my hopes and dreams.", createdAt="Mon Dec 13 2021 14:22:52", updatedAt="Sat Dec 25 2021 22:02:03")
    comment35b = Comment(videoId=205, channelId=97, content="Patricia loves the sound of nails strongly pressed against the chalkboard.", createdAt="Tue Mar 01 2022 20:05:26", updatedAt="Sun Apr 18 2021 06:16:34")
    comment36b = Comment(videoId=651, channelId=17, content="There were three sphered rocks congregating in a cubed room.", createdAt="Sun Oct 31 2021 12:15:16", updatedAt="Tue Jul 27 2021 08:15:39")
    comment37b = Comment(videoId=676, channelId=40, content="The sign said there was road work ahead so he decided to speed up.", createdAt="Tue Apr 05 2022 20:01:13", updatedAt="Sat Nov 27 2021 14:05:33")
    comment38b = Comment(videoId=774, channelId=37, content="8% of 25 is the same as 25% of 8 and one of them is much easier to do in your head.", createdAt="Tue Apr 13 2021 05:28:50", updatedAt="Fri Aug 06 2021 08:48:54")
    comment39b = Comment(videoId=296, channelId=43, content="Pink horses galloped across the sea.", createdAt="Fri Mar 18 2022 20:26:34", updatedAt="Sat Jan 01 2022 22:21:28")
    comment40b = Comment(videoId=610, channelId=92, content="The waves were crashing on the shore; it was a lovely sight.", createdAt="Thu Jul 01 2021 18:30:05", updatedAt="Fri May 28 2021 05:47:51")
    comment41b = Comment(videoId=350, channelId=84, content="She learned that water bottles are no longer just to hold liquid, but they're also status symbols.", createdAt="Tue Sep 28 2021 11:25:10", updatedAt="Fri Jul 02 2021 13:00:59")
    comment42b = Comment(videoId=468, channelId=10, content="She did her best to help him.", createdAt="Sun Jun 20 2021 08:57:17", updatedAt="Wed Sep 08 2021 03:11:35")
    comment43b = Comment(videoId=558, channelId=79, content="He walked into the basement with the horror movie from the night before playing in his head.", createdAt="Mon Dec 20 2021 06:25:04", updatedAt="Thu Jul 08 2021 12:06:21")
    comment44b = Comment(videoId=659, channelId=23, content="She wore green lipstick like a fashion icon.", createdAt="Sat Jun 26 2021 22:32:00", updatedAt="Wed Dec 29 2021 04:49:19")
    comment45b = Comment(videoId=695, channelId=33, content="He colored deep space a soft yellow.", createdAt="Tue Dec 28 2021 14:23:21", updatedAt="Fri Jul 09 2021 10:11:47")
    comment46b = Comment(videoId=429, channelId=46, content="He poured rocks in the dungeon of his mind.", createdAt="Thu Nov 25 2021 03:51:46", updatedAt="Mon Aug 02 2021 10:39:39")
    comment47b = Comment(videoId=760, channelId=42, content="Mr. Montoya knows the way to the bakery even though he's never been there.", createdAt="Sat Jul 03 2021 09:33:21", updatedAt="Sun Oct 03 2021 21:13:04")
    comment48b = Comment(videoId=126, channelId=47, content="Gwen had her best sleep ever on her new bed of nails.", createdAt="Wed Oct 06 2021 23:55:45", updatedAt="Wed Dec 29 2021 19:21:43")
    comment49b = Comment(videoId=312, channelId=87, content="She had a habit of taking showers in lemonade.", createdAt="Mon Jan 03 2022 08:47:10", updatedAt="Wed Apr 14 2021 15:49:08")
    comment50b = Comment(videoId=332, channelId=6, content="He used to get confused between soldiers and shoulders, but as a military man, he now soldiers responsibility.", createdAt="Fri Jan 14 2022 03:24:31", updatedAt="Tue Nov 09 2021 14:17:33")
    comment51b = Comment(videoId=11, channelId=80, content="The group quickly understood that toxic waste was the most effective barrier to use against the zombies.", createdAt="Fri Nov 05 2021 02:40:53", updatedAt="Sat Sep 18 2021 10:42:56")
    comment52b = Comment(videoId=266, channelId=74, content="The chic gangster liked to start the day with a pink scarf.", createdAt="Tue Nov 09 2021 21:51:00", updatedAt="Mon Mar 07 2022 15:03:45")
    comment53b = Comment(videoId=31, channelId=68, content="The teens wondered what was kept in the red shed on the far edge of the school grounds.", createdAt="Wed Mar 16 2022 09:12:30", updatedAt="Mon Oct 11 2021 17:26:45")
    comment54b = Comment(videoId=400, channelId=4, content="He had decided to accept his fate of accepting his fate.", createdAt="Fri Jun 11 2021 07:07:38", updatedAt="Fri Mar 25 2022 11:14:06")
    comment55b = Comment(videoId=205, channelId=49, content="I caught my squirrel rustling through my gym bag.", createdAt="Tue Feb 01 2022 05:40:03", updatedAt="Sat Apr 24 2021 06:26:44")
    comment56b = Comment(videoId=227, channelId=40, content="He walked into the basement with the horror movie from the night before playing in his head.", createdAt="Wed Nov 10 2021 06:40:44", updatedAt="Sat Jul 10 2021 00:23:32")
    comment57b = Comment(videoId=111, channelId=47, content="The secret ingredient to his wonderful life was crime.", createdAt="Wed Feb 23 2022 15:57:15", updatedAt="Sat Sep 18 2021 23:30:05")
    comment58b = Comment(videoId=174, channelId=27, content="Honestly, I didn't care much for the first season, so I didn't bother with the second.", createdAt="Sun Apr 11 2021 12:50:37", updatedAt="Mon Jan 10 2022 05:48:50")
    comment59b = Comment(videoId=598, channelId=30, content="She moved forward only because she trusted that the ending she now was going through must be followed by a new beginning.", createdAt="Sat Jun 19 2021 03:59:14", updatedAt="Thu Jul 01 2021 13:18:03")
    comment60b = Comment(videoId=295, channelId=69, content="There's a message for you if you look up.", createdAt="Wed Sep 01 2021 09:43:48", updatedAt="Thu Sep 16 2021 07:05:57")
    comment61b = Comment(videoId=9, channelId=67, content="The paintbrush was angry at the color the artist chose to use.", createdAt="Thu Apr 07 2022 01:25:18", updatedAt="Sat Jun 12 2021 11:20:07")
    comment62b = Comment(videoId=179, channelId=55, content="Seek success, but always be prepared for random cats.", createdAt="Thu Oct 14 2021 03:03:22", updatedAt="Sat Jun 05 2021 14:01:18")
    comment63b = Comment(videoId=125, channelId=54, content="He uses onomatopoeia as a weapon of mental destruction.", createdAt="Tue May 25 2021 20:34:52", updatedAt="Mon Jul 12 2021 00:27:59")
    comment64b = Comment(videoId=447, channelId=6, content="I used to live in my neighbor's fishpond, but the aesthetic wasn't to my taste.", createdAt="Thu Mar 31 2022 05:44:16", updatedAt="Mon Jun 28 2021 11:24:47")
    comment65b = Comment(videoId=671, channelId=13, content="He was all business when he wore his clown suit.", createdAt="Wed Nov 17 2021 08:55:47", updatedAt="Mon May 24 2021 15:31:40")
    comment66b = Comment(videoId=387, channelId=98, content="If any cop asks you where you were, just say you were visiting Kansas.", createdAt="Mon Aug 16 2021 07:16:48", updatedAt="Wed Sep 01 2021 07:09:52")
    comment67b = Comment(videoId=274, channelId=76, content="The fact that there's a stairway to heaven and a highway to hell explains life well.", createdAt="Tue Sep 21 2021 17:06:05", updatedAt="Thu Jul 01 2021 17:51:26")
    comment68b = Comment(videoId=703, channelId=80, content="She couldn't understand why nobody else could see that the sky is full of cotton candy.", createdAt="Wed Jan 26 2022 02:56:04", updatedAt="Sun May 23 2021 05:23:49")
    comment69b = Comment(videoId=660, channelId=17, content="The fox in the tophat whispered into the ear of the rabbit.", createdAt="Sun Jul 18 2021 18:49:34", updatedAt="Fri Aug 20 2021 05:42:30")
    comment70b = Comment(videoId=389, channelId=55, content="She insisted that cleaning out your closet was the key to good driving.", createdAt="Fri Jan 21 2022 22:52:05", updatedAt="Wed Nov 24 2021 11:14:41")
    comment71b = Comment(videoId=6, channelId=59, content="The efficiency we have at removing trash has made creating trash more acceptable.", createdAt="Sun Dec 05 2021 14:17:39", updatedAt="Sun Mar 06 2022 02:48:41")
    comment72b = Comment(videoId=450, channelId=25, content="Everybody should read Chaucer to improve their everyday vocabulary.", createdAt="Sun May 30 2021 11:03:28", updatedAt="Wed Jun 30 2021 08:10:03")
    comment73b = Comment(videoId=617, channelId=20, content="The clock within this blog and the clock on my laptop are 1 hour different from each other.", createdAt="Wed Oct 13 2021 16:36:20", updatedAt="Sun Dec 05 2021 08:23:53")
    comment74b = Comment(videoId=605, channelId=78, content="I am happy to take your donation; any amount will be greatly appreciated.", createdAt="Mon Nov 22 2021 20:52:32", updatedAt="Mon Jun 07 2021 00:08:31")
    comment75b = Comment(videoId=238, channelId=27, content="The estate agent quickly marked out his territory on the dance floor.", createdAt="Tue Aug 24 2021 13:37:03", updatedAt="Tue Feb 08 2022 19:08:19")
    comment76b = Comment(videoId=6, channelId=18, content="Carol drank the blood as if she were a vampire.", createdAt="Tue Nov 09 2021 20:56:47", updatedAt="Tue Aug 10 2021 19:29:50")
    comment77b = Comment(videoId=211, channelId=68, content="Art doesn't have to be intentional.", createdAt="Sun Aug 15 2021 05:02:01", updatedAt="Sun Jan 23 2022 11:02:14")
    comment78b = Comment(videoId=575, channelId=24, content="The toy brought back fond memories of being lost in the rain forest.", createdAt="Thu Sep 02 2021 22:43:03", updatedAt="Sun Jan 02 2022 04:30:48")
    comment79b = Comment(videoId=742, channelId=36, content="The busker hoped that the people passing by would throw money, but they threw tomatoes instead, so he exchanged his hat for a juicer.", createdAt="Sat Nov 20 2021 04:23:38", updatedAt="Thu Mar 03 2022 19:00:01")
    comment80b = Comment(videoId=779, channelId=18, content="It was the best sandcastle he had ever seen.", createdAt="Thu Apr 07 2022 06:18:45", updatedAt="Wed Aug 25 2021 06:46:05")
    comment81b = Comment(videoId=250, channelId=75, content="Improve your goldfish's physical fitness by getting him a bicycle.", createdAt="Thu Apr 22 2021 22:57:36", updatedAt="Sun Feb 20 2022 16:10:11")
    comment82b = Comment(videoId=566, channelId=53, content="The family’s excitement over going to Disneyland was crazier than she anticipated.", createdAt="Thu Feb 24 2022 15:11:52", updatedAt="Sat Jul 17 2021 21:54:27")
    comment83b = Comment(videoId=98, channelId=43, content="Twin 4-month-olds slept in the shade of the palm tree while the mother tanned in the sun.", createdAt="Fri Oct 01 2021 14:43:19", updatedAt="Sun Jan 23 2022 08:37:12")
    comment84b = Comment(videoId=298, channelId=37, content="I ate a sock because people on the Internet told me to.", createdAt="Wed Nov 17 2021 14:27:18", updatedAt="Fri Feb 04 2022 23:38:51")
    comment85b = Comment(videoId=639, channelId=37, content="The tour bus was packed with teenage girls heading toward their next adventure.", createdAt="Sun Sep 12 2021 01:07:08", updatedAt="Sat Nov 13 2021 07:36:53")
    comment86b = Comment(videoId=52, channelId=91, content="Stop waiting for exceptional things to just happen.", createdAt="Sun Sep 12 2021 05:53:39", updatedAt="Sun Oct 10 2021 19:53:22")
    comment87b = Comment(videoId=557, channelId=26, content="Erin accidentally created a new universe.", createdAt="Tue Jun 22 2021 01:31:01", updatedAt="Sun Jan 23 2022 05:03:52")
    comment88b = Comment(videoId=763, channelId=42, content="My Mum tries to be cool by saying that she likes all the same things that I do.", createdAt="Sun Sep 19 2021 11:37:47", updatedAt="Fri May 21 2021 17:13:21")
    comment89b = Comment(videoId=518, channelId=77, content="She traveled because it cost the same as therapy and was a lot more enjoyable.", createdAt="Tue Jul 06 2021 23:43:43", updatedAt="Fri Jul 16 2021 23:05:38")
    comment90b = Comment(videoId=310, channelId=83, content="As the years pass by, we all know owners look more and more like their dogs.", createdAt="Fri Mar 18 2022 08:28:15", updatedAt="Fri Nov 19 2021 01:45:52")
    comment91b = Comment(videoId=586, channelId=14, content="The pet shop stocks everything you need to keep your anaconda happy.", createdAt="Thu Dec 16 2021 06:40:34", updatedAt="Sat Jun 05 2021 06:09:57")
    comment92b = Comment(videoId=225, channelId=81, content="The doll spun around in circles in hopes of coming alive.", createdAt="Wed Dec 01 2021 00:36:15", updatedAt="Mon Apr 19 2021 01:24:59")
    comment94b = Comment(videoId=561, channelId=38, content="The sunblock was handed to the girl before practice, but the burned skin was proof she did not apply it.", createdAt="Wed Jun 02 2021 06:45:42", updatedAt="Wed Oct 27 2021 06:14:15")
    comment95b = Comment(videoId=276, channelId=21, content="He stomped on his fruit loops and thus became a cereal killer.", createdAt="Sat Dec 25 2021 22:07:55", updatedAt="Sat Jun 26 2021 16:00:29")
    comment96b = Comment(videoId=410, channelId=36, content="Even though he thought the world was flat he didn’t see the irony of wanting to travel around the world.", createdAt="Mon Oct 04 2021 01:41:56", updatedAt="Thu Jan 06 2022 08:51:58")
    comment97b = Comment(videoId=33, channelId=32, content="The manager of the fruit stand always sat and only sold vegetables.", createdAt="Thu Jul 08 2021 14:04:05", updatedAt="Sat Dec 18 2021 21:35:38")
    comment98b = Comment(videoId=702, channelId=80, content="A kangaroo is really just a rabbit on steroids.", createdAt="Wed Jun 16 2021 13:17:21", updatedAt="Sat Nov 13 2021 13:26:36")
    comment99b = Comment(videoId=727, channelId=61, content="They're playing the piano while flying in the plane.", createdAt="Sun Aug 22 2021 20:36:42", updatedAt="Wed Sep 29 2021 16:38:41")
    comment100b = Comment(videoId=152, channelId=89, content="Today I dressed my unicorn in preparation for the race.", createdAt="Thu Jul 22 2021 23:43:58", updatedAt="Sun Dec 05 2021 09:40:21")
    comment101b = Comment(videoId=421, channelId=61, content="The llama couldn't resist trying the lemonade.", createdAt="Tue Jun 01 2021 18:50:01", updatedAt="Thu May 13 2021 20:50:40")
    comment103b = Comment(videoId=342, channelId=21, content="She had a habit of taking showers in lemonade.", createdAt="Fri Apr 08 2022 08:42:17", updatedAt="Sat Aug 14 2021 10:48:10")
    comment104b = Comment(videoId=142, channelId=56, content="Separation anxiety is what happens when you can't find your phone.", createdAt="Sat Sep 18 2021 16:01:33", updatedAt="Sun Jan 09 2022 11:14:44")
    comment105b = Comment(videoId=99, channelId=60, content="I love eating toasted cheese and tuna sandwiches.", createdAt="Sat Jan 01 2022 07:03:14", updatedAt="Mon Jan 10 2022 06:47:51")
    comment106b = Comment(videoId=713, channelId=89, content="So long and thanks for the fish.", createdAt="Fri Apr 23 2021 16:03:51", updatedAt="Mon Dec 06 2021 04:32:32")
    comment107b = Comment(videoId=234, channelId=92, content="He was sitting in a trash can with high street class.", createdAt="Thu Dec 23 2021 08:37:59", updatedAt="Sun Apr 18 2021 15:33:19")
    comment108b = Comment(videoId=489, channelId=3, content="Despite multiple complications and her near-death experience", createdAt="Wed Jan 19 2022 23:08:03", updatedAt="Thu Sep 30 2021 01:42:32")
    comment109b = Comment(videoId=525, channelId=86, content="It isn't difficult to do a handstand if you just stand on your hands.", createdAt="Thu Feb 17 2022 00:39:12", updatedAt="Tue Sep 14 2021 15:56:51")
    comment110b = Comment(videoId=588, channelId=56, content="The old apple revels in its authority.", createdAt="Tue Mar 22 2022 03:07:49", updatedAt="Thu Jul 29 2021 05:08:27")
    comment111b = Comment(videoId=661, channelId=31, content="The minute she landed she understood the reason this was a fly-over state.", createdAt="Wed Oct 20 2021 17:47:25", updatedAt="Sun Mar 06 2022 16:36:37")
    comment112b = Comment(videoId=639, channelId=13, content="You've been eyeing me all day and waiting for your move like a lion stalking a gazelle in a savannah.", createdAt="Wed Jan 26 2022 21:43:46", updatedAt="Sat Oct 09 2021 05:07:58")
    comment113b = Comment(videoId=447, channelId=80, content="Blue sounded too cold at the time and yet it seemed to work for gin.", createdAt="Mon May 10 2021 02:57:50", updatedAt="Sat Aug 28 2021 04:13:18")
    comment114b = Comment(videoId=264, channelId=23, content="Whenever he saw a red flag warning at the beach he grabbed his surfboard.", createdAt="Fri Dec 10 2021 12:41:54", updatedAt="Sun Aug 29 2021 09:16:41")
    comment115b = Comment(videoId=222, channelId=2, content="He said he was not there yesterday; however, many people saw him there.", createdAt="Thu Jul 01 2021 20:29:27", updatedAt="Sun Oct 24 2021 00:34:38")
    comment116b = Comment(videoId=750, channelId=78, content="Baby wipes are made of chocolate stardust.", createdAt="Thu Oct 28 2021 07:01:41", updatedAt="Thu Jul 08 2021 20:20:12")
    comment117b = Comment(videoId=740, channelId=31, content="Beach-combing replaced wine tasting as his new obsession.", createdAt="Sun May 16 2021 22:40:48", updatedAt="Sun Jan 23 2022 05:35:31")
    comment118b = Comment(videoId=163, channelId=79, content="The teenage boy was accused of breaking his arm simply to get out of the test.", createdAt="Tue Mar 01 2022 06:04:40", updatedAt="Wed Nov 24 2021 12:06:57")
    comment119b = Comment(videoId=574, channelId=31, content="She was too short to see over the fence.", createdAt="Thu Aug 12 2021 08:02:37", updatedAt="Wed Apr 14 2021 09:47:04")
    comment120b = Comment(videoId=710, channelId=32, content="The golden retriever loved the fireworks each Fourth of July.", createdAt="Fri Apr 08 2022 20:58:51", updatedAt="Sat May 08 2021 07:25:04")
    comment121b = Comment(videoId=159, channelId=53, content="A kangaroo is really just a rabbit on steroids.", createdAt="Wed Dec 01 2021 01:18:20", updatedAt="Sun Mar 20 2022 14:50:14")
    comment122b = Comment(videoId=729, channelId=39, content="At that moment I was the most fearsome weasel in the entire swamp.", createdAt="Wed Sep 08 2021 00:42:57", updatedAt="Thu Sep 30 2021 12:08:22")
    comment123b = Comment(videoId=576, channelId=64, content="In that instant, everything changed.", createdAt="Fri May 21 2021 04:03:28", updatedAt="Sun Apr 03 2022 17:27:35")
    comment124b = Comment(videoId=152, channelId=32, content="The stranger officiates the meal.", createdAt="Tue Aug 31 2021 11:45:35", updatedAt="Thu Sep 30 2021 12:29:06")
    comment125b = Comment(videoId=180, channelId=60, content="Being unacquainted with the chief raccoon was harming his prospects for promotion.", createdAt="Tue Jun 08 2021 23:45:28", updatedAt="Sat May 08 2021 15:29:19")
    comment126b = Comment(videoId=418, channelId=10, content="The most exciting eureka moment I've had was when I realized that the instructions on food packets were just guidelines.", createdAt="Sun Mar 20 2022 04:07:31", updatedAt="Fri Sep 03 2021 14:19:16")
    comment127b = Comment(videoId=228, channelId=99, content="The small white buoys marked the location of hundreds of crab pots.", createdAt="Mon Oct 04 2021 03:29:53", updatedAt="Sat Nov 20 2021 07:07:33")
    comment128b = Comment(videoId=252, channelId=98, content="She only paints with bold colors; she does not like pastels.", createdAt="Sun Sep 26 2021 00:58:40", updatedAt="Tue Nov 16 2021 06:38:06")
    comment129b = Comment(videoId=251, channelId=88, content="He was sure the Devil created red sparkly glitter.", createdAt="Wed Jul 21 2021 03:07:22", updatedAt="Sat Apr 09 2022 22:13:24")
    comment130b = Comment(videoId=413, channelId=94, content="The wake behind the boat told of the past while the open sea for told life in the unknown future.", createdAt="Wed Jun 30 2021 18:55:21", updatedAt="Mon Aug 09 2021 08:15:12")
    comment131b = Comment(videoId=128, channelId=39, content="Pink horses galloped across the sea.", createdAt="Thu Jun 24 2021 04:59:10", updatedAt="Thu Sep 16 2021 09:45:25")
    comment132b = Comment(videoId=593, channelId=48, content="She had that tint of craziness in her soul that made her believe she could actually make a difference.", createdAt="Tue Feb 15 2022 15:53:50", updatedAt="Sun Sep 05 2021 08:14:29")
    comment134b = Comment(videoId=227, channelId=75, content="He fumbled in the darkness looking for the light switch, but when he finally found it there was someone already there.", createdAt="Fri Feb 11 2022 14:15:35", updatedAt="Sat Jul 10 2021 12:37:30")
    comment135b = Comment(videoId=541, channelId=52, content="He learned the hardest lesson of his life and had the scars, both physical and mental, to prove it.", createdAt="Wed Feb 23 2022 01:39:25", updatedAt="Sat May 15 2021 16:14:11")
    comment136b = Comment(videoId=241, channelId=59, content="Gary didn't understand why Doug went upstairs to get one dollar bills when he invited him to go cow tipping.", createdAt="Tue Nov 30 2021 20:44:33", updatedAt="Sat Apr 09 2022 18:04:52")
    comment137b = Comment(videoId=553, channelId=49, content="I’m working on a sweet potato farm.", createdAt="Thu Nov 25 2021 23:55:59", updatedAt="Thu Dec 09 2021 23:44:52")
    comment138b = Comment(videoId=396, channelId=69, content="If any cop asks you where you were, just say you were visiting Kansas.", createdAt="Fri Apr 23 2021 03:48:34", updatedAt="Thu Aug 05 2021 19:44:03")
    comment139b = Comment(videoId=258, channelId=11, content="Nobody loves a pig wearing lipstick.", createdAt="Tue Jun 29 2021 22:16:54", updatedAt="Tue May 04 2021 15:12:38")
    comment140b = Comment(videoId=672, channelId=37, content="As he entered the church he could hear the soft voice of someone whispering into a cell phone.", createdAt="Thu Sep 09 2021 01:27:35", updatedAt="Mon Jun 07 2021 01:11:23")
    comment141b = Comment(videoId=470, channelId=32, content="The blue parrot drove by the hitchhiking mongoose.", createdAt="Tue Jul 06 2021 20:03:53", updatedAt="Mon Mar 21 2022 02:19:20")
    comment142b = Comment(videoId=34, channelId=25, content="It didn't make sense unless you had the power to eat colors.", createdAt="Sat Dec 04 2021 21:31:32", updatedAt="Fri Dec 17 2021 02:39:01")
    comment143b = Comment(videoId=733, channelId=10, content="The Tsunami wave crashed against the raised houses and broke the pilings as if they were toothpicks.", createdAt="Tue Jul 13 2021 06:43:06", updatedAt="Mon Feb 07 2022 23:04:37")
    comment144b = Comment(videoId=745, channelId=39, content="The random sentence generator generated a random sentence about a random sentence.", createdAt="Mon Sep 27 2021 02:22:18", updatedAt="Sun Feb 20 2022 14:50:11")
    comment145b = Comment(videoId=68, channelId=13, content="He went back to the video to see what had been recorded and was shocked at what he saw.", createdAt="Sat Jan 22 2022 03:50:49", updatedAt="Thu Dec 16 2021 17:23:30")
    comment146b = Comment(videoId=250, channelId=67, content="Please wait outside of the house.", createdAt="Thu Jul 15 2021 05:38:31", updatedAt="Wed Sep 29 2021 01:12:43")
    comment147b = Comment(videoId=200, channelId=41, content="I only enjoy window shopping when the windows are transparent.", createdAt="Thu Jun 17 2021 01:40:24", updatedAt="Tue Oct 19 2021 09:07:52")
    comment148b = Comment(videoId=601, channelId=4, content="They ran around the corner to find that they had traveled back in time.", createdAt="Sat Aug 14 2021 08:40:01", updatedAt="Sat Jul 03 2021 06:22:28")
    comment149b = Comment(videoId=262, channelId=3, content="Flash photography is best used in full sunlight.", createdAt="Mon Mar 07 2022 13:41:04", updatedAt="Mon Jan 31 2022 15:36:36")
    comment150b = Comment(videoId=376, channelId=69, content="The truth is that you pay for your lifestyle in hours.", createdAt="Fri Jan 28 2022 09:30:18", updatedAt="Thu May 27 2021 02:23:33")
    comment151b = Comment(videoId=74, channelId=92, content="Let me help you with your baggage.", createdAt="Fri Dec 17 2021 15:11:39", updatedAt="Mon Jun 21 2021 12:26:32")
    comment152b = Comment(videoId=412, channelId=50, content="Trash covered the landscape like sprinkles do a birthday cake.", createdAt="Tue Mar 29 2022 15:57:53", updatedAt="Mon Nov 29 2021 17:36:21")
    comment153b = Comment(videoId=688, channelId=2, content="I was offended by the suggestion that my baby brother was a jewel thief.", createdAt="Thu May 13 2021 06:40:33", updatedAt="Fri Nov 26 2021 11:58:50")
    comment154b = Comment(videoId=433, channelId=21, content="Patricia found the meaning of life in a bowl of Cheerios.", createdAt="Fri Sep 10 2021 10:44:24", updatedAt="Fri Feb 04 2022 00:16:22")
    comment155b = Comment(videoId=493, channelId=68, content="I always dreamed about being stranded on a desert island until it actually happened.", createdAt="Mon Mar 14 2022 06:11:57", updatedAt="Fri Apr 08 2022 23:19:01")
    comment156b = Comment(videoId=214, channelId=26, content="Normal activities took extraordinary amounts of concentration at the high altitude.", createdAt="Tue Aug 03 2021 07:54:44", updatedAt="Sat Jun 12 2021 23:00:31")
    comment157b = Comment(videoId=552, channelId=3, content="I'm confused: when people ask me what's up, and I point, they groan.", createdAt="Fri Jul 09 2021 15:18:48", updatedAt="Fri Oct 08 2021 22:06:20")
    comment158b = Comment(videoId=286, channelId=59, content="He didn't heed the warning and it had turned out surprisingly well.", createdAt="Sun Sep 26 2021 23:30:08", updatedAt="Mon Dec 13 2021 16:12:10")
    comment159b = Comment(videoId=111, channelId=12, content="My biggest joy is roasting almonds while stalking prey.", createdAt="Sun Feb 27 2022 22:28:36", updatedAt="Sun May 16 2021 05:14:13")
    comment160b = Comment(videoId=343, channelId=2, content="100 years old is such a young age if you happen to be a bristlecone pine.", createdAt="Thu Aug 19 2021 01:37:35", updatedAt="Fri Apr 08 2022 14:46:59")
    comment161b = Comment(videoId=588, channelId=59, content="The sudden rainstorm washed crocodiles into the ocean.", createdAt="Thu Jan 27 2022 15:16:41", updatedAt="Fri Apr 01 2022 18:59:49")
    comment162b = Comment(videoId=569, channelId=52, content="She felt that chill that makes the hairs on the back of your neck when he walked into the room.", createdAt="Sun Apr 25 2021 10:13:37", updatedAt="Wed Jun 02 2021 21:05:00")
    comment163b = Comment(videoId=182, channelId=2, content="The body piercing didn't go exactly as he expected.", createdAt="Wed Dec 15 2021 15:37:59", updatedAt="Fri Nov 12 2021 08:34:42")
    comment164b = Comment(videoId=51, channelId=2, content="I want more detailed information.", createdAt="Sat Aug 07 2021 18:28:29", updatedAt="Sat May 22 2021 18:03:59")
    comment165b = Comment(videoId=255, channelId=94, content="The secret code they created made no sense, even to them.", createdAt="Sat Oct 02 2021 16:21:52", updatedAt="Sat Dec 11 2021 00:21:10")
    comment166b = Comment(videoId=669, channelId=34, content="Gary didn't understand why Doug went upstairs to get one dollar bills when he invited him to go cow tipping.", createdAt="Tue Aug 03 2021 20:47:08", updatedAt="Sat Oct 02 2021 19:25:08")
    comment167b = Comment(videoId=476, channelId=62, content="Purple is the best city in the forest.", createdAt="Tue Oct 19 2021 14:09:32", updatedAt="Wed Sep 15 2021 04:37:47")
    comment168b = Comment(videoId=776, channelId=31, content="He had a hidden stash underneath the floorboards in the back room of the house.", createdAt="Sat Feb 05 2022 16:38:53", updatedAt="Mon May 17 2021 16:00:36")
    comment169b = Comment(videoId=649, channelId=58, content="She wasn't sure whether to be impressed or concerned that he folded underwear in neat little packages.", createdAt="Fri Jan 28 2022 03:27:42", updatedAt="Tue May 11 2021 01:02:59")
    comment170b = Comment(videoId=470, channelId=44, content="The tree fell unexpectedly short.", createdAt="Tue Mar 22 2022 11:46:24", updatedAt="Sun Mar 20 2022 14:43:54")
    comment171b = Comment(videoId=181, channelId=39, content="Lightning Paradise was the local hangout joint where the group usually ended up spending the night.", createdAt="Wed Sep 29 2021 14:18:13", updatedAt="Tue Nov 30 2021 22:05:12")
    comment172b = Comment(videoId=644, channelId=3, content="After fighting off the alligator, Brian still had to face the anaconda.", createdAt="Fri Jul 16 2021 02:25:01", updatedAt="Thu Nov 11 2021 18:46:32")
    comment173b = Comment(videoId=59, channelId=69, content="He was sitting in a trash can with high street class.", createdAt="Wed Jun 23 2021 17:42:32", updatedAt="Fri Jan 28 2022 22:56:21")
    comment174b = Comment(videoId=481, channelId=27, content="The delicious aroma from the kitchen was ruined by cigarette smoke.", createdAt="Sun Dec 26 2021 11:40:59", updatedAt="Tue Nov 16 2021 15:31:29")
    comment175b = Comment(videoId=299, channelId=19, content="I'd rather be a bird than a fish.", createdAt="Sun Sep 19 2021 09:09:15", updatedAt="Mon Aug 23 2021 00:16:39")
    comment176b = Comment(videoId=233, channelId=83, content="I had a friend in high school named Rick Shaw, but he was fairly useless as a mode of transport.", createdAt="Tue Jul 06 2021 18:28:57", updatedAt="Wed Jun 23 2021 11:52:30")
    comment177b = Comment(videoId=7, channelId=29, content="The water flowing down the river didn’t look that powerful from the car", createdAt="Tue May 25 2021 01:42:25", updatedAt="Sat Dec 25 2021 09:25:24")
    comment178b = Comment(videoId=264, channelId=51, content="He walked into the basement with the horror movie from the night before playing in his head.", createdAt="Mon Jan 10 2022 22:52:24", updatedAt="Thu Jul 22 2021 09:22:46")
    comment179b = Comment(videoId=123, channelId=36, content="Jason lived his life by the motto, \"Anything worth doing is worth doing poorly.", createdAt="Sun Jan 23 2022 16:16:49", updatedAt="Fri Sep 24 2021 04:50:17")
    comment180b = Comment(videoId=672, channelId=90, content="Today I heard something new and unmemorable.", createdAt="Thu Jul 01 2021 18:34:03", updatedAt="Tue Jul 06 2021 00:57:08")
    comment181b = Comment(videoId=642, channelId=49, content="Her hair was windswept as she rode in the black convertible.", createdAt="Sat Jan 08 2022 08:22:00", updatedAt="Tue Mar 29 2022 06:21:15")
    comment182b = Comment(videoId=104, channelId=78, content="She borrowed the book from him many years ago and hasn't yet returned it.", createdAt="Sun Aug 22 2021 15:00:12", updatedAt="Mon Nov 01 2021 15:07:04")
    comment183b = Comment(videoId=756, channelId=55, content="There are few things better in life than a slice of pie.", createdAt="Thu Oct 28 2021 08:57:03", updatedAt="Mon Aug 16 2021 15:46:48")
    comment184b = Comment(videoId=651, channelId=53, content="It was a slippery slope and he was willing to slide all the way to the deepest depths.", createdAt="Sat May 15 2021 01:47:22", updatedAt="Wed Jun 02 2021 16:01:05")
    comment185b = Comment(videoId=232, channelId=50, content="The trick to getting kids to eat anything is to put catchup on it.", createdAt="Tue Jan 25 2022 19:24:42", updatedAt="Sat Dec 11 2021 18:35:33")
    comment186b = Comment(videoId=527, channelId=5, content="When he asked her favorite number, she answered without hesitation that it was diamonds.", createdAt="Fri Jan 14 2022 06:22:01", updatedAt="Thu May 27 2021 14:01:06")
    comment187b = Comment(videoId=153, channelId=88, content="Please wait outside of the house.", createdAt="Sat Sep 25 2021 14:26:50", updatedAt="Sun Apr 03 2022 12:43:50")
    comment188b = Comment(videoId=725, channelId=80, content="As time wore on, simple dog commands turned into full paragraphs explaining why the dog couldn’t do something.", createdAt="Wed Oct 20 2021 18:54:28", updatedAt="Tue Nov 16 2021 05:48:27")
    comment189b = Comment(videoId=709, channelId=69, content="It turns out you don't need all that stuff you insisted you did.", createdAt="Sun Oct 31 2021 04:21:21", updatedAt="Wed Dec 15 2021 21:54:49")
    comment190b = Comment(videoId=279, channelId=76, content="I like to leave work after my eight-hour tea-break.", createdAt="Sat Jan 29 2022 15:00:51", updatedAt="Wed Apr 21 2021 10:29:58")
    comment191b = Comment(videoId=441, channelId=3, content="Toddlers feeding raccoons surprised even the seasoned park ranger.", createdAt="Sun Dec 12 2021 07:24:24", updatedAt="Thu Jul 29 2021 12:58:24")
    comment192b = Comment(videoId=673, channelId=11, content="Honestly, I didn't care much for the first season, so I didn't bother with the second.", createdAt="Wed Sep 15 2021 01:38:20", updatedAt="Sun Sep 05 2021 01:04:45")
    comment193b = Comment(videoId=563, channelId=86, content="Check back tomorrow; I will see if the book has arrived.", createdAt="Thu Apr 07 2022 11:55:01", updatedAt="Sat Nov 13 2021 23:36:12")
    comment194b = Comment(videoId=181, channelId=51, content="It doesn't sound like that will ever be on my travel list.", createdAt="Mon Oct 04 2021 21:55:29", updatedAt="Sun Sep 19 2021 19:04:15")
    comment195b = Comment(videoId=202, channelId=77, content="He was the type of guy who liked Christmas lights on his house in the middle of July.", createdAt="Fri Apr 08 2022 02:22:45", updatedAt="Tue Mar 15 2022 19:52:38")
    comment196b = Comment(videoId=212, channelId=13, content="Imagine his surprise when he discovered that the safe was full of pudding.", createdAt="Mon Nov 01 2021 04:26:31", updatedAt="Fri Dec 17 2021 19:15:18")
    comment197b = Comment(videoId=509, channelId=21, content="Everyone says they love nature until they realize how dangerous she can be.", createdAt="Wed Mar 23 2022 09:26:54", updatedAt="Sun Oct 10 2021 00:09:59")
    comment198b = Comment(videoId=627, channelId=41, content="The light in his life was actually a fire burning all around him.", createdAt="Sat Mar 19 2022 01:10:03", updatedAt="Sat Apr 17 2021 13:26:42")
    comment200b = Comment(videoId=520, channelId=75, content="It's never been my responsibility to glaze the donuts.", createdAt="Mon May 03 2021 18:11:31", updatedAt="Thu May 06 2021 12:11:54")
    comment201b = Comment(videoId=207, channelId=52, content="Excitement replaced fear until the final moment.", createdAt="Thu Aug 19 2021 08:20:11", updatedAt="Tue Mar 22 2022 01:51:12")
    comment202b = Comment(videoId=448, channelId=1, content="They say that dogs are man's best friend, but this cat was setting out to sabotage that theory.", createdAt="Fri May 07 2021 13:29:52", updatedAt="Wed Sep 15 2021 22:30:59")
    comment203b = Comment(videoId=693, channelId=43, content="Jim liked driving around town with his hazard lights on.", createdAt="Tue Apr 13 2021 00:37:33", updatedAt="Sat Mar 12 2022 19:40:07")
    comment204b = Comment(videoId=411, channelId=75, content="He loved eating his bananas in hot dog buns.", createdAt="Sun Jul 04 2021 20:30:55", updatedAt="Thu Nov 18 2021 16:24:42")
    comment205b = Comment(videoId=3, channelId=69, content="I cheated while playing the darts tournament by using a longbow.", createdAt="Tue May 25 2021 06:19:44", updatedAt="Thu Aug 05 2021 17:04:24")
    comment206b = Comment(videoId=633, channelId=29, content="Homesickness became contagious in the young campers' cabin.", createdAt="Mon Oct 18 2021 03:55:41", updatedAt="Thu Aug 12 2021 16:38:14")
    comment207b = Comment(videoId=744, channelId=34, content="Behind the window was a reflection that only instilled fear.", createdAt="Fri Nov 19 2021 13:25:56", updatedAt="Sun Sep 26 2021 03:03:18")
    comment208b = Comment(videoId=432, channelId=37, content="Strawberries must be the one food that doesn't go well with this brand of paint.", createdAt="Fri Sep 24 2021 10:31:14", updatedAt="Sat May 22 2021 15:35:19")
    comment209b = Comment(videoId=592, channelId=82, content="He didn't heed the warning and it had turned out surprisingly well.", createdAt="Wed May 26 2021 05:16:33", updatedAt="Tue May 25 2021 17:39:40")
    comment210b = Comment(videoId=496, channelId=50, content="She traveled because it cost the same as therapy and was a lot more enjoyable.", createdAt="Thu Jun 17 2021 00:42:30", updatedAt="Sat Dec 11 2021 14:39:00")
    comment212b = Comment(videoId=739, channelId=58, content="Her scream silenced the rowdy teenagers.", createdAt="Mon Jan 17 2022 19:12:18", updatedAt="Fri Jan 14 2022 02:59:44")
    comment213b = Comment(videoId=339, channelId=57, content="A purple pig and a green donkey flew a kite in the middle of the night and ended up sunburnt.", createdAt="Tue Jun 15 2021 22:31:22", updatedAt="Thu Feb 17 2022 11:58:49")
    comment214b = Comment(videoId=589, channelId=33, content="It didn't make sense unless you had the power to eat colors.", createdAt="Tue Sep 14 2021 11:02:43", updatedAt="Sat Feb 19 2022 10:44:37")
    comment215b = Comment(videoId=145, channelId=66, content="He poured rocks in the dungeon of his mind.", createdAt="Wed Nov 24 2021 17:19:55", updatedAt="Tue Nov 09 2021 10:48:40")
    comment216b = Comment(videoId=649, channelId=59, content="Nothing is as cautiously cuddly as a pet porcupine.", createdAt="Fri Oct 01 2021 16:59:31", updatedAt="Thu Apr 07 2022 13:31:54")
    comment217b = Comment(videoId=56, channelId=88, content="The truth is that you pay for your lifestyle in hours.", createdAt="Wed Apr 06 2022 03:15:22", updatedAt="Sat Jan 22 2022 16:02:17")
    comment218b = Comment(videoId=604, channelId=82, content="You're unsure whether or not to trust him, but very thankful that you wore a turtle neck.", createdAt="Thu Nov 18 2021 02:07:45", updatedAt="Sat Jun 05 2021 00:55:55")
    comment219b = Comment(videoId=703, channelId=33, content="They did nothing as the raccoon attacked the lady’s bag of food.", createdAt="Thu Nov 04 2021 10:01:09", updatedAt="Fri Jan 14 2022 05:59:05")
    comment220b = Comment(videoId=590, channelId=36, content="It's much more difficult to play tennis with a bowling ball than it is to bowl with a tennis ball.", createdAt="Thu Nov 18 2021 22:30:15", updatedAt="Fri Nov 19 2021 21:59:28")
    comment221b = Comment(videoId=35, channelId=26, content="The stranger officiates the meal.", createdAt="Tue Jun 08 2021 20:21:02", updatedAt="Wed Mar 09 2022 18:38:08")
    comment222b = Comment(videoId=475, channelId=50, content="He fumbled in the darkness looking for the light switch, but when he finally found it there was someone already there.", createdAt="Thu Oct 21 2021 08:22:44", updatedAt="Wed Mar 16 2022 23:39:12")
    comment223b = Comment(videoId=143, channelId=41, content="Hang on, my kittens are scratching at the bathtub and they'll upset by the lack of biscuits.", createdAt="Thu May 06 2021 19:16:42", updatedAt="Fri Mar 11 2022 10:49:50")
    comment224b = Comment(videoId=357, channelId=1, content="There was coal in his stocking and he was thrilled.", createdAt="Sat Jul 24 2021 10:10:10", updatedAt="Tue Dec 28 2021 00:45:08")
    comment225b = Comment(videoId=698, channelId=58, content="He was disappointed when he found the beach to be so sandy and the sun so sunny.", createdAt="Wed Jan 19 2022 10:18:39", updatedAt="Thu Jun 10 2021 12:43:02")
    comment226b = Comment(videoId=764, channelId=71, content="The ice-cream trucks bring back bad memories for all of us.", createdAt="Mon Aug 30 2021 06:32:25", updatedAt="Thu Mar 10 2022 21:03:30")
    comment227b = Comment(videoId=685, channelId=9, content="The Tsunami wave crashed against the raised houses and broke the pilings as if they were toothpicks.", createdAt="Thu Jan 06 2022 00:13:25", updatedAt="Thu Dec 16 2021 16:02:58")
    comment228b = Comment(videoId=200, channelId=13, content="When she didn’t like a guy who was trying to pick her up, she started using sign language.", createdAt="Sat Oct 23 2021 15:36:25", updatedAt="Sun Mar 13 2022 18:39:24")
    comment229b = Comment(videoId=659, channelId=54, content="Her daily goal was to improve on yesterday.", createdAt="Wed Dec 08 2021 23:28:16", updatedAt="Sun Mar 13 2022 19:16:20")
    comment230b = Comment(videoId=75, channelId=71, content="I would be delighted if the sea were full of cucumber juice.", createdAt="Thu Sep 16 2021 23:16:27", updatedAt="Wed Jan 12 2022 14:09:06")
    comment231b = Comment(videoId=131, channelId=62, content="He picked up trash in his spare time to dump in his neighbor's yard.", createdAt="Sun Aug 29 2021 06:01:36", updatedAt="Thu Jun 03 2021 04:05:09")
    comment233b = Comment(videoId=515, channelId=28, content="It was at that moment that he learned there are certain parts of the body that you should never Nair.", createdAt="Sat Jul 24 2021 01:13:46", updatedAt="Wed Feb 02 2022 07:39:28")
    comment234b = Comment(videoId=650, channelId=71, content="Abstraction is often one floor above you.", createdAt="Sun Aug 01 2021 19:03:00", updatedAt="Tue Apr 05 2022 13:40:38")
    comment235b = Comment(videoId=244, channelId=56, content="Written warnings in instruction manuals are worthless since rabbits can't read.", createdAt="Tue Mar 08 2022 04:04:20", updatedAt="Sun Dec 12 2021 06:28:58")
    comment236b = Comment(videoId=80, channelId=94, content="The tortoise jumped into the lake with dreams of becoming a sea turtle.", createdAt="Fri Feb 04 2022 07:22:41", updatedAt="Fri Feb 18 2022 22:47:44")
    comment237b = Comment(videoId=764, channelId=39, content="Despite what your teacher may have told you, there is a wrong way to wield a lasso.", createdAt="Wed Mar 23 2022 21:37:03", updatedAt="Wed Jan 19 2022 19:10:25")
    comment238b = Comment(videoId=421, channelId=60, content="Pink horses galloped across the sea.", createdAt="Fri Jan 07 2022 21:43:14", updatedAt="Sun Sep 19 2021 10:03:41")
    comment239b = Comment(videoId=5, channelId=37, content="It's not often you find a soggy banana on the street.", createdAt="Tue Apr 05 2022 04:45:29", updatedAt="Sun Aug 29 2021 19:46:57")
    comment240b = Comment(videoId=289, channelId=18, content="She says she has the ability to hear the soundtrack of your life.", createdAt="Tue Aug 24 2021 09:50:05", updatedAt="Mon Feb 21 2022 22:12:46")
    comment241b = Comment(videoId=761, channelId=61, content="They desperately needed another drummer since the current one only knew how to play bongos.", createdAt="Sat Apr 09 2022 05:09:43", updatedAt="Mon Nov 22 2021 19:20:45")
    comment242b = Comment(videoId=676, channelId=35, content="It was a really good Monday for being a Saturday.", createdAt="Mon Jan 03 2022 06:12:45", updatedAt="Mon Sep 27 2021 04:26:10")
    comment243b = Comment(videoId=373, channelId=7, content="The thick foliage and intertwined vines made the hike nearly impossible.", createdAt="Sat Mar 05 2022 18:38:26", updatedAt="Sun Aug 08 2021 02:50:59")
    comment244b = Comment(videoId=102, channelId=47, content="Let me help you with your baggage.", createdAt="Wed May 05 2021 13:46:05", updatedAt="Wed Aug 04 2021 17:17:16")
    comment245b = Comment(videoId=520, channelId=49, content="Lets all be unique together until we realise we are all the same.", createdAt="Sat May 08 2021 00:50:45", updatedAt="Fri Dec 31 2021 02:08:45")
    comment246b = Comment(videoId=676, channelId=68, content="The sky is clear; the stars are twinkling.", createdAt="Fri Nov 05 2021 03:46:31", updatedAt="Sun Apr 18 2021 21:04:28")
    comment247b = Comment(videoId=524, channelId=64, content="The sign said there was road work ahead so he decided to speed up.", createdAt="Tue Jan 18 2022 13:25:11", updatedAt="Fri May 28 2021 05:08:41")
    comment248b = Comment(videoId=521, channelId=23, content="I caught my squirrel rustling through my gym bag.", createdAt="Sat Feb 26 2022 00:15:24", updatedAt="Fri Jun 18 2021 03:44:07")
    comment249b = Comment(videoId=44, channelId=22, content="They finished building the road they knew no one would ever use.", createdAt="Fri Aug 27 2021 07:23:54", updatedAt="Tue Jan 11 2022 01:16:48")
    comment250b = Comment(videoId=267, channelId=62, content="The tumbleweed refused to tumble but was more than willing to prance.", createdAt="Fri Jul 02 2021 03:21:19", updatedAt="Sun Sep 19 2021 15:43:40")
    comment251b = Comment(videoId=479, channelId=85, content="She had a habit of taking showers in lemonade.", createdAt="Thu Aug 26 2021 00:19:39", updatedAt="Thu Apr 15 2021 00:37:06")
    comment252b = Comment(videoId=720, channelId=61, content="This is the last random sentence I will be writing and I am going to stop mid-sent", createdAt="Mon Jan 03 2022 21:53:48", updatedAt="Mon Jul 26 2021 02:07:34")
    comment253b = Comment(videoId=725, channelId=64, content="She can live her life however she wants as long as she listens to what I have to say.", createdAt="Thu Oct 07 2021 07:50:50", updatedAt="Thu Jan 20 2022 03:07:00")
    comment254b = Comment(videoId=284, channelId=33, content="My Mum tries to be cool by saying that she likes all the same things that I do.", createdAt="Fri Nov 05 2021 15:31:18", updatedAt="Fri May 07 2021 03:35:39")
    comment255b = Comment(videoId=683, channelId=96, content="Improve your goldfish's physical fitness by getting him a bicycle.", createdAt="Wed Jun 02 2021 06:44:56", updatedAt="Sat May 01 2021 23:38:46")
    comment256b = Comment(videoId=714, channelId=85, content="They called out her name time and again, but were met with nothing but silence.", createdAt="Sat May 01 2021 14:44:35", updatedAt="Sun Dec 26 2021 04:18:32")
    comment257b = Comment(videoId=730, channelId=72, content="We need to rent a room for our party.", createdAt="Mon Feb 28 2022 17:39:57", updatedAt="Fri Jun 11 2021 09:56:37")
    comment258b = Comment(videoId=522, channelId=90, content="Buried deep in the snow, he hoped his batteries were fresh in his avalanche beacon.", createdAt="Tue Aug 03 2021 03:41:35", updatedAt="Sun Mar 06 2022 19:27:06")
    comment259b = Comment(videoId=515, channelId=9, content="She wore green lipstick like a fashion icon.", createdAt="Thu Apr 15 2021 23:06:49", updatedAt="Wed Jul 14 2021 17:32:19")
    comment260b = Comment(videoId=194, channelId=82, content="When I cook spaghetti, I like to boil it a few minutes past al dente so the noodles are super slippery.", createdAt="Thu Mar 24 2022 07:33:37", updatedAt="Wed Dec 29 2021 01:00:43")
    comment261b = Comment(videoId=574, channelId=54, content="Strawberries must be the one food that doesn't go well with this brand of paint.", createdAt="Fri Feb 11 2022 02:13:00", updatedAt="Sat May 22 2021 18:04:32")
    comment262b = Comment(videoId=194, channelId=40, content="The Japanese yen for commerce is still well-known.", createdAt="Mon Aug 23 2021 19:42:40", updatedAt="Tue Mar 22 2022 23:46:52")
    comment263b = Comment(videoId=542, channelId=81, content="Everyone pretends to like wheat until you mention barley.", createdAt="Mon Nov 29 2021 02:57:50", updatedAt="Thu Jul 01 2021 06:14:01")
    comment264b = Comment(videoId=480, channelId=18, content="He is good at eating pickles and telling women about his emotional problems.", createdAt="Mon Oct 11 2021 01:28:16", updatedAt="Tue Jan 18 2022 08:16:31")
    comment265b = Comment(videoId=379, channelId=48, content="He was the only member of the club who didn't like plum pudding.", createdAt="Sat Sep 25 2021 11:11:06", updatedAt="Thu Nov 18 2021 09:04:55")
    comment266b = Comment(videoId=307, channelId=38, content="The pigs were insulted that they were named hamburgers.", createdAt="Thu Sep 16 2021 00:39:00", updatedAt="Mon Jul 19 2021 18:30:23")
    comment268b = Comment(videoId=260, channelId=4, content="My uncle's favorite pastime was building cars out of noodles.", createdAt="Sat Jan 15 2022 19:39:18", updatedAt="Tue Mar 08 2022 06:34:30")
    comment269b = Comment(videoId=242, channelId=1, content="He's in a boy band which doesn't make much sense for a snake.", createdAt="Fri Nov 05 2021 14:13:01", updatedAt="Fri Nov 05 2021 12:28:55")
    comment270b = Comment(videoId=496, channelId=46, content="She did not cheat on the test, for it was not the right thing to do.", createdAt="Sat Jul 03 2021 22:32:48", updatedAt="Tue Jun 22 2021 09:31:05")
    comment271b = Comment(videoId=567, channelId=84, content="She was sad to hear that fireflies are facing extinction due to artificial light, habitat loss, and pesticides.", createdAt="Sun Mar 20 2022 22:32:56", updatedAt="Mon Mar 28 2022 12:30:59")
    comment272b = Comment(videoId=144, channelId=45, content="It doesn't sound like that will ever be on my travel list.", createdAt="Fri Jul 16 2021 20:18:52", updatedAt="Mon Jan 10 2022 01:02:06")
    comment273b = Comment(videoId=726, channelId=100, content="The Guinea fowl flies through the air with all the grace of a turtle.", createdAt="Mon Mar 07 2022 02:35:16", updatedAt="Mon Jan 03 2022 21:40:01")
    comment274b = Comment(videoId=478, channelId=19, content="Plans for this weekend include turning wine into water.", createdAt="Fri Jul 23 2021 02:07:30", updatedAt="Sun Nov 28 2021 04:35:35")
    comment276b = Comment(videoId=211, channelId=77, content="The urgent care center was flooded with patients after the news of a new deadly virus was made public.", createdAt="Wed Jan 19 2022 10:09:53", updatedAt="Thu Jul 01 2021 01:19:31")
    comment277b = Comment(videoId=279, channelId=71, content="It took him a while to realize that everything he decided not to change, he was actually choosing.", createdAt="Tue Dec 07 2021 20:03:01", updatedAt="Wed Jan 19 2022 20:55:57")
    comment278b = Comment(videoId=610, channelId=74, content="Every manager should be able to recite at least ten nursery rhymes backward.", createdAt="Sun Apr 03 2022 10:05:52", updatedAt="Sat Mar 19 2022 22:58:30")
    comment280b = Comment(videoId=689, channelId=11, content="He had accidentally hacked into his company's server.", createdAt="Fri Mar 25 2022 04:19:22", updatedAt="Fri Sep 10 2021 12:25:30")
    comment281b = Comment(videoId=142, channelId=90, content="I only enjoy window shopping when the windows are transparent.", createdAt="Sat Jan 29 2022 20:11:07", updatedAt="Tue Oct 12 2021 09:49:44")
    comment282b = Comment(videoId=218, channelId=63, content="I come from a tribe of head-hunters, so I will never need a shrink.", createdAt="Sat Jan 15 2022 18:01:44", updatedAt="Mon Feb 14 2022 13:32:45")
    comment283b = Comment(videoId=711, channelId=58, content="He played the game as if his life depended on it and the truth was that it did.", createdAt="Tue Jul 06 2021 23:15:32", updatedAt="Sat Dec 04 2021 07:36:36")
    comment284b = Comment(videoId=129, channelId=12, content="She hadn't had her cup of coffee, and that made things all the worse.", createdAt="Fri Dec 03 2021 06:01:09", updatedAt="Sun Mar 27 2022 04:41:22")
    comment285b = Comment(videoId=295, channelId=30, content="If you don't like toenails, you probably shouldn't look at your feet.", createdAt="Thu Jul 29 2021 11:42:25", updatedAt="Sat Nov 20 2021 18:06:53")
    comment286b = Comment(videoId=439, channelId=29, content="The secret code they created made no sense, even to them.", createdAt="Thu Apr 22 2021 19:36:25", updatedAt="Sun Nov 21 2021 03:53:26")
    comment287b = Comment(videoId=466, channelId=32, content="The best key lime pie is still up for debate.", createdAt="Thu Mar 24 2022 10:13:42", updatedAt="Wed Jul 28 2021 21:37:00")
    comment288b = Comment(videoId=229, channelId=70, content="Pair your designer cowboy hat with scuba gear for a memorable occasion.", createdAt="Thu Nov 18 2021 08:12:37", updatedAt="Wed Aug 18 2021 19:35:51")
    comment289b = Comment(videoId=22, channelId=51, content="Sometimes, all you need to do is completely make an ass of yourself and laugh it off to realise that life isn’t so bad after all.", createdAt="Fri Jul 09 2021 13:06:48", updatedAt="Thu Mar 10 2022 00:39:41")
    comment290b = Comment(videoId=729, channelId=7, content="We have a lot of rain in June.", createdAt="Thu Apr 22 2021 17:58:45", updatedAt="Mon Aug 02 2021 06:26:11")
    comment291b = Comment(videoId=240, channelId=48, content="The spa attendant applied the deep cleaning mask to the gentleman’s back.", createdAt="Fri Dec 31 2021 04:53:17", updatedAt="Sat Dec 25 2021 04:29:18")
    comment292b = Comment(videoId=428, channelId=27, content="I want more detailed information.", createdAt="Mon Jun 21 2021 18:26:52", updatedAt="Mon Jul 26 2021 07:32:13")
    comment293b = Comment(videoId=233, channelId=26, content="There were three sphered rocks congregating in a cubed room.", createdAt="Sun May 02 2021 13:10:14", updatedAt="Mon Dec 27 2021 02:25:06")
    comment294b = Comment(videoId=756, channelId=87, content="Happiness can be found in the depths of chocolate pudding.", createdAt="Mon Sep 13 2021 17:59:12", updatedAt="Mon Feb 28 2022 19:34:56")
    comment295b = Comment(videoId=173, channelId=92, content="People keep telling me \"orange\" but I still prefer \"pink\".", createdAt="Sat Jul 31 2021 18:10:14", updatedAt="Wed Mar 23 2022 02:41:55")
    comment296b = Comment(videoId=673, channelId=63, content="He would only survive if he kept the fire going and he could hear thunder in the distance.", createdAt="Mon Jan 17 2022 18:14:31", updatedAt="Fri Sep 03 2021 01:58:23")
    comment297b = Comment(videoId=364, channelId=99, content="Random words in front of other random words create a random sentence.", createdAt="Wed May 12 2021 12:23:36", updatedAt="Wed Jan 26 2022 19:45:50")
    comment298b = Comment(videoId=490, channelId=68, content="The team members were hard to tell apart since they all wore their hair in a ponytail.", createdAt="Wed Aug 18 2021 12:31:52", updatedAt="Thu Jul 01 2021 02:55:23")
    comment299b = Comment(videoId=37, channelId=80, content="So long and thanks for the fish.", createdAt="Tue Jan 04 2022 01:00:27", updatedAt="Sat Jul 31 2021 10:02:39")
    comment300b = Comment(videoId=596, channelId=1, content="Traveling became almost extinct during the pandemic.", createdAt="Mon Jan 03 2022 12:54:40", updatedAt="Sat Jul 03 2021 18:33:48")
    comment301b = Comment(videoId=317, channelId=97, content="He invested some skill points in Charisma and Strength.", createdAt="Sat Sep 25 2021 08:31:21", updatedAt="Fri May 07 2021 14:59:53")
    comment302b = Comment(videoId=458, channelId=54, content="The busker hoped that the people passing by would throw money, but they threw tomatoes instead, so he exchanged his hat for a juicer.", createdAt="Wed Dec 22 2021 18:00:25", updatedAt="Tue Mar 22 2022 15:35:51")
    comment303b = Comment(videoId=121, channelId=6, content="She wondered what his eyes were saying beneath his mirrored sunglasses.", createdAt="Mon Sep 13 2021 18:56:01", updatedAt="Tue Nov 16 2021 13:07:52")
    comment304b = Comment(videoId=344, channelId=21, content="The toddler’s endless tantrum caused the entire plane anxiety.", createdAt="Sun Oct 03 2021 21:44:41", updatedAt="Mon Jun 28 2021 19:54:59")
    comment305b = Comment(videoId=447, channelId=1, content="Thirty years later, she still thought it was okay to put the toilet paper roll under rather than over.", createdAt="Mon Feb 14 2022 17:01:09", updatedAt="Fri Aug 13 2021 05:48:11")
    comment306b = Comment(videoId=311, channelId=17, content="You should never take advice from someone who thinks red paint dries quicker than blue paint.", createdAt="Thu Jun 03 2021 22:28:17", updatedAt="Sun Mar 20 2022 19:47:22")
    comment307b = Comment(videoId=252, channelId=17, content="She couldn't decide of the glass was half empty or half full so she drank it.", createdAt="Sun Nov 21 2021 08:07:24", updatedAt="Mon Nov 01 2021 06:16:51")
    comment308b = Comment(videoId=603, channelId=87, content="He was the only member of the club who didn't like plum pudding.", createdAt="Mon May 17 2021 17:32:25", updatedAt="Sat Apr 24 2021 04:37:02")
    comment309b = Comment(videoId=605, channelId=71, content="The bees decided to have a mutiny against their queen.", createdAt="Tue Nov 09 2021 07:04:13", updatedAt="Sat Apr 17 2021 10:41:19")
    comment310b = Comment(videoId=692, channelId=35, content="He dreamed of eating green apples with worms.", createdAt="Sat Jan 08 2022 22:11:34", updatedAt="Sat Dec 25 2021 18:37:59")
    comment311b = Comment(videoId=171, channelId=39, content="The near-death experience brought new ideas to light.", createdAt="Tue Feb 08 2022 18:48:42", updatedAt="Sun Jan 09 2022 08:53:22")
    comment312b = Comment(videoId=376, channelId=43, content="Potato wedges probably are not best for relationships.", createdAt="Tue Sep 28 2021 02:07:57", updatedAt="Sun Aug 01 2021 06:24:22")
    comment313b = Comment(videoId=464, channelId=59, content="It's always a good idea to seek shelter from the evil gaze of the sun.", createdAt="Sun Nov 07 2021 23:34:45", updatedAt="Sat Feb 26 2022 07:10:32")
    comment314b = Comment(videoId=144, channelId=45, content="As he entered the church he could hear the soft voice of someone whispering into a cell phone.", createdAt="Sun Jan 23 2022 16:37:44", updatedAt="Tue Sep 14 2021 04:40:38")
    comment315b = Comment(videoId=183, channelId=100, content="There was no ice cream in the freezer, nor did they have money to go to the store.", createdAt="Mon Jul 12 2021 20:17:52", updatedAt="Mon Nov 22 2021 13:33:12")
    comment316b = Comment(videoId=443, channelId=90, content="He wondered if it could be called a beach if there was no sand.", createdAt="Wed Nov 03 2021 07:37:06", updatedAt="Mon Nov 22 2021 23:11:55")
    comment317b = Comment(videoId=83, channelId=82, content="Watching the geriatric men’s softball team brought back memories of 3 yr olds playing t-ball.", createdAt="Mon Mar 14 2022 23:33:52", updatedAt="Mon Mar 21 2022 20:35:29")
    comment319b = Comment(videoId=61, channelId=2, content="Harrold felt confident that nobody would ever suspect his spy pigeon.", createdAt="Sat Apr 09 2022 08:15:45", updatedAt="Thu Aug 19 2021 22:11:37")
    comment320b = Comment(videoId=124, channelId=18, content="Bill ran from the giraffe toward the dolphin.", createdAt="Thu Feb 17 2022 08:06:59", updatedAt="Sun Oct 10 2021 13:43:38")
    comment321b = Comment(videoId=409, channelId=17, content="Although it wasn't a pot of gold, Nancy was still enthralled at what she found at the end of the rainbow.", createdAt="Tue Dec 21 2021 11:00:16", updatedAt="Sat Nov 06 2021 04:09:51")
    comment322b = Comment(videoId=700, channelId=9, content="There was no telling what thoughts would come from the machine.", createdAt="Sat Jun 05 2021 15:15:18", updatedAt="Thu Nov 04 2021 08:17:16")
    comment323b = Comment(videoId=654, channelId=81, content="The fence was confused about whether it was supposed to keep things in or keep things out.", createdAt="Tue Mar 08 2022 18:07:49", updatedAt="Mon Oct 18 2021 19:14:11")
    comment324b = Comment(videoId=578, channelId=24, content="The memory we used to share is no longer coherent.", createdAt="Sat Mar 26 2022 10:08:11", updatedAt="Mon Feb 28 2022 14:36:48")
    comment326b = Comment(videoId=365, channelId=2, content="She folded her handkerchief neatly.", createdAt="Sun Oct 03 2021 22:59:07", updatedAt="Sun Nov 21 2021 09:59:15")
    comment327b = Comment(videoId=740, channelId=55, content="She had some amazing news to share but nobody to share it with.", createdAt="Thu Jan 20 2022 14:20:21", updatedAt="Mon Jun 21 2021 05:31:18")
    comment328b = Comment(videoId=230, channelId=99, content="It doesn't sound like that will ever be on my travel list.", createdAt="Sat Sep 25 2021 19:20:41", updatedAt="Wed Jan 12 2022 00:39:35")
    comment329b = Comment(videoId=365, channelId=31, content="They throw cabbage that turns your brain into emotional baggage.", createdAt="Sat Nov 13 2021 12:16:41", updatedAt="Sun Dec 12 2021 14:04:24")
    comment330b = Comment(videoId=533, channelId=62, content="Gary didn't understand why Doug went upstairs to get one dollar bills when he invited him to go cow tipping.", createdAt="Sat Apr 17 2021 16:11:23", updatedAt="Sun May 16 2021 03:21:36")
    comment331b = Comment(videoId=615, channelId=89, content="I liked their first two albums but changed my mind after that charity gig.", createdAt="Sun Apr 25 2021 07:58:48", updatedAt="Wed Oct 20 2021 00:40:04")
    comment332b = Comment(videoId=104, channelId=42, content="Twin 4-month-olds slept in the shade of the palm tree while the mother tanned in the sun.", createdAt="Mon Feb 14 2022 00:27:09", updatedAt="Wed Feb 16 2022 01:09:39")
    comment333b = Comment(videoId=415, channelId=5, content="Always bring cinnamon buns on a deep-sea diving expedition.", createdAt="Tue Jul 27 2021 21:56:13", updatedAt="Wed Mar 09 2022 00:58:25")
    comment334b = Comment(videoId=371, channelId=8, content="The body piercing didn't go exactly as he expected.", createdAt="Sat Oct 16 2021 15:30:13", updatedAt="Wed Dec 15 2021 18:56:58")
    comment335b = Comment(videoId=396, channelId=71, content="You'll see the rainbow bridge after it rains cats and dogs.", createdAt="Thu Feb 24 2022 08:51:20", updatedAt="Sat Jul 10 2021 20:03:47")
    comment336b = Comment(videoId=453, channelId=69, content="You realize you're not alone as you sit in your bedroom massaging your calves after a long day of playing tug-of-war with Grandpa Joe in the hospital.", createdAt="Fri Dec 31 2021 19:11:36", updatedAt="Fri Mar 11 2022 21:19:38")
    comment337b = Comment(videoId=604, channelId=18, content="In hopes of finding out the truth, he entered the one-room library.", createdAt="Wed Jul 21 2021 09:22:16", updatedAt="Thu Feb 17 2022 00:39:43")
    comment338b = Comment(videoId=470, channelId=20, content="You bite up because of your lower jaw.", createdAt="Fri Mar 11 2022 11:16:38", updatedAt="Fri Apr 08 2022 19:42:17")
    comment339b = Comment(videoId=436, channelId=81, content="As time wore on, simple dog commands turned into full paragraphs explaining why the dog couldn’t do something.", createdAt="Thu Aug 12 2021 16:36:32", updatedAt="Sun Sep 05 2021 11:40:57")
    comment340b = Comment(videoId=369, channelId=84, content="The opportunity of a lifetime passed before him as he tried to decide between a cone or a cup.", createdAt="Tue May 04 2021 04:30:00", updatedAt="Tue Jan 11 2022 19:36:19")
    comment341b = Comment(videoId=196, channelId=2, content="It was difficult for Mary to admit that most of her workout consisted of exercising poor judgment.", createdAt="Sun Apr 10 2022 09:10:47", updatedAt="Wed Jun 23 2021 13:03:10")
    comment342b = Comment(videoId=76, channelId=80, content="Thigh-high in the water, the fisherman’s hope for dinner soon turned to despair.", createdAt="Tue Mar 15 2022 11:07:37", updatedAt="Wed Nov 24 2021 22:19:08")
    comment343b = Comment(videoId=244, channelId=22, content="I had a friend in high school named Rick Shaw, but he was fairly useless as a mode of transport.", createdAt="Sat Mar 26 2022 16:00:34", updatedAt="Thu Oct 14 2021 15:58:11")
    comment344b = Comment(videoId=133, channelId=63, content="Joe discovered that traffic cones make excellent megaphones.", createdAt="Mon Apr 26 2021 21:31:50", updatedAt="Mon Feb 14 2022 04:53:03")
    comment345b = Comment(videoId=631, channelId=87, content="I love bacon, beer, birds, and baboons.", createdAt="Thu Oct 07 2021 00:07:37", updatedAt="Sun Nov 07 2021 03:49:38")
    comment346b = Comment(videoId=726, channelId=31, content="The secret ingredient to his wonderful life was crime.", createdAt="Fri Oct 15 2021 03:11:02", updatedAt="Sun Jun 27 2021 12:53:07")
    comment347b = Comment(videoId=344, channelId=64, content="Mom didn’t understand why no one else wanted a hot tub full of jello.", createdAt="Mon Aug 09 2021 09:29:46", updatedAt="Thu Aug 05 2021 04:09:43")
    comment348b = Comment(videoId=229, channelId=72, content="While on the first date he accidentally hit his head on the beam.", createdAt="Sun Apr 03 2022 15:13:41", updatedAt="Mon Mar 28 2022 06:13:37")
    comment349b = Comment(videoId=400, channelId=73, content="The bug was having an excellent day until he hit the windshield.", createdAt="Tue Feb 15 2022 01:57:01", updatedAt="Fri Apr 01 2022 22:13:22")
    comment350b = Comment(videoId=316, channelId=72, content="She did her best to help him.", createdAt="Sat Dec 11 2021 00:01:53", updatedAt="Mon May 17 2021 23:46:57")
    comment351b = Comment(videoId=740, channelId=100, content="One small action would change her life, but whether it would be for better or for worse was yet to be determined.", createdAt="Tue Jul 13 2021 13:05:28", updatedAt="Sun Aug 29 2021 09:20:02")
    comment352b = Comment(videoId=393, channelId=12, content="He had a vague sense that trees gave birth to dinosaurs.", createdAt="Tue Nov 09 2021 05:44:46", updatedAt="Thu Jun 10 2021 00:17:13")
    comment353b = Comment(videoId=217, channelId=45, content="The external scars tell only part of the story.", createdAt="Sat Jun 19 2021 10:59:56", updatedAt="Mon Jan 03 2022 04:16:39")
    comment354b = Comment(videoId=779, channelId=6, content="Mary plays the piano.", createdAt="Tue Nov 30 2021 23:27:49", updatedAt="Tue Aug 24 2021 12:42:38")
    comment355b = Comment(videoId=362, channelId=3, content="She had the gift of being able to paint songs.", createdAt="Tue Oct 05 2021 14:12:59", updatedAt="Fri Nov 12 2021 04:57:43")
    comment356b = Comment(videoId=331, channelId=24, content="His confidence would have bee admirable if it wasn't for his stupidity.", createdAt="Wed Mar 02 2022 03:57:53", updatedAt="Tue Sep 07 2021 20:40:10")
    comment357b = Comment(videoId=492, channelId=33, content="I had a friend in high school named Rick Shaw, but he was fairly useless as a mode of transport.", createdAt="Wed Dec 29 2021 18:28:37", updatedAt="Wed May 12 2021 06:34:44")
    comment358b = Comment(videoId=496, channelId=21, content="The waves were crashing on the shore; it was a lovely sight.", createdAt="Fri May 14 2021 02:02:10", updatedAt="Wed Sep 08 2021 12:13:02")
    comment359b = Comment(videoId=325, channelId=57, content="She finally understood that grief was her love with no place for it to go.", createdAt="Sat Aug 07 2021 13:22:51", updatedAt="Mon May 17 2021 14:14:42")
    comment360b = Comment(videoId=739, channelId=41, content="Joe made the sugar cookies; Susan decorated them.", createdAt="Mon Nov 29 2021 22:27:43", updatedAt="Thu Sep 16 2021 19:42:17")
    comment361b = Comment(videoId=135, channelId=94, content="He told us a very exciting adventure story.", createdAt="Sun Dec 12 2021 20:06:22", updatedAt="Mon Oct 25 2021 13:39:54")
    comment362b = Comment(videoId=637, channelId=55, content="She used her own hair in the soup to give it more flavor.", createdAt="Wed Aug 18 2021 16:58:05", updatedAt="Sun Mar 27 2022 21:13:32")
    comment363b = Comment(videoId=542, channelId=51, content="He was disappointed when he found the beach to be so sandy and the sun so sunny.", createdAt="Fri May 14 2021 23:07:48", updatedAt="Wed Dec 15 2021 16:44:58")
    comment364b = Comment(videoId=714, channelId=61, content="For the 216th time, he said he would quit drinking soda after this last Coke.", createdAt="Sun Sep 19 2021 08:41:42", updatedAt="Sun Feb 13 2022 12:29:26")
    comment365b = Comment(videoId=376, channelId=43, content="He had decided to accept his fate of accepting his fate.", createdAt="Tue Aug 03 2021 20:47:16", updatedAt="Mon Mar 28 2022 17:41:09")
    comment366b = Comment(videoId=33, channelId=42, content="It's never comforting to know that your fate depends on something as unpredictable as the popping of corn.", createdAt="Wed Jul 14 2021 00:14:43", updatedAt="Mon Dec 06 2021 00:31:54")
    comment367b = Comment(videoId=65, channelId=15, content="The fog was so dense even a laser decided it wasn't worth the effort.", createdAt="Wed Sep 15 2021 01:09:25", updatedAt="Thu Apr 15 2021 03:59:00")
    comment368b = Comment(videoId=87, channelId=8, content="The pet shop stocks everything you need to keep your anaconda happy.", createdAt="Thu Feb 03 2022 03:32:28", updatedAt="Sat Sep 11 2021 09:37:32")
    comment369b = Comment(videoId=379, channelId=56, content="Mary realized if her calculator had a history, it would be more embarrassing than her computer browser history.", createdAt="Mon Apr 26 2021 02:54:47", updatedAt="Thu Jun 24 2021 02:37:45")
    comment371b = Comment(videoId=617, channelId=60, content="Pink horses galloped across the sea.", createdAt="Fri Jan 21 2022 16:02:14", updatedAt="Thu Aug 26 2021 10:32:03")
    comment372b = Comment(videoId=406, channelId=84, content="Most shark attacks occur about 10 feet from the beach since that's where the people are.", createdAt="Wed Oct 20 2021 17:46:14", updatedAt="Mon May 03 2021 07:15:46")
    comment373b = Comment(videoId=614, channelId=27, content="He learned the hardest lesson of his life and had the scars, both physical and mental, to prove it.", createdAt="Tue Nov 02 2021 17:28:15", updatedAt="Sat Apr 02 2022 11:18:44")
    comment374b = Comment(videoId=697, channelId=66, content="If you really strain your ears, you can just about hear the sound of no one giving a damn.", createdAt="Sat Jan 22 2022 06:36:23", updatedAt="Sat Jan 22 2022 02:50:37")
    comment375b = Comment(videoId=181, channelId=26, content="Three generations with six decades of life experience.", createdAt="Thu Sep 09 2021 07:14:47", updatedAt="Fri Nov 26 2021 02:27:38")
    comment376b = Comment(videoId=292, channelId=18, content="This made him feel like an old-style rootbeer float smells.", createdAt="Wed Mar 02 2022 21:13:59", updatedAt="Tue May 04 2021 20:40:28")
    comment377b = Comment(videoId=374, channelId=93, content="Despite multiple complications and her near-death experience", createdAt="Wed Jun 02 2021 11:48:27", updatedAt="Mon Jan 03 2022 14:11:45")
    comment378b = Comment(videoId=749, channelId=29, content="He wore the surgical mask in public not to keep from catching a virus, but to keep people away from him.", createdAt="Mon Apr 26 2021 05:00:12", updatedAt="Thu Mar 03 2022 03:19:15")
    comment379b = Comment(videoId=295, channelId=22, content="She wrote him a long letter, but he didn't read it.", createdAt="Mon Jan 31 2022 12:20:24", updatedAt="Tue Mar 29 2022 18:34:23")
    comment380b = Comment(videoId=391, channelId=47, content="The most exciting eureka moment I've had was when I realized that the instructions on food packets were just guidelines.", createdAt="Thu Jul 15 2021 12:51:14", updatedAt="Tue May 04 2021 08:54:20")
    comment381b = Comment(videoId=666, channelId=96, content="There should have been a time and a place, but this wasn't it.", createdAt="Mon Jan 17 2022 06:46:14", updatedAt="Sun Jul 11 2021 21:22:31")
    comment382b = Comment(videoId=608, channelId=96, content="Everybody should read Chaucer to improve their everyday vocabulary.", createdAt="Sun Sep 12 2021 05:37:10", updatedAt="Mon Jan 10 2022 20:14:17")
    comment383b = Comment(videoId=306, channelId=51, content="Andy loved to sleep on a bed of nails.", createdAt="Mon Jun 07 2021 12:08:23", updatedAt="Tue Jul 27 2021 12:54:32")
    comment384b = Comment(videoId=578, channelId=5, content="He wasn't bitter that she had moved on but from the radish.", createdAt="Sat Jan 15 2022 15:14:06", updatedAt="Sat Jul 10 2021 13:32:31")
    comment385b = Comment(videoId=652, channelId=93, content="We have a lot of rain in June.", createdAt="Tue Aug 03 2021 10:38:30", updatedAt="Mon May 17 2021 13:50:11")
    comment386b = Comment(videoId=616, channelId=4, content="Everyone pretends to like wheat until you mention barley.", createdAt="Sat Feb 12 2022 21:00:15", updatedAt="Sat Jan 29 2022 13:03:43")
    comment387b = Comment(videoId=378, channelId=97, content="He was all business when he wore his clown suit.", createdAt="Fri Jan 21 2022 09:12:10", updatedAt="Fri Apr 30 2021 00:59:32")
    comment388b = Comment(videoId=650, channelId=40, content="I used to live in my neighbor's fishpond, but the aesthetic wasn't to my taste.", createdAt="Wed Jan 12 2022 17:20:33", updatedAt="Fri Feb 04 2022 07:40:24")
    comment389b = Comment(videoId=94, channelId=11, content="Honestly, I didn't care much for the first season, so I didn't bother with the second.", createdAt="Tue Aug 24 2021 01:12:39", updatedAt="Sun Jan 23 2022 01:16:40")
    comment390b = Comment(videoId=265, channelId=83, content="Some bathing suits just shouldn’t be worn by some people.", createdAt="Sat May 15 2021 08:21:57", updatedAt="Wed Sep 01 2021 22:41:38")
    comment391b = Comment(videoId=420, channelId=98, content="Martha came to the conclusion that shake weights are a great gift for any occasion.", createdAt="Thu Jul 22 2021 23:12:55", updatedAt="Tue Jun 29 2021 20:03:49")
    comment392b = Comment(videoId=192, channelId=92, content="He appeared to be confusingly perplexed.", createdAt="Sat Apr 02 2022 03:37:06", updatedAt="Fri Jul 23 2021 05:57:32")
    comment393b = Comment(videoId=238, channelId=73, content="I’m a living furnace.", createdAt="Fri Jun 11 2021 15:43:28", updatedAt="Thu Apr 29 2021 23:07:42")
    comment394b = Comment(videoId=294, channelId=34, content="She is never happy until she finds something to be unhappy about; then, she is overjoyed.", createdAt="Wed Nov 10 2021 01:24:19", updatedAt="Mon Dec 06 2021 09:40:54")
    comment395b = Comment(videoId=376, channelId=92, content="Today I bought a raincoat and wore it on a sunny day.", createdAt="Sun Jan 23 2022 17:35:01", updatedAt="Tue Jul 13 2021 02:15:29")
    comment396b = Comment(videoId=26, channelId=24, content="Jeanne wished she has chosen the red button.", createdAt="Wed Dec 22 2021 22:23:42", updatedAt="Fri Apr 08 2022 08:09:52")
    comment397b = Comment(videoId=556, channelId=56, content="The elephant didn't want to talk about the person in the room.", createdAt="Fri Dec 03 2021 17:38:00", updatedAt="Tue Jun 15 2021 01:32:39")
    comment398b = Comment(videoId=71, channelId=34, content="The teenage boy was accused of breaking his arm simply to get out of the test.", createdAt="Fri Oct 08 2021 13:40:07", updatedAt="Mon Feb 21 2022 00:08:18")
    comment399b = Comment(videoId=166, channelId=6, content="Stop waiting for exceptional things to just happen.", createdAt="Sun Sep 05 2021 05:29:08", updatedAt="Fri Feb 25 2022 22:32:14")
    comment400b = Comment(videoId=115, channelId=74, content="I really want to go to work, but I am too sick to drive.", createdAt="Tue Jan 04 2022 10:41:30", updatedAt="Sun Aug 22 2021 15:18:00")
    comment401b = Comment(videoId=218, channelId=19, content="Let me help you with your baggage.", createdAt="Wed Apr 28 2021 05:48:57", updatedAt="Sat Jan 01 2022 03:44:33")
    comment402b = Comment(videoId=682, channelId=81, content="Giving directions that the mountains are to the west only works when you can see them.", createdAt="Sun Jan 02 2022 11:03:44", updatedAt="Sat Apr 24 2021 13:42:14")
    comment403b = Comment(videoId=436, channelId=75, content="He put heat on the wound to see what would grow.", createdAt="Thu Feb 03 2022 05:34:28", updatedAt="Tue Apr 05 2022 05:14:24")
    comment404b = Comment(videoId=163, channelId=20, content="I became paranoid that the school of jellyfish was spying on me.", createdAt="Sun Dec 26 2021 01:54:51", updatedAt="Thu Dec 23 2021 14:45:15")
    comment405b = Comment(videoId=33, channelId=90, content="Thigh-high in the water, the fisherman’s hope for dinner soon turned to despair.", createdAt="Thu Aug 12 2021 20:14:51", updatedAt="Wed Nov 10 2021 08:12:22")
    comment407b = Comment(videoId=258, channelId=56, content="Everyone was curious about the large white blimp that appeared overnight.", createdAt="Sat Jun 26 2021 04:14:17", updatedAt="Mon Apr 12 2021 14:30:34")
    comment408b = Comment(videoId=683, channelId=9, content="On a scale from one to ten, what's your favorite flavor of random grammar?", createdAt="Fri Oct 15 2021 11:59:05", updatedAt="Mon Mar 21 2022 23:28:29")
    comment409b = Comment(videoId=586, channelId=40, content="The furnace repairman indicated the heating system was acting as an air conditioner.", createdAt="Fri May 14 2021 23:09:30", updatedAt="Sun Feb 20 2022 12:20:27")
    comment410b = Comment(videoId=322, channelId=52, content="She wanted a pet platypus but ended up getting a duck and a ferret instead.", createdAt="Mon Jul 12 2021 19:40:46", updatedAt="Mon Oct 18 2021 13:21:05")
    comment411b = Comment(videoId=340, channelId=73, content="He kept telling himself that one day it would all somehow make sense.", createdAt="Sun Apr 18 2021 01:54:52", updatedAt="Fri Dec 10 2021 16:35:45")
    comment412b = Comment(videoId=465, channelId=74, content="Patricia loves the sound of nails strongly pressed against the chalkboard.", createdAt="Sat Feb 05 2022 02:58:13", updatedAt="Tue May 11 2021 21:06:58")
    comment413b = Comment(videoId=222, channelId=97, content="He felt that dining on the bridge brought romance to his relationship with his cat.", createdAt="Sat Mar 26 2022 14:19:47", updatedAt="Mon Aug 02 2021 07:40:29")
    comment414b = Comment(videoId=82, channelId=4, content="The minute she landed she understood the reason this was a fly-over state.", createdAt="Sun Feb 27 2022 00:49:54", updatedAt="Tue Apr 05 2022 20:31:41")
    comment415b = Comment(videoId=35, channelId=12, content="Henry couldn't decide if he was an auto mechanic or a priest.", createdAt="Fri Jun 04 2021 01:48:52", updatedAt="Thu Jul 08 2021 00:57:13")
    comment416b = Comment(videoId=56, channelId=85, content="Her life in the confines of the house became her new normal.", createdAt="Sun Aug 01 2021 22:28:47", updatedAt="Tue Mar 01 2022 06:42:35")
    comment417b = Comment(videoId=313, channelId=48, content="The elderly neighborhood became enraged over the coyotes who had been blamed for the poodle’s disappearance.", createdAt="Tue Apr 13 2021 02:09:06", updatedAt="Thu Sep 02 2021 07:50:38")
    comment418b = Comment(videoId=715, channelId=26, content="Greetings from the galaxy MACS0647-JD, or what we call home.", createdAt="Thu Oct 21 2021 11:20:27", updatedAt="Wed Feb 16 2022 08:56:57")
    comment419b = Comment(videoId=119, channelId=92, content="There's a reason that roses have thorns.", createdAt="Tue Mar 08 2022 22:35:00", updatedAt="Thu Sep 09 2021 15:51:09")
    comment420b = Comment(videoId=600, channelId=73, content="He excelled at firing people nicely.", createdAt="Mon Aug 23 2021 20:59:36", updatedAt="Tue Oct 12 2021 08:52:46")
    comment421b = Comment(videoId=374, channelId=70, content="So long and thanks for the fish.", createdAt="Mon May 03 2021 15:59:27", updatedAt="Fri Oct 29 2021 04:53:28")
    comment422b = Comment(videoId=217, channelId=58, content="I covered my friend in baby oil.", createdAt="Sat Dec 18 2021 17:59:59", updatedAt="Thu Sep 30 2021 14:16:59")
    comment423b = Comment(videoId=58, channelId=29, content="He wondered why at 18 he was old enough to go to war, but not old enough to buy cigarettes.", createdAt="Thu Mar 10 2022 22:38:50", updatedAt="Sat Aug 28 2021 10:06:54")
    comment424b = Comment(videoId=716, channelId=91, content="She wore green lipstick like a fashion icon.", createdAt="Sat Apr 09 2022 18:54:13", updatedAt="Thu Jun 17 2021 00:28:26")
    comment425b = Comment(videoId=254, channelId=74, content="He loved eating his bananas in hot dog buns.", createdAt="Sun Oct 24 2021 11:37:21", updatedAt="Fri Dec 24 2021 23:27:02")
    comment426b = Comment(videoId=134, channelId=25, content="Although it wasn't a pot of gold, Nancy was still enthralled at what she found at the end of the rainbow.", createdAt="Sat Apr 24 2021 04:54:01", updatedAt="Tue Sep 21 2021 21:39:18")
    comment427b = Comment(videoId=646, channelId=74, content="My Mum tries to be cool by saying that she likes all the same things that I do.", createdAt="Sat May 01 2021 05:04:02", updatedAt="Sat Feb 19 2022 19:10:48")
    comment428b = Comment(videoId=562, channelId=3, content="I liked their first two albums but changed my mind after that charity gig.", createdAt="Mon Apr 12 2021 12:14:58", updatedAt="Sat Dec 04 2021 11:14:43")
    comment429b = Comment(videoId=76, channelId=10, content="He went back to the video to see what had been recorded and was shocked at what he saw.", createdAt="Sun Dec 12 2021 03:26:47", updatedAt="Wed Jan 19 2022 09:56:12")
    comment430b = Comment(videoId=242, channelId=14, content="It doesn't sound like that will ever be on my travel list.", createdAt="Wed Oct 27 2021 20:47:46", updatedAt="Wed Aug 04 2021 02:27:57")
    comment431b = Comment(videoId=533, channelId=22, content="He decided water-skiing on a frozen lake wasn’t a good idea.", createdAt="Fri Feb 18 2022 09:43:16", updatedAt="Thu Jul 15 2021 05:49:11")
    comment432b = Comment(videoId=45, channelId=47, content="She did her best to help him.", createdAt="Sun Dec 05 2021 23:23:18", updatedAt="Tue Jun 08 2021 01:09:37")
    comment433b = Comment(videoId=273, channelId=30, content="I've always wanted to go to Tajikistan, but my cat would miss me.", createdAt="Tue Dec 21 2021 07:20:27", updatedAt="Wed May 19 2021 01:36:13")
    comment434b = Comment(videoId=259, channelId=61, content="Baby wipes are made of chocolate stardust.", createdAt="Mon Apr 19 2021 20:20:34", updatedAt="Wed Jun 09 2021 20:33:24")
    comment435b = Comment(videoId=144, channelId=85, content="He watched the dancing piglets with panda bear tummies in the swimming pool.", createdAt="Sun Jun 27 2021 23:03:30", updatedAt="Sat Oct 09 2021 22:48:56")
    comment436b = Comment(videoId=231, channelId=36, content="The hand sanitizer was actually clear glue.", createdAt="Tue May 25 2021 23:14:42", updatedAt="Wed May 05 2021 14:14:37")
    comment437b = Comment(videoId=162, channelId=5, content="If you like tuna and tomato sauce, try combining the two, it’s really not as bad as it sounds.", createdAt="Thu Sep 02 2021 12:32:43", updatedAt="Sat Aug 28 2021 19:04:24")
    comment438b = Comment(videoId=433, channelId=64, content="There are over 500 starfish in the bathroom drawer.", createdAt="Sat Jul 31 2021 21:16:21", updatedAt="Tue Jun 15 2021 06:18:13")
    comment439b = Comment(videoId=735, channelId=96, content="The knives were out and she was sharpening hers.", createdAt="Tue Mar 01 2022 18:55:53", updatedAt="Sat May 15 2021 08:15:56")
    comment440b = Comment(videoId=529, channelId=50, content="Even though he thought the world was flat he didn’t see the irony of wanting to travel around the world.", createdAt="Wed Oct 20 2021 16:30:24", updatedAt="Tue Nov 02 2021 22:54:39")
    comment441b = Comment(videoId=220, channelId=66, content="He hated that he loved what she hated about hate.", createdAt="Wed Mar 02 2022 13:25:59", updatedAt="Mon Dec 27 2021 07:08:28")
    comment442b = Comment(videoId=311, channelId=38, content="Siri became confused when we reused to follow her directions.", createdAt="Fri Aug 27 2021 02:00:17", updatedAt="Fri Oct 01 2021 20:22:39")
    comment443b = Comment(videoId=675, channelId=43, content="Three years later, the coffin was still full of Jello.", createdAt="Thu Sep 16 2021 22:29:42", updatedAt="Wed Jul 14 2021 18:13:57")
    comment444b = Comment(videoId=420, channelId=35, content="I used to practice weaving with spaghetti three hours a day but stopped because I didn't want to die alone.", createdAt="Sun Nov 21 2021 04:15:24", updatedAt="Mon Mar 21 2022 22:43:30")
    comment445b = Comment(videoId=717, channelId=69, content="Most shark attacks occur about 10 feet from the beach since that's where the people are.", createdAt="Thu Feb 17 2022 13:41:51", updatedAt="Wed Dec 29 2021 17:36:08")
    comment446b = Comment(videoId=180, channelId=49, content="She wanted to be rescued, but only if it was Tuesday and raining.", createdAt="Sat Oct 30 2021 09:30:28", updatedAt="Tue Feb 01 2022 09:59:34")
    comment447b = Comment(videoId=683, channelId=8, content="The waves were crashing on the shore; it was a lovely sight.", createdAt="Wed Mar 30 2022 09:27:41", updatedAt="Sun Apr 25 2021 09:07:08")
    comment448b = Comment(videoId=422, channelId=41, content="In that instant, everything changed.", createdAt="Sat Aug 14 2021 05:24:28", updatedAt="Sun Nov 14 2021 21:19:52")
    comment449b = Comment(videoId=90, channelId=66, content="It dawned on her that others could make her happier, but only she could make herself happy.", createdAt="Tue Sep 21 2021 04:52:24", updatedAt="Thu May 20 2021 03:49:07")
    comment450b = Comment(videoId=148, channelId=56, content="Charles ate the french fries knowing they would be his last meal.", createdAt="Fri Sep 03 2021 14:32:18", updatedAt="Tue May 25 2021 06:17:57")
    comment451b = Comment(videoId=10, channelId=52, content="The body piercing didn't go exactly as he expected.", createdAt="Thu Jun 03 2021 03:07:17", updatedAt="Fri Nov 05 2021 04:37:24")
    comment452b = Comment(videoId=685, channelId=3, content="The water flowing down the river didn’t look that powerful from the car", createdAt="Tue May 11 2021 13:42:33", updatedAt="Wed Jun 23 2021 12:19:09")
    comment453b = Comment(videoId=122, channelId=68, content="The skeleton had skeletons of his own in the closet.", createdAt="Sun May 16 2021 04:59:31", updatedAt="Thu Nov 18 2021 08:04:58")
    comment454b = Comment(videoId=718, channelId=91, content="The light that burns twice as bright burns half as long.", createdAt="Thu Jul 29 2021 04:35:08", updatedAt="Thu Jun 03 2021 11:19:18")
    comment455b = Comment(videoId=566, channelId=20, content="It must be five o'clock somewhere.", createdAt="Tue Aug 03 2021 05:18:43", updatedAt="Thu Sep 02 2021 17:04:37")
    comment456b = Comment(videoId=56, channelId=24, content="I used to practice weaving with spaghetti three hours a day but stopped because I didn't want to die alone.", createdAt="Mon Mar 14 2022 03:32:57", updatedAt="Thu Jul 08 2021 19:51:01")
    comment457b = Comment(videoId=684, channelId=15, content="You realize you're not alone as you sit in your bedroom massaging your calves after a long day of playing tug-of-war with Grandpa Joe in the hospital.", createdAt="Sat Jul 17 2021 23:20:35", updatedAt="Wed Oct 13 2021 03:15:44")
    comment458b = Comment(videoId=593, channelId=16, content="The book is in front of the table.", createdAt="Thu Jan 06 2022 16:47:31", updatedAt="Thu Apr 07 2022 02:23:57")
    comment459b = Comment(videoId=516, channelId=72, content="My secretary is the only person who truly understands my stamp-collecting obsession.", createdAt="Sun Jan 30 2022 22:40:54", updatedAt="Fri Nov 26 2021 00:14:55")
    comment460b = Comment(videoId=638, channelId=48, content="He didn't understand why the bird wanted to ride the bicycle.", createdAt="Wed Sep 08 2021 12:35:34", updatedAt="Wed Jun 09 2021 23:19:41")
    comment461b = Comment(videoId=249, channelId=50, content="Although it wasn't a pot of gold, Nancy was still enthralled at what she found at the end of the rainbow.", createdAt="Thu Dec 16 2021 15:06:50", updatedAt="Fri Apr 08 2022 15:46:01")
    comment462b = Comment(videoId=611, channelId=64, content="He stomped on his fruit loops and thus became a cereal killer.", createdAt="Wed Sep 22 2021 22:09:41", updatedAt="Sun Apr 18 2021 16:15:59")
    comment463b = Comment(videoId=637, channelId=60, content="Standing on one's head at job interviews forms a lasting impression.", createdAt="Wed Jan 26 2022 09:01:58", updatedAt="Mon Jan 10 2022 23:48:51")
    comment464b = Comment(videoId=593, channelId=15, content="The dead trees waited to be ignited by the smallest spark and seek their revenge.", createdAt="Wed Jul 07 2021 17:29:40", updatedAt="Wed Dec 22 2021 01:05:50")
    comment465b = Comment(videoId=45, channelId=30, content="There are over 500 starfish in the bathroom drawer.", createdAt="Mon Feb 21 2022 11:36:13", updatedAt="Fri Sep 10 2021 20:19:34")
    comment466b = Comment(videoId=308, channelId=22, content="My Mum tries to be cool by saying that she likes all the same things that I do.", createdAt="Fri Jan 14 2022 18:48:12", updatedAt="Fri Mar 18 2022 12:48:16")
    comment467b = Comment(videoId=457, channelId=91, content="Writing a list of random sentences is harder than I initially thought it would be.", createdAt="Sat Jan 01 2022 09:48:29", updatedAt="Sun Apr 11 2021 13:16:00")
    comment468b = Comment(videoId=489, channelId=46, content="The overpass went under the highway and into a secret world.", createdAt="Sun May 30 2021 16:44:47", updatedAt="Thu Apr 07 2022 13:25:12")
    comment469b = Comment(videoId=367, channelId=18, content="His son quipped that power bars were nothing more than adult candy bars.", createdAt="Fri Jan 07 2022 03:48:03", updatedAt="Wed Jul 21 2021 01:34:34")
    comment470b = Comment(videoId=231, channelId=28, content="When nobody is around, the trees gossip about the people who have walked under them.", createdAt="Fri Oct 01 2021 23:23:39", updatedAt="Sun Aug 15 2021 14:04:34")
    comment471b = Comment(videoId=67, channelId=90, content="We will not allow you to bring your pet armadillo along.", createdAt="Mon Aug 16 2021 10:45:34", updatedAt="Wed May 19 2021 18:37:06")
    comment472b = Comment(videoId=488, channelId=44, content="Grape jelly was leaking out the hole in the roof.", createdAt="Fri Sep 24 2021 21:19:07", updatedAt="Mon Nov 08 2021 15:25:10")
    comment473b = Comment(videoId=552, channelId=60, content="The toddler’s endless tantrum caused the entire plane anxiety.", createdAt="Thu May 20 2021 11:12:31", updatedAt="Thu Sep 09 2021 07:09:06")
    comment474b = Comment(videoId=595, channelId=29, content="She learned that water bottles are no longer just to hold liquid, but they're also status symbols.", createdAt="Mon Jun 28 2021 01:12:05", updatedAt="Wed Jun 30 2021 11:27:02")
    comment475b = Comment(videoId=631, channelId=56, content="Imagine his surprise when he discovered that the safe was full of pudding.", createdAt="Mon Aug 02 2021 01:10:06", updatedAt="Sun Oct 17 2021 20:06:36")
    comment476b = Comment(videoId=333, channelId=14, content="I often see the time 11:11 or 12:34 on clocks.", createdAt="Sat Sep 11 2021 15:38:51", updatedAt="Tue Mar 22 2022 17:39:41")
    comment477b = Comment(videoId=589, channelId=36, content="She opened up her third bottle of wine of the night.", createdAt="Sat Mar 05 2022 04:31:15", updatedAt="Sat Mar 12 2022 20:32:54")
    comment478b = Comment(videoId=192, channelId=82, content="I checked to make sure that he was still alive.", createdAt="Mon Nov 22 2021 03:32:47", updatedAt="Wed Jun 30 2021 20:57:29")
    comment479b = Comment(videoId=217, channelId=1, content="The spa attendant applied the deep cleaning mask to the gentleman’s back.", createdAt="Thu Jun 24 2021 17:58:33", updatedAt="Fri Oct 01 2021 12:24:16")
    comment481b = Comment(videoId=501, channelId=40, content="Flash photography is best used in full sunlight.", createdAt="Sat Sep 25 2021 08:36:02", updatedAt="Thu Jun 03 2021 09:33:17")
    comment482b = Comment(videoId=102, channelId=36, content="The trick to getting kids to eat anything is to put catchup on it.", createdAt="Fri Jan 07 2022 01:11:51", updatedAt="Fri Nov 19 2021 00:21:08")
    comment483b = Comment(videoId=725, channelId=55, content="Iguanas were falling out of the trees.", createdAt="Tue Mar 15 2022 14:45:00", updatedAt="Mon May 03 2021 03:23:41")
    comment484b = Comment(videoId=202, channelId=80, content="Charles ate the french fries knowing they would be his last meal.", createdAt="Wed Jul 28 2021 22:29:36", updatedAt="Sat Mar 12 2022 09:07:45")
    comment485b = Comment(videoId=691, channelId=55, content="People generally approve of dogs eating cat food but not cats eating dog food.", createdAt="Sun Aug 08 2021 03:09:48", updatedAt="Thu May 27 2021 10:29:04")
    comment486b = Comment(videoId=626, channelId=4, content="The father died during childbirth.", createdAt="Mon Apr 04 2022 18:56:36", updatedAt="Tue Nov 09 2021 01:04:34")
    comment487b = Comment(videoId=452, channelId=77, content="The waitress was not amused when he ordered green eggs and ham.", createdAt="Mon Nov 15 2021 04:22:09", updatedAt="Sun Feb 06 2022 04:15:44")
    comment488b = Comment(videoId=545, channelId=95, content="He decided to fake his disappearance to avoid jail.", createdAt="Mon Aug 16 2021 14:16:28", updatedAt="Thu Sep 23 2021 15:57:55")
    comment489b = Comment(videoId=641, channelId=9, content="Purple is the best city in the forest.", createdAt="Mon Nov 01 2021 19:23:25", updatedAt="Thu Feb 24 2022 23:12:31")
    comment490b = Comment(videoId=729, channelId=80, content="Buried deep in the snow, he hoped his batteries were fresh in his avalanche beacon.", createdAt="Wed Feb 09 2022 15:05:17", updatedAt="Tue May 11 2021 00:24:34")
    comment491b = Comment(videoId=456, channelId=53, content="He took one look at what was under the table and noped the hell out of there.", createdAt="Sat Mar 05 2022 13:55:28", updatedAt="Fri Aug 06 2021 03:02:57")
    comment492b = Comment(videoId=660, channelId=98, content="He kept telling himself that one day it would all somehow make sense.", createdAt="Tue Oct 12 2021 18:49:33", updatedAt="Fri Jan 07 2022 07:49:27")
    comment493b = Comment(videoId=161, channelId=92, content="Nothing seemed out of place except the washing machine in the bar.", createdAt="Sun Feb 20 2022 08:57:06", updatedAt="Mon Oct 18 2021 20:11:08")
    comment494b = Comment(videoId=206, channelId=62, content="I'd always thought lightning was something only I could see.", createdAt="Mon Mar 21 2022 18:22:14", updatedAt="Thu Jul 15 2021 08:43:34")
    comment495b = Comment(videoId=540, channelId=6, content="Chocolate covered crickets were his favorite snack.", createdAt="Wed Jul 07 2021 20:17:58", updatedAt="Thu Mar 03 2022 00:15:30")
    comment496b = Comment(videoId=667, channelId=16, content="Weather is not trivial - it's especially important when you're standing in it.", createdAt="Thu Jun 10 2021 14:24:48", updatedAt="Tue Mar 15 2022 23:27:55")
    comment497b = Comment(videoId=504, channelId=76, content="You're good at English when you know the difference between a man eating chicken and a man-eating chicken.", createdAt="Fri Jul 16 2021 23:20:36", updatedAt="Sun Aug 29 2021 11:48:06")
    comment498b = Comment(videoId=70, channelId=4, content="Dolores wouldn't have eaten the meal if she had known what it actually was.", createdAt="Tue Nov 30 2021 11:47:10", updatedAt="Mon Apr 12 2021 01:22:36")
    comment499b = Comment(videoId=726, channelId=100, content="He was the only member of the club who didn't like plum pudding.", createdAt="Sat Jan 15 2022 03:58:19", updatedAt="Sat Apr 17 2021 21:12:36")
    comment500b = Comment(videoId=680, channelId=84, content="They improved dramatically once the lead singer left.", createdAt="Wed Mar 16 2022 09:45:34", updatedAt="Mon Jun 14 2021 06:50:38")
    comment501b = Comment(videoId=513, channelId=16, content="Just go ahead and press that button.", createdAt="Thu Dec 16 2021 19:40:29", updatedAt="Mon Dec 13 2021 10:36:10")
    comment502b = Comment(videoId=662, channelId=25, content="All you need to do is pick up the pen and begin.", createdAt="Wed Jan 12 2022 23:30:14", updatedAt="Mon Mar 21 2022 17:07:36")
    comment503b = Comment(videoId=177, channelId=43, content="Art doesn't have to be intentional.", createdAt="Fri Apr 08 2022 08:20:25", updatedAt="Tue Jun 29 2021 21:33:31")
    comment504b = Comment(videoId=747, channelId=66, content="She had the gift of being able to paint songs.", createdAt="Tue Dec 07 2021 05:18:29", updatedAt="Wed Nov 17 2021 08:10:41")
    comment505b = Comment(videoId=371, channelId=99, content="He didn't heed the warning and it had turned out surprisingly well.", createdAt="Sun Aug 01 2021 23:42:46", updatedAt="Wed Dec 29 2021 20:40:21")
    comment506b = Comment(videoId=24, channelId=71, content="Cats are good pets, for they are clean and are not noisy.", createdAt="Wed Apr 21 2021 04:12:33", updatedAt="Mon Dec 20 2021 00:07:52")
    comment507b = Comment(videoId=308, channelId=100, content="On each full moon", createdAt="Wed May 19 2021 21:38:11", updatedAt="Sat Jun 12 2021 00:50:00")
    comment508b = Comment(videoId=744, channelId=8, content="When I cook spaghetti, I like to boil it a few minutes past al dente so the noodles are super slippery.", createdAt="Tue Mar 29 2022 17:32:10", updatedAt="Sun Nov 28 2021 18:29:24")
    comment509b = Comment(videoId=356, channelId=21, content="You bite up because of your lower jaw.", createdAt="Tue Oct 19 2021 20:43:56", updatedAt="Fri Dec 10 2021 10:08:48")
    comment510b = Comment(videoId=420, channelId=78, content="Don't put peanut butter on the dog's nose.", createdAt="Thu Jan 20 2022 06:40:12", updatedAt="Fri Nov 05 2021 07:16:37")
    comment511b = Comment(videoId=641, channelId=35, content="If eating three-egg omelets causes weight-gain, budgie eggs are a good substitute.", createdAt="Wed Apr 14 2021 09:44:22", updatedAt="Tue Aug 03 2021 10:21:54")
    comment512b = Comment(videoId=562, channelId=84, content="Imagine his surprise when he discovered that the safe was full of pudding.", createdAt="Thu Mar 17 2022 14:44:50", updatedAt="Sun Feb 06 2022 07:23:16")
    comment513b = Comment(videoId=525, channelId=3, content="The hand sanitizer was actually clear glue.", createdAt="Mon Jan 24 2022 19:39:39", updatedAt="Sun Dec 19 2021 14:46:02")
    comment514b = Comment(videoId=433, channelId=56, content="On a scale from one to ten, what's your favorite flavor of random grammar?", createdAt="Mon Jan 31 2022 18:03:42", updatedAt="Thu Nov 11 2021 01:53:31")
    comment515b = Comment(videoId=468, channelId=24, content="The father handed each child a roadmap at the beginning of the 2-day road trip and explained it was so they could find their way home.", createdAt="Sun Aug 15 2021 00:41:40", updatedAt="Mon Sep 13 2021 16:26:35")
    comment516b = Comment(videoId=369, channelId=87, content="It took me too long to realize that the ceiling hadn't been painted to look like the sky.", createdAt="Mon Nov 29 2021 16:34:36", updatedAt="Fri Jan 28 2022 15:34:22")
    comment517b = Comment(videoId=723, channelId=9, content="It's not often you find a soggy banana on the street.", createdAt="Sun Oct 31 2021 04:10:31", updatedAt="Sat Dec 25 2021 03:53:33")
    comment518b = Comment(videoId=353, channelId=64, content="Trash covered the landscape like sprinkles do a birthday cake.", createdAt="Sat Mar 26 2022 08:24:39", updatedAt="Sun Mar 20 2022 11:56:18")
    comment519b = Comment(videoId=336, channelId=97, content="He wondered why at 18 he was old enough to go to war, but not old enough to buy cigarettes.", createdAt="Tue Aug 17 2021 03:58:04", updatedAt="Mon Oct 25 2021 00:26:47")
    comment520b = Comment(videoId=481, channelId=69, content="They decided to plant an orchard of cotton candy.", createdAt="Wed May 26 2021 15:56:30", updatedAt="Sun May 30 2021 00:48:20")
    comment521b = Comment(videoId=689, channelId=91, content="So long and thanks for the fish.", createdAt="Sun Sep 05 2021 13:46:42", updatedAt="Mon Oct 25 2021 17:58:23")
    comment522b = Comment(videoId=711, channelId=50, content="He was sure the Devil created red sparkly glitter.", createdAt="Sat Aug 14 2021 08:29:34", updatedAt="Mon Jan 10 2022 01:04:32")
    comment523b = Comment(videoId=204, channelId=76, content="He created a pig burger out of beef.", createdAt="Tue Oct 05 2021 02:50:14", updatedAt="Thu Feb 03 2022 23:17:29")
    comment524b = Comment(videoId=668, channelId=26, content="It isn't true that my mattress is made of cotton candy.", createdAt="Sat Sep 11 2021 22:48:18", updatedAt="Thu Jan 27 2022 11:17:51")
    comment525b = Comment(videoId=541, channelId=27, content="At last", createdAt="Mon Apr 26 2021 21:42:32", updatedAt="Mon Aug 16 2021 15:35:26")
    comment526b = Comment(videoId=12, channelId=44, content="I was very proud of my nickname throughout high school but today- I couldn’t be any different to what my nickname was.", createdAt="Sun Aug 29 2021 00:59:23", updatedAt="Mon Nov 08 2021 02:44:53")
    comment527b = Comment(videoId=10, channelId=37, content="People generally approve of dogs eating cat food but not cats eating dog food.", createdAt="Sat Nov 13 2021 10:29:25", updatedAt="Mon Nov 15 2021 02:59:23")
    comment528b = Comment(videoId=514, channelId=77, content="She always had an interesting perspective on why the world must be flat.", createdAt="Mon Jul 19 2021 03:59:44", updatedAt="Wed Sep 01 2021 16:45:20")
    comment529b = Comment(videoId=115, channelId=47, content="She saw no irony asking me to change but wanting me to accept her for who she is.", createdAt="Sat Feb 26 2022 01:43:03", updatedAt="Sun Mar 13 2022 14:47:03")
    comment531b = Comment(videoId=94, channelId=44, content="The glacier came alive as the climbers hiked closer.", createdAt="Sat Apr 17 2021 12:16:19", updatedAt="Tue Jul 20 2021 17:27:52")
    comment532b = Comment(videoId=21, channelId=64, content="When he asked her favorite number, she answered without hesitation that it was diamonds.", createdAt="Thu Sep 09 2021 10:08:27", updatedAt="Thu May 20 2021 15:56:44")
    comment533b = Comment(videoId=641, channelId=91, content="The irony of the situation wasn't lost on anyone in the room.", createdAt="Thu Dec 09 2021 21:56:31", updatedAt="Wed Aug 04 2021 14:46:45")
    comment534b = Comment(videoId=92, channelId=82, content="Lucifer was surprised at the amount of life at Death Valley.", createdAt="Tue Feb 22 2022 18:34:26", updatedAt="Fri Sep 17 2021 14:14:58")
    comment535b = Comment(videoId=339, channelId=74, content="Everyone pretends to like wheat until you mention barley.", createdAt="Thu Aug 12 2021 02:01:23", updatedAt="Sat May 22 2021 21:04:35")
    comment536b = Comment(videoId=60, channelId=52, content="He decided water-skiing on a frozen lake wasn’t a good idea.", createdAt="Wed Sep 22 2021 08:29:48", updatedAt="Tue Jul 06 2021 10:28:08")
    comment537b = Comment(videoId=246, channelId=62, content="The manager of the fruit stand always sat and only sold vegetables.", createdAt="Thu Sep 23 2021 00:35:55", updatedAt="Fri Feb 18 2022 22:04:26")
    comment538b = Comment(videoId=222, channelId=76, content="When motorists sped in and out of traffic, all she could think of was those in need of a transplant.", createdAt="Thu Nov 04 2021 18:04:58", updatedAt="Sat Apr 24 2021 11:53:59")
    comment539b = Comment(videoId=68, channelId=49, content="There is no better feeling than staring at a wall with closed eyes.", createdAt="Wed Nov 24 2021 16:10:47", updatedAt="Fri Apr 16 2021 14:05:22")
    comment541b = Comment(videoId=397, channelId=12, content="Peanuts don't grow on trees, but cashews do.", createdAt="Sun May 30 2021 16:34:08", updatedAt="Tue Jun 29 2021 07:18:29")
    comment542b = Comment(videoId=242, channelId=28, content="There's a message for you if you look up.", createdAt="Sat Nov 13 2021 04:42:13", updatedAt="Tue Dec 28 2021 09:58:49")
    comment543b = Comment(videoId=738, channelId=48, content="No matter how beautiful the sunset, it saddened her knowing she was one day older.", createdAt="Tue Oct 05 2021 02:57:59", updatedAt="Tue Apr 27 2021 12:47:50")
    comment544b = Comment(videoId=489, channelId=3, content="Standing on one's head at job interviews forms a lasting impression.", createdAt="Sun Mar 06 2022 02:41:55", updatedAt="Fri Dec 03 2021 03:13:56")
    comment545b = Comment(videoId=42, channelId=97, content="The random sentence generator generated a random sentence about a random sentence.", createdAt="Mon Aug 23 2021 10:16:40", updatedAt="Sun Feb 27 2022 06:23:30")
    comment546b = Comment(videoId=421, channelId=49, content="The tattered work gloves speak of the many hours of hard labor he endured throughout his life.", createdAt="Thu May 06 2021 00:12:36", updatedAt="Sat Oct 09 2021 12:12:49")
    comment547b = Comment(videoId=602, channelId=100, content="When he encountered maize for the first time, he thought it incredibly corny.", createdAt="Mon Sep 13 2021 13:23:27", updatedAt="Wed Mar 09 2022 17:30:00")
    comment548b = Comment(videoId=46, channelId=71, content="He had a hidden stash underneath the floorboards in the back room of the house.", createdAt="Wed Oct 13 2021 21:52:32", updatedAt="Mon Sep 13 2021 00:49:16")
    comment549b = Comment(videoId=773, channelId=8, content="Shakespeare was a famous 17th-century diesel mechanic.", createdAt="Sat Aug 07 2021 15:28:32", updatedAt="Fri Mar 04 2022 09:28:15")
    comment550b = Comment(videoId=452, channelId=51, content="I caught my squirrel rustling through my gym bag.", createdAt="Sat May 15 2021 18:03:44", updatedAt="Tue Aug 10 2021 08:47:40")
    comment551b = Comment(videoId=293, channelId=80, content="There were three sphered rocks congregating in a cubed room.", createdAt="Sun Jul 04 2021 02:22:47", updatedAt="Fri Aug 27 2021 11:01:22")
    comment553b = Comment(videoId=623, channelId=99, content="Tuesdays are free if you bring a gnome costume.", createdAt="Thu Sep 02 2021 17:21:56", updatedAt="Tue Mar 22 2022 09:25:18")
    comment554b = Comment(videoId=207, channelId=82, content="Three years later, the coffin was still full of Jello.", createdAt="Sat Apr 10 2021 19:16:11", updatedAt="Tue May 25 2021 11:13:18")
    comment555b = Comment(videoId=473, channelId=37, content="I love eating toasted cheese and tuna sandwiches.", createdAt="Fri Jul 02 2021 20:40:07", updatedAt="Tue Feb 01 2022 03:32:42")
    comment556b = Comment(videoId=299, channelId=66, content="His ultimate dream fantasy consisted of being content and sleeping eight hours in a row.", createdAt="Sat Aug 07 2021 12:28:52", updatedAt="Mon Jun 28 2021 07:58:25")
    comment557b = Comment(videoId=719, channelId=91, content="That must be the tenth time I've been arrested for selling deep-fried cigars.", createdAt="Tue Oct 19 2021 03:01:19", updatedAt="Mon Nov 01 2021 06:41:27")
    comment558b = Comment(videoId=285, channelId=82, content="He was the only member of the club who didn't like plum pudding.", createdAt="Tue Dec 21 2021 02:56:14", updatedAt="Fri Sep 10 2021 21:49:30")
    comment559b = Comment(videoId=702, channelId=20, content="The teens wondered what was kept in the red shed on the far edge of the school grounds.", createdAt="Fri Jan 07 2022 16:29:48", updatedAt="Sun Oct 10 2021 01:50:40")
    comment560b = Comment(videoId=402, channelId=27, content="Abstraction is often one floor above you.", createdAt="Sat Sep 04 2021 07:56:53", updatedAt="Fri Jan 21 2022 06:45:36")
    comment561b = Comment(videoId=95, channelId=34, content="Peter found road kill an excellent way to save money on dinner.", createdAt="Sat Apr 02 2022 20:48:53", updatedAt="Thu Jun 24 2021 23:49:55")
    comment562b = Comment(videoId=279, channelId=57, content="You should never take advice from someone who thinks red paint dries quicker than blue paint.", createdAt="Sat Apr 09 2022 02:53:29", updatedAt="Sat Mar 12 2022 14:56:23")
    comment563b = Comment(videoId=241, channelId=87, content="They did nothing as the raccoon attacked the lady’s bag of food.", createdAt="Thu Mar 03 2022 01:20:47", updatedAt="Mon May 10 2021 09:58:24")
    comment564b = Comment(videoId=701, channelId=47, content="The dead trees waited to be ignited by the smallest spark and seek their revenge.", createdAt="Wed Mar 23 2022 15:04:18", updatedAt="Mon Oct 11 2021 15:18:44")
    comment565b = Comment(videoId=744, channelId=27, content="Just go ahead and press that button.", createdAt="Sun May 16 2021 06:49:40", updatedAt="Wed Aug 25 2021 06:02:04")
    comment566b = Comment(videoId=583, channelId=68, content="Pantyhose and heels are an interesting choice of attire for the beach.", createdAt="Tue Dec 21 2021 10:32:35", updatedAt="Sat Jun 12 2021 09:01:19")
    comment567b = Comment(videoId=591, channelId=86, content="We should play with legos at camp.", createdAt="Wed Jun 23 2021 14:43:37", updatedAt="Mon Feb 07 2022 23:56:47")
    comment568b = Comment(videoId=575, channelId=64, content="Baby wipes are made of chocolate stardust.", createdAt="Sun Mar 06 2022 02:56:10", updatedAt="Wed Jul 21 2021 22:46:46")
    comment569b = Comment(videoId=495, channelId=2, content="Sometimes you have to just give up and win by cheating.", createdAt="Thu Oct 21 2021 10:43:37", updatedAt="Wed Dec 29 2021 00:52:20")
    comment570b = Comment(videoId=274, channelId=63, content="Jim liked driving around town with his hazard lights on.", createdAt="Sun Sep 05 2021 15:39:02", updatedAt="Thu Apr 15 2021 17:01:46")
    comment571b = Comment(videoId=290, channelId=74, content="The manager of the fruit stand always sat and only sold vegetables.", createdAt="Fri Aug 27 2021 18:18:32", updatedAt="Sat Feb 05 2022 10:28:21")
    comment572b = Comment(videoId=261, channelId=23, content="He hated that he loved what she hated about hate.", createdAt="Sun Jun 27 2021 04:22:01", updatedAt="Wed Oct 20 2021 03:24:41")
    comment573b = Comment(videoId=657, channelId=32, content="He realized there had been several deaths on this road, but his concern rose when he saw the exact number.", createdAt="Sun Feb 27 2022 09:48:14", updatedAt="Wed Aug 04 2021 07:39:38")
    comment574b = Comment(videoId=282, channelId=72, content="The hummingbird's wings blurred while it eagerly sipped the sugar water from the feeder.", createdAt="Thu Mar 24 2022 11:11:36", updatedAt="Tue Jul 20 2021 02:04:04")
    comment575b = Comment(videoId=279, channelId=85, content="Despite multiple complications and her near-death experience", createdAt="Tue Aug 31 2021 13:56:58", updatedAt="Sat Feb 12 2022 23:08:18")
    comment576b = Comment(videoId=346, channelId=73, content="I covered my friend in baby oil.", createdAt="Tue Apr 27 2021 18:13:07", updatedAt="Wed Jan 12 2022 18:28:37")
    comment577b = Comment(videoId=168, channelId=95, content="Choosing to do nothing is still a choice, after all.", createdAt="Sat Oct 23 2021 03:39:27", updatedAt="Wed Aug 25 2021 05:04:00")
    comment578b = Comment(videoId=122, channelId=38, content="This book is sure to liquefy your brain.", createdAt="Wed Jun 30 2021 09:01:01", updatedAt="Sun Jun 13 2021 21:44:46")
    comment579b = Comment(videoId=497, channelId=49, content="Green should have smelled more tranquil, but somehow it just tasted rotten.", createdAt="Wed Jun 16 2021 21:34:18", updatedAt="Sat Jan 01 2022 21:54:11")
    comment580b = Comment(videoId=208, channelId=22, content="At last", createdAt="Tue Dec 28 2021 02:26:10", updatedAt="Wed Mar 30 2022 13:28:18")
    comment581b = Comment(videoId=543, channelId=13, content="The book is in front of the table.", createdAt="Thu Mar 17 2022 17:04:16", updatedAt="Sat Jun 26 2021 19:57:23")
    comment582b = Comment(videoId=313, channelId=34, content="The sun had set and so had his dreams.", createdAt="Tue Dec 07 2021 07:04:10", updatedAt="Fri Oct 15 2021 23:40:49")
    comment583b = Comment(videoId=564, channelId=16, content="Normal activities took extraordinary amounts of concentration at the high altitude.", createdAt="Sun Aug 08 2021 17:48:16", updatedAt="Wed Sep 29 2021 00:18:20")
    comment584b = Comment(videoId=658, channelId=71, content="It was the best sandcastle he had ever seen.", createdAt="Thu Dec 23 2021 01:33:26", updatedAt="Sun Jul 04 2021 11:35:50")
    comment585b = Comment(videoId=371, channelId=3, content="It was the scarcity that fueled his creativity.", createdAt="Thu Sep 16 2021 09:14:26", updatedAt="Mon Mar 28 2022 02:53:54")
    comment586b = Comment(videoId=543, channelId=36, content="His son quipped that power bars were nothing more than adult candy bars.", createdAt="Tue Mar 08 2022 08:07:40", updatedAt="Sat May 22 2021 23:08:18")
    comment587b = Comment(videoId=528, channelId=74, content="She wrote him a long letter, but he didn't read it.", createdAt="Fri Apr 23 2021 05:17:15", updatedAt="Fri May 28 2021 12:41:04")
    comment588b = Comment(videoId=422, channelId=35, content="You have no right to call yourself creative until you look at a trowel and think that it would make a great lockpick.", createdAt="Mon Oct 11 2021 10:01:16", updatedAt="Sun Aug 22 2021 13:44:56")
    comment589b = Comment(videoId=693, channelId=9, content="All she wanted was the answer, but she had no idea how much she would hate it.", createdAt="Sun May 09 2021 05:02:44", updatedAt="Fri Oct 01 2021 14:25:04")
    comment590b = Comment(videoId=89, channelId=31, content="Mr. Montoya knows the way to the bakery even though he's never been there.", createdAt="Sat Dec 18 2021 18:02:12", updatedAt="Wed Jan 26 2022 05:47:06")
    comment591b = Comment(videoId=537, channelId=24, content="Mary plays the piano.", createdAt="Thu Oct 28 2021 19:25:12", updatedAt="Thu Mar 31 2022 14:23:33")
    comment592b = Comment(videoId=340, channelId=62, content="I had a friend in high school named Rick Shaw, but he was fairly useless as a mode of transport.", createdAt="Mon Feb 21 2022 20:49:17", updatedAt="Mon Mar 28 2022 10:15:57")
    comment593b = Comment(videoId=285, channelId=93, content="I would have gotten the promotion, but my attendance wasn’t good enough.", createdAt="Sat Jan 15 2022 16:44:22", updatedAt="Sat Oct 09 2021 21:45:42")
    comment594b = Comment(videoId=381, channelId=55, content="There are no heroes in a punk rock band.", createdAt="Sun Oct 24 2021 03:22:04", updatedAt="Mon Apr 26 2021 01:21:43")
    comment595b = Comment(videoId=745, channelId=24, content="Let me help you with your baggage.", createdAt="Fri Sep 17 2021 13:30:14", updatedAt="Sun Feb 27 2022 22:18:20")
    comment596b = Comment(videoId=234, channelId=5, content="Siri became confused when we reused to follow her directions.", createdAt="Thu Apr 07 2022 14:39:55", updatedAt="Sat Dec 25 2021 10:55:52")
    comment598b = Comment(videoId=667, channelId=34, content="Henry couldn't decide if he was an auto mechanic or a priest.", createdAt="Tue Mar 08 2022 21:40:43", updatedAt="Sun Oct 24 2021 22:31:36")
    comment599b = Comment(videoId=576, channelId=48, content="The efficiency with which he paired the socks in the drawer was quite admirable.", createdAt="Mon May 03 2021 07:41:51", updatedAt="Mon Oct 04 2021 17:14:14")
    comment600b = Comment(videoId=291, channelId=30, content="I used to practice weaving with spaghetti three hours a day but stopped because I didn't want to die alone.", createdAt="Wed Jun 09 2021 17:59:10", updatedAt="Thu Sep 09 2021 09:37:20")
    comment601b = Comment(videoId=309, channelId=60, content="Three years later, the coffin was still full of Jello.", createdAt="Wed Mar 30 2022 13:48:14", updatedAt="Tue Apr 20 2021 03:47:39")
    comment602b = Comment(videoId=664, channelId=25, content="Too many prisons have become early coffins.", createdAt="Thu Apr 07 2022 07:10:05", updatedAt="Tue Oct 26 2021 07:06:19")
    comment603b = Comment(videoId=295, channelId=95, content="As the years pass by, we all know owners look more and more like their dogs.", createdAt="Thu Apr 15 2021 15:44:08", updatedAt="Sun Jan 23 2022 18:32:34")
    comment604b = Comment(videoId=308, channelId=42, content="Twin 4-month-olds slept in the shade of the palm tree while the mother tanned in the sun.", createdAt="Thu Jun 10 2021 23:10:59", updatedAt="Thu Feb 03 2022 19:52:17")
    comment605b = Comment(videoId=316, channelId=90, content="The waitress was not amused when he ordered green eggs and ham.", createdAt="Sat Aug 07 2021 10:53:28", updatedAt="Wed Nov 10 2021 12:43:52")
    comment606b = Comment(videoId=78, channelId=53, content="Jenny made the announcement that her baby was an alien.", createdAt="Tue Sep 28 2021 20:38:17", updatedAt="Wed Aug 04 2021 17:41:49")
    comment607b = Comment(videoId=153, channelId=63, content="They decided to plant an orchard of cotton candy.", createdAt="Wed Jan 12 2022 10:50:59", updatedAt="Wed Sep 08 2021 21:01:51")
    comment608b = Comment(videoId=689, channelId=4, content="The minute she landed she understood the reason this was a fly-over state.", createdAt="Fri Jun 25 2021 20:58:25", updatedAt="Wed Sep 15 2021 00:15:16")
    comment609b = Comment(videoId=537, channelId=15, content="They got there early, and they got really good seats.", createdAt="Fri Dec 10 2021 00:32:14", updatedAt="Fri Jun 04 2021 11:36:50")
    comment610b = Comment(videoId=615, channelId=9, content="He embraced his new life as an eggplant.", createdAt="Fri Apr 01 2022 18:21:21", updatedAt="Tue Sep 14 2021 19:57:26")
    comment611b = Comment(videoId=416, channelId=61, content="I've never seen a more beautiful brandy glass filled with wine.", createdAt="Wed Aug 11 2021 12:10:10", updatedAt="Tue Oct 19 2021 11:44:56")
    comment612b = Comment(videoId=734, channelId=47, content="It didn't make sense unless you had the power to eat colors.", createdAt="Wed Nov 03 2021 00:02:16", updatedAt="Fri Oct 15 2021 01:35:08")
    comment613b = Comment(videoId=595, channelId=27, content="She had a difficult time owning up to her own crazy self.", createdAt="Sat Sep 04 2021 11:43:56", updatedAt="Sat Dec 11 2021 00:46:42")
    comment614b = Comment(videoId=132, channelId=29, content="They're playing the piano while flying in the plane.", createdAt="Wed Dec 22 2021 11:10:15", updatedAt="Sat Oct 23 2021 22:35:47")
    comment615b = Comment(videoId=713, channelId=5, content="Today I heard something new and unmemorable.", createdAt="Fri Sep 03 2021 17:32:56", updatedAt="Fri Jan 07 2022 10:05:23")
    comment617b = Comment(videoId=23, channelId=42, content="The secret code they created made no sense, even to them.", createdAt="Fri Dec 24 2021 15:42:23", updatedAt="Tue May 25 2021 08:33:40")
    comment619b = Comment(videoId=645, channelId=47, content="It must be easy to commit crimes as a snake because you don't have to worry about leaving fingerprints.", createdAt="Mon Sep 06 2021 20:11:26", updatedAt="Sat Sep 25 2021 23:29:31")
    comment620b = Comment(videoId=702, channelId=33, content="The worst thing about being at the top of the career ladder is that there's a long way to fall.", createdAt="Fri Aug 27 2021 16:54:58", updatedAt="Wed Sep 01 2021 12:33:58")
    comment621b = Comment(videoId=439, channelId=33, content="She opened up her third bottle of wine of the night.", createdAt="Sun Aug 22 2021 19:36:28", updatedAt="Mon May 10 2021 04:45:19")
    comment622b = Comment(videoId=185, channelId=67, content="I thought red would have felt warmer in summer but I didn't think about the equator.", createdAt="Thu Jul 08 2021 11:43:02", updatedAt="Fri Jan 28 2022 19:19:36")
    comment623b = Comment(videoId=651, channelId=19, content="The doll spun around in circles in hopes of coming alive.", createdAt="Sun Jun 13 2021 07:59:25", updatedAt="Sun Feb 06 2022 10:57:32")
    comment624b = Comment(videoId=367, channelId=37, content="I honestly find her about as intimidating as a basket of kittens.", createdAt="Wed Nov 10 2021 20:43:21", updatedAt="Fri May 14 2021 19:31:11")
    comment625b = Comment(videoId=364, channelId=17, content="She saw the brake lights, but not in time.", createdAt="Wed Dec 08 2021 17:15:42", updatedAt="Wed May 12 2021 05:58:29")
    comment626b = Comment(videoId=554, channelId=87, content="My biggest joy is roasting almonds while stalking prey.", createdAt="Sat Apr 09 2022 07:27:43", updatedAt="Fri Jan 14 2022 08:58:48")
    comment627b = Comment(videoId=162, channelId=49, content="He was so preoccupied with whether or not he could that he failed to stop to consider if he should.", createdAt="Tue Jul 06 2021 03:08:06", updatedAt="Tue Jan 04 2022 03:17:07")
    comment628b = Comment(videoId=436, channelId=39, content="As he waited for the shower to warm, he noticed that he could hear water change temperature.", createdAt="Wed Sep 22 2021 14:31:46", updatedAt="Fri Apr 30 2021 05:00:04")
    comment629b = Comment(videoId=435, channelId=11, content="My Mum tries to be cool by saying that she likes all the same things that I do.", createdAt="Mon Oct 04 2021 09:10:07", updatedAt="Thu Jul 22 2021 11:33:07")
    comment630b = Comment(videoId=457, channelId=19, content="She did a happy dance because all of the socks from the dryer matched.", createdAt="Sat Apr 24 2021 13:22:19", updatedAt="Tue Jul 06 2021 06:20:02")
    comment631b = Comment(videoId=718, channelId=10, content="Sarah ran from the serial killer holding a jug of milk.", createdAt="Thu Feb 17 2022 02:36:08", updatedAt="Wed Oct 13 2021 05:43:20")
    comment632b = Comment(videoId=357, channelId=59, content="When motorists sped in and out of traffic, all she could think of was those in need of a transplant.", createdAt="Wed May 26 2021 18:13:51", updatedAt="Mon Jun 07 2021 21:28:45")
    comment633b = Comment(videoId=385, channelId=46, content="He dreamed of leaving his law firm to open a portable dog wash.", createdAt="Thu Apr 07 2022 03:45:26", updatedAt="Wed Aug 11 2021 13:25:47")
    comment634b = Comment(videoId=267, channelId=93, content="He found the end of the rainbow and was surprised at what he found there.", createdAt="Sun Jan 16 2022 08:39:41", updatedAt="Fri Jul 23 2021 09:14:43")
    comment635b = Comment(videoId=539, channelId=87, content="Sometimes, all you need to do is completely make an ass of yourself and laugh it off to realise that life isn’t so bad after all.", createdAt="Thu Apr 29 2021 23:03:39", updatedAt="Sat Jan 22 2022 08:20:41")
    comment636b = Comment(videoId=269, channelId=53, content="It's not often you find a soggy banana on the street.", createdAt="Tue Nov 30 2021 19:31:46", updatedAt="Mon Mar 28 2022 18:15:47")
    comment637b = Comment(videoId=276, channelId=56, content="Acres of almond trees lined the interstate highway which complimented the crazy driving nuts.", createdAt="Sat Aug 28 2021 11:14:16", updatedAt="Thu May 13 2021 22:45:03")
    comment638b = Comment(videoId=281, channelId=45, content="The opportunity of a lifetime passed before him as he tried to decide between a cone or a cup.", createdAt="Mon Apr 26 2021 09:07:53", updatedAt="Wed Jan 19 2022 22:02:57")
    comment639b = Comment(videoId=271, channelId=74, content="At last", createdAt="Fri Dec 10 2021 20:17:28", updatedAt="Sat Oct 30 2021 00:35:13")
    comment640b = Comment(videoId=204, channelId=88, content="The teens wondered what was kept in the red shed on the far edge of the school grounds.", createdAt="Wed Jun 30 2021 19:02:46", updatedAt="Fri Sep 17 2021 09:40:33")
    comment641b = Comment(videoId=365, channelId=71, content="The blue parrot drove by the hitchhiking mongoose.", createdAt="Fri Mar 18 2022 21:12:02", updatedAt="Fri Jun 04 2021 06:44:27")
    comment642b = Comment(videoId=699, channelId=5, content="It took him a while to realize that everything he decided not to change, he was actually choosing.", createdAt="Mon Nov 22 2021 11:28:04", updatedAt="Mon Apr 26 2021 15:59:00")
    comment643b = Comment(videoId=324, channelId=5, content="I am counting my calories, yet I really want dessert.", createdAt="Mon Dec 20 2021 10:12:07", updatedAt="Sun Jun 27 2021 06:18:38")
    comment644b = Comment(videoId=78, channelId=38, content="He wondered if it could be called a beach if there was no sand.", createdAt="Tue Jun 01 2021 05:26:08", updatedAt="Mon Sep 06 2021 10:51:21")
    comment645b = Comment(videoId=83, channelId=38, content="He walked into the basement with the horror movie from the night before playing in his head.", createdAt="Wed Feb 16 2022 19:19:40", updatedAt="Fri Jan 21 2022 06:56:57")
    comment646b = Comment(videoId=456, channelId=66, content="There's a reason that roses have thorns.", createdAt="Thu Jul 08 2021 21:01:31", updatedAt="Sat Sep 25 2021 19:19:54")
    comment647b = Comment(videoId=232, channelId=34, content="The tortoise jumped into the lake with dreams of becoming a sea turtle.", createdAt="Wed Jun 16 2021 09:08:32", updatedAt="Tue Dec 21 2021 18:29:49")
    comment648b = Comment(videoId=206, channelId=92, content="I never knew what hardship looked like until it started raining bowling balls.", createdAt="Mon Mar 28 2022 03:55:02", updatedAt="Fri Sep 24 2021 01:27:12")
    comment649b = Comment(videoId=676, channelId=57, content="Everyone was curious about the large white blimp that appeared overnight.", createdAt="Fri Mar 18 2022 13:23:40", updatedAt="Sun Aug 22 2021 21:24:54")
    comment650b = Comment(videoId=733, channelId=81, content="We should play with legos at camp.", createdAt="Tue Oct 05 2021 00:08:00", updatedAt="Sun Apr 18 2021 20:44:04")
    comment651b = Comment(videoId=716, channelId=3, content="If my calculator had a history, it would be more embarrassing than my browser history.", createdAt="Sun May 09 2021 20:33:00", updatedAt="Sat Jul 31 2021 01:54:17")
    comment652b = Comment(videoId=549, channelId=50, content="Mom didn’t understand why no one else wanted a hot tub full of jello.", createdAt="Sun Aug 22 2021 06:15:14", updatedAt="Mon Sep 20 2021 21:44:10")
    comment653b = Comment(videoId=557, channelId=43, content="I was very proud of my nickname throughout high school but today- I couldn’t be any different to what my nickname was.", createdAt="Tue Jul 20 2021 16:13:47", updatedAt="Tue Oct 19 2021 17:41:20")
    comment654b = Comment(videoId=133, channelId=38, content="The knives were out and she was sharpening hers.", createdAt="Sat Feb 19 2022 21:53:02", updatedAt="Wed Apr 21 2021 14:08:21")
    comment655b = Comment(videoId=583, channelId=7, content="She had a difficult time owning up to her own crazy self.", createdAt="Sun Feb 06 2022 10:49:30", updatedAt="Sun Jul 18 2021 05:10:05")
    comment656b = Comment(videoId=519, channelId=14, content="Erin accidentally created a new universe.", createdAt="Wed Feb 02 2022 12:57:00", updatedAt="Wed Apr 21 2021 12:37:09")
    comment657b = Comment(videoId=763, channelId=10, content="They wandered into a strange Tiki bar on the edge of the small beach town.", createdAt="Mon Nov 15 2021 07:42:52", updatedAt="Mon Dec 20 2021 16:54:36")
    comment658b = Comment(videoId=574, channelId=3, content="I think I will buy the red car, or I will lease the blue one.", createdAt="Fri Jun 18 2021 17:45:57", updatedAt="Sat Jul 24 2021 14:01:40")
    comment659b = Comment(videoId=44, channelId=27, content="She felt that chill that makes the hairs on the back of your neck when he walked into the room.", createdAt="Sun Mar 13 2022 16:30:46", updatedAt="Sat Apr 02 2022 18:12:23")
    comment660b = Comment(videoId=393, channelId=25, content="Bill ran from the giraffe toward the dolphin.", createdAt="Wed Jul 07 2021 09:22:34", updatedAt="Sat Mar 19 2022 09:37:33")
    comment661b = Comment(videoId=488, channelId=44, content="When she didn’t like a guy who was trying to pick her up, she started using sign language.", createdAt="Thu Feb 03 2022 01:12:51", updatedAt="Mon Aug 23 2021 02:10:40")
    comment662b = Comment(videoId=141, channelId=6, content="We need to rent a room for our party.", createdAt="Mon Jun 28 2021 15:04:27", updatedAt="Sat May 01 2021 01:48:07")
    comment663b = Comment(videoId=210, channelId=18, content="Nobody has encountered an explosive daisy and lived to tell the tale.", createdAt="Mon Dec 06 2021 23:47:43", updatedAt="Sat Sep 04 2021 06:52:07")
    comment664b = Comment(videoId=415, channelId=93, content="She was the type of girl who wanted to live in a pink house.", createdAt="Sun Feb 20 2022 21:49:24", updatedAt="Sat Jun 26 2021 11:28:15")
    comment665b = Comment(videoId=395, channelId=30, content="Of course, she loves her pink bunny slippers.", createdAt="Wed Jan 26 2022 08:59:07", updatedAt="Wed Sep 08 2021 12:05:46")
    comment666b = Comment(videoId=290, channelId=86, content="Her life in the confines of the house became her new normal.", createdAt="Fri Mar 11 2022 21:41:01", updatedAt="Sun Feb 06 2022 05:22:26")
    comment667b = Comment(videoId=442, channelId=97, content="I met an interesting turtle while the song on the radio blasted away.", createdAt="Fri Oct 01 2021 15:24:23", updatedAt="Wed Sep 08 2021 18:26:57")
    comment668b = Comment(videoId=632, channelId=97, content="The near-death experience brought new ideas to light.", createdAt="Tue Jul 20 2021 03:54:35", updatedAt="Sun Jun 20 2021 16:55:38")
    comment669b = Comment(videoId=192, channelId=4, content="Boulders lined the side of the road foretelling what could come next.", createdAt="Wed Dec 01 2021 07:28:16", updatedAt="Fri Jul 16 2021 16:45:20")
    comment670b = Comment(videoId=24, channelId=37, content="I'm not a party animal, but I do like animal parties.", createdAt="Sat Jan 08 2022 23:46:16", updatedAt="Sat Dec 11 2021 21:48:52")
    comment671b = Comment(videoId=604, channelId=36, content="We will not allow you to bring your pet armadillo along.", createdAt="Sun Jan 30 2022 06:51:50", updatedAt="Mon Jun 14 2021 06:25:54")
    comment672b = Comment(videoId=234, channelId=30, content="She wasn't sure whether to be impressed or concerned that he folded underwear in neat little packages.", createdAt="Fri Sep 10 2021 00:13:19", updatedAt="Mon Jul 19 2021 02:47:31")
    comment673b = Comment(videoId=245, channelId=83, content="The water flowing down the river didn’t look that powerful from the car", createdAt="Mon Mar 21 2022 04:01:53", updatedAt="Wed Mar 23 2022 19:03:57")
    comment674b = Comment(videoId=535, channelId=62, content="Nothing seemed out of place except the washing machine in the bar.", createdAt="Sat Aug 14 2021 02:41:20", updatedAt="Sun Mar 06 2022 22:52:58")
    comment675b = Comment(videoId=399, channelId=81, content="There have been days when I wished to be separated from my body, but today wasn’t one of those days.", createdAt="Sun Nov 21 2021 13:42:07", updatedAt="Fri Mar 04 2022 19:06:31")
    comment676b = Comment(videoId=754, channelId=38, content="He spiked his hair green to support his iguana.", createdAt="Mon Jul 19 2021 05:14:46", updatedAt="Wed Jul 07 2021 20:08:37")
    comment677b = Comment(videoId=211, channelId=40, content="He was the only member of the club who didn't like plum pudding.", createdAt="Sat Dec 18 2021 00:20:11", updatedAt="Sat Mar 19 2022 00:59:01")
    comment678b = Comment(videoId=561, channelId=79, content="Green should have smelled more tranquil, but somehow it just tasted rotten.", createdAt="Thu Jan 20 2022 20:12:41", updatedAt="Wed Oct 06 2021 03:23:57")
    comment679b = Comment(videoId=552, channelId=62, content="He found a leprechaun in his walnut shell.", createdAt="Mon Oct 11 2021 23:41:03", updatedAt="Sat May 22 2021 18:48:35")
    comment680b = Comment(videoId=662, channelId=67, content="The llama couldn't resist trying the lemonade.", createdAt="Tue Apr 27 2021 23:58:04", updatedAt="Thu Nov 25 2021 17:13:44")
    comment681b = Comment(videoId=30, channelId=12, content="I don’t respect anybody who can’t tell the difference between Pepsi and Coke.", createdAt="Tue Dec 21 2021 14:45:30", updatedAt="Fri Jul 23 2021 10:45:45")
    comment682b = Comment(videoId=64, channelId=28, content="It must be five o'clock somewhere.", createdAt="Tue Jan 11 2022 05:50:37", updatedAt="Fri Apr 16 2021 19:15:02")
    comment683b = Comment(videoId=222, channelId=45, content="Peanut butter and jelly caused the elderly lady to think about her past.", createdAt="Tue Jul 20 2021 03:28:12", updatedAt="Sat Jun 05 2021 07:40:37")
    comment684b = Comment(videoId=26, channelId=10, content="The light in his life was actually a fire burning all around him.", createdAt="Mon Dec 06 2021 18:29:21", updatedAt="Sun Mar 13 2022 17:31:08")
    comment685b = Comment(videoId=600, channelId=12, content="It was the scarcity that fueled his creativity.", createdAt="Wed Oct 06 2021 04:19:49", updatedAt="Fri Oct 15 2021 17:08:33")
    comment686b = Comment(videoId=143, channelId=40, content="Mothers spend months of their lives waiting on their children.", createdAt="Thu Jan 06 2022 01:03:58", updatedAt="Fri Jun 18 2021 16:04:47")
    comment687b = Comment(videoId=382, channelId=35, content="Poison ivy grew through the fence they said was impenetrable.", createdAt="Thu Jul 15 2021 17:42:58", updatedAt="Sun May 30 2021 23:26:16")
    comment688b = Comment(videoId=705, channelId=95, content="Always bring cinnamon buns on a deep-sea diving expedition.", createdAt="Mon Mar 14 2022 05:38:03", updatedAt="Thu Feb 10 2022 06:06:28")
    comment689b = Comment(videoId=47, channelId=17, content="I'd always thought lightning was something only I could see.", createdAt="Sat Nov 27 2021 07:59:27", updatedAt="Sun Jun 13 2021 23:29:16")
    comment690b = Comment(videoId=559, channelId=50, content="Never underestimate the willingness of the greedy to throw you under the bus.", createdAt="Wed Jul 14 2021 18:16:10", updatedAt="Tue Oct 19 2021 19:34:58")
    comment691b = Comment(videoId=377, channelId=49, content="In the end, he realized he could see sound and hear words.", createdAt="Sat Oct 23 2021 22:33:12", updatedAt="Wed Jun 02 2021 20:29:16")
    comment692b = Comment(videoId=244, channelId=43, content="He wondered if she would appreciate his toenail collection.", createdAt="Sat Oct 02 2021 16:42:06", updatedAt="Sun Oct 17 2021 11:16:04")
    comment693b = Comment(videoId=311, channelId=72, content="The furnace repairman indicated the heating system was acting as an air conditioner.", createdAt="Thu Dec 16 2021 16:35:59", updatedAt="Sun Oct 17 2021 11:21:39")
    comment694b = Comment(videoId=574, channelId=52, content="The toddler’s endless tantrum caused the entire plane anxiety.", createdAt="Fri Jul 09 2021 17:45:45", updatedAt="Wed Sep 08 2021 09:42:14")
    comment695b = Comment(videoId=744, channelId=64, content="The old apple revels in its authority.", createdAt="Mon Jan 10 2022 06:10:54", updatedAt="Sun Apr 25 2021 04:31:07")
    comment696b = Comment(videoId=522, channelId=26, content="The worst thing about being at the top of the career ladder is that there's a long way to fall.", createdAt="Sat Feb 26 2022 16:58:50", updatedAt="Thu Jan 27 2022 06:11:18")
    comment697b = Comment(videoId=140, channelId=46, content="She had some amazing news to share but nobody to share it with.", createdAt="Tue May 18 2021 17:16:45", updatedAt="Sun Feb 20 2022 05:10:27")
    comment698b = Comment(videoId=194, channelId=47, content="Sometimes I stare at a door or a wall and I wonder what is this reality, why am I alive, and what is this all about?", createdAt="Fri Mar 25 2022 09:46:19", updatedAt="Thu Oct 07 2021 01:12:00")
    comment699b = Comment(videoId=186, channelId=74, content="Let me help you with your baggage.", createdAt="Fri Jun 25 2021 05:02:05", updatedAt="Thu Jan 20 2022 16:55:59")
    comment700b = Comment(videoId=491, channelId=18, content="While all her friends were positive that Mary had a sixth sense, she knew she actually had a seventh sense.", createdAt="Fri Aug 27 2021 06:24:36", updatedAt="Tue Aug 24 2021 06:58:53")
    comment701b = Comment(videoId=205, channelId=52, content="Three generations with six decades of life experience.", createdAt="Sat Jun 05 2021 00:30:56", updatedAt="Mon Feb 28 2022 09:24:25")
    comment702b = Comment(videoId=779, channelId=21, content="They ran around the corner to find that they had traveled back in time.", createdAt="Wed Oct 27 2021 22:05:45", updatedAt="Fri Mar 18 2022 10:55:58")
    comment703b = Comment(videoId=291, channelId=28, content="his seven-layer cake only had six layers.", createdAt="Sat Dec 04 2021 23:20:55", updatedAt="Tue Apr 20 2021 12:08:49")
    comment704b = Comment(videoId=320, channelId=67, content="Jim liked driving around town with his hazard lights on.", createdAt="Wed Jun 02 2021 05:44:19", updatedAt="Sun Jun 13 2021 09:36:11")
    comment705b = Comment(videoId=84, channelId=30, content="The spa attendant applied the deep cleaning mask to the gentleman’s back.", createdAt="Tue Jan 11 2022 10:29:24", updatedAt="Tue Apr 05 2022 02:12:15")
    comment706b = Comment(videoId=401, channelId=55, content="I’m working on a sweet potato farm.", createdAt="Mon Sep 20 2021 16:39:25", updatedAt="Wed Sep 15 2021 01:31:44")
    comment707b = Comment(videoId=630, channelId=93, content="The hawk didn’t understand why the ground squirrels didn’t want to be his friend.", createdAt="Tue Nov 09 2021 10:03:20", updatedAt="Tue Dec 21 2021 02:12:36")
    comment708b = Comment(videoId=344, channelId=19, content="Twin 4-month-olds slept in the shade of the palm tree while the mother tanned in the sun.", createdAt="Sat Jan 15 2022 19:25:43", updatedAt="Sat Nov 06 2021 12:46:16")
    comment709b = Comment(videoId=503, channelId=46, content="She borrowed the book from him many years ago and hasn't yet returned it.", createdAt="Thu May 06 2021 09:17:54", updatedAt="Fri Oct 29 2021 18:39:46")
    comment710b = Comment(videoId=125, channelId=31, content="I've traveled all around Africa and still haven't found the gnu who stole my scarf.", createdAt="Wed Sep 22 2021 15:10:04", updatedAt="Fri Dec 10 2021 10:56:45")
    comment711b = Comment(videoId=452, channelId=94, content="He spiked his hair green to support his iguana.", createdAt="Wed Jul 28 2021 16:34:30", updatedAt="Sat Dec 25 2021 18:04:33")
    comment712b = Comment(videoId=709, channelId=89, content="She moved forward only because she trusted that the ending she now was going through must be followed by a new beginning.", createdAt="Fri Aug 06 2021 11:00:34", updatedAt="Mon Oct 11 2021 09:02:42")
    comment713b = Comment(videoId=276, channelId=25, content="They desperately needed another drummer since the current one only knew how to play bongos.", createdAt="Tue Jul 06 2021 00:59:10", updatedAt="Sat Oct 16 2021 00:58:10")
    comment714b = Comment(videoId=527, channelId=1, content="Buried deep in the snow, he hoped his batteries were fresh in his avalanche beacon.", createdAt="Sat Jul 24 2021 14:06:27", updatedAt="Fri Apr 08 2022 11:31:21")
    comment715b = Comment(videoId=515, channelId=94, content="I am never at home on Sundays.", createdAt="Fri Feb 11 2022 04:47:39", updatedAt="Sat Jan 15 2022 23:27:29")
    comment716b = Comment(videoId=187, channelId=16, content="Gwen had her best sleep ever on her new bed of nails.", createdAt="Mon Apr 26 2021 19:05:51", updatedAt="Tue Apr 27 2021 10:37:32")
    comment717b = Comment(videoId=660, channelId=29, content="The chic gangster liked to start the day with a pink scarf.", createdAt="Sun Nov 21 2021 13:11:53", updatedAt="Fri Jan 21 2022 15:50:22")
    comment718b = Comment(videoId=15, channelId=45, content="The overpass went under the highway and into a secret world.", createdAt="Wed Jun 23 2021 21:06:14", updatedAt="Sun Aug 15 2021 21:08:52")
    comment719b = Comment(videoId=162, channelId=32, content="In that instant, everything changed.", createdAt="Sat Jan 15 2022 22:02:29", updatedAt="Wed Oct 20 2021 05:20:44")
    comment720b = Comment(videoId=580, channelId=57, content="Malls are great places to shop; I can find everything I need under one roof.", createdAt="Tue May 25 2021 14:41:36", updatedAt="Fri Jun 25 2021 01:35:10")
    comment721b = Comment(videoId=573, channelId=82, content="My secretary is the only person who truly understands my stamp-collecting obsession.", createdAt="Wed Jun 23 2021 02:17:43", updatedAt="Mon May 17 2021 08:18:10")
    comment722b = Comment(videoId=205, channelId=81, content="He decided to count all the sand on the beach as a hobby.", createdAt="Tue Jul 20 2021 00:10:25", updatedAt="Sat Dec 11 2021 22:06:08")
    comment723b = Comment(videoId=630, channelId=38, content="There can never be too many cherries on an ice cream sundae.", createdAt="Thu Sep 23 2021 17:03:59", updatedAt="Fri Jan 21 2022 04:42:36")
    comment724b = Comment(videoId=546, channelId=64, content="It took him a month to finish the meal.", createdAt="Mon Apr 04 2022 06:12:39", updatedAt="Sat Nov 20 2021 22:56:13")
    comment725b = Comment(videoId=66, channelId=52, content="He found the end of the rainbow and was surprised at what he found there.", createdAt="Sun Oct 31 2021 08:56:19", updatedAt="Sun Jan 16 2022 21:49:03")
    comment726b = Comment(videoId=516, channelId=38, content="All you need to do is pick up the pen and begin.", createdAt="Tue Mar 08 2022 03:49:36", updatedAt="Wed Apr 28 2021 07:42:36")
    comment727b = Comment(videoId=712, channelId=99, content="Thigh-high in the water, the fisherman’s hope for dinner soon turned to despair.", createdAt="Mon Mar 28 2022 21:27:43", updatedAt="Sun Oct 03 2021 01:42:13")
    comment728b = Comment(videoId=347, channelId=63, content="It turns out you don't need all that stuff you insisted you did.", createdAt="Wed Nov 24 2021 09:15:14", updatedAt="Sun Jul 11 2021 06:44:56")
    comment729b = Comment(videoId=635, channelId=98, content="Acres of almond trees lined the interstate highway which complimented the crazy driving nuts.", createdAt="Mon Dec 27 2021 04:44:03", updatedAt="Wed Oct 06 2021 04:45:17")
    comment730b = Comment(videoId=43, channelId=92, content="Tomorrow will bring something new, so leave today as a memory.", createdAt="Sat Jan 08 2022 12:12:17", updatedAt="Tue Jun 29 2021 13:06:59")
    comment731b = Comment(videoId=685, channelId=54, content="It didn't make sense unless you had the power to eat colors.", createdAt="Sat Mar 26 2022 07:49:09", updatedAt="Sat May 01 2021 19:44:42")
    comment732b = Comment(videoId=189, channelId=85, content="Tomatoes make great weapons when water balloons aren’t available.", createdAt="Thu Jul 29 2021 14:41:23", updatedAt="Fri Jul 09 2021 14:15:53")
    comment733b = Comment(videoId=760, channelId=99, content="If eating three-egg omelets causes weight-gain, budgie eggs are a good substitute.", createdAt="Fri Aug 06 2021 05:12:41", updatedAt="Mon Oct 18 2021 15:52:48")
    comment734b = Comment(videoId=142, channelId=86, content="Mary plays the piano.", createdAt="Wed Apr 21 2021 03:26:01", updatedAt="Sun Nov 07 2021 00:49:08")
    comment735b = Comment(videoId=125, channelId=90, content="When money was tight, he'd get his lunch money from the local wishing well.", createdAt="Mon May 10 2021 15:50:06", updatedAt="Fri Apr 08 2022 15:53:46")
    comment736b = Comment(videoId=27, channelId=29, content="Some bathing suits just shouldn’t be worn by some people.", createdAt="Sun Sep 12 2021 19:06:45", updatedAt="Fri May 21 2021 06:54:54")
    comment737b = Comment(videoId=152, channelId=85, content="Martha came to the conclusion that shake weights are a great gift for any occasion.", createdAt="Fri Jun 18 2021 16:46:04", updatedAt="Thu Dec 30 2021 04:41:04")
    comment738b = Comment(videoId=25, channelId=50, content="The virus had powers none of us knew existed.", createdAt="Sun Feb 27 2022 04:59:58", updatedAt="Sun Dec 12 2021 23:51:44")
    comment739b = Comment(videoId=73, channelId=23, content="Despite multiple complications and her near-death experience", createdAt="Sat Dec 18 2021 16:46:05", updatedAt="Fri Jan 14 2022 11:48:16")
    comment740b = Comment(videoId=539, channelId=56, content="Today we gathered moss for my uncle's wedding.", createdAt="Sun Mar 27 2022 13:10:16", updatedAt="Fri Nov 05 2021 03:17:28")
    comment741b = Comment(videoId=702, channelId=50, content="He found a leprechaun in his walnut shell.", createdAt="Sat Feb 12 2022 06:01:10", updatedAt="Thu Dec 23 2021 11:44:34")
    comment742b = Comment(videoId=554, channelId=48, content="I'm a great listener, really good with empathy vs sympathy and all that, but I hate people.", createdAt="Fri Mar 11 2022 16:00:30", updatedAt="Mon Feb 28 2022 20:38:33")
    comment743b = Comment(videoId=440, channelId=31, content="The best part of marriage is animal crackers with peanut butter.", createdAt="Sun Oct 31 2021 07:43:11", updatedAt="Tue Jun 08 2021 01:50:38")
    comment744b = Comment(videoId=163, channelId=15, content="She always speaks to him in a loud voice.", createdAt="Mon Dec 20 2021 21:00:32", updatedAt="Thu Apr 07 2022 23:32:37")
    comment745b = Comment(videoId=327, channelId=24, content="The three-year-old girl ran down the beach as the kite flew behind her.", createdAt="Wed Jun 23 2021 06:40:23", updatedAt="Tue Nov 02 2021 18:47:42")
    comment746b = Comment(videoId=599, channelId=52, content="I've always wanted to go to Tajikistan, but my cat would miss me.", createdAt="Thu Dec 30 2021 09:37:00", updatedAt="Sat May 29 2021 07:38:52")
    comment747b = Comment(videoId=675, channelId=28, content="He had a vague sense that trees gave birth to dinosaurs.", createdAt="Mon Nov 08 2021 22:56:11", updatedAt="Thu Jan 20 2022 18:36:23")
    comment748b = Comment(videoId=754, channelId=44, content="He's in a boy band which doesn't make much sense for a snake.", createdAt="Fri Oct 29 2021 17:11:35", updatedAt="Mon Apr 19 2021 09:38:24")
    comment749b = Comment(videoId=728, channelId=70, content="He decided water-skiing on a frozen lake wasn’t a good idea.", createdAt="Sat Jul 31 2021 10:04:44", updatedAt="Sat Apr 09 2022 20:13:59")
    comment750b = Comment(videoId=153, channelId=91, content="The stench from the feedlot permeated the car despite having the air conditioning on recycled air.", createdAt="Sun Aug 22 2021 14:20:48", updatedAt="Fri Mar 04 2022 20:28:09")
    comment751b = Comment(videoId=296, channelId=21, content="Just go ahead and press that button.", createdAt="Sat Jan 22 2022 03:15:32", updatedAt="Mon Apr 26 2021 14:01:27")
    comment752b = Comment(videoId=260, channelId=13, content="They wandered into a strange Tiki bar on the edge of the small beach town.", createdAt="Sat Aug 14 2021 17:42:36", updatedAt="Wed Feb 02 2022 00:53:48")
    comment753b = Comment(videoId=160, channelId=75, content="The white water rafting trip was suddenly halted by the unexpected brick wall.", createdAt="Tue Nov 16 2021 21:05:32", updatedAt="Sat Oct 23 2021 13:36:08")
    comment754b = Comment(videoId=748, channelId=14, content="The beauty of the sunset was obscured by the industrial cranes.", createdAt="Wed Jul 21 2021 18:28:58", updatedAt="Wed Dec 22 2021 05:15:33")
    comment755b = Comment(videoId=520, channelId=17, content="He kept telling himself that one day it would all somehow make sense.", createdAt="Wed Nov 03 2021 00:24:41", updatedAt="Thu May 20 2021 01:19:37")
    comment756b = Comment(videoId=94, channelId=90, content="Carol drank the blood as if she were a vampire.", createdAt="Sat Jul 31 2021 20:58:03", updatedAt="Sun Aug 08 2021 21:44:32")
    comment757b = Comment(videoId=350, channelId=84, content="She only paints with bold colors; she does not like pastels.", createdAt="Fri Mar 04 2022 00:33:23", updatedAt="Fri Oct 22 2021 03:52:35")
    comment759b = Comment(videoId=345, channelId=25, content="Henry couldn't decide if he was an auto mechanic or a priest.", createdAt="Sun May 30 2021 21:33:43", updatedAt="Sun Feb 20 2022 10:37:40")
    comment760b = Comment(videoId=396, channelId=81, content="Malls are great places to shop; I can find everything I need under one roof.", createdAt="Sat Mar 12 2022 13:55:12", updatedAt="Sun Aug 08 2021 05:25:22")
    comment761b = Comment(videoId=700, channelId=61, content="He didn't understand why the bird wanted to ride the bicycle.", createdAt="Thu Jan 27 2022 20:50:56", updatedAt="Mon Mar 21 2022 18:20:11")
    comment762b = Comment(videoId=399, channelId=52, content="Stop waiting for exceptional things to just happen.", createdAt="Fri Aug 13 2021 05:47:43", updatedAt="Sat Jun 26 2021 23:54:12")
    comment763b = Comment(videoId=456, channelId=75, content="He uses onomatopoeia as a weapon of mental destruction.", createdAt="Wed Jun 16 2021 10:09:08", updatedAt="Sat Mar 19 2022 17:27:54")
    comment764b = Comment(videoId=438, channelId=18, content="He swore he just saw his sushi move.", createdAt="Mon Oct 25 2021 10:12:57", updatedAt="Sun Mar 20 2022 01:06:20")
    comment765b = Comment(videoId=340, channelId=11, content="They desperately needed another drummer since the current one only knew how to play bongos.", createdAt="Thu Oct 21 2021 06:03:17", updatedAt="Sat Jul 17 2021 06:39:51")
    comment766b = Comment(videoId=165, channelId=42, content="Joyce enjoyed eating pancakes with ketchup.", createdAt="Tue Mar 15 2022 23:59:39", updatedAt="Sat Mar 12 2022 07:07:46")
    comment767b = Comment(videoId=141, channelId=88, content="He colored deep space a soft yellow.", createdAt="Thu Jul 15 2021 05:47:52", updatedAt="Sat Mar 19 2022 17:35:35")
    comment768b = Comment(videoId=307, channelId=81, content="He set out for a short walk, but now all he could see were mangroves and water were for miles.", createdAt="Tue May 18 2021 09:34:52", updatedAt="Sat Mar 19 2022 21:40:34")
    comment769b = Comment(videoId=208, channelId=64, content="She wore green lipstick like a fashion icon.", createdAt="Wed May 12 2021 21:25:09", updatedAt="Fri May 07 2021 15:40:48")
    comment770b = Comment(videoId=363, channelId=12, content="We should play with legos at camp.", createdAt="Sun Jul 11 2021 05:36:27", updatedAt="Thu Aug 05 2021 05:23:34")
    comment771b = Comment(videoId=524, channelId=48, content="He created a pig burger out of beef.", createdAt="Mon Mar 14 2022 07:32:07", updatedAt="Thu Feb 10 2022 16:51:51")
    comment772b = Comment(videoId=740, channelId=18, content="Jason didn’t understand why his parents wouldn’t let him sell his little sister at the garage sale.", createdAt="Wed Jan 05 2022 20:44:37", updatedAt="Sat Jan 22 2022 19:27:07")
    comment773b = Comment(videoId=752, channelId=6, content="The crowd yells and screams for more memes.", createdAt="Wed Oct 13 2021 01:27:24", updatedAt="Mon Feb 07 2022 23:42:29")
    comment774b = Comment(videoId=249, channelId=85, content="The bird had a belief that it was really a groundhog.", createdAt="Fri Nov 12 2021 13:45:52", updatedAt="Fri Apr 08 2022 20:07:43")
    comment775b = Comment(videoId=376, channelId=88, content="Your girlfriend bought your favorite cookie crisp cereal but forgot to get milk.", createdAt="Wed Dec 08 2021 03:28:16", updatedAt="Wed Jan 19 2022 20:51:39")
    comment776b = Comment(videoId=431, channelId=81, content="Green should have smelled more tranquil, but somehow it just tasted rotten.", createdAt="Fri Jun 18 2021 07:50:04", updatedAt="Sun Sep 05 2021 09:46:22")
    comment777b = Comment(videoId=710, channelId=99, content="Going from child, to childish, to childlike is only a matter of time.", createdAt="Wed Feb 23 2022 03:09:40", updatedAt="Sun Nov 21 2021 02:01:04")
    comment778b = Comment(videoId=93, channelId=66, content="I'd rather be a bird than a fish.", createdAt="Mon Aug 02 2021 02:16:03", updatedAt="Sat Apr 09 2022 04:04:48")
    comment779b = Comment(videoId=165, channelId=50, content="I want to buy a onesie… but know it won’t suit me.", createdAt="Sat Oct 09 2021 10:29:59", updatedAt="Wed Jan 26 2022 21:22:09")
    comment780b = Comment(videoId=586, channelId=38, content="Erin accidentally created a new universe.", createdAt="Mon Apr 04 2022 12:47:52", updatedAt="Thu Sep 23 2021 20:16:57")
    comment781b = Comment(videoId=127, channelId=28, content="He decided to fake his disappearance to avoid jail.", createdAt="Tue Mar 22 2022 08:59:13", updatedAt="Tue Oct 05 2021 21:56:02")
    comment782b = Comment(videoId=177, channelId=95, content="He was all business when he wore his clown suit.", createdAt="Thu Jan 06 2022 13:06:31", updatedAt="Tue Sep 28 2021 02:56:14")
    comment783b = Comment(videoId=315, channelId=98, content="I don’t respect anybody who can’t tell the difference between Pepsi and Coke.", createdAt="Thu Mar 31 2022 02:51:35", updatedAt="Fri Nov 26 2021 12:34:59")
    comment784b = Comment(videoId=297, channelId=20, content="They called out her name time and again, but were met with nothing but silence.", createdAt="Fri Dec 03 2021 10:35:10", updatedAt="Fri May 14 2021 08:17:42")
    comment785b = Comment(videoId=695, channelId=99, content="Before he moved to the inner city, he had always believed that security complexes were psychological.", createdAt="Thu Nov 18 2021 15:43:11", updatedAt="Tue Sep 14 2021 10:25:20")
    comment786b = Comment(videoId=366, channelId=38, content="I've always wanted to go to Tajikistan, but my cat would miss me.", createdAt="Sun Jul 04 2021 03:45:12", updatedAt="Sun Oct 03 2021 10:06:56")
    comment787b = Comment(videoId=604, channelId=85, content="For the 216th time, he said he would quit drinking soda after this last Coke.", createdAt="Sun Jul 18 2021 11:22:03", updatedAt="Fri Mar 25 2022 20:15:29")
    comment789b = Comment(videoId=716, channelId=77, content="It was the best sandcastle he had ever seen.", createdAt="Fri Mar 11 2022 09:10:56", updatedAt="Mon Mar 14 2022 09:00:36")
    comment790b = Comment(videoId=595, channelId=93, content="My biggest joy is roasting almonds while stalking prey.", createdAt="Mon Sep 20 2021 01:41:32", updatedAt="Mon Apr 04 2022 05:31:39")
    comment791b = Comment(videoId=35, channelId=31, content="Harrold felt confident that nobody would ever suspect his spy pigeon.", createdAt="Sun Nov 21 2021 12:54:35", updatedAt="Sun Jan 23 2022 22:52:03")
    comment792b = Comment(videoId=231, channelId=96, content="All they could see was the blue water surrounding their sailboat.", createdAt="Tue Nov 30 2021 07:34:59", updatedAt="Tue Mar 22 2022 16:06:19")
    comment793b = Comment(videoId=336, channelId=49, content="He felt that dining on the bridge brought romance to his relationship with his cat.", createdAt="Fri Nov 26 2021 00:50:13", updatedAt="Sat Jan 29 2022 18:03:33")
    comment794b = Comment(videoId=726, channelId=51, content="If any cop asks you where you were, just say you were visiting Kansas.", createdAt="Wed Nov 24 2021 03:04:13", updatedAt="Thu Oct 07 2021 00:30:02")
    comment795b = Comment(videoId=259, channelId=87, content="The trick to getting kids to eat anything is to put catchup on it.", createdAt="Sun Feb 20 2022 15:45:34", updatedAt="Wed Aug 25 2021 03:02:11")
    comment796b = Comment(videoId=777, channelId=66, content="He always wore his sunglasses at night.", createdAt="Mon Aug 16 2021 00:00:15", updatedAt="Sat Mar 26 2022 16:17:05")
    comment797b = Comment(videoId=581, channelId=85, content="She had that tint of craziness in her soul that made her believe she could actually make a difference.", createdAt="Tue Feb 15 2022 04:10:05", updatedAt="Sun Dec 26 2021 06:48:35")
    comment798b = Comment(videoId=484, channelId=29, content="She discovered van life is difficult with 2 cats and a dog.", createdAt="Tue Apr 20 2021 17:36:53", updatedAt="Sat Nov 27 2021 19:18:25")
    comment799b = Comment(videoId=522, channelId=21, content="She moved forward only because she trusted that the ending she now was going through must be followed by a new beginning.", createdAt="Fri Mar 25 2022 20:31:13", updatedAt="Wed Apr 28 2021 05:32:44")
    comment800b = Comment(videoId=588, channelId=82, content="If you like tuna and tomato sauce, try combining the two, it’s really not as bad as it sounds.", createdAt="Sat Sep 25 2021 01:39:19", updatedAt="Tue Jul 06 2021 16:49:38")
    comment801b = Comment(videoId=212, channelId=48, content="The best part of marriage is animal crackers with peanut butter.", createdAt="Sat Oct 23 2021 17:37:50", updatedAt="Sun Jul 11 2021 03:39:22")
    comment802b = Comment(videoId=580, channelId=60, content="For oil spots on the floor, nothing beats parking a motorbike in the lounge.", createdAt="Fri Aug 13 2021 15:46:51", updatedAt="Sun Oct 24 2021 12:47:08")
    comment803b = Comment(videoId=352, channelId=63, content="Yeah, I think it's a good environment for learning English.", createdAt="Thu Dec 16 2021 18:15:44", updatedAt="Mon Aug 02 2021 05:44:15")
    comment804b = Comment(videoId=428, channelId=21, content="The sun had set and so had his dreams.", createdAt="Wed Sep 29 2021 19:44:59", updatedAt="Wed May 05 2021 12:43:20")
    comment805b = Comment(videoId=398, channelId=89, content="She couldn't decide of the glass was half empty or half full so she drank it.", createdAt="Thu Jul 08 2021 11:13:10", updatedAt="Sun Apr 25 2021 10:57:31")
    comment806b = Comment(videoId=710, channelId=46, content="Art doesn't have to be intentional.", createdAt="Wed Jun 09 2021 04:41:13", updatedAt="Wed Aug 18 2021 06:51:27")
    comment807b = Comment(videoId=12, channelId=83, content="She cried diamonds.", createdAt="Wed Oct 06 2021 04:15:05", updatedAt="Fri Apr 01 2022 19:19:08")
    comment808b = Comment(videoId=237, channelId=75, content="Lightning Paradise was the local hangout joint where the group usually ended up spending the night.", createdAt="Sat Nov 20 2021 00:46:17", updatedAt="Wed Jun 02 2021 18:54:23")
    comment809b = Comment(videoId=548, channelId=16, content="Don't step on the broken glass.", createdAt="Sun Aug 29 2021 21:30:19", updatedAt="Tue Mar 15 2022 14:36:42")
    comment810b = Comment(videoId=424, channelId=86, content="He realized there had been several deaths on this road, but his concern rose when he saw the exact number.", createdAt="Thu Dec 30 2021 21:49:52", updatedAt="Tue Feb 22 2022 22:47:34")
    comment811b = Comment(videoId=191, channelId=76, content="At that moment he wasn't listening to music, he was living an experience.", createdAt="Sun Sep 05 2021 08:52:45", updatedAt="Mon Apr 12 2021 12:13:57")
    comment812b = Comment(videoId=773, channelId=31, content="She saw no irony asking me to change but wanting me to accept her for who she is.", createdAt="Sun Jan 09 2022 13:28:41", updatedAt="Sun Feb 06 2022 17:50:41")
    comment813b = Comment(videoId=753, channelId=58, content="Dan ate the clouds like cotton candy.", createdAt="Mon Sep 20 2021 13:24:35", updatedAt="Fri Dec 17 2021 20:26:42")
    comment814b = Comment(videoId=40, channelId=31, content="As he dangled from the rope deep inside the crevasse", createdAt="Thu Oct 28 2021 05:10:47", updatedAt="Sun Jun 13 2021 21:09:56")
    comment815b = Comment(videoId=637, channelId=98, content="The miniature pet elephant became the envy of the neighborhood.", createdAt="Sun Dec 19 2021 20:03:23", updatedAt="Tue Oct 26 2021 21:49:41")
    comment816b = Comment(videoId=479, channelId=19, content="On a scale from one to ten, what's your favorite flavor of random grammar?", createdAt="Wed Feb 23 2022 20:28:35", updatedAt="Wed Apr 06 2022 20:37:03")
    comment817b = Comment(videoId=299, channelId=38, content="I used to practice weaving with spaghetti three hours a day but stopped because I didn't want to die alone.", createdAt="Wed Oct 20 2021 17:38:35", updatedAt="Mon Mar 28 2022 15:59:21")
    comment818b = Comment(videoId=430, channelId=92, content="It was her first experience training a rainbow unicorn.", createdAt="Wed May 05 2021 05:20:00", updatedAt="Fri Jan 07 2022 03:04:54")
    comment819b = Comment(videoId=421, channelId=72, content="The truth is that you pay for your lifestyle in hours.", createdAt="Tue Oct 12 2021 06:04:56", updatedAt="Wed Mar 16 2022 07:01:46")
    comment820b = Comment(videoId=204, channelId=99, content="Three generations with six decades of life experience.", createdAt="Tue Sep 14 2021 03:54:04", updatedAt="Tue May 25 2021 22:55:42")
    comment821b = Comment(videoId=163, channelId=56, content="The urgent care center was flooded with patients after the news of a new deadly virus was made public.", createdAt="Fri Nov 19 2021 22:05:27", updatedAt="Wed Feb 16 2022 23:06:21")
    comment822b = Comment(videoId=454, channelId=30, content="His son quipped that power bars were nothing more than adult candy bars.", createdAt="Sun Dec 12 2021 05:21:02", updatedAt="Tue Oct 05 2021 06:38:33")
    comment823b = Comment(videoId=155, channelId=44, content="He dreamed of eating green apples with worms.", createdAt="Wed May 19 2021 05:25:55", updatedAt="Wed Feb 23 2022 03:23:31")
    comment824b = Comment(videoId=142, channelId=44, content="Siri became confused when we reused to follow her directions.", createdAt="Fri Mar 18 2022 16:32:27", updatedAt="Mon Apr 04 2022 07:18:09")
    comment825b = Comment(videoId=119, channelId=48, content="She was sad to hear that fireflies are facing extinction due to artificial light, habitat loss, and pesticides.", createdAt="Sat Jan 15 2022 18:59:01", updatedAt="Sun Dec 05 2021 20:46:17")
    comment826b = Comment(videoId=619, channelId=90, content="He was an introvert that extroverts seemed to love.", createdAt="Mon Nov 15 2021 22:22:10", updatedAt="Mon Dec 20 2021 19:01:10")
    comment828b = Comment(videoId=185, channelId=62, content="The external scars tell only part of the story.", createdAt="Tue Sep 21 2021 09:26:07", updatedAt="Sat Oct 09 2021 12:57:14")
    comment829b = Comment(videoId=131, channelId=74, content="The book is in front of the table.", createdAt="Sat Aug 21 2021 01:58:44", updatedAt="Mon Aug 02 2021 03:46:01")
    comment830b = Comment(videoId=70, channelId=80, content="The father died during childbirth.", createdAt="Sat Dec 18 2021 05:18:29", updatedAt="Thu Sep 30 2021 12:41:29")
    comment831b = Comment(videoId=118, channelId=61, content="He was surprised that his immense laziness was inspirational to others.", createdAt="Tue Nov 02 2021 09:12:57", updatedAt="Mon May 24 2021 12:29:38")
    comment832b = Comment(videoId=250, channelId=1, content="Waffles are always better without fire ants and fleas.", createdAt="Sat Mar 26 2022 13:28:48", updatedAt="Sat Jul 10 2021 01:28:30")
    comment833b = Comment(videoId=138, channelId=46, content="He ended up burning his fingers poking someone else's fire.", createdAt="Thu Feb 24 2022 00:34:57", updatedAt="Wed Jul 14 2021 14:00:20")
    comment834b = Comment(videoId=67, channelId=66, content="If you like tuna and tomato sauce, try combining the two, it’s really not as bad as it sounds.", createdAt="Mon Sep 06 2021 20:44:55", updatedAt="Sun Oct 24 2021 00:09:47")
    comment835b = Comment(videoId=495, channelId=93, content="Please tell me you don't work in a morgue.", createdAt="Tue Apr 20 2021 17:29:58", updatedAt="Tue May 25 2021 01:03:44")
    comment836b = Comment(videoId=577, channelId=87, content="The water flowing down the river didn’t look that powerful from the car", createdAt="Tue Mar 08 2022 23:52:48", updatedAt="Fri Aug 06 2021 11:03:05")
    comment837b = Comment(videoId=767, channelId=81, content="The blue parrot drove by the hitchhiking mongoose.", createdAt="Sat Oct 09 2021 11:40:31", updatedAt="Mon Jun 21 2021 13:48:44")
    comment838b = Comment(videoId=22, channelId=60, content="The old apple revels in its authority.", createdAt="Sun Feb 20 2022 06:29:52", updatedAt="Mon Aug 02 2021 12:11:48")
    comment839b = Comment(videoId=609, channelId=66, content="Imagine his surprise when he discovered that the safe was full of pudding.", createdAt="Fri Mar 04 2022 23:10:22", updatedAt="Sun Nov 28 2021 20:52:30")
    comment840b = Comment(videoId=713, channelId=53, content="It turns out you don't need all that stuff you insisted you did.", createdAt="Thu Aug 26 2021 13:02:03", updatedAt="Tue Jul 20 2021 03:11:30")
    comment841b = Comment(videoId=86, channelId=41, content="I may struggle with geography, but I'm sure I'm somewhere around here.", createdAt="Fri Feb 04 2022 16:12:37", updatedAt="Wed Jun 30 2021 17:34:26")
    comment842b = Comment(videoId=571, channelId=6, content="One small action would change her life, but whether it would be for better or for worse was yet to be determined.", createdAt="Wed Mar 09 2022 14:45:04", updatedAt="Sun Dec 26 2021 21:56:53")
    comment843b = Comment(videoId=400, channelId=62, content="I often see the time 11:11 or 12:34 on clocks.", createdAt="Sat Nov 13 2021 22:31:00", updatedAt="Thu Nov 18 2021 13:48:04")
    comment844b = Comment(videoId=181, channelId=77, content="The furnace repairman indicated the heating system was acting as an air conditioner.", createdAt="Sun Jun 20 2021 08:02:15", updatedAt="Mon Jan 31 2022 03:45:04")
    comment845b = Comment(videoId=139, channelId=92, content="Behind the window was a reflection that only instilled fear.", createdAt="Fri Feb 11 2022 07:39:57", updatedAt="Thu Apr 29 2021 20:11:19")
    comment846b = Comment(videoId=545, channelId=22, content="his seven-layer cake only had six layers.", createdAt="Mon Aug 23 2021 05:42:04", updatedAt="Wed Feb 02 2022 21:59:19")
    comment847b = Comment(videoId=188, channelId=99, content="There's a message for you if you look up.", createdAt="Mon Nov 01 2021 10:33:02", updatedAt="Sun Feb 27 2022 14:38:10")
    comment848b = Comment(videoId=654, channelId=93, content="He kept telling himself that one day it would all somehow make sense.", createdAt="Sun Feb 06 2022 05:40:14", updatedAt="Tue Jan 25 2022 07:41:49")
    comment849b = Comment(videoId=279, channelId=54, content="As the asteroid hurtled toward earth, Becky was upset her dentist appointment had been canceled.", createdAt="Sun Jan 02 2022 11:36:44", updatedAt="Sun Apr 11 2021 00:18:34")
    comment850b = Comment(videoId=605, channelId=44, content="I'd always thought lightning was something only I could see.", createdAt="Wed Jul 21 2021 01:40:58", updatedAt="Wed Feb 16 2022 08:10:58")
    comment852b = Comment(videoId=530, channelId=10, content="He went back to the video to see what had been recorded and was shocked at what he saw.", createdAt="Fri Jul 23 2021 13:04:52", updatedAt="Wed Apr 06 2022 05:43:27")
    comment853b = Comment(videoId=158, channelId=50, content="Dan ate the clouds like cotton candy.", createdAt="Wed Jan 05 2022 13:07:50", updatedAt="Fri Nov 19 2021 07:49:44")
    comment854b = Comment(videoId=335, channelId=17, content="Flying fish flew by the space station.", createdAt="Fri Jan 07 2022 20:43:26", updatedAt="Mon Feb 28 2022 00:16:38")
    comment855b = Comment(videoId=331, channelId=60, content="Various sea birds are elegant, but nothing is as elegant as a gliding pelican.", createdAt="Mon Jan 24 2022 02:06:16", updatedAt="Sat Feb 12 2022 23:01:47")
    comment856b = Comment(videoId=52, channelId=13, content="He stepped gingerly onto the bridge knowing that enchantment awaited on the other side.", createdAt="Sun Aug 15 2021 15:03:34", updatedAt="Fri Aug 20 2021 00:18:48")
    comment857b = Comment(videoId=456, channelId=74, content="The truth is that you pay for your lifestyle in hours.", createdAt="Sun May 23 2021 02:01:23", updatedAt="Thu Dec 16 2021 17:41:57")
    comment858b = Comment(videoId=165, channelId=76, content="Sometimes it is better to just walk away from things and go back to them later when you’re in a better frame of mind.", createdAt="Fri Apr 16 2021 16:46:08", updatedAt="Tue Aug 17 2021 07:56:14")
    comment859b = Comment(videoId=109, channelId=57, content="Sometimes I stare at a door or a wall and I wonder what is this reality, why am I alive, and what is this all about?", createdAt="Tue May 11 2021 02:48:46", updatedAt="Mon Oct 11 2021 20:42:51")
    comment860b = Comment(videoId=699, channelId=64, content="The secret ingredient to his wonderful life was crime.", createdAt="Thu Sep 23 2021 03:27:05", updatedAt="Sun Jul 04 2021 18:56:27")
    comment861b = Comment(videoId=639, channelId=56, content="The doll spun around in circles in hopes of coming alive.", createdAt="Thu Oct 21 2021 19:26:54", updatedAt="Fri Oct 29 2021 10:43:52")
    comment862b = Comment(videoId=187, channelId=41, content="Too many prisons have become early coffins.", createdAt="Wed Mar 23 2022 16:12:28", updatedAt="Wed Apr 06 2022 00:56:03")
    comment863b = Comment(videoId=705, channelId=68, content="He played the game as if his life depended on it and the truth was that it did.", createdAt="Mon Dec 06 2021 19:43:29", updatedAt="Wed Oct 20 2021 07:28:56")
    comment864b = Comment(videoId=374, channelId=26, content="The tour bus was packed with teenage girls heading toward their next adventure.", createdAt="Wed Sep 22 2021 03:15:49", updatedAt="Sun Feb 13 2022 05:41:36")
    comment865b = Comment(videoId=575, channelId=47, content="She saw no irony asking me to change but wanting me to accept her for who she is.", createdAt="Sun Nov 14 2021 00:38:45", updatedAt="Thu Nov 04 2021 01:41:44")
    comment866b = Comment(videoId=496, channelId=27, content="The furnace repairman indicated the heating system was acting as an air conditioner.", createdAt="Wed Jun 02 2021 10:22:31", updatedAt="Sun Feb 13 2022 11:30:50")
    comment867b = Comment(videoId=419, channelId=52, content="Some bathing suits just shouldn’t be worn by some people.", createdAt="Thu Jun 03 2021 07:09:38", updatedAt="Mon May 03 2021 05:17:50")
    comment868b = Comment(videoId=462, channelId=45, content="They did nothing as the raccoon attacked the lady’s bag of food.", createdAt="Sun Feb 20 2022 17:52:55", updatedAt="Sat May 01 2021 04:15:10")
    comment869b = Comment(videoId=573, channelId=77, content="He's in a boy band which doesn't make much sense for a snake.", createdAt="Fri Jan 07 2022 11:36:20", updatedAt="Tue Dec 14 2021 06:20:02")
    comment870b = Comment(videoId=753, channelId=75, content="Hit me with your pet shark!", createdAt="Sat Jul 03 2021 08:31:31", updatedAt="Mon Feb 14 2022 04:00:32")
    comment871b = Comment(videoId=42, channelId=11, content="The tree fell unexpectedly short.", createdAt="Sat Jul 03 2021 00:00:10", updatedAt="Tue Jan 11 2022 20:14:11")
    comment872b = Comment(videoId=319, channelId=80, content="The quick brown fox jumps over the lazy dog.", createdAt="Tue Jun 15 2021 14:56:32", updatedAt="Mon Jul 12 2021 21:44:18")
    comment873b = Comment(videoId=462, channelId=9, content="Jim liked driving around town with his hazard lights on.", createdAt="Sun Jul 25 2021 03:39:28", updatedAt="Wed Sep 29 2021 17:02:33")
    comment874b = Comment(videoId=143, channelId=4, content="There was no ice cream in the freezer, nor did they have money to go to the store.", createdAt="Sun Jul 25 2021 12:17:21", updatedAt="Sat Dec 04 2021 16:32:35")
    comment875b = Comment(videoId=548, channelId=14, content="He shaved the peach to prove a point.", createdAt="Fri Aug 27 2021 08:07:14", updatedAt="Fri Sep 17 2021 14:24:08")
    comment876b = Comment(videoId=640, channelId=12, content="The bees decided to have a mutiny against their queen.", createdAt="Sat Mar 05 2022 08:47:58", updatedAt="Sun Dec 12 2021 07:31:29")
    comment877b = Comment(videoId=730, channelId=20, content="The elephant didn't want to talk about the person in the room.", createdAt="Sat Nov 27 2021 14:25:46", updatedAt="Sat Apr 02 2022 05:13:05")
    comment878b = Comment(videoId=79, channelId=69, content="Imagine his surprise when he discovered that the safe was full of pudding.", createdAt="Sun Oct 10 2021 09:35:31", updatedAt="Sat May 01 2021 06:39:07")
    comment879b = Comment(videoId=575, channelId=49, content="He was disappointed when he found the beach to be so sandy and the sun so sunny.", createdAt="Sun Feb 27 2022 06:59:36", updatedAt="Sun Sep 19 2021 10:15:50")
    comment880b = Comment(videoId=561, channelId=73, content="Dolores wouldn't have eaten the meal if she had known what it actually was.", createdAt="Sun Dec 12 2021 17:28:08", updatedAt="Fri Mar 11 2022 06:52:39")
    comment881b = Comment(videoId=47, channelId=51, content="I honestly find her about as intimidating as a basket of kittens.", createdAt="Sun Feb 20 2022 05:57:08", updatedAt="Sat Dec 18 2021 04:27:40")
    comment882b = Comment(videoId=654, channelId=22, content="He kept telling himself that one day it would all somehow make sense.", createdAt="Tue Apr 27 2021 23:48:36", updatedAt="Wed Sep 08 2021 22:02:34")
    comment883b = Comment(videoId=376, channelId=33, content="She was disgusted he couldn’t tell the difference between lemonade and limeade.", createdAt="Fri Jul 09 2021 18:39:16", updatedAt="Fri Oct 29 2021 03:19:28")
    comment884b = Comment(videoId=133, channelId=25, content="There's a message for you if you look up.", createdAt="Sat Oct 02 2021 17:46:26", updatedAt="Mon Mar 07 2022 18:03:33")
    comment885b = Comment(videoId=411, channelId=99, content="Nobody questions who built the pyramids in Mexico.", createdAt="Wed May 19 2021 06:38:20", updatedAt="Wed Jun 02 2021 12:51:36")
    comment886b = Comment(videoId=500, channelId=21, content="You're unsure whether or not to trust him, but very thankful that you wore a turtle neck.", createdAt="Tue Jun 15 2021 10:30:53", updatedAt="Sun Aug 29 2021 02:40:31")
    comment887b = Comment(videoId=748, channelId=9, content="The bird had a belief that it was really a groundhog.", createdAt="Tue Mar 29 2022 16:15:28", updatedAt="Sat Nov 06 2021 06:39:06")
    comment888b = Comment(videoId=660, channelId=4, content="I purchased a baby clown from the Russian terrorist black market.", createdAt="Fri Jul 23 2021 00:06:20", updatedAt="Sat May 15 2021 14:13:36")
    comment889b = Comment(videoId=382, channelId=57, content="It's never comforting to know that your fate depends on something as unpredictable as the popping of corn.", createdAt="Tue Jul 27 2021 04:55:46", updatedAt="Fri May 14 2021 22:16:59")
    comment890b = Comment(videoId=763, channelId=73, content="I've traveled all around Africa and still haven't found the gnu who stole my scarf.", createdAt="Fri May 14 2021 07:15:18", updatedAt="Fri Sep 03 2021 06:03:22")
    comment891b = Comment(videoId=110, channelId=61, content="25 years later, she still regretted that specific moment.", createdAt="Wed Jun 09 2021 14:50:40", updatedAt="Tue Dec 14 2021 11:24:40")
    comment892b = Comment(videoId=497, channelId=57, content="There are no heroes in a punk rock band.", createdAt="Mon Oct 25 2021 04:07:20", updatedAt="Mon May 03 2021 04:42:11")
    comment893b = Comment(videoId=504, channelId=100, content="There have been days when I wished to be separated from my body, but today wasn’t one of those days.", createdAt="Mon Jul 12 2021 09:11:29", updatedAt="Wed Jun 23 2021 00:33:51")
    comment894b = Comment(videoId=492, channelId=88, content="You'll see the rainbow bridge after it rains cats and dogs.", createdAt="Sun Nov 21 2021 20:35:43", updatedAt="Sun Sep 05 2021 13:43:58")
    comment895b = Comment(videoId=304, channelId=98, content="Today I dressed my unicorn in preparation for the race.", createdAt="Thu Dec 09 2021 23:20:41", updatedAt="Fri Dec 31 2021 17:32:11")
    comment896b = Comment(videoId=759, channelId=24, content="He created a pig burger out of beef.", createdAt="Sun Dec 26 2021 06:16:42", updatedAt="Sun Jun 20 2021 21:42:07")
    comment897b = Comment(videoId=236, channelId=86, content="The miniature pet elephant became the envy of the neighborhood.", createdAt="Fri Apr 23 2021 06:20:30", updatedAt="Mon Dec 06 2021 15:25:02")
    comment898b = Comment(videoId=192, channelId=100, content="Pat ordered a ghost pepper pie.", createdAt="Wed Oct 20 2021 17:32:45", updatedAt="Thu Oct 14 2021 02:49:02")
    comment899b = Comment(videoId=753, channelId=58, content="He was surprised that his immense laziness was inspirational to others.", createdAt="Thu Apr 29 2021 21:57:15", updatedAt="Sun Sep 05 2021 23:46:53")
    comment900b = Comment(videoId=96, channelId=62, content="The external scars tell only part of the story.", createdAt="Fri Jul 16 2021 12:21:51", updatedAt="Mon May 24 2021 08:31:39")
    comment901b = Comment(videoId=233, channelId=39, content="I covered my friend in baby oil.", createdAt="Sun Oct 31 2021 08:27:17", updatedAt="Sun Apr 18 2021 09:19:50")
    comment902b = Comment(videoId=180, channelId=71, content="All you need to do is pick up the pen and begin.", createdAt="Fri Aug 27 2021 18:03:53", updatedAt="Wed Feb 23 2022 20:48:13")
    comment903b = Comment(videoId=38, channelId=46, content="Tomorrow will bring something new, so leave today as a memory.", createdAt="Tue Oct 05 2021 17:59:32", updatedAt="Thu Jul 01 2021 14:22:27")
    comment904b = Comment(videoId=770, channelId=40, content="I may struggle with geography, but I'm sure I'm somewhere around here.", createdAt="Thu Apr 29 2021 15:58:18", updatedAt="Thu Mar 31 2022 11:36:54")
    comment905b = Comment(videoId=164, channelId=29, content="I am never at home on Sundays.", createdAt="Tue Mar 01 2022 18:26:29", updatedAt="Thu Jul 22 2021 14:40:36")
    comment906b = Comment(videoId=44, channelId=6, content="Two seats were vacant.", createdAt="Thu Dec 23 2021 10:01:30", updatedAt="Fri Jan 14 2022 17:47:34")
    comment907b = Comment(videoId=269, channelId=41, content="She advised him to come back at once.", createdAt="Mon Jul 26 2021 20:21:09", updatedAt="Thu May 20 2021 10:57:56")
    comment908b = Comment(videoId=558, channelId=12, content="He waited for the stop sign to turn to a go sign.", createdAt="Thu Apr 22 2021 23:54:19", updatedAt="Mon Aug 02 2021 14:14:02")
    comment909b = Comment(videoId=456, channelId=26, content="Today is the day I'll finally know what brick tastes like.", createdAt="Sun Aug 22 2021 23:49:52", updatedAt="Sun Aug 15 2021 07:21:06")
    comment910b = Comment(videoId=235, channelId=44, content="Various sea birds are elegant, but nothing is as elegant as a gliding pelican.", createdAt="Mon Jan 03 2022 13:30:54", updatedAt="Fri Nov 12 2021 20:17:18")
    comment911b = Comment(videoId=530, channelId=41, content="She felt that chill that makes the hairs on the back of your neck when he walked into the room.", createdAt="Wed Nov 17 2021 01:45:51", updatedAt="Fri Jul 09 2021 16:50:39")
    comment912b = Comment(videoId=298, channelId=18, content="She had that tint of craziness in her soul that made her believe she could actually make a difference.", createdAt="Sat Jun 05 2021 12:29:14", updatedAt="Sat Jan 22 2022 15:34:37")
    comment913b = Comment(videoId=335, channelId=10, content="The overpass went under the highway and into a secret world.", createdAt="Sat May 08 2021 07:36:18", updatedAt="Wed Nov 24 2021 02:20:43")
    comment914b = Comment(videoId=239, channelId=12, content="We should play with legos at camp.", createdAt="Fri Jan 14 2022 13:15:35", updatedAt="Thu Dec 09 2021 11:50:00")
    comment915b = Comment(videoId=615, channelId=13, content="The sign said there was road work ahead so he decided to speed up.", createdAt="Sat Jan 01 2022 21:47:17", updatedAt="Thu Apr 29 2021 17:08:52")
    comment916b = Comment(videoId=4, channelId=100, content="Despite what your teacher may have told you, there is a wrong way to wield a lasso.", createdAt="Mon Apr 04 2022 04:06:22", updatedAt="Mon Jan 10 2022 22:49:25")
    comment917b = Comment(videoId=59, channelId=67, content="It was always dangerous to drive with him since he insisted the safety cones were a slalom course.", createdAt="Wed Dec 15 2021 16:08:13", updatedAt="Wed May 26 2021 23:27:19")
    comment918b = Comment(videoId=537, channelId=46, content="Greetings from the real universe.", createdAt="Tue Mar 15 2022 21:16:18", updatedAt="Sat Jul 10 2021 00:55:12")
    comment919b = Comment(videoId=159, channelId=91, content="The sight of his goatee made me want to run and hide under my sister-in-law's bed.", createdAt="Sat Apr 17 2021 23:19:25", updatedAt="Sat Dec 18 2021 01:58:21")
    comment920b = Comment(videoId=499, channelId=9, content="Tuesdays are free if you bring a gnome costume.", createdAt="Sat Aug 14 2021 05:54:54", updatedAt="Fri Dec 31 2021 15:23:05")
    comment921b = Comment(videoId=90, channelId=100, content="A purple pig and a green donkey flew a kite in the middle of the night and ended up sunburnt.", createdAt="Fri Nov 19 2021 10:54:53", updatedAt="Thu Mar 10 2022 02:06:16")
    comment922b = Comment(videoId=339, channelId=85, content="I've always wanted to go to Tajikistan, but my cat would miss me.", createdAt="Tue Jan 25 2022 03:35:56", updatedAt="Sat Jul 24 2021 00:38:52")
    comment924b = Comment(videoId=110, channelId=21, content="He excelled at firing people nicely.", createdAt="Mon Sep 13 2021 05:58:32", updatedAt="Mon Oct 11 2021 19:56:10")
    comment925b = Comment(videoId=714, channelId=12, content="You bite up because of your lower jaw.", createdAt="Sun Jul 18 2021 01:48:39", updatedAt="Tue Oct 05 2021 01:36:52")
    comment926b = Comment(videoId=364, channelId=37, content="The dead trees waited to be ignited by the smallest spark and seek their revenge.", createdAt="Thu Oct 28 2021 10:57:57", updatedAt="Sun Jun 27 2021 10:38:43")
    comment927b = Comment(videoId=347, channelId=36, content="At that moment I was the most fearsome weasel in the entire swamp.", createdAt="Sun Jul 11 2021 17:56:22", updatedAt="Thu Dec 02 2021 08:15:51")
    comment928b = Comment(videoId=179, channelId=67, content="When transplanting seedlings, candied teapots will make the task easier.", createdAt="Sun Sep 19 2021 14:40:19", updatedAt="Fri Nov 05 2021 01:42:07")
    comment929b = Comment(videoId=607, channelId=69, content="There's a message for you if you look up.", createdAt="Mon Apr 12 2021 14:02:50", updatedAt="Fri Mar 25 2022 03:49:43")
    comment930b = Comment(videoId=428, channelId=16, content="She couldn't decide of the glass was half empty or half full so she drank it.", createdAt="Tue Mar 01 2022 12:05:29", updatedAt="Fri Jul 23 2021 02:11:42")
    comment931b = Comment(videoId=380, channelId=97, content="All she wanted was the answer, but she had no idea how much she would hate it.", createdAt="Sun Jul 18 2021 11:27:13", updatedAt="Sat Apr 24 2021 05:58:06")
    comment932b = Comment(videoId=347, channelId=34, content="As he dangled from the rope deep inside the crevasse", createdAt="Tue Jul 13 2021 14:04:21", updatedAt="Sun Mar 27 2022 16:41:28")
    comment933b = Comment(videoId=578, channelId=32, content="The shark-infested South Pine channel was the only way in or out.", createdAt="Sat Jul 17 2021 16:28:52", updatedAt="Thu Jan 06 2022 04:21:49")
    comment934b = Comment(videoId=696, channelId=52, content="The lyrics of the song sounded like fingernails on a chalkboard.", createdAt="Sat Oct 09 2021 05:20:57", updatedAt="Mon Mar 21 2022 08:37:42")
    comment935b = Comment(videoId=261, channelId=83, content="They desperately needed another drummer since the current one only knew how to play bongos.", createdAt="Sat Aug 07 2021 15:04:17", updatedAt="Thu Sep 09 2021 21:15:41")
    comment936b = Comment(videoId=660, channelId=89, content="Sixty-Four comes asking for bread.", createdAt="Sun Feb 13 2022 21:16:47", updatedAt="Sat Nov 20 2021 23:06:07")
    comment937b = Comment(videoId=163, channelId=12, content="She was only made the society president because she can whistle with her toes.", createdAt="Mon Jul 26 2021 18:36:29", updatedAt="Sat Nov 20 2021 16:14:31")
    comment938b = Comment(videoId=115, channelId=2, content="He knew it was going to be a bad day when he saw mountain lions roaming the streets.", createdAt="Sun Jul 11 2021 19:29:00", updatedAt="Sun May 02 2021 11:01:35")
    comment939b = Comment(videoId=494, channelId=41, content="his seven-layer cake only had six layers.", createdAt="Wed Feb 02 2022 15:16:43", updatedAt="Fri Aug 27 2021 04:43:00")
    comment940b = Comment(videoId=773, channelId=57, content="Today I bought a raincoat and wore it on a sunny day.", createdAt="Sun Jun 13 2021 14:03:59", updatedAt="Tue Feb 08 2022 20:46:17")
    comment941b = Comment(videoId=36, channelId=63, content="I made myself a peanut butter sandwich as I didn't want to subsist on veggie crackers.", createdAt="Fri Apr 23 2021 22:53:44", updatedAt="Sat Sep 25 2021 11:00:11")
    comment942b = Comment(videoId=640, channelId=42, content="Nudist colonies shun fig-leaf couture.", createdAt="Sun May 09 2021 08:29:33", updatedAt="Thu May 20 2021 09:25:54")
    comment943b = Comment(videoId=112, channelId=40, content="It was at that moment that he learned there are certain parts of the body that you should never Nair.", createdAt="Tue Jun 29 2021 15:52:34", updatedAt="Mon May 03 2021 18:44:35")
    comment944b = Comment(videoId=739, channelId=69, content="Choosing to do nothing is still a choice, after all.", createdAt="Fri Apr 16 2021 03:55:45", updatedAt="Sat Mar 19 2022 09:57:36")
    comment945b = Comment(videoId=54, channelId=49, content="Nancy was proud that she ran a tight shipwreck.", createdAt="Sat Sep 11 2021 16:29:40", updatedAt="Sat May 08 2021 19:39:30")
    comment946b = Comment(videoId=775, channelId=55, content="For the 216th time, he said he would quit drinking soda after this last Coke.", createdAt="Sat Aug 07 2021 12:42:39", updatedAt="Tue Sep 07 2021 22:41:13")
    comment947b = Comment(videoId=29, channelId=57, content="The minute she landed she understood the reason this was a fly-over state.", createdAt="Sat Sep 25 2021 12:36:05", updatedAt="Sun May 02 2021 08:50:13")
    comment948b = Comment(videoId=368, channelId=39, content="The bird had a belief that it was really a groundhog.", createdAt="Sun Sep 26 2021 20:07:59", updatedAt="Tue Jan 11 2022 14:52:12")
    comment949b = Comment(videoId=571, channelId=51, content="We have young kids who often walk into our room at night for various reasons including clowns in the closet.", createdAt="Mon Apr 04 2022 15:33:28", updatedAt="Mon Apr 26 2021 02:00:48")
    comment950b = Comment(videoId=397, channelId=2, content="Garlic ice-cream was her favorite.", createdAt="Sat Oct 16 2021 04:53:51", updatedAt="Thu May 06 2021 16:58:35")
    comment952b = Comment(videoId=543, channelId=55, content="I only enjoy window shopping when the windows are transparent.", createdAt="Sat Aug 21 2021 15:01:58", updatedAt="Sun Aug 15 2021 02:55:37")
    comment953b = Comment(videoId=673, channelId=48, content="She learned that water bottles are no longer just to hold liquid, but they're also status symbols.", createdAt="Sun Mar 20 2022 12:05:45", updatedAt="Wed Dec 15 2021 20:43:05")
    comment954b = Comment(videoId=336, channelId=66, content="The underground bunker was filled with chips and candy.", createdAt="Thu Dec 09 2021 06:28:28", updatedAt="Sun Mar 20 2022 22:00:15")
    comment955b = Comment(videoId=146, channelId=39, content="When confronted with a rotary dial phone the teenager was perplexed.", createdAt="Mon Oct 18 2021 20:44:13", updatedAt="Wed Dec 08 2021 09:18:32")
    comment956b = Comment(videoId=332, channelId=80, content="She wasn't sure whether to be impressed or concerned that he folded underwear in neat little packages.", createdAt="Wed Apr 21 2021 13:53:03", updatedAt="Fri Jul 23 2021 21:07:47")
    comment957b = Comment(videoId=204, channelId=52, content="Lucifer was surprised at the amount of life at Death Valley.", createdAt="Tue Jun 22 2021 13:17:20", updatedAt="Fri May 07 2021 12:33:02")
    comment958b = Comment(videoId=77, channelId=69, content="I checked to make sure that he was still alive.", createdAt="Thu Feb 03 2022 23:34:45", updatedAt="Sun Aug 08 2021 11:26:08")
    comment959b = Comment(videoId=338, channelId=78, content="It would have been a better night if the guys next to us weren't in the splash zone.", createdAt="Sat Feb 05 2022 05:27:10", updatedAt="Fri Apr 23 2021 10:27:02")
    comment960b = Comment(videoId=297, channelId=69, content="The tart lemonade quenched her thirst, but not her longing.", createdAt="Sun Mar 06 2022 12:16:35", updatedAt="Tue Mar 22 2022 06:32:22")
    comment961b = Comment(videoId=435, channelId=10, content="He never understood why what, when, and where left out who.", createdAt="Mon Mar 21 2022 09:31:17", updatedAt="Fri Apr 01 2022 12:33:15")
    comment962b = Comment(videoId=109, channelId=100, content="For some unfathomable reason, the response team didn't consider a lack of milk for my cereal as a proper emergency.", createdAt="Sun Jul 04 2021 08:12:57", updatedAt="Tue May 04 2021 17:26:06")
    comment963b = Comment(videoId=140, channelId=53, content="As you consider all the possible ways to improve yourself and the world, you notice John Travolta seems fairly unhappy.", createdAt="Sat Feb 05 2022 05:53:10", updatedAt="Tue Nov 02 2021 02:07:54")
    comment964b = Comment(videoId=618, channelId=51, content="I was very proud of my nickname throughout high school but today- I couldn’t be any different to what my nickname was.", createdAt="Tue Oct 12 2021 07:46:34", updatedAt="Sun Oct 10 2021 20:50:24")
    comment965b = Comment(videoId=276, channelId=14, content="You have no right to call yourself creative until you look at a trowel and think that it would make a great lockpick.", createdAt="Thu Sep 02 2021 10:22:22", updatedAt="Thu Oct 28 2021 01:08:50")
    comment966b = Comment(videoId=35, channelId=53, content="Having no hair made him look even hairier.", createdAt="Mon Oct 04 2021 07:02:29", updatedAt="Sat Feb 05 2022 20:51:06")
    comment967b = Comment(videoId=679, channelId=60, content="Sometimes you have to just give up and win by cheating.", createdAt="Tue Jul 06 2021 15:59:00", updatedAt="Mon Apr 26 2021 13:12:44")
    comment968b = Comment(videoId=206, channelId=37, content="When transplanting seedlings, candied teapots will make the task easier.", createdAt="Thu Sep 09 2021 21:10:46", updatedAt="Fri Oct 15 2021 17:59:27")
    comment969b = Comment(videoId=266, channelId=18, content="Too many prisons have become early coffins.", createdAt="Tue Apr 27 2021 22:32:37", updatedAt="Sat Jun 19 2021 08:27:00")
    comment970b = Comment(videoId=773, channelId=9, content="The waitress was not amused when he ordered green eggs and ham.", createdAt="Wed May 26 2021 03:37:40", updatedAt="Wed Oct 06 2021 04:24:31")
    comment971b = Comment(videoId=229, channelId=39, content="The fish listened intently to what the frogs had to say.", createdAt="Sun Feb 06 2022 17:56:28", updatedAt="Tue Mar 15 2022 06:02:18")
    comment972b = Comment(videoId=710, channelId=10, content="The bird had a belief that it was really a groundhog.", createdAt="Fri Feb 04 2022 12:08:01", updatedAt="Wed Jun 09 2021 13:37:51")
    comment973b = Comment(videoId=321, channelId=8, content="So long and thanks for the fish.", createdAt="Mon Apr 26 2021 17:38:12", updatedAt="Sat Jun 19 2021 15:06:24")
    comment974b = Comment(videoId=568, channelId=58, content="Iron pyrite is the most foolish of all minerals.", createdAt="Sun Dec 26 2021 11:48:16", updatedAt="Sat Feb 05 2022 14:18:51")
    comment975b = Comment(videoId=205, channelId=54, content="The heat", createdAt="Thu Oct 21 2021 14:37:08", updatedAt="Sun Mar 20 2022 03:53:47")
    comment976b = Comment(videoId=743, channelId=48, content="He turned in the research paper on Friday; otherwise, he would have not passed the class.", createdAt="Sat Jun 12 2021 19:18:13", updatedAt="Mon Apr 19 2021 21:27:02")
    comment977b = Comment(videoId=417, channelId=74, content="Potato wedges probably are not best for relationships.", createdAt="Sun Sep 05 2021 13:26:53", updatedAt="Tue Aug 17 2021 20:31:20")
    comment978b = Comment(videoId=571, channelId=82, content="He had accidentally hacked into his company's server.", createdAt="Tue Aug 17 2021 13:15:00", updatedAt="Tue Jan 04 2022 14:50:20")
    comment979b = Comment(videoId=117, channelId=54, content="We need to rent a room for our party.", createdAt="Wed Nov 03 2021 01:31:56", updatedAt="Tue Nov 30 2021 18:06:44")
    comment980b = Comment(videoId=321, channelId=36, content="There were three sphered rocks congregating in a cubed room.", createdAt="Thu Dec 23 2021 22:57:10", updatedAt="Mon Sep 13 2021 19:51:32")
    comment981b = Comment(videoId=202, channelId=60, content="The dead trees waited to be ignited by the smallest spark and seek their revenge.", createdAt="Sat May 15 2021 05:23:52", updatedAt="Sat Feb 05 2022 14:46:43")
    comment982b = Comment(videoId=750, channelId=86, content="Barking dogs and screaming toddlers have the unique ability to turn friendly neighbors into cranky enemies.", createdAt="Sat Jan 29 2022 17:45:15", updatedAt="Tue Oct 19 2021 11:32:56")
    comment983b = Comment(videoId=378, channelId=82, content="The father died during childbirth.", createdAt="Wed Sep 01 2021 03:02:27", updatedAt="Thu Aug 26 2021 11:27:22")
    comment984b = Comment(videoId=137, channelId=87, content="He found his art never progressed when he literally used his sweat and tears.", createdAt="Sun Aug 15 2021 05:18:09", updatedAt="Sat Mar 05 2022 07:28:39")
    comment985b = Comment(videoId=721, channelId=27, content="They say that dogs are man's best friend, but this cat was setting out to sabotage that theory.", createdAt="Fri Nov 19 2021 09:42:52", updatedAt="Sat Jan 29 2022 03:35:01")
    comment986b = Comment(videoId=382, channelId=12, content="Traveling became almost extinct during the pandemic.", createdAt="Thu May 06 2021 22:11:55", updatedAt="Sun Jul 25 2021 14:42:42")
    comment987b = Comment(videoId=549, channelId=71, content="Tomatoes make great weapons when water balloons aren’t available.", createdAt="Sat Oct 09 2021 00:00:33", updatedAt="Thu Jul 01 2021 04:53:47")
    comment988b = Comment(videoId=527, channelId=59, content="With the high wind warning", createdAt="Tue Mar 15 2022 04:04:10", updatedAt="Sun May 23 2021 23:45:41")
    comment989b = Comment(videoId=766, channelId=15, content="Mary realized if her calculator had a history, it would be more embarrassing than her computer browser history.", createdAt="Wed Apr 06 2022 15:05:19", updatedAt="Thu Feb 10 2022 06:29:18")
    comment990b = Comment(videoId=304, channelId=38, content="The family’s excitement over going to Disneyland was crazier than she anticipated.", createdAt="Fri May 21 2021 16:27:25", updatedAt="Tue Nov 16 2021 21:40:20")
    comment991b = Comment(videoId=357, channelId=42, content="Art doesn't have to be intentional.", createdAt="Tue Jun 22 2021 00:13:53", updatedAt="Mon Oct 04 2021 06:06:34")
    comment992b = Comment(videoId=146, channelId=57, content="The shooter says goodbye to his love.", createdAt="Sun Oct 24 2021 05:34:58", updatedAt="Sat Dec 18 2021 23:39:29")
    comment993b = Comment(videoId=260, channelId=57, content="Last Friday I saw a spotted striped blue worm shake hands with a legless lizard.", createdAt="Mon Oct 04 2021 07:51:57", updatedAt="Sat Aug 21 2021 11:58:38")
    comment994b = Comment(videoId=429, channelId=51, content="Mr. Montoya knows the way to the bakery even though he's never been there.", createdAt="Wed Dec 15 2021 05:53:35", updatedAt="Sat Mar 19 2022 09:42:52")
    comment995b = Comment(videoId=576, channelId=43, content="She had a habit of taking showers in lemonade.", createdAt="Tue Sep 21 2021 06:36:56", updatedAt="Thu Oct 28 2021 22:50:59")
    comment996b = Comment(videoId=529, channelId=91, content="Nothing is as cautiously cuddly as a pet porcupine.", createdAt="Tue May 18 2021 01:32:17", updatedAt="Thu Mar 03 2022 11:24:24")
    comment997b = Comment(videoId=239, channelId=64, content="That must be the tenth time I've been arrested for selling deep-fried cigars.", createdAt="Thu Feb 17 2022 23:53:34", updatedAt="Wed Mar 23 2022 11:13:40")
    comment998b = Comment(videoId=203, channelId=18, content="She had some amazing news to share but nobody to share it with.", createdAt="Sat Aug 28 2021 02:35:45", updatedAt="Thu Dec 30 2021 06:57:56")
    comment999b = Comment(videoId=654, channelId=37, content="Sometimes I stare at a door or a wall and I wonder what is this reality, why am I alive, and what is this all about?", createdAt="Tue Sep 21 2021 17:54:31", updatedAt="Fri Oct 08 2021 17:26:43")
    comment1000b = Comment(videoId=449, channelId=92, content="The rusty nail stood erect, angled at a 45-degree angle, just waiting for the perfect barefoot to come along.", createdAt="Sat May 15 2021 04:16:01", updatedAt="Fri Jan 07 2022 05:37:06")
    comment1001b = Comment(videoId=536, channelId=93, content="The complicated school homework left the parents trying to help their kids quite confused.", createdAt="Thu Apr 29 2021 10:16:23", updatedAt="Fri Apr 23 2021 03:31:22")
    comment1003b = Comment(videoId=429, channelId=85, content="She let the balloon float up into the air with her hopes and dreams.", createdAt="Thu Jan 27 2022 09:55:34", updatedAt="Fri Apr 30 2021 15:39:13")
    comment1004b = Comment(videoId=44, channelId=94, content="No matter how beautiful the sunset, it saddened her knowing she was one day older.", createdAt="Wed Aug 04 2021 17:12:55", updatedAt="Sat Mar 05 2022 22:54:34")
    comment1005b = Comment(videoId=629, channelId=98, content="The fish listened intently to what the frogs had to say.", createdAt="Fri Jun 11 2021 05:22:22", updatedAt="Thu Jan 27 2022 03:25:23")
    comment1006b = Comment(videoId=422, channelId=94, content="I currently have 4 windows open up… and I don’t know why.", createdAt="Sun Sep 26 2021 07:12:59", updatedAt="Tue Feb 08 2022 17:20:50")
    comment1007b = Comment(videoId=147, channelId=86, content="Nancy thought the best way to create a welcoming home was to line it with barbed wire.", createdAt="Mon Nov 01 2021 21:53:33", updatedAt="Fri Mar 04 2022 09:41:53")
    comment1008b = Comment(videoId=175, channelId=90, content="The external scars tell only part of the story.", createdAt="Thu May 06 2021 07:30:56", updatedAt="Sun Jul 25 2021 15:11:25")
    comment1009b = Comment(videoId=388, channelId=95, content="I always dreamed about being stranded on a desert island until it actually happened.", createdAt="Mon Jan 31 2022 06:39:54", updatedAt="Tue Sep 28 2021 21:23:31")
    comment1010b = Comment(videoId=28, channelId=97, content="They're playing the piano while flying in the plane.", createdAt="Fri Dec 10 2021 09:49:39", updatedAt="Wed Jul 28 2021 16:42:47")
    comment1011b = Comment(videoId=751, channelId=85, content="If you spin around three times, you'll start to feel melancholy.", createdAt="Mon Dec 20 2021 14:59:22", updatedAt="Sun Mar 20 2022 21:56:31")
    comment1012b = Comment(videoId=203, channelId=93, content="She was only made the society president because she can whistle with her toes.", createdAt="Sun Jan 23 2022 02:23:03", updatedAt="Sun Aug 22 2021 16:38:06")
    comment1013b = Comment(videoId=245, channelId=91, content="He put heat on the wound to see what would grow.", createdAt="Sun Apr 25 2021 01:12:10", updatedAt="Sun Jun 20 2021 13:54:23")
    comment1014b = Comment(videoId=571, channelId=90, content="He figured a few sticks of dynamite were easier than a fishing pole to catch fish.", createdAt="Sun Jun 20 2021 05:29:37", updatedAt="Fri Jun 25 2021 03:38:13")
    comment1015b = Comment(videoId=448, channelId=91, content="The blinking lights of the antenna tower came into focus just as I heard a loud snap.", createdAt="Fri Feb 11 2022 21:43:44", updatedAt="Mon Sep 13 2021 18:09:54")
    comment1016b = Comment(videoId=440, channelId=93, content="The elderly neighborhood became enraged over the coyotes who had been blamed for the poodle’s disappearance.", createdAt="Sun Nov 07 2021 19:53:39", updatedAt="Mon Apr 12 2021 14:49:09")
    comment1017b = Comment(videoId=594, channelId=97, content="She was amazed by the large chunks of ice washing up on the beach.", createdAt="Wed Oct 20 2021 07:54:02", updatedAt="Mon Apr 26 2021 16:25:24")
    comment1018b = Comment(videoId=11, channelId=94, content="It had been sixteen days since the zombies first attacked.", createdAt="Thu Jul 15 2021 09:24:04", updatedAt="Sun Aug 08 2021 17:17:09")
    comment1019b = Comment(videoId=282, channelId=94, content="So long and thanks for the fish.", createdAt="Wed Jan 26 2022 15:14:53", updatedAt="Sat Jun 05 2021 22:10:17")
    comment1021b = Comment(videoId=649, channelId=90, content="He liked to play with words in the bathtub.", createdAt="Mon Jul 26 2021 19:36:57", updatedAt="Sat Feb 12 2022 17:26:34")
    comment1022b = Comment(videoId=47, channelId=97, content="The blue parrot drove by the hitchhiking mongoose.", createdAt="Mon Nov 29 2021 22:41:52", updatedAt="Mon Sep 27 2021 08:51:38")
    comment1023b = Comment(videoId=530, channelId=87, content="As the rental car rolled to a stop on the dark road, her fear increased by the moment.", createdAt="Wed Sep 08 2021 21:46:11", updatedAt="Wed Apr 28 2021 15:52:37")
    comment1024b = Comment(videoId=368, channelId=95, content="Jason lived his life by the motto, \"Anything worth doing is worth doing poorly.\"", createdAt="Wed Jun 16 2021 17:16:02", updatedAt="Fri Dec 24 2021 21:40:44")
    comment1025b = Comment(videoId=501, channelId=93, content="Normal activities took extraordinary amounts of concentration at the high altitude.", createdAt="Sun Sep 19 2021 20:29:11", updatedAt="Tue Jan 25 2022 05:01:47")
    comment1026b = Comment(videoId=181, channelId=92, content="She traveled because it cost the same as therapy and was a lot more enjoyable.", createdAt="Mon Nov 29 2021 10:06:53", updatedAt="Sat Sep 18 2021 22:09:01")
    comment1027b = Comment(videoId=601, channelId=95, content="Everyone was busy, so I went to the movie alone.", createdAt="Tue Jun 15 2021 20:58:39", updatedAt="Tue Aug 24 2021 22:24:10")
    comment1028b = Comment(videoId=517, channelId=96, content="It was a really good Monday for being a Saturday.", createdAt="Sat Apr 09 2022 20:07:31", updatedAt="Thu Mar 17 2022 20:12:32")
    comment1029b = Comment(videoId=143, channelId=92, content="There should have been a time and a place, but this wasn't it.", createdAt="Thu Oct 21 2021 18:42:10", updatedAt="Tue Jun 08 2021 15:39:58")
    comment1030b = Comment(videoId=627, channelId=94, content="Be careful with that butter knife.", createdAt="Sun Aug 08 2021 05:00:46", updatedAt="Sun Jun 20 2021 15:23:30")
    comment1031b = Comment(videoId=197, channelId=86, content="Three years later, the coffin was still full of Jello.", createdAt="Tue Oct 12 2021 09:12:42", updatedAt="Tue Jun 29 2021 20:05:52")
    comment1032b = Comment(videoId=182, channelId=93, content="She had a difficult time owning up to her own crazy self.", createdAt="Fri Sep 10 2021 17:06:38", updatedAt="Thu Sep 23 2021 02:09:05")
    comment1033b = Comment(videoId=326, channelId=97, content="The tortoise jumped into the lake with dreams of becoming a sea turtle.", createdAt="Mon Apr 19 2021 23:24:46", updatedAt="Mon Sep 13 2021 01:55:46")
    comment1034b = Comment(videoId=669, channelId=91, content="He stomped on his fruit loops and thus became a cereal killer.", createdAt="Sat Apr 24 2021 16:47:47", updatedAt="Wed Sep 01 2021 20:44:11")
    comment1035b = Comment(videoId=411, channelId=94, content="Nothing is as cautiously cuddly as a pet porcupine.", createdAt="Mon Nov 22 2021 04:26:02", updatedAt="Mon Oct 04 2021 08:43:36")
    comment1036b = Comment(videoId=260, channelId=88, content="Poison ivy grew through the fence they said was impenetrable.", createdAt="Tue Nov 16 2021 18:21:07", updatedAt="Tue Apr 13 2021 04:15:10")
    comment1037b = Comment(videoId=320, channelId=95, content="We have a lot of rain in June.", createdAt="Mon Feb 14 2022 11:43:31", updatedAt="Sat May 15 2021 17:17:58")
    comment1038b = Comment(videoId=671, channelId=89, content="It didn't take long for Gary to detect the robbers were amateurs.", createdAt="Fri Jan 14 2022 09:14:34", updatedAt="Mon Feb 28 2022 17:39:52")
    comment1039b = Comment(videoId=652, channelId=96, content="A quiet house is nice until you are ordered to stay in it for months.", createdAt="Wed Feb 02 2022 07:43:29", updatedAt="Thu Apr 22 2021 22:34:36")
    comment1040b = Comment(videoId=571, channelId=92, content="Situps are a terrible way to end your day.", createdAt="Mon Dec 13 2021 17:32:54", updatedAt="Sat Dec 04 2021 13:13:19")
    comment1041b = Comment(videoId=585, channelId=90, content="There's no reason a hula hoop can't also be a circus ring.", createdAt="Sun Feb 06 2022 11:12:07", updatedAt="Wed Oct 20 2021 16:33:15")
    comment1042b = Comment(videoId=616, channelId=94, content="The overpass went under the highway and into a secret world.", createdAt="Mon Jul 12 2021 09:57:32", updatedAt="Fri Jul 02 2021 08:34:05")
    comment1043b = Comment(videoId=591, channelId=94, content="Chocolate covered crickets were his favorite snack.", createdAt="Sun Mar 27 2022 06:45:15", updatedAt="Thu Sep 02 2021 14:24:51")
    comment1044b = Comment(videoId=576, channelId=96, content="The Tsunami wave crashed against the raised houses and broke the pilings as if they were toothpicks.", createdAt="Wed Nov 10 2021 01:48:06", updatedAt="Tue May 11 2021 17:53:51")
    comment1045b = Comment(videoId=585, channelId=91, content="Tom got a small piece of pie.", createdAt="Wed Jan 05 2022 11:44:34", updatedAt="Fri Apr 01 2022 12:12:26")
    comment1046b = Comment(videoId=215, channelId=90, content="They wandered into a strange Tiki bar on the edge of the small beach town.", createdAt="Mon Nov 08 2021 03:46:10", updatedAt="Thu Mar 17 2022 02:04:54")
    comment1047b = Comment(videoId=98, channelId=89, content="She was sad to hear that fireflies are facing extinction due to artificial light, habitat loss, and pesticides.", createdAt="Thu Nov 04 2021 13:20:49", updatedAt="Fri May 21 2021 21:07:29")
    comment1048b = Comment(videoId=593, channelId=90, content="The tattered work gloves speak of the many hours of hard labor he endured throughout his life.", createdAt="Fri Feb 25 2022 11:30:48", updatedAt="Wed Oct 20 2021 12:13:24")
    comment1049b = Comment(videoId=195, channelId=87, content="People who insist on picking their teeth with their elbows are so annoying!", createdAt="Sat Mar 19 2022 11:52:13", updatedAt="Thu Dec 02 2021 08:40:24")
    comment1050b = Comment(videoId=535, channelId=91, content="He was an introvert that extroverts seemed to love.", createdAt="Tue May 04 2021 01:53:30", updatedAt="Thu Jan 20 2022 21:18:10")
    comment1051b = Comment(videoId=417, channelId=90, content="The lake is a long way from here.", createdAt="Tue Apr 05 2022 07:54:13", updatedAt="Fri Apr 16 2021 06:34:48")
    comment1052b = Comment(videoId=435, channelId=87, content="Swim at your own risk was taken as a challenge for the group of Kansas City college students.", createdAt="Sun Sep 05 2021 04:09:39", updatedAt="Tue Nov 09 2021 05:29:13")
    comment1054b = Comment(videoId=74, channelId=97, content="She had that tint of craziness in her soul that made her believe she could actually make a difference.", createdAt="Sat Jun 05 2021 07:25:01", updatedAt="Sun Jul 25 2021 14:36:06")
    comment1056b = Comment(videoId=264, channelId=86, content="Separation anxiety is what happens when you can't find your phone.", createdAt="Wed Jul 28 2021 18:46:15", updatedAt="Mon Feb 07 2022 11:45:16")
    comment1057b = Comment(videoId=604, channelId=91, content="I love bacon, beer, birds, and baboons.", createdAt="Sun Mar 20 2022 02:37:54", updatedAt="Fri Nov 12 2021 21:15:48")
    comment1058b = Comment(videoId=319, channelId=88, content="The Guinea fowl flies through the air with all the grace of a turtle.", createdAt="Fri Sep 10 2021 01:33:08", updatedAt="Sat Dec 18 2021 15:14:31")
    comment1059b = Comment(videoId=570, channelId=96, content="There's no reason a hula hoop can't also be a circus ring.", createdAt="Mon Sep 06 2021 14:12:16", updatedAt="Mon Jan 10 2022 11:01:28")
    comment1060b = Comment(videoId=554, channelId=95, content="The worst thing about being at the top of the career ladder is that there's a long way to fall.", createdAt="Fri Nov 19 2021 02:47:46", updatedAt="Wed Jun 16 2021 06:15:43")
    comment1061b = Comment(videoId=776, channelId=98, content="I am counting my calories, yet I really want dessert.", createdAt="Mon Oct 11 2021 08:43:47", updatedAt="Tue Aug 31 2021 02:08:15")
    comment1062b = Comment(videoId=502, channelId=97, content="All she wanted was the answer, but she had no idea how much she would hate it.", createdAt="Wed Oct 27 2021 08:56:27", updatedAt="Thu Sep 30 2021 23:29:02")
    comment1063b = Comment(videoId=436, channelId=88, content="There are over 500 starfish in the bathroom drawer.", createdAt="Wed Sep 22 2021 15:38:34", updatedAt="Fri Aug 06 2021 14:37:30")
    comment1064b = Comment(videoId=116, channelId=95, content="Charles ate the french fries knowing they would be his last meal.", createdAt="Mon Jul 05 2021 07:51:45", updatedAt="Fri Mar 25 2022 14:09:07")
    comment1065b = Comment(videoId=441, channelId=98, content="His mind was blown that there was nothing in space except space itself.", createdAt="Mon Aug 09 2021 15:42:17", updatedAt="Thu Jun 24 2021 22:01:52")
    comment1066b = Comment(videoId=462, channelId=94, content="The lake is a long way from here.", createdAt="Mon Jul 12 2021 09:15:08", updatedAt="Sun Nov 28 2021 01:18:38")
    comment1067b = Comment(videoId=565, channelId=93, content="She could hear him in the shower singing with a joy she hoped he'd retain after she delivered the news.", createdAt="Mon Jan 10 2022 08:29:01", updatedAt="Wed Dec 22 2021 22:23:24")
    comment1068b = Comment(videoId=256, channelId=93, content="It caught him off guard that space smelled of seared steak.", createdAt="Thu Jul 08 2021 09:34:05", updatedAt="Fri Dec 31 2021 18:26:13")
    comment1069b = Comment(videoId=22, channelId=87, content="You bite up because of your lower jaw.", createdAt="Wed Apr 14 2021 20:36:00", updatedAt="Wed Mar 30 2022 02:23:13")
    comment1070b = Comment(videoId=129, channelId=85, content="The heat", createdAt="Sat Jul 10 2021 00:16:22", updatedAt="Tue Apr 20 2021 19:47:51")
    comment1071b = Comment(videoId=78, channelId=94, content="This book is sure to liquefy your brain.", createdAt="Sat Dec 11 2021 09:16:46", updatedAt="Mon Dec 06 2021 04:24:55")
    comment1072b = Comment(videoId=233, channelId=92, content="She borrowed the book from him many years ago and hasn't yet returned it.", createdAt="Fri Nov 19 2021 09:33:50", updatedAt="Sun Sep 26 2021 18:45:10")
    comment1073b = Comment(videoId=733, channelId=95, content="There have been days when I wished to be separated from my body, but today wasn’t one of those days.", createdAt="Tue Jun 08 2021 06:04:44", updatedAt="Wed Aug 18 2021 00:26:38")
    comment1074b = Comment(videoId=525, channelId=87, content="Improve your goldfish's physical fitness by getting him a bicycle.", createdAt="Fri Jan 28 2022 19:30:43", updatedAt="Sun May 30 2021 11:56:42")
    comment1075b = Comment(videoId=165, channelId=85, content="Shingle color was not something the couple had ever talked about.", createdAt="Fri Mar 25 2022 04:48:56", updatedAt="Sun Oct 17 2021 16:49:24")
    comment1076b = Comment(videoId=541, channelId=89, content="When transplanting seedlings, candied teapots will make the task easier.", createdAt="Tue May 04 2021 07:37:00", updatedAt="Wed Jun 16 2021 09:57:51")
    comment1077b = Comment(videoId=601, channelId=98, content="8% of 25 is the same as 25% of 8 and one of them is much easier to do in your head.", createdAt="Sat Nov 13 2021 20:54:40", updatedAt="Mon May 24 2021 22:38:35")
    comment1078b = Comment(videoId=184, channelId=96, content="Today I dressed my unicorn in preparation for the race.", createdAt="Sat Oct 02 2021 11:35:09", updatedAt="Wed Aug 25 2021 18:17:47")
    comment1079b = Comment(videoId=329, channelId=88, content="His confidence would have bee admirable if it wasn't for his stupidity.", createdAt="Mon Aug 09 2021 01:28:09", updatedAt="Mon Nov 29 2021 08:55:16")
    comment1080b = Comment(videoId=54, channelId=95, content="I want more detailed information.", createdAt="Sun Jul 04 2021 01:31:47", updatedAt="Sun Feb 06 2022 11:04:52")
    comment1081b = Comment(videoId=85, channelId=89, content="Flying fish flew by the space station.", createdAt="Mon Oct 04 2021 19:30:18", updatedAt="Tue Mar 08 2022 00:41:12")
    comment1082b = Comment(videoId=575, channelId=88, content="Andy loved to sleep on a bed of nails.", createdAt="Wed Jan 12 2022 08:23:06", updatedAt="Mon Nov 08 2021 09:16:09")
    comment1083b = Comment(videoId=128, channelId=95, content="The bird had a belief that it was really a groundhog.", createdAt="Tue Dec 07 2021 07:03:38", updatedAt="Fri Jun 25 2021 05:36:50")
    comment1084b = Comment(videoId=48, channelId=86, content="It's not often you find a soggy banana on the street.", createdAt="Mon Dec 27 2021 18:09:29", updatedAt="Sun Feb 06 2022 06:14:03")
    comment1085b = Comment(videoId=21, channelId=92, content="This is a Japanese doll.", createdAt="Thu Dec 16 2021 09:17:45", updatedAt="Sun Jul 11 2021 13:49:29")
    comment1086b = Comment(videoId=384, channelId=96, content="Homesickness became contagious in the young campers' cabin.", createdAt="Thu May 06 2021 16:27:25", updatedAt="Fri May 28 2021 05:25:20")
    comment1087b = Comment(videoId=44, channelId=92, content="Although it wasn't a pot of gold, Nancy was still enthralled at what she found at the end of the rainbow.", createdAt="Fri May 14 2021 11:32:24", updatedAt="Wed Dec 08 2021 15:36:27")
    comment1088b = Comment(videoId=466, channelId=89, content="He used to get confused between soldiers and shoulders, but as a military man, he now soldiers responsibility.", createdAt="Sun Aug 01 2021 11:35:05", updatedAt="Wed Jul 21 2021 21:20:23")
    comment1089b = Comment(videoId=169, channelId=86, content="Some bathing suits just shouldn’t be worn by some people.", createdAt="Sun May 23 2021 08:04:02", updatedAt="Thu Jul 15 2021 17:24:37")
    comment1090b = Comment(videoId=624, channelId=87, content="We have young kids who often walk into our room at night for various reasons including clowns in the closet.", createdAt="Fri May 14 2021 15:38:10", updatedAt="Thu Feb 24 2022 01:47:03")
    comment1091b = Comment(videoId=243, channelId=92, content="Happiness can be found in the depths of chocolate pudding.", createdAt="Tue Mar 22 2022 22:52:00", updatedAt="Thu Sep 09 2021 04:03:52")
    comment1092b = Comment(videoId=360, channelId=92, content="She was too short to see over the fence.", createdAt="Mon Feb 07 2022 00:37:13", updatedAt="Sun Jul 11 2021 05:30:35")
    comment1093b = Comment(videoId=657, channelId=97, content="Mr. Montoya knows the way to the bakery even though he's never been there.", createdAt="Sun Jun 20 2021 19:16:47", updatedAt="Sun Sep 26 2021 12:24:52")
    comment1094b = Comment(videoId=61, channelId=97, content="With a single flip of the coin, his life changed forever.", createdAt="Thu Jun 24 2021 14:28:58", updatedAt="Fri Dec 31 2021 11:25:10")
    comment1095b = Comment(videoId=287, channelId=93, content="Situps are a terrible way to end your day.", createdAt="Tue Feb 01 2022 05:20:58", updatedAt="Wed Sep 15 2021 12:31:18")
    comment1096b = Comment(videoId=295, channelId=90, content="She hadn't had her cup of coffee, and that made things all the worse.", createdAt="Fri Aug 27 2021 14:16:47", updatedAt="Mon Nov 22 2021 01:16:37")
    comment1097b = Comment(videoId=201, channelId=85, content="They finished building the road they knew no one would ever use.", createdAt="Mon Mar 21 2022 17:32:58", updatedAt="Sat Nov 20 2021 05:26:19")
    comment1098b = Comment(videoId=336, channelId=88, content="It's never been my responsibility to glaze the donuts.", createdAt="Sat Aug 07 2021 20:27:33", updatedAt="Fri Sep 03 2021 05:53:13")
    comment1099b = Comment(videoId=245, channelId=86, content="Malls are great places to shop; I can find everything I need under one roof.", createdAt="Thu Mar 03 2022 21:11:06", updatedAt="Tue Aug 03 2021 06:02:36")
    comment1100b = Comment(videoId=180, channelId=91, content="He wondered if it could be called a beach if there was no sand.", createdAt="Tue Dec 21 2021 23:21:45", updatedAt="Sat Jan 08 2022 16:50:28")
    comment1101b = Comment(videoId=432, channelId=86, content="There is no better feeling than staring at a wall with closed eyes.", createdAt="Sat Jul 24 2021 13:27:52", updatedAt="Thu Nov 25 2021 20:21:58")
    comment1102b = Comment(videoId=272, channelId=90, content="The shark-infested South Pine channel was the only way in or out.", createdAt="Wed Nov 03 2021 02:26:24", updatedAt="Sun May 09 2021 02:40:16")
    comment1103b = Comment(videoId=383, channelId=95, content="Peter found road kill an excellent way to save money on dinner.", createdAt="Tue Nov 09 2021 02:03:01", updatedAt="Wed Jun 30 2021 08:59:39")
    comment1104b = Comment(videoId=765, channelId=88, content="Gary didn't understand why Doug went upstairs to get one dollar bills when he invited him to go cow tipping.", createdAt="Wed Aug 04 2021 18:54:26", updatedAt="Sat Oct 23 2021 22:52:11")
    comment1105b = Comment(videoId=134, channelId=90, content="I just wanted to tell you I could see the love you have for your child by the way you look at her.", createdAt="Sat Apr 17 2021 12:59:23", updatedAt="Wed Nov 10 2021 12:43:24")
    comment1106b = Comment(videoId=449, channelId=97, content="The stench from the feedlot permeated the car despite having the air conditioning on recycled air.", createdAt="Fri Nov 19 2021 13:51:30", updatedAt="Sun Jun 13 2021 11:10:27")
    comment1107b = Comment(videoId=106, channelId=95, content="Going from child, to childish, to childlike is only a matter of time.", createdAt="Mon Jan 17 2022 21:42:26", updatedAt="Wed Dec 22 2021 18:17:52")
    comment1108b = Comment(videoId=572, channelId=91, content="his seven-layer cake only had six layers.", createdAt="Sun Jul 18 2021 18:18:17", updatedAt="Fri Aug 06 2021 16:32:52")
    comment1109b = Comment(videoId=421, channelId=93, content="He was willing to find the depths of the rabbit hole in order to be with her.", createdAt="Tue Mar 22 2022 15:17:44", updatedAt="Thu Sep 02 2021 14:54:31")
    comment1110b = Comment(videoId=557, channelId=89, content="I like to leave work after my eight-hour tea-break.", createdAt="Mon Mar 21 2022 19:33:03", updatedAt="Wed Sep 15 2021 12:39:36")
    comment1111b = Comment(videoId=56, channelId=87, content="It took me too long to realize that the ceiling hadn't been painted to look like the sky.", createdAt="Tue Jan 11 2022 07:44:42", updatedAt="Sun Nov 14 2021 02:57:33")
    comment1112b = Comment(videoId=573, channelId=88, content="There have been days when I wished to be separated from my body, but today wasn’t one of those days.", createdAt="Tue Oct 19 2021 12:11:05", updatedAt="Sun Apr 25 2021 03:32:25")
    comment1113b = Comment(videoId=229, channelId=95, content="If eating three-egg omelets causes weight-gain, budgie eggs are a good substitute.", createdAt="Wed Mar 02 2022 06:18:50", updatedAt="Wed Aug 18 2021 15:06:20")
    comment1114b = Comment(videoId=164, channelId=87, content="Choosing to do nothing is still a choice, after all.", createdAt="Sat Jan 29 2022 06:17:18", updatedAt="Fri Feb 04 2022 00:28:54")
    comment1115b = Comment(videoId=772, channelId=93, content="He wondered if it could be called a beach if there was no sand.", createdAt="Sun Nov 28 2021 23:21:43", updatedAt="Sun Apr 25 2021 11:34:17")
    comment1116b = Comment(videoId=483, channelId=86, content="Her scream silenced the rowdy teenagers.", createdAt="Sun Apr 11 2021 11:04:21", updatedAt="Sat Jul 17 2021 13:02:58")
    comment1117b = Comment(videoId=149, channelId=87, content="For the 216th time, he said he would quit drinking soda after this last Coke.", createdAt="Sun Jul 25 2021 21:11:03", updatedAt="Fri Apr 30 2021 09:24:30")
    comment1118b = Comment(videoId=214, channelId=87, content="There was no telling what thoughts would come from the machine.", createdAt="Tue Sep 14 2021 03:41:26", updatedAt="Thu Sep 09 2021 10:29:26")
    comment1119b = Comment(videoId=742, channelId=97, content="In the end, he realized he could see sound and hear words.", createdAt="Sun Feb 13 2022 20:52:02", updatedAt="Thu Jan 06 2022 23:36:03")
    comment1120b = Comment(videoId=80, channelId=89, content="He had a vague sense that trees gave birth to dinosaurs.", createdAt="Sat Jan 29 2022 09:41:24", updatedAt="Tue Nov 30 2021 03:15:52")
    comment1121b = Comment(videoId=320, channelId=89, content="Buried deep in the snow, he hoped his batteries were fresh in his avalanche beacon.", createdAt="Sun Feb 13 2022 02:01:01", updatedAt="Wed Dec 29 2021 11:33:53")
    comment1122b = Comment(videoId=95, channelId=85, content="You should never take advice from someone who thinks red paint dries quicker than blue paint.", createdAt="Fri Aug 13 2021 04:51:51", updatedAt="Thu Aug 26 2021 10:18:03")
    comment1123b = Comment(videoId=666, channelId=96, content="It had been sixteen days since the zombies first attacked.", createdAt="Mon Oct 18 2021 11:41:43", updatedAt="Tue Jan 04 2022 07:04:55")
    comment1124b = Comment(videoId=728, channelId=87, content="She felt that chill that makes the hairs on the back of your neck when he walked into the room.", createdAt="Thu Jan 20 2022 14:00:18", updatedAt="Mon Nov 01 2021 16:00:50")
    comment1125b = Comment(videoId=619, channelId=97, content="He had concluded that pigs must be able to fly in Hog Heaven.", createdAt="Sun Dec 12 2021 02:32:24", updatedAt="Fri Jan 28 2022 21:17:04")
    comment1126b = Comment(videoId=29, channelId=87, content="He liked to play with words in the bathtub.", createdAt="Mon Jun 28 2021 14:47:08", updatedAt="Thu Mar 03 2022 16:13:41")
    comment1127b = Comment(videoId=92, channelId=88, content="I come from a tribe of head-hunters, so I will never need a shrink.", createdAt="Sun Mar 06 2022 05:45:02", updatedAt="Sat Sep 04 2021 20:38:20")
    comment1128b = Comment(videoId=535, channelId=97, content="I was fishing for compliments and accidentally caught a trout.", createdAt="Tue Feb 22 2022 05:08:58", updatedAt="Wed Dec 08 2021 03:19:46")
    comment1129b = Comment(videoId=54, channelId=93, content="I covered my friend in baby oil.", createdAt="Sat Jan 08 2022 12:46:31", updatedAt="Mon Jan 10 2022 13:49:23")
    comment1130b = Comment(videoId=420, channelId=97, content="His get rich quick scheme was to grow a cactus farm.", createdAt="Sat Jun 19 2021 03:51:56", updatedAt="Mon Nov 15 2021 20:55:33")
    comment1131b = Comment(videoId=44, channelId=92, content="For some unfathomable reason, the response team didn't consider a lack of milk for my cereal as a proper emergency.", createdAt="Thu Apr 07 2022 22:33:35", updatedAt="Tue Nov 02 2021 12:31:03")
    comment1132b = Comment(videoId=108, channelId=96, content="The sun had set and so had his dreams.", createdAt="Sat Apr 24 2021 05:08:53", updatedAt="Sat Nov 06 2021 06:51:19")
    comment1133b = Comment(videoId=720, channelId=91, content="The worst thing about being at the top of the career ladder is that there's a long way to fall.", createdAt="Thu Sep 23 2021 20:05:41", updatedAt="Tue Dec 21 2021 16:44:01")
    comment1134b = Comment(videoId=233, channelId=94, content="As he looked out the window, he saw a clown walk by.", createdAt="Sun Apr 11 2021 07:05:30", updatedAt="Mon Apr 26 2021 22:25:15")
    comment1135b = Comment(videoId=2, channelId=96, content="Nobody questions who built the pyramids in Mexico.", createdAt="Wed Mar 09 2022 22:11:04", updatedAt="Tue Sep 07 2021 12:26:14")
    comment1136b = Comment(videoId=113, channelId=91, content="I trust everything that's written in purple ink.", createdAt="Sun Jan 09 2022 21:48:46", updatedAt="Wed Feb 23 2022 22:08:34")
    comment1137b = Comment(videoId=743, channelId=95, content="The fact that there's a stairway to heaven and a highway to hell explains life well.", createdAt="Sat Jan 29 2022 16:34:51", updatedAt="Wed Nov 24 2021 08:34:52")
    comment1138b = Comment(videoId=101, channelId=97, content="Her hair was windswept as she rode in the black convertible.", createdAt="Mon May 03 2021 08:00:44", updatedAt="Fri Dec 24 2021 09:42:48")
    comment1139b = Comment(videoId=22, channelId=87, content="He had a hidden stash underneath the floorboards in the back room of the house.", createdAt="Fri Jan 28 2022 11:30:28", updatedAt="Tue Jun 01 2021 11:00:32")
    comment1140b = Comment(videoId=436, channelId=93, content="I've traveled all around Africa and still haven't found the gnu who stole my scarf.", createdAt="Wed Nov 10 2021 00:37:11", updatedAt="Tue Jul 13 2021 06:27:37")
    comment1141b = Comment(videoId=690, channelId=91, content="That was how he came to win $1 million.", createdAt="Sun Jul 04 2021 01:30:07", updatedAt="Wed Mar 16 2022 14:11:20")
    comment1142b = Comment(videoId=492, channelId=85, content="They called out her name time and again, but were met with nothing but silence.", createdAt="Sun May 16 2021 20:14:14", updatedAt="Sun Sep 26 2021 14:50:03")
    comment1143b = Comment(videoId=486, channelId=98, content="Her daily goal was to improve on yesterday.", createdAt="Wed Oct 20 2021 23:59:12", updatedAt="Thu Apr 07 2022 04:04:18")
    comment1144b = Comment(videoId=155, channelId=86, content="The teenage boy was accused of breaking his arm simply to get out of the test.", createdAt="Sat Jun 19 2021 19:18:03", updatedAt="Thu Nov 25 2021 05:39:09")
    comment1145b = Comment(videoId=560, channelId=92, content="Baby wipes are made of chocolate stardust.", createdAt="Fri Oct 01 2021 20:54:54", updatedAt="Tue May 04 2021 19:35:11")
    comment1146b = Comment(videoId=774, channelId=88, content="Trash covered the landscape like sprinkles do a birthday cake.", createdAt="Thu Feb 17 2022 04:09:59", updatedAt="Wed Nov 10 2021 00:26:22")
    comment1147b = Comment(videoId=735, channelId=89, content="Three years later, the coffin was still full of Jello.", createdAt="Thu Mar 31 2022 02:40:26", updatedAt="Sun Nov 07 2021 13:22:36")
    comment1148b = Comment(videoId=9, channelId=88, content="I would be delighted if the sea were full of cucumber juice.", createdAt="Wed Nov 17 2021 22:48:58", updatedAt="Sun Dec 05 2021 00:48:15")
    comment1149b = Comment(videoId=37, channelId=93, content="The elephant didn't want to talk about the person in the room.", createdAt="Thu Mar 17 2022 02:47:48", updatedAt="Sun Oct 31 2021 14:01:14")
    comment1150b = Comment(videoId=737, channelId=88, content="She lived on Monkey Jungle Road and that seemed to explain all of her strangeness.", createdAt="Thu Jul 15 2021 12:11:38", updatedAt="Sat Apr 24 2021 00:24:18")
    comment1151b = Comment(videoId=642, channelId=96, content="I made myself a peanut butter sandwich as I didn't want to subsist on veggie crackers.", createdAt="Sun Jun 06 2021 21:30:16", updatedAt="Mon Aug 02 2021 15:05:11")
    comment1152b = Comment(videoId=329, channelId=98, content="The heat", createdAt="Tue Jul 20 2021 05:52:42", updatedAt="Sun Oct 31 2021 18:46:50")
    comment1153b = Comment(videoId=703, channelId=93, content="Normal activities took extraordinary amounts of concentration at the high altitude.", createdAt="Sun Apr 11 2021 11:30:01", updatedAt="Wed Feb 23 2022 12:51:08")
    comment1155b = Comment(videoId=43, channelId=91, content="There's no reason a hula hoop can't also be a circus ring.", createdAt="Sun Jun 13 2021 12:25:07", updatedAt="Sun Apr 11 2021 21:57:24")
    comment1156b = Comment(videoId=723, channelId=85, content="I like to leave work after my eight-hour tea-break.", createdAt="Wed May 12 2021 18:38:33", updatedAt="Thu Dec 09 2021 05:00:02")
    comment1157b = Comment(videoId=576, channelId=88, content="I've always wanted to go to Tajikistan, but my cat would miss me.", createdAt="Sat Nov 13 2021 13:07:33", updatedAt="Sun Apr 11 2021 15:56:34")
    comment1158b = Comment(videoId=440, channelId=90, content="The irony of the situation wasn't lost on anyone in the room.", createdAt="Wed Mar 09 2022 10:47:25", updatedAt="Wed Dec 01 2021 09:41:44")
    comment1159b = Comment(videoId=351, channelId=94, content="I currently have 4 windows open up… and I don’t know why.", createdAt="Thu Dec 09 2021 21:33:24", updatedAt="Sun May 02 2021 14:20:09")
    comment1160b = Comment(videoId=779, channelId=95, content="Mary realized if her calculator had a history, it would be more embarrassing than her computer browser history.", createdAt="Sat Jul 24 2021 10:45:15", updatedAt="Fri Nov 05 2021 16:49:06")
    comment1161b = Comment(videoId=82, channelId=88, content="Sometimes, all you need to do is completely make an ass of yourself and laugh it off to realise that life isn’t so bad after all.", createdAt="Mon Nov 15 2021 05:19:36", updatedAt="Fri Apr 16 2021 18:44:34")
    comment1162b = Comment(videoId=231, channelId=91, content="The tattered work gloves speak of the many hours of hard labor he endured throughout his life.", createdAt="Sat May 01 2021 16:25:07", updatedAt="Mon Nov 15 2021 10:05:55")
    comment1163b = Comment(videoId=426, channelId=90, content="It dawned on her that others could make her happier, but only she could make herself happy.", createdAt="Fri Oct 01 2021 05:52:12", updatedAt="Fri Dec 03 2021 15:17:30")
    comment1164b = Comment(videoId=680, channelId=94, content="He was surprised that his immense laziness was inspirational to others.", createdAt="Mon Feb 14 2022 05:29:55", updatedAt="Tue Apr 27 2021 20:26:43")
    comment1165b = Comment(videoId=388, channelId=86, content="The tortoise jumped into the lake with dreams of becoming a sea turtle.", createdAt="Tue Aug 10 2021 21:37:01", updatedAt="Thu Jan 13 2022 22:10:37")
    comment1166b = Comment(videoId=752, channelId=95, content="The complicated school homework left the parents trying to help their kids quite confused.", createdAt="Fri May 28 2021 14:29:09", updatedAt="Thu Dec 02 2021 16:00:29")
    comment1167b = Comment(videoId=162, channelId=87, content="If you spin around three times, you'll start to feel melancholy.", createdAt="Sat Sep 11 2021 16:13:57", updatedAt="Wed Jul 28 2021 01:36:07")
    comment1168b = Comment(videoId=260, channelId=92, content="Erin accidentally created a new universe.", createdAt="Fri May 14 2021 22:45:23", updatedAt="Thu Jul 29 2021 13:25:46")
    comment1169b = Comment(videoId=263, channelId=88, content="Sometimes you have to just give up and win by cheating.", createdAt="Thu Oct 21 2021 01:36:35", updatedAt="Thu Oct 14 2021 09:51:33")
    comment1170b = Comment(videoId=168, channelId=91, content="The clock within this blog and the clock on my laptop are 1 hour different from each other.", createdAt="Sat May 01 2021 09:28:04", updatedAt="Sat Aug 21 2021 19:59:27")
    comment1171b = Comment(videoId=13, channelId=94, content="It's not often you find a soggy banana on the street.", createdAt="Sat Aug 21 2021 01:58:05", updatedAt="Thu Mar 24 2022 21:09:29")
    comment1172b = Comment(videoId=298, channelId=97, content="I received a heavy fine but it failed to crush my spirit.", createdAt="Fri May 07 2021 13:19:20", updatedAt="Fri Jun 11 2021 04:41:47")
    comment1173b = Comment(videoId=308, channelId=87, content="Toddlers feeding raccoons surprised even the seasoned park ranger.", createdAt="Mon Nov 08 2021 13:09:23", updatedAt="Fri Mar 11 2022 14:12:56")
    comment1174b = Comment(videoId=179, channelId=88, content="I can't believe this is the eighth time I'm smashing open my piggy bank on the same day!", createdAt="Fri Jun 04 2021 01:25:52", updatedAt="Tue Nov 09 2021 09:40:44")
    comment1175b = Comment(videoId=107, channelId=85, content="He put heat on the wound to see what would grow.", createdAt="Wed Jun 16 2021 20:20:59", updatedAt="Fri Nov 26 2021 10:51:09")
    comment1176b = Comment(videoId=15, channelId=86, content="100 years old is such a young age if you happen to be a bristlecone pine.", createdAt="Sun Mar 06 2022 01:19:13", updatedAt="Thu Jun 10 2021 00:32:16")
    comment1177b = Comment(videoId=439, channelId=93, content="The efficiency we have at removing trash has made creating trash more acceptable.", createdAt="Mon Jul 19 2021 16:52:51", updatedAt="Tue Feb 15 2022 06:28:38")
    comment1178b = Comment(videoId=157, channelId=95, content="He waited for the stop sign to turn to a go sign.", createdAt="Mon Jun 28 2021 05:24:19", updatedAt="Mon Sep 13 2021 18:22:38")
    comment1179b = Comment(videoId=439, channelId=89, content="He didn't heed the warning and it had turned out surprisingly well.", createdAt="Fri Feb 25 2022 08:10:22", updatedAt="Fri May 14 2021 05:19:29")
    comment1180b = Comment(videoId=574, channelId=85, content="They say people remember important moments in their life well, yet no one even remembers their own birth.", createdAt="Wed Jun 02 2021 07:50:09", updatedAt="Thu Jul 22 2021 04:51:10")
    comment1181b = Comment(videoId=75, channelId=87, content="For the 216th time, he said he would quit drinking soda after this last Coke.", createdAt="Sun Aug 15 2021 15:34:29", updatedAt="Fri Aug 27 2021 06:39:32")
    comment1182b = Comment(videoId=763, channelId=92, content="When he asked her favorite number, she answered without hesitation that it was diamonds.", createdAt="Mon Aug 16 2021 15:51:05", updatedAt="Thu Apr 22 2021 14:39:21")
    comment1183b = Comment(videoId=535, channelId=95, content="The family’s excitement over going to Disneyland was crazier than she anticipated.", createdAt="Wed Sep 22 2021 00:04:29", updatedAt="Fri Dec 31 2021 03:40:02")
    comment1184b = Comment(videoId=352, channelId=92, content="It was the scarcity that fueled his creativity.", createdAt="Sun Aug 29 2021 02:45:46", updatedAt="Sat Apr 09 2022 01:12:28")
    comment1185b = Comment(videoId=354, channelId=89, content="Before he moved to the inner city, he had always believed that security complexes were psychological.", createdAt="Wed Dec 22 2021 23:39:34", updatedAt="Wed Nov 24 2021 07:16:17")
    comment1186b = Comment(videoId=289, channelId=86, content="If any cop asks you where you were, just say you were visiting Kansas.", createdAt="Tue Feb 15 2022 16:26:05", updatedAt="Sun May 09 2021 03:13:33")
    comment1187b = Comment(videoId=645, channelId=92, content="The sky is clear; the stars are twinkling.", createdAt="Sat Jun 19 2021 04:40:23", updatedAt="Wed Dec 15 2021 21:38:29")
    comment1188b = Comment(videoId=2, channelId=92, content="It was obvious she was hot, sweaty, and tired.", createdAt="Mon Aug 02 2021 15:02:26", updatedAt="Sat Aug 07 2021 19:00:53")
    comment1189b = Comment(videoId=237, channelId=86, content="The busker hoped that the people passing by would throw money, but they threw tomatoes instead, so he exchanged his hat for a juicer.", createdAt="Thu May 20 2021 12:03:58", updatedAt="Wed Jun 09 2021 15:14:05")
    comment1190b = Comment(videoId=57, channelId=94, content="It's important to remember to be aware of rampaging grizzly bears.", createdAt="Mon Dec 27 2021 04:32:44", updatedAt="Sat Apr 17 2021 01:22:44")
    comment1191b = Comment(videoId=382, channelId=88, content="Cursive writing is the best way to build a race track.", createdAt="Thu Aug 26 2021 01:01:47", updatedAt="Mon May 24 2021 02:50:04")
    comment1192b = Comment(videoId=578, channelId=97, content="I cheated while playing the darts tournament by using a longbow.", createdAt="Mon Sep 27 2021 09:26:18", updatedAt="Fri Jun 25 2021 00:48:39")
    comment1193b = Comment(videoId=27, channelId=86, content="She moved forward only because she trusted that the ending she now was going through must be followed by a new beginning.", createdAt="Sun Sep 05 2021 00:13:34", updatedAt="Wed Nov 10 2021 07:19:45")
    comment1194b = Comment(videoId=389, channelId=87, content="He appeared to be confusingly perplexed.", createdAt="Sat May 15 2021 21:24:12", updatedAt="Wed Oct 06 2021 13:07:06")
    comment1195b = Comment(videoId=251, channelId=85, content="Two seats were vacant.", createdAt="Sun Feb 27 2022 05:07:44", updatedAt="Sat Jul 03 2021 02:27:14")
    comment1196b = Comment(videoId=743, channelId=88, content="I'm a great listener, really good with empathy vs sympathy and all that, but I hate people.", createdAt="Tue May 11 2021 07:48:46", updatedAt="Sat Oct 09 2021 02:09:49")
    comment1197b = Comment(videoId=87, channelId=91, content="The virus had powers none of us knew existed.", createdAt="Sat Sep 18 2021 20:50:00", updatedAt="Sat Jan 15 2022 17:11:34")
    comment1198b = Comment(videoId=748, channelId=85, content="Nancy was proud that she ran a tight shipwreck.", createdAt="Wed Apr 06 2022 20:20:23", updatedAt="Thu May 13 2021 07:48:45")
    comment1199b = Comment(videoId=193, channelId=85, content="She was amazed by the large chunks of ice washing up on the beach.", createdAt="Wed Mar 30 2022 10:13:46", updatedAt="Sat Jun 19 2021 03:23:11")
    comment1200b = Comment(videoId=474, channelId=91, content="People keep telling me \"orange\" but I still prefer \"pink\".", createdAt="Fri Oct 22 2021 10:17:40", updatedAt="Mon Jun 21 2021 12:20:21")
    comment1201b = Comment(videoId=266, channelId=92, content="A song can make or ruin a person’s day if they let it get to them.", createdAt="Mon Sep 27 2021 22:50:41", updatedAt="Fri Dec 10 2021 16:50:43")
    comment1202b = Comment(videoId=92, channelId=97, content="I just wanted to tell you I could see the love you have for your child by the way you look at her.", createdAt="Fri Jan 07 2022 23:56:56", updatedAt="Tue Apr 05 2022 10:01:30")
    comment1203b = Comment(videoId=304, channelId=96, content="I think I will buy the red car, or I will lease the blue one.", createdAt="Wed Jan 05 2022 10:01:05", updatedAt="Tue Jul 06 2021 11:15:38")
    comment1204b = Comment(videoId=664, channelId=94, content="The father handed each child a roadmap at the beginning of the 2-day road trip and explained it was so they could find their way home.", createdAt="Wed Dec 01 2021 10:06:07", updatedAt="Wed Oct 20 2021 04:20:02")
    comment1205b = Comment(videoId=437, channelId=96, content="Various sea birds are elegant, but nothing is as elegant as a gliding pelican.", createdAt="Mon Apr 12 2021 00:08:22", updatedAt="Wed Mar 02 2022 11:47:15")
    comment1206b = Comment(videoId=76, channelId=87, content="The bird had a belief that it was really a groundhog.", createdAt="Sat Nov 20 2021 06:07:22", updatedAt="Wed May 12 2021 23:02:50")
    comment1207b = Comment(videoId=652, channelId=95, content="There's no reason a hula hoop can't also be a circus ring.", createdAt="Wed Apr 28 2021 13:22:05", updatedAt="Mon Aug 09 2021 02:13:49")
    comment1208b = Comment(videoId=574, channelId=88, content="Truth in advertising and dinosaurs with skateboards have much in common.", createdAt="Sun Oct 17 2021 20:39:24", updatedAt="Tue Aug 17 2021 03:40:22")
    comment1209b = Comment(videoId=570, channelId=88, content="She used her own hair in the soup to give it more flavor.", createdAt="Sun Oct 03 2021 09:51:09", updatedAt="Tue Jan 25 2022 03:03:20")
    comment1210b = Comment(videoId=8, channelId=86, content="The toy brought back fond memories of being lost in the rain forest.", createdAt="Thu Jan 06 2022 01:08:08", updatedAt="Tue May 11 2021 22:34:32")
    comment1211b = Comment(videoId=7, channelId=86, content="The furnace repairman indicated the heating system was acting as an air conditioner.", createdAt="Fri Mar 04 2022 02:17:35", updatedAt="Sat Dec 04 2021 12:47:49")
    comment1212b = Comment(videoId=696, channelId=89, content="Carol drank the blood as if she were a vampire.", createdAt="Fri Jul 30 2021 20:09:41", updatedAt="Tue Oct 19 2021 03:53:10")
    comment1213b = Comment(videoId=475, channelId=87, content="Karen believed all traffic laws should be obeyed by all except herself.", createdAt="Mon Nov 15 2021 10:27:12", updatedAt="Wed Sep 29 2021 16:52:38")
    comment1214b = Comment(videoId=177, channelId=95, content="She can live her life however she wants as long as she listens to what I have to say.", createdAt="Tue Oct 19 2021 15:16:28", updatedAt="Fri Dec 03 2021 01:02:59")
    comment1215b = Comment(videoId=30, channelId=95, content="He learned the hardest lesson of his life and had the scars, both physical and mental, to prove it.", createdAt="Wed Aug 04 2021 17:06:45", updatedAt="Sat Dec 11 2021 17:18:54")
    comment1216b = Comment(videoId=101, channelId=97, content="It had been sixteen days since the zombies first attacked.", createdAt="Wed Nov 03 2021 00:35:04", updatedAt="Sun Jan 23 2022 07:54:17")
    comment1217b = Comment(videoId=94, channelId=90, content="He was disappointed when he found the beach to be so sandy and the sun so sunny.", createdAt="Sat Oct 09 2021 04:23:11", updatedAt="Sat Mar 26 2022 10:50:22")
    comment1218b = Comment(videoId=338, channelId=85, content="Jenny made the announcement that her baby was an alien.", createdAt="Wed Aug 25 2021 06:20:56", updatedAt="Fri Feb 25 2022 11:27:04")
    comment1219b = Comment(videoId=564, channelId=93, content="Nudist colonies shun fig-leaf couture.", createdAt="Wed Mar 02 2022 15:17:09", updatedAt="Mon Jan 03 2022 17:42:35")
    comment1220b = Comment(videoId=387, channelId=85, content="Flash photography is best used in full sunlight.", createdAt="Mon Sep 13 2021 03:08:29", updatedAt="Sat Jun 12 2021 01:25:16")
    comment1221b = Comment(videoId=520, channelId=91, content="Homesickness became contagious in the young campers' cabin.", createdAt="Thu May 20 2021 08:31:04", updatedAt="Sun Jul 18 2021 17:27:24")
    comment1222b = Comment(videoId=409, channelId=90, content="I liked their first two albums but changed my mind after that charity gig.", createdAt="Tue Nov 02 2021 02:46:07", updatedAt="Thu Oct 07 2021 05:44:22")
    comment1223b = Comment(videoId=467, channelId=95, content="She had some amazing news to share but nobody to share it with.", createdAt="Tue Nov 02 2021 16:43:34", updatedAt="Sat May 15 2021 01:28:51")
    comment1224b = Comment(videoId=357, channelId=88, content="He colored deep space a soft yellow.", createdAt="Sun Feb 20 2022 04:02:42", updatedAt="Sun Dec 26 2021 02:34:49")
    comment1225b = Comment(videoId=159, channelId=85, content="As he entered the church he could hear the soft voice of someone whispering into a cell phone.", createdAt="Sat Oct 02 2021 22:23:45", updatedAt="Mon May 03 2021 21:37:23")
    comment1226b = Comment(videoId=505, channelId=89, content="I don’t respect anybody who can’t tell the difference between Pepsi and Coke.", createdAt="Sun Mar 27 2022 09:59:14", updatedAt="Sat Mar 12 2022 02:21:05")
    comment1227b = Comment(videoId=444, channelId=93, content="The pet shop stocks everything you need to keep your anaconda happy.", createdAt="Sat Jun 19 2021 01:55:32", updatedAt="Wed Feb 23 2022 02:07:12")
    comment1228b = Comment(videoId=582, channelId=95, content="Separation anxiety is what happens when you can't find your phone.", createdAt="Fri Feb 04 2022 10:29:22", updatedAt="Mon Aug 09 2021 09:17:25")
    comment1229b = Comment(videoId=546, channelId=93, content="The toddler’s endless tantrum caused the entire plane anxiety.", createdAt="Fri Jan 14 2022 20:42:35", updatedAt="Mon Mar 21 2022 17:51:11")
    comment1230b = Comment(videoId=41, channelId=95, content="More RVs were seen in the storage lot than at the campground.", createdAt="Sat Jan 22 2022 18:28:36", updatedAt="Fri May 21 2021 23:06:18")
    comment1231b = Comment(videoId=540, channelId=94, content="The three-year-old girl ran down the beach as the kite flew behind her.", createdAt="Thu Jul 22 2021 06:25:42", updatedAt="Fri Nov 12 2021 18:54:00")
    comment1232b = Comment(videoId=717, channelId=95, content="The waitress was not amused when he ordered green eggs and ham.", createdAt="Mon Nov 01 2021 04:29:06", updatedAt="Wed Mar 16 2022 03:14:07")
    comment1233b = Comment(videoId=697, channelId=93, content="She wasn't sure whether to be impressed or concerned that he folded underwear in neat little packages.", createdAt="Tue Sep 21 2021 00:36:15", updatedAt="Wed Apr 14 2021 15:45:20")
    comment1234b = Comment(videoId=83, channelId=90, content="Kevin embraced his ability to be at the wrong place at the wrong time.", createdAt="Thu May 20 2021 20:00:16", updatedAt="Mon Dec 20 2021 02:26:46")
    comment1235b = Comment(videoId=123, channelId=90, content="I want more detailed information.", createdAt="Sun Dec 12 2021 01:42:23", updatedAt="Sun Oct 24 2021 23:28:28")
    comment1236b = Comment(videoId=596, channelId=95, content="She tilted her head back and let whip cream stream into her mouth while taking a bath.", createdAt="Tue Jan 18 2022 12:17:20", updatedAt="Thu Dec 02 2021 05:00:40")
    comment1237b = Comment(videoId=490, channelId=92, content="My Mum tries to be cool by saying that she likes all the same things that I do.", createdAt="Sun Jan 23 2022 13:37:57", updatedAt="Sat Mar 12 2022 07:58:02")
    comment1238b = Comment(videoId=735, channelId=89, content="I'm worried by the fact that my daughter looks to the local carpet seller as a role model.", createdAt="Mon Jan 10 2022 23:31:16", updatedAt="Wed Sep 01 2021 23:11:24")
    comment1239b = Comment(videoId=224, channelId=88, content="My biggest joy is roasting almonds while stalking prey.", createdAt="Mon May 10 2021 18:11:34", updatedAt="Mon Aug 16 2021 18:06:30")
    comment1240b = Comment(videoId=774, channelId=96, content="Nancy thought the best way to create a welcoming home was to line it with barbed wire.", createdAt="Tue May 18 2021 15:09:53", updatedAt="Mon Jun 28 2021 09:20:33")
    comment1241b = Comment(videoId=558, channelId=96, content="I cheated while playing the darts tournament by using a longbow.", createdAt="Thu May 06 2021 17:06:29", updatedAt="Tue Aug 31 2021 05:25:49")
    comment1242b = Comment(videoId=383, channelId=98, content="The efficiency with which he paired the socks in the drawer was quite admirable.", createdAt="Wed Jul 28 2021 05:11:34", updatedAt="Thu Jul 15 2021 20:10:08")
    comment1243b = Comment(videoId=180, channelId=90, content="Cursive writing is the best way to build a race track.", createdAt="Fri Jan 28 2022 02:17:06", updatedAt="Fri Aug 27 2021 05:39:53")
    comment1245b = Comment(videoId=412, channelId=93, content="The light in his life was actually a fire burning all around him.", createdAt="Wed Nov 24 2021 15:09:28", updatedAt="Thu Sep 09 2021 12:06:13")
    comment1246b = Comment(videoId=273, channelId=96, content="The two walked down the slot canyon oblivious to the sound of thunder in the distance.", createdAt="Sat Jul 17 2021 09:16:07", updatedAt="Tue Dec 14 2021 06:37:26")
    comment1247b = Comment(videoId=555, channelId=95, content="When transplanting seedlings, candied teapots will make the task easier.", createdAt="Sat Apr 02 2022 22:22:18", updatedAt="Mon Sep 20 2021 20:15:02")
    comment1248b = Comment(videoId=329, channelId=97, content="With a single flip of the coin, his life changed forever.", createdAt="Tue Jan 25 2022 16:39:53", updatedAt="Sun Aug 15 2021 12:30:33")
    comment1249b = Comment(videoId=641, channelId=91, content="The beach was crowded with snow leopards.", createdAt="Fri Jul 30 2021 14:58:12", updatedAt="Thu May 27 2021 06:46:55")
    comment1250b = Comment(videoId=494, channelId=90, content="The lake is a long way from here.", createdAt="Fri May 28 2021 11:11:03", updatedAt="Tue Apr 27 2021 09:45:14")
    comment1251b = Comment(videoId=362, channelId=96, content="Jerry liked to look at paintings while eating garlic ice cream.", createdAt="Sun Jul 04 2021 22:33:16", updatedAt="Mon Jul 05 2021 12:05:07")
    comment1252b = Comment(videoId=475, channelId=89, content="He is good at eating pickles and telling women about his emotional problems.", createdAt="Sat Aug 28 2021 14:16:08", updatedAt="Thu Oct 21 2021 15:53:37")
    comment1253b = Comment(videoId=624, channelId=90, content="He created a pig burger out of beef.", createdAt="Tue Oct 19 2021 14:24:32", updatedAt="Mon Aug 02 2021 23:25:35")
    comment1254b = Comment(videoId=301, channelId=87, content="He watched the dancing piglets with panda bear tummies in the swimming pool.", createdAt="Sat Feb 12 2022 22:49:47", updatedAt="Mon May 10 2021 22:48:56")
    comment1255b = Comment(videoId=24, channelId=89, content="He played the game as if his life depended on it and the truth was that it did.", createdAt="Mon May 24 2021 09:28:37", updatedAt="Fri Mar 11 2022 14:45:23")
    comment1256b = Comment(videoId=756, channelId=86, content="He excelled at firing people nicely.", createdAt="Mon Dec 27 2021 21:16:56", updatedAt="Wed Nov 17 2021 20:40:14")
    comment1257b = Comment(videoId=142, channelId=97, content="She tilted her head back and let whip cream stream into her mouth while taking a bath.", createdAt="Wed Dec 29 2021 15:11:52", updatedAt="Tue Nov 30 2021 06:42:54")
    comment1258b = Comment(videoId=84, channelId=92, content="He dreamed of eating green apples with worms.", createdAt="Fri Mar 04 2022 08:25:49", updatedAt="Sun Oct 31 2021 21:57:00")
    comment1259b = Comment(videoId=432, channelId=85, content="Whenever he saw a red flag warning at the beach he grabbed his surfboard.", createdAt="Tue Nov 02 2021 17:15:31", updatedAt="Sun Apr 25 2021 11:04:38")
    comment1260b = Comment(videoId=257, channelId=95, content="The waitress was not amused when he ordered green eggs and ham.", createdAt="Thu Nov 04 2021 02:11:33", updatedAt="Tue Aug 17 2021 11:55:06")
    comment1261b = Comment(videoId=649, channelId=91, content="After fighting off the alligator, Brian still had to face the anaconda.", createdAt="Tue Nov 09 2021 07:53:44", updatedAt="Sun Jan 16 2022 10:47:49")
    comment1262b = Comment(videoId=272, channelId=87, content="Everybody should read Chaucer to improve their everyday vocabulary.", createdAt="Fri Oct 29 2021 13:38:23", updatedAt="Fri May 14 2021 07:54:56")
    comment1263b = Comment(videoId=293, channelId=85, content="Don't put peanut butter on the dog's nose.", createdAt="Mon Jul 26 2021 21:30:37", updatedAt="Sun Nov 07 2021 01:51:38")
    comment1264b = Comment(videoId=192, channelId=87, content="I made myself a peanut butter sandwich as I didn't want to subsist on veggie crackers.", createdAt="Thu Feb 24 2022 01:33:41", updatedAt="Fri Sep 17 2021 20:52:25")
    comment1265b = Comment(videoId=181, channelId=96, content="He was so preoccupied with whether or not he could that he failed to stop to consider if he should.", createdAt="Sun Jun 06 2021 15:30:42", updatedAt="Wed Feb 02 2022 14:56:38")
    comment1266b = Comment(videoId=676, channelId=97, content="I'm not a party animal, but I do like animal parties.", createdAt="Mon Dec 06 2021 19:59:59", updatedAt="Fri Aug 27 2021 14:58:03")
    comment1267b = Comment(videoId=34, channelId=93, content="I was fishing for compliments and accidentally caught a trout.", createdAt="Wed Mar 09 2022 21:19:31", updatedAt="Wed Feb 02 2022 02:15:14")
    comment1268b = Comment(videoId=65, channelId=98, content="We have never been to Asia, nor have we visited Africa.", createdAt="Sat Jun 19 2021 10:07:25", updatedAt="Fri Dec 17 2021 10:55:11")
    comment1269b = Comment(videoId=646, channelId=86, content="Today I bought a raincoat and wore it on a sunny day.", createdAt="Sat Jul 24 2021 04:21:21", updatedAt="Wed May 19 2021 14:59:13")
    comment1270b = Comment(videoId=77, channelId=90, content="He is no James Bond; his name is Roger Moore.", createdAt="Thu Feb 24 2022 14:06:31", updatedAt="Thu Jul 15 2021 04:01:03")
    comment1271b = Comment(videoId=540, channelId=92, content="The old rusted farm equipment surrounded the house predicting its demise.", createdAt="Tue Apr 27 2021 16:31:39", updatedAt="Thu Oct 07 2021 10:58:25")
    comment1272b = Comment(videoId=22, channelId=95, content="While on the first date he accidentally hit his head on the beam.", createdAt="Tue May 11 2021 19:01:12", updatedAt="Fri Feb 25 2022 16:07:48")
    comment1273b = Comment(videoId=70, channelId=90, content="She works two jobs to make ends meet; at least, that was her reason for not having time to join us.", createdAt="Sat Jul 10 2021 22:08:22", updatedAt="Sat Aug 21 2021 14:57:58")
    comment1274b = Comment(videoId=461, channelId=87, content="It's much more difficult to play tennis with a bowling ball than it is to bowl with a tennis ball.", createdAt="Tue Sep 21 2021 00:40:56", updatedAt="Thu May 27 2021 16:09:34")
    comment1275b = Comment(videoId=607, channelId=98, content="The door swung open to reveal pink giraffes and red elephants.", createdAt="Mon Dec 06 2021 10:31:24", updatedAt="Fri Jun 25 2021 06:20:01")
    comment1276b = Comment(videoId=695, channelId=98, content="He looked behind the door and didn't like what he saw.", createdAt="Sun Mar 20 2022 05:40:05", updatedAt="Sat Aug 07 2021 19:45:04")
    comment1277b = Comment(videoId=530, channelId=91, content="He never understood why what, when, and where left out who.", createdAt="Sun Jul 04 2021 03:50:38", updatedAt="Mon Jan 17 2022 11:47:43")
    comment1278b = Comment(videoId=424, channelId=96, content="They called out her name time and again, but were met with nothing but silence.", createdAt="Wed Apr 14 2021 01:26:29", updatedAt="Tue Jun 08 2021 14:01:09")
    comment1279b = Comment(videoId=767, channelId=86, content="The llama couldn't resist trying the lemonade.", createdAt="Mon Jan 17 2022 08:08:43", updatedAt="Sun Jul 04 2021 08:24:26")
    comment1280b = Comment(videoId=354, channelId=98, content="The random sentence generator generated a random sentence about a random sentence.", createdAt="Fri Feb 18 2022 21:22:21", updatedAt="Tue Mar 08 2022 22:29:50")
    comment1281b = Comment(videoId=482, channelId=85, content="There was coal in his stocking and he was thrilled.", createdAt="Tue Jun 15 2021 19:00:10", updatedAt="Tue Oct 19 2021 20:33:34")
    comment1282b = Comment(videoId=656, channelId=97, content="Sarah ran from the serial killer holding a jug of milk.", createdAt="Thu Dec 09 2021 10:36:24", updatedAt="Fri May 21 2021 20:30:29")
    comment1283b = Comment(videoId=165, channelId=88, content="The elephant didn't want to talk about the person in the room.", createdAt="Sat Oct 09 2021 10:31:25", updatedAt="Sun Jul 18 2021 03:07:39")
    comment1284b = Comment(videoId=119, channelId=89, content="The child’s favorite Christmas gift was the large box her father’s lawnmower came in.", createdAt="Thu Dec 09 2021 02:04:04", updatedAt="Sat Jan 08 2022 04:30:40")
    comment1285b = Comment(videoId=291, channelId=95, content="Today we gathered moss for my uncle's wedding.", createdAt="Mon Jan 03 2022 07:06:56", updatedAt="Mon Apr 19 2021 16:45:18")
    comment1286b = Comment(videoId=637, channelId=86, content="There is no better feeling than staring at a wall with closed eyes.", createdAt="Sun Jan 30 2022 02:52:05", updatedAt="Sat Jul 03 2021 01:01:48")
    comment1287b = Comment(videoId=130, channelId=87, content="Watching the geriatric men’s softball team brought back memories of 3 yr olds playing t-ball.", createdAt="Fri Feb 04 2022 03:15:33", updatedAt="Sun Nov 14 2021 17:29:40")
    comment1288b = Comment(videoId=747, channelId=97, content="The elderly neighborhood became enraged over the coyotes who had been blamed for the poodle’s disappearance.", createdAt="Thu Jul 15 2021 01:50:08", updatedAt="Fri Apr 08 2022 15:56:10")
    comment1289b = Comment(videoId=99, channelId=97, content="As he entered the church he could hear the soft voice of someone whispering into a cell phone.", createdAt="Sat Jul 24 2021 07:12:44", updatedAt="Wed Oct 20 2021 22:01:41")
    comment1290b = Comment(videoId=273, channelId=89, content="When nobody is around, the trees gossip about the people who have walked under them.", createdAt="Fri Jul 02 2021 14:00:15", updatedAt="Thu Dec 30 2021 19:13:21")
    comment1291b = Comment(videoId=267, channelId=89, content="It was at that moment that he learned there are certain parts of the body that you should never Nair.", createdAt="Sat Apr 09 2022 06:49:52", updatedAt="Mon Feb 28 2022 09:25:47")
    comment1292b = Comment(videoId=236, channelId=95, content="He decided to live his life by the big beats manifesto.", createdAt="Tue Oct 19 2021 09:06:31", updatedAt="Fri Dec 31 2021 01:48:54")
    comment1293b = Comment(videoId=515, channelId=92, content="Grape jelly was leaking out the hole in the roof.", createdAt="Tue Jun 22 2021 23:08:37", updatedAt="Wed Dec 08 2021 14:00:37")
    comment1294b = Comment(videoId=380, channelId=90, content="The blue parrot drove by the hitchhiking mongoose.", createdAt="Sat Nov 27 2021 08:30:51", updatedAt="Mon Aug 23 2021 14:17:15")
    comment1295b = Comment(videoId=712, channelId=85, content="He would only survive if he kept the fire going and he could hear thunder in the distance.", createdAt="Wed Jan 26 2022 02:48:32", updatedAt="Sun Dec 19 2021 16:18:21")
    comment1296b = Comment(videoId=439, channelId=87, content="As the years pass by, we all know owners look more and more like their dogs.", createdAt="Thu Apr 22 2021 18:50:40", updatedAt="Sat May 22 2021 01:54:50")
    comment1297b = Comment(videoId=778, channelId=96, content="It's difficult to understand the lengths he'd go to remain short.", createdAt="Mon Feb 21 2022 06:58:31", updatedAt="Wed Jan 05 2022 12:32:50")
    comment1298b = Comment(videoId=101, channelId=93, content="Check back tomorrow; I will see if the book has arrived.", createdAt="Thu Jul 29 2021 21:05:22", updatedAt="Wed Apr 21 2021 09:50:59")
    comment1299b = Comment(videoId=234, channelId=86, content="I liked their first two albums but changed my mind after that charity gig.", createdAt="Sat Feb 26 2022 19:38:56", updatedAt="Sun Sep 19 2021 19:05:18")
    comment1300b = Comment(videoId=637, channelId=93, content="For some unfathomable reason, the response team didn't consider a lack of milk for my cereal as a proper emergency.", createdAt="Tue May 04 2021 12:04:21", updatedAt="Mon May 24 2021 13:04:55")
    comment1301b = Comment(videoId=456, channelId=87, content="The gruff old man sat in the back of the bait shop grumbling to himself as he scooped out a handful of worms.", createdAt="Wed Aug 04 2021 17:06:05", updatedAt="Sat Jul 24 2021 06:31:24")
    comment1302b = Comment(videoId=391, channelId=98, content="You've been eyeing me all day and waiting for your move like a lion stalking a gazelle in a savannah.", createdAt="Fri Jun 18 2021 15:58:13", updatedAt="Mon Sep 13 2021 03:34:13")
    comment1303b = Comment(videoId=330, channelId=95, content="There were white out conditions in the town; subsequently, the roads were impassable.", createdAt="Sun Oct 03 2021 04:45:26", updatedAt="Mon Oct 11 2021 22:58:33")
    comment1304b = Comment(videoId=677, channelId=89, content="People who insist on picking their teeth with their elbows are so annoying!", createdAt="Thu Dec 23 2021 12:30:44", updatedAt="Sat Dec 25 2021 18:53:13")
    comment1305b = Comment(videoId=356, channelId=95, content="He told us a very exciting adventure story.", createdAt="Wed Sep 29 2021 21:28:28", updatedAt="Sun Jul 11 2021 21:25:46")
    comment1306b = Comment(videoId=452, channelId=87, content="She finally understood that grief was her love with no place for it to go.", createdAt="Mon Jan 10 2022 08:55:34", updatedAt="Tue Jun 22 2021 10:53:44")
    comment1307b = Comment(videoId=626, channelId=92, content="You're unsure whether or not to trust him, but very thankful that you wore a turtle neck.", createdAt="Sun Mar 06 2022 03:29:18", updatedAt="Sat Dec 04 2021 17:50:57")
    comment1308b = Comment(videoId=733, channelId=87, content="The stench from the feedlot permeated the car despite having the air conditioning on recycled air.", createdAt="Wed Jan 05 2022 15:37:21", updatedAt="Thu Apr 07 2022 06:54:31")
    comment1309b = Comment(videoId=200, channelId=94, content="Pair your designer cowboy hat with scuba gear for a memorable occasion.", createdAt="Fri Apr 23 2021 12:32:46", updatedAt="Tue Jan 04 2022 10:46:34")
    comment1310b = Comment(videoId=641, channelId=86, content="When nobody is around, the trees gossip about the people who have walked under them.", createdAt="Sun Sep 05 2021 19:17:26", updatedAt="Sun Nov 28 2021 22:50:27")
    comment1311b = Comment(videoId=701, channelId=91, content="The reservoir water level continued to lower while we enjoyed our long shower.", createdAt="Thu May 27 2021 12:17:53", updatedAt="Fri Feb 18 2022 06:42:48")
    comment1312b = Comment(videoId=765, channelId=93, content="25 years later, she still regretted that specific moment.", createdAt="Sun Feb 20 2022 18:08:19", updatedAt="Sat Jul 03 2021 10:08:43")
    comment1313b = Comment(videoId=83, channelId=88, content="If you don't like toenails, you probably shouldn't look at your feet.", createdAt="Sat Oct 16 2021 23:27:53", updatedAt="Sun May 23 2021 10:11:07")
    comment1314b = Comment(videoId=444, channelId=88, content="Blue sounded too cold at the time and yet it seemed to work for gin.", createdAt="Fri Aug 27 2021 08:33:12", updatedAt="Tue Sep 07 2021 04:28:04")
    comment1315b = Comment(videoId=168, channelId=92, content="For some unfathomable reason, the response team didn't consider a lack of milk for my cereal as a proper emergency.", createdAt="Wed Oct 20 2021 05:11:21", updatedAt="Mon Sep 20 2021 03:56:32")
    comment1316b = Comment(videoId=722, channelId=97, content="The fish listened intently to what the frogs had to say.", createdAt="Wed Sep 01 2021 14:42:48", updatedAt="Sat Feb 12 2022 01:07:47")
    comment1317b = Comment(videoId=605, channelId=87, content="It's never been my responsibility to glaze the donuts.", createdAt="Sat May 01 2021 00:51:25", updatedAt="Sat Jun 05 2021 15:49:43")
    comment1318b = Comment(videoId=601, channelId=88, content="Greetings from the galaxy MACS0647-JD, or what we call home.", createdAt="Wed Oct 27 2021 00:27:28", updatedAt="Tue Oct 19 2021 22:27:03")
    comment1319b = Comment(videoId=591, channelId=88, content="Sixty-Four comes asking for bread.", createdAt="Sat Jun 26 2021 02:14:49", updatedAt="Mon Apr 26 2021 17:09:25")
    comment1320b = Comment(videoId=201, channelId=90, content="He is no James Bond; his name is Roger Moore.", createdAt="Sun Jan 23 2022 02:35:57", updatedAt="Wed Mar 23 2022 14:55:52")
    comment1321b = Comment(videoId=507, channelId=96, content="The teens wondered what was kept in the red shed on the far edge of the school grounds.", createdAt="Tue Oct 05 2021 21:05:14", updatedAt="Tue Sep 28 2021 12:06:50")
    comment1322b = Comment(videoId=358, channelId=94, content="I'm a great listener, really good with empathy vs sympathy and all that, but I hate people.", createdAt="Thu Jan 20 2022 20:53:51", updatedAt="Thu Jun 03 2021 02:47:47")
    comment1323b = Comment(videoId=757, channelId=92, content="She wrote him a long letter, but he didn't read it.", createdAt="Sat Jul 31 2021 09:52:08", updatedAt="Sun Jul 04 2021 16:23:17")
    comment1324b = Comment(videoId=6, channelId=87, content="I think I will buy the red car, or I will lease the blue one.", createdAt="Tue Feb 08 2022 07:48:52", updatedAt="Thu Jul 22 2021 15:59:44")
    comment1325b = Comment(videoId=283, channelId=88, content="There was coal in his stocking and he was thrilled.", createdAt="Sat Jun 19 2021 05:38:24", updatedAt="Sat Oct 30 2021 18:08:34")
    comment1326b = Comment(videoId=409, channelId=91, content="Nancy decided to make the porta-potty her home.", createdAt="Sat Jan 15 2022 09:18:09", updatedAt="Tue Aug 17 2021 11:49:56")
    comment1327b = Comment(videoId=54, channelId=98, content="It was her first experience training a rainbow unicorn.", createdAt="Sat Apr 02 2022 13:45:01", updatedAt="Thu Aug 19 2021 10:34:48")
    comment1328b = Comment(videoId=676, channelId=96, content="Most shark attacks occur about 10 feet from the beach since that's where the people are.", createdAt="Wed Dec 01 2021 11:04:14", updatedAt="Thu Jul 22 2021 17:02:33")
    comment1329b = Comment(videoId=150, channelId=88, content="All she wanted was the answer, but she had no idea how much she would hate it.", createdAt="Sun Jul 11 2021 15:49:34", updatedAt="Thu Dec 23 2021 15:53:15")
    comment1330b = Comment(videoId=445, channelId=94, content="I’m working on a sweet potato farm.", createdAt="Wed Jan 05 2022 12:56:16", updatedAt="Thu Mar 17 2022 23:20:59")
    comment1331b = Comment(videoId=429, channelId=98, content="Always bring cinnamon buns on a deep-sea diving expedition.", createdAt="Mon May 03 2021 23:54:33", updatedAt="Sun Sep 19 2021 09:55:57")
    comment1332b = Comment(videoId=627, channelId=94, content="David subscribes to the \"stuff your tent into the bag\" strategy over nicely folding it.", createdAt="Sun Oct 31 2021 05:25:11", updatedAt="Thu Jul 01 2021 16:18:06")
    comment1333b = Comment(videoId=176, channelId=88, content="Shakespeare was a famous 17th-century diesel mechanic.", createdAt="Mon Jan 17 2022 14:58:54", updatedAt="Wed May 12 2021 09:47:08")
    comment1334b = Comment(videoId=347, channelId=88, content="He didn't understand why the bird wanted to ride the bicycle.", createdAt="Sun Oct 31 2021 17:54:01", updatedAt="Sat Nov 27 2021 14:03:08")
    comment1335b = Comment(videoId=242, channelId=96, content="The manager of the fruit stand always sat and only sold vegetables.", createdAt="Sun Jan 09 2022 09:51:20", updatedAt="Thu Dec 16 2021 05:07:16")
    comment1336b = Comment(videoId=550, channelId=96, content="It's not often you find a soggy banana on the street.", createdAt="Fri Oct 15 2021 09:56:44", updatedAt="Sat Nov 13 2021 02:44:27")
    comment1337b = Comment(videoId=657, channelId=95, content="Swim at your own risk was taken as a challenge for the group of Kansas City college students.", createdAt="Sat Jan 08 2022 13:24:50", updatedAt="Mon Feb 07 2022 18:19:09")
    comment1338b = Comment(videoId=281, channelId=97, content="Martha came to the conclusion that shake weights are a great gift for any occasion.", createdAt="Thu Apr 15 2021 10:35:20", updatedAt="Sat Aug 21 2021 13:05:22")
    comment1339b = Comment(videoId=503, channelId=91, content="Hit me with your pet shark!", createdAt="Tue Mar 01 2022 11:36:51", updatedAt="Mon Dec 20 2021 18:06:46")
    comment1340b = Comment(videoId=86, channelId=88, content="More RVs were seen in the storage lot than at the campground.", createdAt="Tue Jun 22 2021 06:41:41", updatedAt="Sun Jul 04 2021 02:31:15")
    comment1341b = Comment(videoId=543, channelId=93, content="He fumbled in the darkness looking for the light switch, but when he finally found it there was someone already there.", createdAt="Mon Jan 24 2022 00:39:15", updatedAt="Tue May 04 2021 14:10:33")
    comment1342b = Comment(videoId=104, channelId=85, content="He wondered if she would appreciate his toenail collection.", createdAt="Fri Aug 06 2021 01:27:12", updatedAt="Wed Feb 16 2022 20:11:22")
    comment1343b = Comment(videoId=39, channelId=87, content="All they could see was the blue water surrounding their sailboat.", createdAt="Thu Apr 22 2021 17:06:05", updatedAt="Fri May 21 2021 09:34:22")
    comment1344b = Comment(videoId=204, channelId=93, content="Don't step on the broken glass.", createdAt="Mon Oct 18 2021 15:04:42", updatedAt="Wed Oct 27 2021 23:01:36")
    comment1345b = Comment(videoId=559, channelId=92, content="Just go ahead and press that button.", createdAt="Fri Aug 27 2021 13:41:59", updatedAt="Sat May 01 2021 09:22:28")
    comment1346b = Comment(videoId=668, channelId=91, content="Jim liked driving around town with his hazard lights on.", createdAt="Mon May 17 2021 15:32:50", updatedAt="Mon Dec 06 2021 15:19:36")
    comment1347b = Comment(videoId=632, channelId=86, content="Flying fish flew by the space station.", createdAt="Wed Dec 29 2021 06:05:51", updatedAt="Sun Aug 29 2021 15:44:39")
    comment1348b = Comment(videoId=479, channelId=87, content="The irony of the situation wasn't lost on anyone in the room.", createdAt="Fri Apr 23 2021 08:38:54", updatedAt="Sun Jan 16 2022 09:14:35")
    comment1349b = Comment(videoId=710, channelId=95, content="A glittering gem is not enough.", createdAt="Fri Jun 18 2021 10:58:22", updatedAt="Mon Jun 14 2021 04:30:33")
    comment1350b = Comment(videoId=761, channelId=93, content="He wondered if it could be called a beach if there was no sand.", createdAt="Fri Dec 24 2021 13:14:57", updatedAt="Sat Jun 12 2021 23:12:24")
    comment1351b = Comment(videoId=652, channelId=92, content="Two more days and all his problems would be solved.", createdAt="Wed Jul 14 2021 11:44:29", updatedAt="Wed Mar 09 2022 03:40:10")
    comment1352b = Comment(videoId=523, channelId=90, content="Nobody loves a pig wearing lipstick.", createdAt="Sun Aug 22 2021 22:42:53", updatedAt="Mon Jun 14 2021 19:18:47")
    comment1353b = Comment(videoId=775, channelId=87, content="Jason didn’t understand why his parents wouldn’t let him sell his little sister at the garage sale.", createdAt="Tue Nov 16 2021 13:59:13", updatedAt="Fri Jun 25 2021 07:39:10")
    comment1354b = Comment(videoId=488, channelId=86, content="As he looked out the window, he saw a clown walk by.", createdAt="Thu Mar 31 2022 05:25:23", updatedAt="Wed Nov 03 2021 03:13:26")
    comment1355b = Comment(videoId=18, channelId=93, content="The fog was so dense even a laser decided it wasn't worth the effort.", createdAt="Mon May 17 2021 03:13:30", updatedAt="Tue Jul 13 2021 15:55:28")
    comment1356b = Comment(videoId=740, channelId=88, content="Eating eggs on Thursday for choir practice was recommended.", createdAt="Sun Aug 29 2021 08:16:51", updatedAt="Mon Feb 28 2022 11:20:32")
    comment1357b = Comment(videoId=341, channelId=94, content="He is good at eating pickles and telling women about his emotional problems.", createdAt="Thu Nov 11 2021 22:57:41", updatedAt="Fri Sep 10 2021 21:03:56")
    comment1358b = Comment(videoId=75, channelId=97, content="It's never been my responsibility to glaze the donuts.", createdAt="Tue May 18 2021 03:11:44", updatedAt="Thu Nov 04 2021 01:12:37")
    comment1359b = Comment(videoId=606, channelId=86, content="Joe made the sugar cookies; Susan decorated them.", createdAt="Mon Apr 19 2021 18:02:54", updatedAt="Fri Jan 07 2022 11:51:46")
    comment1360b = Comment(videoId=506, channelId=89, content="Nobody has encountered an explosive daisy and lived to tell the tale.", createdAt="Tue Aug 03 2021 01:30:40", updatedAt="Wed Sep 22 2021 12:13:50")
    comment1361b = Comment(videoId=637, channelId=86, content="The group quickly understood that toxic waste was the most effective barrier to use against the zombies.", createdAt="Sun Sep 26 2021 22:32:56", updatedAt="Sat Apr 24 2021 20:57:18")
    comment1362b = Comment(videoId=775, channelId=91, content="The secret ingredient to his wonderful life was crime.", createdAt="Sat Jun 19 2021 08:21:20", updatedAt="Tue Feb 01 2022 10:10:19")
    comment1363b = Comment(videoId=401, channelId=95, content="She works two jobs to make ends meet; at least, that was her reason for not having time to join us.", createdAt="Fri Apr 08 2022 03:16:10", updatedAt="Thu Oct 07 2021 12:46:39")
    comment1364b = Comment(videoId=721, channelId=98, content="I honestly find her about as intimidating as a basket of kittens.", createdAt="Tue Apr 27 2021 12:55:11", updatedAt="Fri Apr 23 2021 07:53:00")
    comment1365b = Comment(videoId=710, channelId=89, content="Shingle color was not something the couple had ever talked about.", createdAt="Thu Jun 10 2021 21:12:47", updatedAt="Fri Jan 07 2022 06:49:33")
    comment1366b = Comment(videoId=680, channelId=96, content="The virus had powers none of us knew existed.", createdAt="Thu Apr 29 2021 03:51:24", updatedAt="Wed Oct 20 2021 05:41:02")
    comment1367b = Comment(videoId=723, channelId=95, content="All you need to do is pick up the pen and begin.", createdAt="Tue Nov 02 2021 17:26:14", updatedAt="Sat Dec 11 2021 15:20:55")
    comment1368b = Comment(videoId=359, channelId=93, content="He had decided to accept his fate of accepting his fate.", createdAt="Tue Nov 23 2021 09:30:10", updatedAt="Sun Jul 25 2021 18:31:05")
    comment1370b = Comment(videoId=152, channelId=98, content="She looked at the masterpiece hanging in the museum but all she could think is that her five-year-old could do better.", createdAt="Sun May 09 2021 16:14:41", updatedAt="Thu Apr 29 2021 20:19:08")
    comment1371b = Comment(videoId=177, channelId=97, content="Today arrived with a crash of my car through the garage door.", createdAt="Sat Jan 22 2022 03:07:08", updatedAt="Mon Feb 21 2022 17:16:33")
    comment1372b = Comment(videoId=765, channelId=89, content="Various sea birds are elegant, but nothing is as elegant as a gliding pelican.", createdAt="Fri May 07 2021 02:03:18", updatedAt="Thu Jul 01 2021 03:00:37")
    comment1373b = Comment(videoId=184, channelId=85, content="He always wore his sunglasses at night.", createdAt="Tue Apr 13 2021 15:52:03", updatedAt="Mon Aug 09 2021 10:07:29")
    comment1374b = Comment(videoId=547, channelId=89, content="Greetings from the real universe.", createdAt="Mon Jun 21 2021 22:02:32", updatedAt="Thu Apr 15 2021 19:45:22")
    comment1375b = Comment(videoId=725, channelId=91, content="The fifty mannequin heads floating in the pool kind of freaked them out.", createdAt="Fri Apr 23 2021 15:54:50", updatedAt="Wed Dec 15 2021 22:45:23")
    comment1376b = Comment(videoId=500, channelId=91, content="The efficiency with which he paired the socks in the drawer was quite admirable.", createdAt="Thu Apr 22 2021 12:56:04", updatedAt="Sun Oct 03 2021 04:37:31")
    comment1377b = Comment(videoId=326, channelId=89, content="Sometimes I stare at a door or a wall and I wonder what is this reality, why am I alive, and what is this all about?", createdAt="Tue Sep 21 2021 13:00:44", updatedAt="Thu Aug 05 2021 20:40:56")
    comment1378b = Comment(videoId=234, channelId=88, content="She was too busy always talking about what she wanted to do to actually do any of it.", createdAt="Sat Nov 20 2021 00:37:17", updatedAt="Thu Aug 05 2021 16:25:27")
    comment1379b = Comment(videoId=151, channelId=88, content="Written warnings in instruction manuals are worthless since rabbits can't read.", createdAt="Sun Dec 26 2021 23:12:15", updatedAt="Fri Sep 17 2021 11:12:48")
    comment1380b = Comment(videoId=634, channelId=87, content="He turned in the research paper on Friday; otherwise, he would have not passed the class.", createdAt="Mon Aug 09 2021 15:11:14", updatedAt="Sat Apr 02 2022 03:27:56")
    comment1381b = Comment(videoId=380, channelId=97, content="I had a friend in high school named Rick Shaw, but he was fairly useless as a mode of transport.", createdAt="Thu Mar 31 2022 09:37:45", updatedAt="Mon Aug 09 2021 08:54:02")
    comment1382b = Comment(videoId=177, channelId=97, content="There should have been a time and a place, but this wasn't it.", createdAt="Sun Jun 20 2021 07:14:57", updatedAt="Wed Oct 27 2021 23:25:27")
    comment1383b = Comment(videoId=774, channelId=85, content="I was very proud of my nickname throughout high school but today- I couldn’t be any different to what my nickname was.", createdAt="Tue May 11 2021 00:08:47", updatedAt="Tue Jan 04 2022 00:09:52")
    comment1384b = Comment(videoId=402, channelId=96, content="He poured rocks in the dungeon of his mind.", createdAt="Sat Jul 17 2021 23:25:27", updatedAt="Tue May 18 2021 11:45:13")
    comment1386b = Comment(videoId=491, channelId=93, content="Patricia found the meaning of life in a bowl of Cheerios.", createdAt="Fri Jun 25 2021 09:25:01", updatedAt="Thu Nov 04 2021 14:11:26")
    comment1387b = Comment(videoId=78, channelId=90, content="Gwen had her best sleep ever on her new bed of nails.", createdAt="Thu Oct 21 2021 20:48:56", updatedAt="Wed Dec 01 2021 09:53:09")
    comment1388b = Comment(videoId=485, channelId=85, content="It caught him off guard that space smelled of seared steak.", createdAt="Fri May 14 2021 20:27:42", updatedAt="Mon May 31 2021 07:07:11")
    comment1389b = Comment(videoId=221, channelId=97, content="The clock within this blog and the clock on my laptop are 1 hour different from each other.", createdAt="Mon Mar 07 2022 16:10:42", updatedAt="Sat May 22 2021 06:08:23")
    comment1390b = Comment(videoId=30, channelId=98, content="More RVs were seen in the storage lot than at the campground.", createdAt="Fri Dec 31 2021 23:08:14", updatedAt="Sat Nov 27 2021 08:59:52")
    comment1391b = Comment(videoId=226, channelId=85, content="He was an introvert that extroverts seemed to love.", createdAt="Tue Jul 20 2021 12:00:40", updatedAt="Mon Jun 21 2021 13:36:45")
    comment1392b = Comment(videoId=616, channelId=89, content="In hopes of finding out the truth, he entered the one-room library.", createdAt="Sun Jan 02 2022 01:55:29", updatedAt="Tue Jun 01 2021 16:38:49")
    comment1393b = Comment(videoId=764, channelId=95, content="Last Friday I saw a spotted striped blue worm shake hands with a legless lizard.", createdAt="Mon Nov 29 2021 17:14:02", updatedAt="Mon Jan 10 2022 14:37:57")
    comment1394b = Comment(videoId=735, channelId=86, content="It was the first time he had ever seen someone cook dinner on an elephant.", createdAt="Thu Jul 29 2021 19:03:42", updatedAt="Tue Oct 05 2021 18:45:53")
    comment1395b = Comment(videoId=397, channelId=93, content="The wake behind the boat told of the past while the open sea for told life in the unknown future.", createdAt="Thu Feb 10 2022 19:12:34", updatedAt="Sun Oct 10 2021 12:56:00")
    comment1396b = Comment(videoId=356, channelId=86, content="He decided to live his life by the big beats manifesto.", createdAt="Sun Mar 27 2022 15:12:46", updatedAt="Fri Jan 28 2022 10:27:49")
    comment1397b = Comment(videoId=195, channelId=92, content="Today I heard something new and unmemorable.", createdAt="Sat Jan 29 2022 07:44:34", updatedAt="Fri Apr 16 2021 19:42:14")
    comment1398b = Comment(videoId=14, channelId=90, content="Blue sounded too cold at the time and yet it seemed to work for gin.", createdAt="Mon Jan 10 2022 02:22:52", updatedAt="Sat Jun 05 2021 19:55:52")
    comment1399b = Comment(videoId=361, channelId=95, content="Before he moved to the inner city, he had always believed that security complexes were psychological.", createdAt="Wed Jan 12 2022 04:51:19", updatedAt="Mon Jun 07 2021 03:45:40")
    comment1400b = Comment(videoId=94, channelId=88, content="There can never be too many cherries on an ice cream sundae.", createdAt="Fri Mar 11 2022 00:42:47", updatedAt="Fri Feb 25 2022 00:53:05")
    comment1401b = Comment(videoId=337, channelId=92, content="All she wanted was the answer, but she had no idea how much she would hate it.", createdAt="Sun Jul 04 2021 14:31:29", updatedAt="Thu Dec 02 2021 01:56:22")
    comment1402b = Comment(videoId=269, channelId=95, content="She hadn't had her cup of coffee, and that made things all the worse.", createdAt="Sun Sep 26 2021 13:14:17", updatedAt="Thu Feb 03 2022 22:45:56")
    comment1404b = Comment(videoId=487, channelId=92, content="Her scream silenced the rowdy teenagers.", createdAt="Thu Feb 24 2022 20:21:36", updatedAt="Tue Aug 17 2021 06:34:20")
    comment1406b = Comment(videoId=289, channelId=93, content="He picked up trash in his spare time to dump in his neighbor's yard.", createdAt="Wed Jan 26 2022 21:30:49", updatedAt="Thu Oct 28 2021 11:28:50")
    comment1407b = Comment(videoId=575, channelId=92, content="The gruff old man sat in the back of the bait shop grumbling to himself as he scooped out a handful of worms.", createdAt="Sat May 01 2021 21:02:55", updatedAt="Sat Apr 09 2022 08:50:31")
    comment1408b = Comment(videoId=485, channelId=86, content="It's important to remember to be aware of rampaging grizzly bears.", createdAt="Mon Jan 31 2022 19:25:13", updatedAt="Fri Jun 11 2021 04:37:18")
    comment1409b = Comment(videoId=13, channelId=91, content="The light that burns twice as bright burns half as long.", createdAt="Fri Jan 28 2022 03:32:28", updatedAt="Sat Feb 05 2022 01:18:30")
    comment1410b = Comment(videoId=596, channelId=90, content="It dawned on her that others could make her happier, but only she could make herself happy.", createdAt="Mon Apr 12 2021 20:51:34", updatedAt="Fri May 28 2021 20:10:23")
    comment1411b = Comment(videoId=450, channelId=95, content="I love bacon, beer, birds, and baboons.", createdAt="Wed Apr 21 2021 12:14:35", updatedAt="Wed May 26 2021 17:02:10")
    comment1412b = Comment(videoId=547, channelId=90, content="Today I bought a raincoat and wore it on a sunny day.", createdAt="Thu Oct 14 2021 23:58:14", updatedAt="Sun Jul 11 2021 11:28:39")
    comment1413b = Comment(videoId=114, channelId=90, content="She traveled because it cost the same as therapy and was a lot more enjoyable.", createdAt="Sun Jan 23 2022 22:25:10", updatedAt="Thu Feb 24 2022 12:23:00")
    comment1414b = Comment(videoId=249, channelId=89, content="He went back to the video to see what had been recorded and was shocked at what he saw.", createdAt="Tue Nov 16 2021 12:47:12", updatedAt="Sat Mar 19 2022 02:15:03")
    comment1415b = Comment(videoId=308, channelId=91, content="Gary didn't understand why Doug went upstairs to get one dollar bills when he invited him to go cow tipping.", createdAt="Sun Oct 10 2021 06:43:29", updatedAt="Sat Dec 25 2021 15:39:17")
    comment1418b = Comment(videoId=228, channelId=95, content="He stepped gingerly onto the bridge knowing that enchantment awaited on the other side.", createdAt="Thu Mar 10 2022 07:03:29", updatedAt="Sun Jun 27 2021 14:51:44")
    comment1419b = Comment(videoId=24, channelId=86, content="Shakespeare was a famous 17th-century diesel mechanic.", createdAt="Wed Jan 05 2022 05:54:26", updatedAt="Wed Dec 15 2021 18:55:06")
    comment1420b = Comment(videoId=759, channelId=95, content="Three years later, the coffin was still full of Jello.", createdAt="Fri Nov 05 2021 19:17:13", updatedAt="Fri Oct 29 2021 04:11:22")
    comment1421b = Comment(videoId=483, channelId=93, content="Every manager should be able to recite at least ten nursery rhymes backward.", createdAt="Tue Aug 03 2021 21:42:39", updatedAt="Fri Jul 16 2021 20:08:23")
    comment1422b = Comment(videoId=188, channelId=92, content="The fence was confused about whether it was supposed to keep things in or keep things out.", createdAt="Sun Jun 13 2021 23:23:36", updatedAt="Thu Feb 03 2022 19:04:24")
    comment1423b = Comment(videoId=543, channelId=98, content="Warm beer on a cold day isn't my idea of fun.", createdAt="Tue Jan 18 2022 15:57:01", updatedAt="Thu Mar 03 2022 03:40:53")
    comment1424b = Comment(videoId=594, channelId=97, content="The fish listened intently to what the frogs had to say.", createdAt="Tue Mar 22 2022 23:49:42", updatedAt="Sat Oct 23 2021 22:10:50")
    comment1425b = Comment(videoId=400, channelId=85, content="Jenny made the announcement that her baby was an alien.", createdAt="Sun Mar 20 2022 17:23:33", updatedAt="Sat Jul 17 2021 22:17:41")
    comment1426b = Comment(videoId=309, channelId=87, content="The lake is a long way from here.", createdAt="Sat Apr 24 2021 04:55:14", updatedAt="Tue Apr 13 2021 22:16:40")
    comment1427b = Comment(videoId=336, channelId=87, content="They throw cabbage that turns your brain into emotional baggage.", createdAt="Fri Feb 04 2022 15:23:07", updatedAt="Sat Mar 12 2022 01:33:28")
    comment1428b = Comment(videoId=373, channelId=97, content="It's never comforting to know that your fate depends on something as unpredictable as the popping of corn.", createdAt="Mon Jul 26 2021 19:15:37", updatedAt="Tue Nov 23 2021 06:37:37")
    comment1429b = Comment(videoId=718, channelId=86, content="If my calculator had a history, it would be more embarrassing than my browser history.", createdAt="Sun May 02 2021 02:15:16", updatedAt="Tue Aug 10 2021 17:57:48")
    comment1430b = Comment(videoId=296, channelId=94, content="Doris enjoyed tapping her nails on the table to annoy everyone.", createdAt="Mon Sep 06 2021 07:08:14", updatedAt="Thu Oct 28 2021 09:40:14")
    comment1431b = Comment(videoId=361, channelId=94, content="I know many children ask for a pony, but I wanted a bicycle with rockets strapped to it.", createdAt="Thu Jul 08 2021 05:35:19", updatedAt="Sat Apr 09 2022 00:58:49")
    comment1432b = Comment(videoId=487, channelId=93, content="Lucifer was surprised at the amount of life at Death Valley.", createdAt="Fri Dec 10 2021 04:59:54", updatedAt="Tue Oct 05 2021 18:23:23")
    comment1433b = Comment(videoId=745, channelId=92, content="Martha came to the conclusion that shake weights are a great gift for any occasion.", createdAt="Sun May 09 2021 03:49:21", updatedAt="Sat Aug 07 2021 14:22:07")
    comment1434b = Comment(videoId=742, channelId=90, content="Kevin embraced his ability to be at the wrong place at the wrong time.", createdAt="Wed Mar 23 2022 17:25:35", updatedAt="Tue Jun 29 2021 12:14:05")
    comment1435b = Comment(videoId=761, channelId=86, content="She only paints with bold colors; she does not like pastels.", createdAt="Tue May 11 2021 03:30:43", updatedAt="Wed Mar 23 2022 15:31:04")
    comment1436b = Comment(videoId=69, channelId=98, content="Sometimes I stare at a door or a wall and I wonder what is this reality, why am I alive, and what is this all about?", createdAt="Wed Jun 02 2021 08:45:36", updatedAt="Wed Feb 09 2022 07:30:11")
    comment1437b = Comment(videoId=699, channelId=93, content="Pair your designer cowboy hat with scuba gear for a memorable occasion.", createdAt="Sat Nov 27 2021 05:21:11", updatedAt="Sun Mar 20 2022 22:45:18")
    comment1438b = Comment(videoId=630, channelId=91, content="Green should have smelled more tranquil, but somehow it just tasted rotten.", createdAt="Wed Nov 24 2021 08:44:01", updatedAt="Sat Sep 11 2021 21:29:09")
    comment1439b = Comment(videoId=109, channelId=92, content="I was starting to worry that my pet turtle could tell what I was thinking.", createdAt="Wed May 12 2021 15:30:58", updatedAt="Mon Dec 13 2021 17:26:29")
    comment1440b = Comment(videoId=327, channelId=96, content="Jim liked driving around town with his hazard lights on.", createdAt="Tue Oct 26 2021 21:12:21", updatedAt="Thu May 20 2021 03:53:44")
    comment1441b = Comment(videoId=754, channelId=89, content="The heat", createdAt="Tue May 11 2021 11:31:10", updatedAt="Sun Feb 20 2022 12:06:22")
    comment1442b = Comment(videoId=125, channelId=98, content="He hated that he loved what she hated about hate.", createdAt="Thu Dec 16 2021 00:02:42", updatedAt="Wed Dec 29 2021 01:12:07")
    comment1443b = Comment(videoId=328, channelId=97, content="The tears of a clown make my lipstick run, but my shower cap is still intact.", createdAt="Fri Jun 04 2021 21:33:32", updatedAt="Fri Oct 01 2021 21:52:10")
    comment1444b = Comment(videoId=482, channelId=97, content="If you like tuna and tomato sauce, try combining the two, it’s really not as bad as it sounds.", createdAt="Fri Jun 18 2021 02:35:24", updatedAt="Tue Jun 29 2021 07:02:46")
    comment1445b = Comment(videoId=577, channelId=94, content="Having no hair made him look even hairier.", createdAt="Fri Jul 02 2021 13:25:49", updatedAt="Sat Nov 06 2021 12:14:46")
    comment1446b = Comment(videoId=10, channelId=93, content="Let me help you with your baggage.", createdAt="Thu Dec 09 2021 11:37:03", updatedAt="Fri Jan 14 2022 06:21:21")
    comment1447b = Comment(videoId=412, channelId=87, content="Please put on these earmuffs because I can't you hear.", createdAt="Wed Jun 09 2021 06:37:16", updatedAt="Wed Mar 16 2022 19:57:17")
    comment1448b = Comment(videoId=104, channelId=86, content="He dreamed of eating green apples with worms.", createdAt="Tue Jul 06 2021 01:25:25", updatedAt="Tue Oct 19 2021 18:18:04")
    comment1449b = Comment(videoId=161, channelId=85, content="Nancy thought the best way to create a welcoming home was to line it with barbed wire.", createdAt="Sat Mar 12 2022 04:31:02", updatedAt="Wed Oct 13 2021 05:47:56")
    comment1450b = Comment(videoId=325, channelId=97, content="As he waited for the shower to warm, he noticed that he could hear water change temperature.", createdAt="Tue Jan 18 2022 04:10:54", updatedAt="Wed Jun 02 2021 15:32:36")
    comment1451b = Comment(videoId=336, channelId=91, content="They looked up at the sky and saw a million stars.", createdAt="Sun Sep 26 2021 08:42:20", updatedAt="Tue Jun 15 2021 23:43:55")
    comment1452b = Comment(videoId=453, channelId=97, content="Nancy decided to make the porta-potty her home.", createdAt="Sat Nov 20 2021 21:07:39", updatedAt="Sat Feb 05 2022 13:43:52")
    comment1453b = Comment(videoId=515, channelId=90, content="Each person who knows you has a different perception of who you are.", createdAt="Thu Aug 19 2021 17:32:04", updatedAt="Mon Aug 16 2021 10:00:41")
    comment1454b = Comment(videoId=607, channelId=94, content="I just wanted to tell you I could see the love you have for your child by the way you look at her.", createdAt="Sat Sep 11 2021 18:47:48", updatedAt="Tue Jun 01 2021 16:28:27")
    comment1455b = Comment(videoId=539, channelId=91, content="This is a Japanese doll.", createdAt="Wed Oct 13 2021 19:52:39", updatedAt="Wed Feb 09 2022 17:54:20")
    comment1457b = Comment(videoId=150, channelId=95, content="Number of Sentences:", createdAt="Wed Aug 11 2021 09:35:28", updatedAt="Tue Jan 04 2022 05:39:47")
    comment1458b = Comment(videoId=309, channelId=92, content="50", createdAt="Thu Mar 03 2022 18:47:28", updatedAt="Tue Nov 30 2021 16:51:21")
    comment1459b = Comment(videoId=6, channelId=90, content="The father handed each child a roadmap at the beginning of the 2-day road trip and explained it was so they could find their way home.", createdAt="Sun May 16 2021 09:31:40", updatedAt="Sun Nov 14 2021 01:54:20")
    comment1460b = Comment(videoId=297, channelId=88, content="She had convinced her kids that any mushroom found on the ground would kill them if they touched it.", createdAt="Fri May 07 2021 06:15:02", updatedAt="Mon Aug 16 2021 04:00:04")
    comment1461b = Comment(videoId=31, channelId=88, content="When money was tight, he'd get his lunch money from the local wishing well.", createdAt="Wed Sep 01 2021 23:05:35", updatedAt="Fri Oct 08 2021 00:12:22")
    comment1462b = Comment(videoId=177, channelId=90, content="He invested some skill points in Charisma and Strength.", createdAt="Fri Oct 29 2021 11:49:19", updatedAt="Fri Aug 13 2021 18:53:51")
    comment1463b = Comment(videoId=612, channelId=95, content="Jenny made the announcement that her baby was an alien.", createdAt="Mon Jan 31 2022 19:45:04", updatedAt="Mon Feb 21 2022 00:50:51")
    comment1464b = Comment(videoId=548, channelId=90, content="On each full moon", createdAt="Mon Nov 15 2021 10:31:44", updatedAt="Sat Oct 16 2021 19:03:12")
    comment1465b = Comment(videoId=698, channelId=90, content="Situps are a terrible way to end your day.", createdAt="Sun Jan 16 2022 13:44:35", updatedAt="Mon Jun 07 2021 07:30:56")
    comment1466b = Comment(videoId=45, channelId=87, content="At that moment he wasn't listening to music, he was living an experience.", createdAt="Wed Jun 23 2021 01:53:20", updatedAt="Mon May 24 2021 11:00:02")
    comment1467b = Comment(videoId=395, channelId=96, content="I never knew what hardship looked like until it started raining bowling balls.", createdAt="Mon Feb 21 2022 14:57:21", updatedAt="Wed Apr 21 2021 09:35:31")
    comment1468b = Comment(videoId=644, channelId=95, content="The door slammed on the watermelon.", createdAt="Tue Dec 21 2021 21:40:35", updatedAt="Mon Jun 21 2021 10:14:15")
    comment1469b = Comment(videoId=422, channelId=85, content="That was how he came to win $1 million.", createdAt="Wed Aug 11 2021 17:21:19", updatedAt="Wed Feb 16 2022 15:51:44")
    comment1470b = Comment(videoId=686, channelId=92, content="People who insist on picking their teeth with their elbows are so annoying!", createdAt="Tue Sep 21 2021 08:22:25", updatedAt="Fri Aug 13 2021 23:24:41")
    comment1471b = Comment(videoId=226, channelId=89, content="He had a vague sense that trees gave birth to dinosaurs.", createdAt="Sun Apr 18 2021 10:31:22", updatedAt="Wed Feb 09 2022 06:15:16")
    comment1472b = Comment(videoId=580, channelId=97, content="Pink horses galloped across the sea.", createdAt="Mon Oct 25 2021 05:16:10", updatedAt="Sat Oct 23 2021 20:57:49")
    comment1473b = Comment(videoId=389, channelId=90, content="Everyone says they love nature until they realize how dangerous she can be.", createdAt="Sat Jun 12 2021 22:17:51", updatedAt="Wed Dec 15 2021 01:25:32")
    comment1474b = Comment(videoId=750, channelId=90, content="His thought process was on so many levels that he gave himself a phobia of heights.", createdAt="Thu Dec 23 2021 10:33:38", updatedAt="Wed Apr 14 2021 21:32:33")
    comment1475b = Comment(videoId=608, channelId=86, content="He kept telling himself that one day it would all somehow make sense.", createdAt="Tue Sep 14 2021 03:39:31", updatedAt="Sun Feb 20 2022 15:08:34")
    comment1476b = Comment(videoId=614, channelId=97, content="Peanuts don't grow on trees, but cashews do.", createdAt="Mon Jan 31 2022 22:48:32", updatedAt="Fri Oct 01 2021 06:05:34")
    comment1477b = Comment(videoId=359, channelId=96, content="The lake is a long way from here.", createdAt="Mon Jun 07 2021 21:00:05", updatedAt="Sun May 02 2021 17:48:02")
    comment1478b = Comment(videoId=447, channelId=86, content="There are few things better in life than a slice of pie.", createdAt="Thu Aug 19 2021 22:38:51", updatedAt="Sun Nov 21 2021 08:49:28")
    comment1479b = Comment(videoId=3, channelId=93, content="He found the end of the rainbow and was surprised at what he found there.", createdAt="Fri Nov 05 2021 02:16:16", updatedAt="Thu Mar 24 2022 22:34:50")
    comment1480b = Comment(videoId=774, channelId=87, content="A kangaroo is really just a rabbit on steroids.", createdAt="Tue May 25 2021 18:35:28", updatedAt="Sat Jan 08 2022 22:00:09")
    comment1481b = Comment(videoId=691, channelId=92, content="I was very proud of my nickname throughout high school but today- I couldn’t be any different to what my nickname was.", createdAt="Thu Nov 11 2021 09:07:39", updatedAt="Sun Jan 09 2022 17:09:26")
    comment1482b = Comment(videoId=386, channelId=96, content="The thunderous roar of the jet overhead confirmed her worst fears.", createdAt="Sat May 08 2021 00:58:22", updatedAt="Fri Apr 08 2022 09:05:31")
    comment1483b = Comment(videoId=592, channelId=93, content="Homesickness became contagious in the young campers' cabin.", createdAt="Thu Dec 02 2021 07:42:13", updatedAt="Sat Sep 18 2021 06:08:09")
    comment1484b = Comment(videoId=329, channelId=92, content="She hadn't had her cup of coffee, and that made things all the worse.", createdAt="Thu Apr 22 2021 13:35:33", updatedAt="Wed Jun 16 2021 18:37:20")
    comment1485b = Comment(videoId=143, channelId=91, content="She can live her life however she wants as long as she listens to what I have to say.", createdAt="Tue Mar 08 2022 03:12:02", updatedAt="Tue Sep 14 2021 12:40:30")
    comment1486b = Comment(videoId=56, channelId=93, content="In that instant, everything changed.", createdAt="Thu Jun 10 2021 23:17:00", updatedAt="Wed Jul 07 2021 08:25:00")
    comment1487b = Comment(videoId=287, channelId=88, content="He learned the important lesson that a picnic at the beach on a windy day is a bad idea.", createdAt="Fri Dec 24 2021 16:21:17", updatedAt="Sat Sep 04 2021 20:56:23")
    comment1488b = Comment(videoId=97, channelId=96, content="He's in a boy band which doesn't make much sense for a snake.", createdAt="Tue Mar 15 2022 04:15:14", updatedAt="Tue Nov 23 2021 18:59:12")
    comment1489b = Comment(videoId=381, channelId=88, content="She did not cheat on the test, for it was not the right thing to do.", createdAt="Tue Nov 30 2021 06:08:47", updatedAt="Sun Aug 01 2021 02:54:05")
    comment1490b = Comment(videoId=615, channelId=89, content="The beauty of the sunset was obscured by the industrial cranes.", createdAt="Sat Jan 08 2022 21:21:34", updatedAt="Wed Apr 14 2021 03:24:32")
    comment1491b = Comment(videoId=629, channelId=92, content="The secret ingredient to his wonderful life was crime.", createdAt="Fri Mar 25 2022 04:06:18", updatedAt="Tue Jan 11 2022 02:50:16")
    comment1492b = Comment(videoId=731, channelId=97, content="They got there early, and they got really good seats.", createdAt="Tue Sep 28 2021 19:35:17", updatedAt="Fri Aug 06 2021 23:59:34")
    comment1493b = Comment(videoId=652, channelId=96, content="The tart lemonade quenched her thirst, but not her longing.", createdAt="Sun Nov 28 2021 16:16:02", updatedAt="Fri Mar 04 2022 20:03:02")
    comment1494b = Comment(videoId=622, channelId=94, content="Pat ordered a ghost pepper pie.", createdAt="Sun Dec 19 2021 16:58:24", updatedAt="Fri Dec 03 2021 08:10:46")
    comment1495b = Comment(videoId=769, channelId=97, content="He fumbled in the darkness looking for the light switch, but when he finally found it there was someone already there.", createdAt="Fri May 28 2021 12:28:15", updatedAt="Sat Jun 12 2021 22:28:33")
    comment1496b = Comment(videoId=715, channelId=95, content="Every manager should be able to recite at least ten nursery rhymes backward.", createdAt="Tue Jul 13 2021 20:19:35", updatedAt="Thu Feb 10 2022 17:16:23")
    comment1497b = Comment(videoId=513, channelId=91, content="At that moment I was the most fearsome weasel in the entire swamp.", createdAt="Mon Jan 17 2022 16:39:42", updatedAt="Fri Sep 10 2021 09:27:52")
    comment1498b = Comment(videoId=125, channelId=96, content="The skeleton had skeletons of his own in the closet.", createdAt="Sun Dec 19 2021 11:23:13", updatedAt="Wed May 26 2021 23:58:29")
    comment1499b = Comment(videoId=708, channelId=91, content="The team members were hard to tell apart since they all wore their hair in a ponytail.", createdAt="Mon Jul 19 2021 13:08:15", updatedAt="Wed Feb 16 2022 16:53:33")
    comment1500b = Comment(videoId=34, channelId=93, content="The fish dreamed of escaping the fishbowl and into the toilet where he saw his friend go.", createdAt="Sat Jul 17 2021 18:18:36", updatedAt="Thu Sep 09 2021 06:16:06")
    comment1501b = Comment(videoId=14, channelId=89, content="Jason didn’t understand why his parents wouldn’t let him sell his little sister at the garage sale.", createdAt="Sat Jul 24 2021 20:03:03", updatedAt="Thu Jul 22 2021 07:59:25")
    comment1502b = Comment(videoId=737, channelId=87, content="We have young kids who often walk into our room at night for various reasons including clowns in the closet.", createdAt="Sun Oct 17 2021 11:17:34", updatedAt="Fri Nov 12 2021 22:51:52")
    comment1503b = Comment(videoId=637, channelId=88, content="He drank life before spitting it out.", createdAt="Mon Aug 02 2021 08:14:05", updatedAt="Sat Mar 19 2022 15:54:34")
    comment1504b = Comment(videoId=49, channelId=94, content="He never understood why what, when, and where left out who.", createdAt="Fri May 28 2021 09:36:44", updatedAt="Sat Oct 16 2021 21:11:19")
    comment1505b = Comment(videoId=652, channelId=92, content="Being unacquainted with the chief raccoon was harming his prospects for promotion.", createdAt="Sat Nov 27 2021 23:11:29", updatedAt="Mon May 31 2021 03:23:02")
    comment1506b = Comment(videoId=434, channelId=86, content="Nothing is as cautiously cuddly as a pet porcupine.", createdAt="Fri Jul 23 2021 04:48:46", updatedAt="Sat Apr 02 2022 09:31:02")
    comment1507b = Comment(videoId=625, channelId=88, content="She was disgusted he couldn’t tell the difference between lemonade and limeade.", createdAt="Mon May 03 2021 17:57:57", updatedAt="Mon Jul 05 2021 08:46:32")
    comment1508b = Comment(videoId=678, channelId=94, content="There are over 500 starfish in the bathroom drawer.", createdAt="Fri Oct 22 2021 07:20:44", updatedAt="Thu Jan 20 2022 09:35:23")
    comment1509b = Comment(videoId=594, channelId=91, content="The light in his life was actually a fire burning all around him.", createdAt="Thu Jan 13 2022 02:21:45", updatedAt="Thu Sep 16 2021 14:54:53")
    comment1510b = Comment(videoId=447, channelId=95, content="Everyone was busy, so I went to the movie alone.", createdAt="Tue Aug 31 2021 05:30:58", updatedAt="Wed Oct 27 2021 00:25:56")
    comment1511b = Comment(videoId=239, channelId=98, content="He had a wall full of masks so she could wear a different face every day.", createdAt="Wed Feb 23 2022 08:33:51", updatedAt="Mon Aug 09 2021 16:03:45")
    comment1512b = Comment(videoId=568, channelId=91, content="My biggest joy is roasting almonds while stalking prey.", createdAt="Thu Jul 22 2021 09:09:36", updatedAt="Sun Feb 13 2022 20:13:41")
    comment1513b = Comment(videoId=468, channelId=95, content="The busker hoped that the people passing by would throw money, but they threw tomatoes instead, so he exchanged his hat for a juicer.", createdAt="Sat Jul 03 2021 17:25:51", updatedAt="Fri Jan 07 2022 05:14:37")
    comment1514b = Comment(videoId=51, channelId=90, content="The clouds formed beautiful animals in the sky that eventually created a tornado to wreak havoc.", createdAt="Wed Jun 23 2021 08:21:44", updatedAt="Sat Sep 11 2021 21:21:48")
    comment1515b = Comment(videoId=712, channelId=93, content="She used her own hair in the soup to give it more flavor.", createdAt="Mon Jan 17 2022 01:24:22", updatedAt="Sun Aug 15 2021 04:38:45")
    comment1516b = Comment(videoId=83, channelId=91, content="It's difficult to understand the lengths he'd go to remain short.", createdAt="Mon May 03 2021 14:02:02", updatedAt="Wed Sep 08 2021 00:51:38")
    comment1517b = Comment(videoId=100, channelId=86, content="I would be delighted if the sea were full of cucumber juice.", createdAt="Wed Dec 22 2021 15:50:19", updatedAt="Sun Oct 17 2021 15:47:06")
    comment1518b = Comment(videoId=746, channelId=94, content="The tattered work gloves speak of the many hours of hard labor he endured throughout his life.", createdAt="Mon May 03 2021 06:36:03", updatedAt="Mon May 03 2021 17:41:24")
    comment1519b = Comment(videoId=645, channelId=94, content="The trick to getting kids to eat anything is to put catchup on it.", createdAt="Fri Aug 27 2021 17:24:51", updatedAt="Sun Sep 05 2021 14:39:13")
    comment1520b = Comment(videoId=47, channelId=94, content="At that moment she realized she had a sixth sense.", createdAt="Sun Mar 27 2022 11:56:31", updatedAt="Tue Aug 31 2021 07:57:30")
    comment1521b = Comment(videoId=386, channelId=85, content="The random sentence generator generated a random sentence about a random sentence.", createdAt="Wed Jun 16 2021 02:06:14", updatedAt="Fri Jun 11 2021 09:06:13")
    comment1522b = Comment(videoId=748, channelId=98, content="Patricia found the meaning of life in a bowl of Cheerios.", createdAt="Tue Mar 22 2022 15:23:51", updatedAt="Thu May 06 2021 15:34:47")
    comment1523b = Comment(videoId=130, channelId=97, content="The llama couldn't resist trying the lemonade.", createdAt="Wed Nov 03 2021 02:40:17", updatedAt="Fri Apr 01 2022 17:45:24")
    comment1524b = Comment(videoId=777, channelId=91, content="Wisdom is easily acquired when hiding under the bed with a saucepan on your head.", createdAt="Tue Jul 06 2021 23:31:24", updatedAt="Wed Jan 05 2022 12:03:15")
    comment1525b = Comment(videoId=660, channelId=98, content="The beauty of the sunset was obscured by the industrial cranes.", createdAt="Tue May 18 2021 07:00:34", updatedAt="Mon Apr 04 2022 14:16:27")
    comment1526b = Comment(videoId=304, channelId=86, content="It was a really good Monday for being a Saturday.", createdAt="Tue Oct 05 2021 04:50:43", updatedAt="Mon Jan 03 2022 09:08:41")
    comment1527b = Comment(videoId=550, channelId=92, content="Two seats were vacant.", createdAt="Tue Nov 09 2021 08:40:54", updatedAt="Fri Aug 13 2021 15:10:00")
    comment1528b = Comment(videoId=556, channelId=97, content="The teens wondered what was kept in the red shed on the far edge of the school grounds.", createdAt="Thu Jan 06 2022 23:15:43", updatedAt="Sun Aug 22 2021 23:55:45")
    comment1529b = Comment(videoId=756, channelId=97, content="The fence was confused about whether it was supposed to keep things in or keep things out.", createdAt="Sat Jan 15 2022 08:22:14", updatedAt="Wed May 05 2021 11:48:24")
    comment1530b = Comment(videoId=275, channelId=95, content="The newly planted trees were held up by wooden frames in hopes they could survive the next storm.", createdAt="Sun Jul 25 2021 11:47:07", updatedAt="Mon Dec 13 2021 13:27:19")
    comment1531b = Comment(videoId=50, channelId=96, content="Situps are a terrible way to end your day.", createdAt="Wed Apr 14 2021 08:50:56", updatedAt="Wed Sep 22 2021 22:40:47")
    comment1532b = Comment(videoId=243, channelId=91, content="She always had an interesting perspective on why the world must be flat.", createdAt="Thu Jun 17 2021 16:16:09", updatedAt="Wed Aug 11 2021 14:17:15")
    comment1533b = Comment(videoId=684, channelId=90, content="He loved eating his bananas in hot dog buns.", createdAt="Sat Oct 23 2021 12:19:53", updatedAt="Thu Sep 16 2021 06:40:18")
    comment1534b = Comment(videoId=198, channelId=93, content="He was the only member of the club who didn't like plum pudding.", createdAt="Wed May 12 2021 20:22:47", updatedAt="Fri Nov 05 2021 05:11:37")
    comment1535b = Comment(videoId=69, channelId=96, content="Plans for this weekend include turning wine into water.", createdAt="Mon Feb 14 2022 12:18:48", updatedAt="Wed Apr 28 2021 04:48:40")
    comment1536b = Comment(videoId=219, channelId=96, content="When money was tight, he'd get his lunch money from the local wishing well.", createdAt="Wed Apr 14 2021 19:05:44", updatedAt="Thu Mar 17 2022 02:20:28")
    comment1537b = Comment(videoId=776, channelId=97, content="The lyrics of the song sounded like fingernails on a chalkboard.", createdAt="Tue May 25 2021 08:09:02", updatedAt="Fri Jul 23 2021 15:13:53")
    comment1538b = Comment(videoId=664, channelId=90, content="He had concluded that pigs must be able to fly in Hog Heaven.", createdAt="Mon May 24 2021 10:49:13", updatedAt="Mon May 31 2021 12:06:52")
    comment1539b = Comment(videoId=404, channelId=95, content="She cried diamonds.", createdAt="Sun May 23 2021 02:57:04", updatedAt="Wed Mar 16 2022 07:49:24")
    comment1540b = Comment(videoId=390, channelId=97, content="You'll see the rainbow bridge after it rains cats and dogs.", createdAt="Sat Oct 16 2021 17:38:11", updatedAt="Mon Feb 28 2022 23:58:53")
    comment1541b = Comment(videoId=43, channelId=94, content="The rusty nail stood erect, angled at a 45-degree angle, just waiting for the perfect barefoot to come along.", createdAt="Mon Sep 06 2021 18:26:51", updatedAt="Fri May 21 2021 19:30:55")
    comment1543b = Comment(videoId=762, channelId=89, content="25 years later, she still regretted that specific moment.", createdAt="Mon May 31 2021 12:52:35", updatedAt="Fri Apr 16 2021 20:32:36")
    comment1544b = Comment(videoId=536, channelId=85, content="Most shark attacks occur about 10 feet from the beach since that's where the people are.", createdAt="Fri Jun 11 2021 15:08:59", updatedAt="Wed Sep 15 2021 02:11:41")
    comment1545b = Comment(videoId=747, channelId=85, content="As time wore on, simple dog commands turned into full paragraphs explaining why the dog couldn’t do something.", createdAt="Sun Apr 18 2021 04:28:50", updatedAt="Thu Feb 03 2022 00:09:44")
    comment1546b = Comment(videoId=406, channelId=98, content="Getting up at dawn is for the birds.", createdAt="Wed Jul 14 2021 11:00:11", updatedAt="Sun Jul 11 2021 22:28:55")
    comment1548b = Comment(videoId=129, channelId=88, content="Car safety systems have come a long way, but he was out to prove they could be outsmarted.", createdAt="Mon Oct 25 2021 12:25:14", updatedAt="Sun May 16 2021 03:51:40")
    comment1549b = Comment(videoId=524, channelId=96, content="As the asteroid hurtled toward earth, Becky was upset her dentist appointment had been canceled.", createdAt="Tue Mar 08 2022 20:26:21", updatedAt="Sat Jan 22 2022 08:27:16")
    comment1550b = Comment(videoId=757, channelId=92, content="Despite multiple complications and her near-death experience", createdAt="Fri Aug 27 2021 09:27:51", updatedAt="Wed Feb 23 2022 06:32:55")
    comment1551b = Comment(videoId=608, channelId=88, content="The sign said there was road work ahead so he decided to speed up.", createdAt="Thu Jul 08 2021 23:46:23", updatedAt="Sun Oct 31 2021 05:03:34")
    comment1552b = Comment(videoId=532, channelId=88, content="His son quipped that power bars were nothing more than adult candy bars.", createdAt="Mon Oct 25 2021 07:08:47", updatedAt="Wed Dec 15 2021 20:41:22")
    comment1553b = Comment(videoId=288, channelId=89, content="The mysterious diary records the voice.", createdAt="Tue Jul 20 2021 01:41:31", updatedAt="Mon Mar 07 2022 18:01:32")
    comment1554b = Comment(videoId=525, channelId=86, content="Mary realized if her calculator had a history, it would be more embarrassing than her computer browser history.", createdAt="Wed Feb 02 2022 09:29:27", updatedAt="Sat Jul 03 2021 03:22:47")
    comment1555b = Comment(videoId=376, channelId=94, content="The light that burns twice as bright burns half as long.", createdAt="Sat Nov 13 2021 06:48:42", updatedAt="Wed Jul 28 2021 01:00:39")
    comment1556b = Comment(videoId=289, channelId=95, content="He used to get confused between soldiers and shoulders, but as a military man, he now soldiers responsibility.", createdAt="Sun Aug 01 2021 12:23:18", updatedAt="Fri Aug 06 2021 21:15:57")
    comment1557b = Comment(videoId=141, channelId=89, content="Mom didn’t understand why no one else wanted a hot tub full of jello.", createdAt="Sat Jul 03 2021 09:55:46", updatedAt="Wed May 05 2021 22:16:57")
    comment1558b = Comment(videoId=237, channelId=89, content="I would have gotten the promotion, but my attendance wasn’t good enough.", createdAt="Tue Feb 08 2022 10:04:07", updatedAt="Tue May 04 2021 02:41:49")
    comment1560b = Comment(videoId=457, channelId=94, content="She did not cheat on the test, for it was not the right thing to do.", createdAt="Sat Sep 11 2021 12:50:35", updatedAt="Thu Jan 27 2022 21:23:41")
    comment1561b = Comment(videoId=623, channelId=93, content="The fifty mannequin heads floating in the pool kind of freaked them out.", createdAt="Fri Dec 10 2021 01:39:44", updatedAt="Fri Jun 04 2021 14:58:00")
    comment1562b = Comment(videoId=730, channelId=95, content="Various sea birds are elegant, but nothing is as elegant as a gliding pelican.", createdAt="Fri Aug 27 2021 10:46:09", updatedAt="Wed Oct 27 2021 06:43:52")
    comment1563b = Comment(videoId=718, channelId=94, content="They got there early, and they got really good seats.", createdAt="Fri Nov 26 2021 08:47:00", updatedAt="Tue Nov 23 2021 04:35:21")
    comment1564b = Comment(videoId=488, channelId=87, content="Tom got a small piece of pie.", createdAt="Thu Jan 20 2022 20:02:34", updatedAt="Tue Mar 01 2022 13:51:29")
    comment1565b = Comment(videoId=270, channelId=96, content="Excitement replaced fear until the final moment.", createdAt="Mon Sep 20 2021 05:28:05", updatedAt="Mon Mar 21 2022 15:09:16")
    comment1566b = Comment(videoId=200, channelId=92, content="I love eating toasted cheese and tuna sandwiches.", createdAt="Sun Feb 27 2022 21:13:30", updatedAt="Tue Nov 09 2021 19:38:55")
    comment1567b = Comment(videoId=323, channelId=92, content="She folded her handkerchief neatly.", createdAt="Fri Nov 26 2021 04:28:32", updatedAt="Tue Feb 01 2022 13:23:20")
    comment1568b = Comment(videoId=73, channelId=96, content="She wore green lipstick like a fashion icon.", createdAt="Sat Sep 11 2021 12:32:33", updatedAt="Wed Oct 13 2021 19:22:36")
    comment1569b = Comment(videoId=429, channelId=98, content="I liked their first two albums but changed my mind after that charity gig.", createdAt="Tue Apr 27 2021 14:46:11", updatedAt="Wed Apr 21 2021 13:21:29")
    comment1570b = Comment(videoId=657, channelId=85, content="Everyone was curious about the large white blimp that appeared overnight.", createdAt="Thu Feb 10 2022 16:23:00", updatedAt="Wed Dec 22 2021 00:52:52")
    comment1571b = Comment(videoId=357, channelId=86, content="That is an appealing treasure map that I can't read.", createdAt="Tue Dec 28 2021 01:43:52", updatedAt="Sat Feb 05 2022 13:25:55")
    comment1572b = Comment(videoId=403, channelId=86, content="The shark-infested South Pine channel was the only way in or out.", createdAt="Tue Sep 07 2021 00:41:04", updatedAt="Thu Oct 14 2021 03:47:18")
    comment1573b = Comment(videoId=355, channelId=87, content="Cursive writing is the best way to build a race track.", createdAt="Tue Dec 21 2021 15:15:15", updatedAt="Wed Dec 22 2021 09:47:47")
    comment1574b = Comment(videoId=420, channelId=95, content="The father died during childbirth.", createdAt="Mon Nov 22 2021 04:02:52", updatedAt="Wed Aug 25 2021 12:12:03")
    comment1575b = Comment(videoId=741, channelId=88, content="The bullet pierced the window shattering it before missing Danny's head by mere millimeters.", createdAt="Fri May 28 2021 21:17:02", updatedAt="Sun Oct 10 2021 14:47:41")
    comment1576b = Comment(videoId=695, channelId=89, content="Don't step on the broken glass.", createdAt="Sat Aug 21 2021 01:17:23", updatedAt="Fri Dec 03 2021 18:23:40")
    comment1577b = Comment(videoId=545, channelId=92, content="She opened up her third bottle of wine of the night.", createdAt="Tue Oct 05 2021 23:22:01", updatedAt="Fri Nov 19 2021 04:56:05")
    comment1578b = Comment(videoId=646, channelId=88, content="My biggest joy is roasting almonds while stalking prey.", createdAt="Wed Sep 01 2021 14:53:57", updatedAt="Wed Mar 16 2022 01:33:35")
    comment1579b = Comment(videoId=443, channelId=94, content="She saw the brake lights, but not in time.", createdAt="Fri Oct 15 2021 23:32:51", updatedAt="Thu Jul 01 2021 00:08:25")
    comment1580b = Comment(videoId=345, channelId=91, content="Today I heard something new and unmemorable.", createdAt="Sat Apr 17 2021 08:18:08", updatedAt="Fri Jun 25 2021 10:54:05")
    comment1581b = Comment(videoId=465, channelId=97, content="Baby wipes are made of chocolate stardust.", createdAt="Mon Jul 12 2021 06:37:59", updatedAt="Sun May 09 2021 04:32:00")
    comment1582b = Comment(videoId=395, channelId=91, content="Normal activities took extraordinary amounts of concentration at the high altitude.", createdAt="Tue Jun 22 2021 11:53:50", updatedAt="Mon Aug 02 2021 17:51:21")
    comment1583b = Comment(videoId=418, channelId=91, content="There was no ice cream in the freezer, nor did they have money to go to the store.", createdAt="Mon Apr 04 2022 14:42:31", updatedAt="Wed Jun 02 2021 10:13:30")
    comment1584b = Comment(videoId=705, channelId=87, content="He was disappointed when he found the beach to be so sandy and the sun so sunny.", createdAt="Sat Mar 05 2022 18:49:24", updatedAt="Thu Dec 16 2021 03:57:23")
    comment1585b = Comment(videoId=308, channelId=86, content="The dead trees waited to be ignited by the smallest spark and seek their revenge.", createdAt="Sun Nov 14 2021 09:28:36", updatedAt="Tue Oct 26 2021 11:16:59")
    comment1586b = Comment(videoId=394, channelId=91, content="Happiness can be found in the depths of chocolate pudding.", createdAt="Sat May 15 2021 16:06:33", updatedAt="Sun Feb 27 2022 15:41:07")
    comment1587b = Comment(videoId=148, channelId=92, content="He fumbled in the darkness looking for the light switch, but when he finally found it there was someone already there.", createdAt="Wed Oct 20 2021 14:20:55", updatedAt="Sun May 09 2021 22:35:51")
    comment1588b = Comment(videoId=774, channelId=97, content="Three years later, the coffin was still full of Jello.", createdAt="Sat Feb 19 2022 09:35:41", updatedAt="Sat Sep 11 2021 01:43:40")
    comment1589b = Comment(videoId=202, channelId=89, content="The trick to getting kids to eat anything is to put catchup on it.", createdAt="Tue Feb 08 2022 01:57:19", updatedAt="Tue Sep 14 2021 01:53:12")
    comment1590b = Comment(videoId=651, channelId=91, content="The three-year-old girl ran down the beach as the kite flew behind her.", createdAt="Thu Oct 28 2021 12:38:46", updatedAt="Sun Dec 19 2021 05:58:35")
    comment1591b = Comment(videoId=302, channelId=93, content="When nobody is around, the trees gossip about the people who have walked under them.", createdAt="Tue Jun 08 2021 10:43:22", updatedAt="Wed Apr 06 2022 02:31:01")
    comment1592b = Comment(videoId=586, channelId=88, content="Poison ivy grew through the fence they said was impenetrable.", createdAt="Sun Aug 15 2021 23:36:39", updatedAt="Wed Oct 13 2021 07:15:48")
    comment1593b = Comment(videoId=183, channelId=95, content="David subscribes to the \"stuff your tent into the bag\" strategy over nicely folding it.", createdAt="Sat Mar 19 2022 05:25:08", updatedAt="Fri Oct 15 2021 00:16:18")
    comment1594b = Comment(videoId=707, channelId=97, content="It's never been my responsibility to glaze the donuts.", createdAt="Fri May 28 2021 12:16:30", updatedAt="Tue Apr 27 2021 12:30:09")
    comment1595b = Comment(videoId=519, channelId=87, content="He strives to keep the best lawn in the neighborhood.", createdAt="Sun Apr 18 2021 09:23:03", updatedAt="Thu Sep 16 2021 04:56:05")
    comment1596b = Comment(videoId=71, channelId=93, content="He wondered why at 18 he was old enough to go to war, but not old enough to buy cigarettes.", createdAt="Fri Feb 18 2022 06:24:31", updatedAt="Tue Nov 09 2021 20:29:12")
    comment1597b = Comment(videoId=516, channelId=86, content="He didn't understand why the bird wanted to ride the bicycle.", createdAt="Wed Dec 01 2021 14:17:06", updatedAt="Wed Apr 28 2021 09:30:52")
    comment1598b = Comment(videoId=358, channelId=85, content="As time wore on, simple dog commands turned into full paragraphs explaining why the dog couldn’t do something.", createdAt="Mon Feb 21 2022 22:57:39", updatedAt="Wed May 26 2021 16:58:24")
    comment1599b = Comment(videoId=766, channelId=89, content="As the rental car rolled to a stop on the dark road, her fear increased by the moment.", createdAt="Fri Sep 17 2021 02:15:54", updatedAt="Sun Dec 19 2021 11:00:43")
    comment1600b = Comment(videoId=589, channelId=90, content="The external scars tell only part of the story.", createdAt="Fri Apr 30 2021 08:58:23", updatedAt="Wed Jan 05 2022 08:35:11")
    comment1601b = Comment(videoId=523, channelId=90, content="Homesickness became contagious in the young campers' cabin.", createdAt="Sat Oct 16 2021 07:30:02", updatedAt="Wed Jan 26 2022 13:29:30")
    comment1602b = Comment(videoId=257, channelId=94, content="Best friends are like old tomatoes and shoelaces.", createdAt="Sun Jul 04 2021 19:36:19", updatedAt="Thu Aug 05 2021 10:53:13")
    comment1603b = Comment(videoId=627, channelId=87, content="He walked into the basement with the horror movie from the night before playing in his head.", createdAt="Sat Jul 03 2021 06:33:03", updatedAt="Mon May 17 2021 02:54:31")
    comment1604b = Comment(videoId=40, channelId=87, content="She borrowed the book from him many years ago and hasn't yet returned it.", createdAt="Mon Oct 11 2021 07:02:17", updatedAt="Sat Oct 23 2021 09:33:53")
    comment1605b = Comment(videoId=241, channelId=92, content="The fog was so dense even a laser decided it wasn't worth the effort.", createdAt="Tue Jan 11 2022 17:30:08", updatedAt="Fri Nov 12 2021 00:53:12")
    comment1606b = Comment(videoId=671, channelId=98, content="I had a friend in high school named Rick Shaw, but he was fairly useless as a mode of transport.", createdAt="Tue Sep 07 2021 04:21:27", updatedAt="Tue May 18 2021 13:55:58")
    comment1607b = Comment(videoId=147, channelId=85, content="In hopes of finding out the truth, he entered the one-room library.", createdAt="Fri Jun 25 2021 15:19:54", updatedAt="Sun Sep 12 2021 22:06:50")
    comment1608b = Comment(videoId=157, channelId=85, content="He had a hidden stash underneath the floorboards in the back room of the house.", createdAt="Fri Sep 24 2021 01:53:21", updatedAt="Wed Apr 06 2022 07:50:12")
    comment1609b = Comment(videoId=103, channelId=96, content="That must be the tenth time I've been arrested for selling deep-fried cigars.", createdAt="Thu Feb 03 2022 18:29:27", updatedAt="Sat Feb 26 2022 06:42:22")
    comment1610b = Comment(videoId=625, channelId=94, content="Her scream silenced the rowdy teenagers.", createdAt="Sat Apr 02 2022 05:41:42", updatedAt="Wed Nov 17 2021 07:31:03")
    comment1611b = Comment(videoId=218, channelId=97, content="It was a really good Monday for being a Saturday.", createdAt="Wed Jun 16 2021 02:11:41", updatedAt="Thu Jun 17 2021 18:35:25")
    comment1612b = Comment(videoId=407, channelId=85, content="Standing on one's head at job interviews forms a lasting impression.", createdAt="Fri Sep 24 2021 10:09:05", updatedAt="Sat Jan 01 2022 16:50:44")
    comment1613b = Comment(videoId=388, channelId=96, content="They were excited to see their first sloth.", createdAt="Wed Mar 23 2022 08:52:30", updatedAt="Tue Apr 05 2022 17:54:13")
    comment1614b = Comment(videoId=547, channelId=90, content="Barking dogs and screaming toddlers have the unique ability to turn friendly neighbors into cranky enemies.", createdAt="Sun Mar 27 2022 18:34:01", updatedAt="Tue Feb 15 2022 21:50:43")
    comment1615b = Comment(videoId=508, channelId=85, content="He would only survive if he kept the fire going and he could hear thunder in the distance.", createdAt="Fri Jan 21 2022 21:10:27", updatedAt="Sat Jul 03 2021 14:50:01")
    comment1616b = Comment(videoId=256, channelId=98, content="I hear that Nancy is very pretty.", createdAt="Sun Aug 01 2021 02:00:41", updatedAt="Tue Aug 17 2021 19:10:46")
    comment1617b = Comment(videoId=514, channelId=92, content="She wasn't sure whether to be impressed or concerned that he folded underwear in neat little packages.", createdAt="Mon Nov 08 2021 16:13:40", updatedAt="Sat Jun 12 2021 16:23:25")
    comment1618b = Comment(videoId=439, channelId=89, content="Garlic ice-cream was her favorite.", createdAt="Sun Sep 12 2021 23:39:03", updatedAt="Tue Mar 29 2022 06:34:50")
    comment1619b = Comment(videoId=117, channelId=94, content="The fish listened intently to what the frogs had to say.", createdAt="Sat Aug 14 2021 08:13:55", updatedAt="Fri Jul 30 2021 07:26:58")
    comment1620b = Comment(videoId=398, channelId=86, content="Nancy was proud that she ran a tight shipwreck.", createdAt="Fri Jan 28 2022 01:54:22", updatedAt="Mon Jan 03 2022 22:51:56")
    comment1621b = Comment(videoId=33, channelId=94, content="The beauty of the sunset was obscured by the industrial cranes.", createdAt="Tue Sep 28 2021 21:55:51", updatedAt="Thu Nov 04 2021 00:29:54")
    comment1622b = Comment(videoId=315, channelId=95, content="They decided to plant an orchard of cotton candy.", createdAt="Tue Feb 01 2022 22:58:32", updatedAt="Sun Apr 11 2021 11:33:38")
    comment1623b = Comment(videoId=261, channelId=97, content="Fluffy pink unicorns are a popular status symbol among macho men.", createdAt="Thu Mar 31 2022 06:30:40", updatedAt="Thu Nov 04 2021 11:50:37")
    comment1624b = Comment(videoId=207, channelId=98, content="The sky is clear; the stars are twinkling.", createdAt="Wed Mar 23 2022 05:13:38", updatedAt="Tue Jul 20 2021 07:25:38")
    comment1625b = Comment(videoId=670, channelId=88, content="Lightning Paradise was the local hangout joint where the group usually ended up spending the night.", createdAt="Sun Jul 18 2021 14:09:45", updatedAt="Thu Sep 23 2021 15:10:47")
    comment1626b = Comment(videoId=5, channelId=88, content="As the asteroid hurtled toward earth, Becky was upset her dentist appointment had been canceled.", createdAt="Sun Nov 28 2021 14:40:23", updatedAt="Thu Sep 09 2021 01:04:55")
    comment1627b = Comment(videoId=658, channelId=89, content="To the surprise of everyone, the Rapture happened yesterday but it didn't quite go as expected.", createdAt="Fri Feb 04 2022 20:21:17", updatedAt="Sat Feb 26 2022 17:47:42")
    comment1628b = Comment(videoId=480, channelId=98, content="He appeared to be confusingly perplexed.", createdAt="Tue Mar 29 2022 04:33:52", updatedAt="Sat Mar 26 2022 22:56:00")
    comment1629b = Comment(videoId=472, channelId=92, content="The murder hornet was disappointed by the preconceived ideas people had of him.", createdAt="Sun Jan 16 2022 13:39:59", updatedAt="Tue Feb 01 2022 08:01:18")
    comment1630b = Comment(videoId=67, channelId=93, content="It's never comforting to know that your fate depends on something as unpredictable as the popping of corn.", createdAt="Sun Jan 02 2022 08:50:52", updatedAt="Sun Feb 27 2022 05:25:38")
    comment1631b = Comment(videoId=445, channelId=89, content="She works two jobs to make ends meet; at least, that was her reason for not having time to join us.", createdAt="Sat May 15 2021 21:06:02", updatedAt="Fri Apr 23 2021 14:13:32")
    comment1632b = Comment(videoId=113, channelId=96, content="She had some amazing news to share but nobody to share it with.", createdAt="Wed Jan 26 2022 03:47:42", updatedAt="Sun Dec 05 2021 18:27:58")
    comment1633b = Comment(videoId=96, channelId=87, content="It must be five o'clock somewhere.", createdAt="Tue Nov 23 2021 01:21:39", updatedAt="Tue Feb 08 2022 17:11:40")
    comment1634b = Comment(videoId=102, channelId=96, content="Swim at your own risk was taken as a challenge for the group of Kansas City college students.", createdAt="Tue Nov 16 2021 02:06:44", updatedAt="Mon Mar 07 2022 06:33:46")
    comment1635b = Comment(videoId=439, channelId=86, content="Jenny made the announcement that her baby was an alien.", createdAt="Mon Sep 13 2021 10:59:09", updatedAt="Thu Sep 30 2021 01:56:03")
    comment1636b = Comment(videoId=661, channelId=95, content="Today I heard something new and unmemorable.", createdAt="Sun Mar 20 2022 14:20:16", updatedAt="Sun Apr 10 2022 03:14:06")
    comment1637b = Comment(videoId=601, channelId=92, content="Written warnings in instruction manuals are worthless since rabbits can't read.", createdAt="Mon Mar 14 2022 04:42:57", updatedAt="Sat Mar 19 2022 07:42:25")
    comment1638b = Comment(videoId=683, channelId=88, content="A glittering gem is not enough.", createdAt="Tue Dec 14 2021 01:28:35", updatedAt="Wed Feb 23 2022 05:24:04")
    comment1639b = Comment(videoId=656, channelId=96, content="Hit me with your pet shark!", createdAt="Fri Oct 01 2021 02:41:14", updatedAt="Sat Jun 19 2021 19:51:45")
    comment1640b = Comment(videoId=660, channelId=89, content="That was how he came to win $1 million.", createdAt="Wed Feb 23 2022 03:34:22", updatedAt="Fri Oct 15 2021 14:06:16")
    comment1641b = Comment(videoId=474, channelId=94, content="Little Red Riding Hood decided to wear orange today.", createdAt="Sun Jan 23 2022 23:56:13", updatedAt="Mon May 31 2021 08:30:46")
    comment1642b = Comment(videoId=724, channelId=96, content="He didn't understand why the bird wanted to ride the bicycle.", createdAt="Thu Oct 14 2021 18:49:38", updatedAt="Sun Oct 24 2021 14:57:58")
    comment1643b = Comment(videoId=33, channelId=85, content="Today we gathered moss for my uncle's wedding.", createdAt="Tue Mar 15 2022 05:30:40", updatedAt="Tue Jan 11 2022 16:23:44")
    comment1644b = Comment(videoId=442, channelId=85, content="Don't put peanut butter on the dog's nose.", createdAt="Sat Aug 21 2021 21:54:35", updatedAt="Sun Oct 31 2021 17:05:43")
    comment1645b = Comment(videoId=676, channelId=92, content="There's a growing trend among teenagers of using frisbees as go-cart wheels.", createdAt="Thu Dec 02 2021 22:40:24", updatedAt="Fri Jan 21 2022 02:50:28")
    comment1646b = Comment(videoId=616, channelId=96, content="He enjoys practicing his ballet in the bathroom.", createdAt="Mon Jun 28 2021 03:36:25", updatedAt="Thu Oct 28 2021 13:31:55")
    comment1647b = Comment(videoId=133, channelId=93, content="The small white buoys marked the location of hundreds of crab pots.", createdAt="Sun Jun 06 2021 04:02:09", updatedAt="Fri Apr 30 2021 04:43:02")
    comment1648b = Comment(videoId=141, channelId=86, content="Despite what your teacher may have told you, there is a wrong way to wield a lasso.", createdAt="Sun May 30 2021 09:37:27", updatedAt="Mon May 03 2021 21:22:34")
    comment1649b = Comment(videoId=714, channelId=87, content="Too many prisons have become early coffins.", createdAt="Tue Jan 11 2022 05:39:18", updatedAt="Sun Jun 20 2021 00:29:20")
    comment1650b = Comment(videoId=765, channelId=98, content="The fox in the tophat whispered into the ear of the rabbit.", createdAt="Fri Jul 16 2021 01:38:01", updatedAt="Wed Dec 29 2021 15:51:28")
    comment1651b = Comment(videoId=213, channelId=96, content="The green tea and avocado smoothie turned out exactly as would be expected.", createdAt="Thu Nov 11 2021 09:21:21", updatedAt="Sun Nov 28 2021 07:28:04")
    comment1652b = Comment(videoId=170, channelId=88, content="She can live her life however she wants as long as she listens to what I have to say.", createdAt="Fri Jul 02 2021 12:39:24", updatedAt="Tue Dec 28 2021 09:24:30")
    comment1653b = Comment(videoId=645, channelId=87, content="Instead of a bachelorette party", createdAt="Mon Jan 17 2022 11:32:13", updatedAt="Wed Jul 28 2021 21:05:18")
    comment1654b = Comment(videoId=580, channelId=85, content="Red is greener than purple, for sure.", createdAt="Thu Jul 29 2021 08:01:56", updatedAt="Fri Feb 25 2022 09:48:37")
    comment1655b = Comment(videoId=147, channelId=88, content="Grape jelly was leaking out the hole in the roof.", createdAt="Sat Jan 01 2022 09:37:35", updatedAt="Sat Sep 18 2021 07:36:37")
    comment1656b = Comment(videoId=261, channelId=95, content="The sun had set and so had his dreams.", createdAt="Mon Dec 20 2021 20:02:00", updatedAt="Thu Oct 14 2021 03:19:20")
    comment1657b = Comment(videoId=367, channelId=95, content="She cried diamonds.", createdAt="Fri Mar 25 2022 15:28:19", updatedAt="Sun Jul 11 2021 13:24:23")
    comment1658b = Comment(videoId=187, channelId=86, content="Poison ivy grew through the fence they said was impenetrable.", createdAt="Thu Apr 29 2021 15:43:58", updatedAt="Tue Dec 28 2021 21:04:10")
    comment1659b = Comment(videoId=550, channelId=89, content="They say that dogs are man's best friend, but this cat was setting out to sabotage that theory.", createdAt="Sat Mar 26 2022 13:51:58", updatedAt="Thu Feb 10 2022 06:28:49")
    comment1660b = Comment(videoId=185, channelId=94, content="Art doesn't have to be intentional.", createdAt="Thu Sep 23 2021 21:30:02", updatedAt="Tue Feb 15 2022 17:26:12")
    comment1661b = Comment(videoId=507, channelId=86, content="He stomped on his fruit loops and thus became a cereal killer.", createdAt="Sat Sep 18 2021 10:15:40", updatedAt="Thu Jul 01 2021 06:20:05")
    comment1662b = Comment(videoId=461, channelId=91, content="Her scream silenced the rowdy teenagers.", createdAt="Sat Oct 30 2021 02:10:38", updatedAt="Tue Mar 01 2022 23:23:43")
    comment1663b = Comment(videoId=679, channelId=85, content="She folded her handkerchief neatly.", createdAt="Thu Dec 09 2021 10:31:08", updatedAt="Thu Nov 18 2021 06:56:16")
    comment1664b = Comment(videoId=300, channelId=87, content="She only paints with bold colors; she does not like pastels.", createdAt="Mon Feb 28 2022 09:28:39", updatedAt="Wed Dec 01 2021 16:58:58")
    comment1665b = Comment(videoId=725, channelId=92, content="If you like tuna and tomato sauce, try combining the two, it’s really not as bad as it sounds.", createdAt="Fri Jan 21 2022 20:58:19", updatedAt="Sun Feb 13 2022 06:05:22")
    comment1666b = Comment(videoId=227, channelId=86, content="The wake behind the boat told of the past while the open sea for told life in the unknown future.", createdAt="Thu Feb 10 2022 10:06:30", updatedAt="Thu Jul 22 2021 08:52:02")
    comment1667b = Comment(videoId=677, channelId=85, content="There aren't enough towels in the world to stop the sewage flowing from his mouth.", createdAt="Fri May 14 2021 18:37:33", updatedAt="Thu Jun 17 2021 17:59:30")
    comment1668b = Comment(videoId=220, channelId=92, content="Someone I know recently combined Maple Syrup & buttered Popcorn thinking it would taste like caramel popcorn. It didn’t and they don’t recommend anyone else do it either.", createdAt="Sat Sep 18 2021 01:32:11", updatedAt="Fri Feb 04 2022 19:31:15")
    comment1669b = Comment(videoId=600, channelId=89, content="He dreamed of eating green apples with worms.", createdAt="Sat Oct 23 2021 23:50:15", updatedAt="Tue Apr 05 2022 07:03:56")
    comment1670b = Comment(videoId=10, channelId=94, content="As the asteroid hurtled toward earth, Becky was upset her dentist appointment had been canceled.", createdAt="Mon Mar 07 2022 00:58:53", updatedAt="Sun Mar 06 2022 03:10:00")
    comment1671b = Comment(videoId=98, channelId=94, content="I've never seen a more beautiful brandy glass filled with wine.", createdAt="Fri Oct 22 2021 20:42:32", updatedAt="Fri Oct 22 2021 20:29:52")
    comment1672b = Comment(videoId=131, channelId=88, content="Iron pyrite is the most foolish of all minerals.", createdAt="Tue Jul 27 2021 20:04:59", updatedAt="Sun Apr 11 2021 02:27:28")
    comment1673b = Comment(videoId=283, channelId=89, content="A suit of armor provides excellent sun protection on hot days.", createdAt="Tue Jul 13 2021 19:32:39", updatedAt="Sun Jul 25 2021 04:18:07")
    comment1674b = Comment(videoId=205, channelId=93, content="I hear that Nancy is very pretty.", createdAt="Sat Jul 31 2021 18:34:09", updatedAt="Tue Jul 20 2021 10:23:46")
    comment1675b = Comment(videoId=469, channelId=98, content="That was how he came to win $1 million.", createdAt="Mon Aug 16 2021 00:26:44", updatedAt="Thu Jul 01 2021 12:09:58")
    comment1676b = Comment(videoId=779, channelId=98, content="Everyone says they love nature until they realize how dangerous she can be.", createdAt="Sun Jul 04 2021 11:21:51", updatedAt="Tue Nov 16 2021 13:57:04")
    comment1677b = Comment(videoId=420, channelId=88, content="The hand sanitizer was actually clear glue.", createdAt="Wed Jun 02 2021 03:04:47", updatedAt="Tue Apr 13 2021 12:51:52")
    comment1678b = Comment(videoId=706, channelId=90, content="The Guinea fowl flies through the air with all the grace of a turtle.", createdAt="Wed Sep 01 2021 03:24:43", updatedAt="Sun Jun 20 2021 05:30:08")
    comment1679b = Comment(videoId=492, channelId=89, content="As she walked along the street and looked in the gutter, she realized facemasks had become the new cigarette butts.", createdAt="Mon Mar 28 2022 11:53:34", updatedAt="Wed May 26 2021 15:25:38")
    comment1680b = Comment(videoId=537, channelId=93, content="That must be the tenth time I've been arrested for selling deep-fried cigars.", createdAt="Fri Jun 04 2021 10:53:48", updatedAt="Fri Jun 04 2021 05:38:35")
    comment1681b = Comment(videoId=272, channelId=94, content="She had a difficult time owning up to her own crazy self.", createdAt="Sat Oct 09 2021 06:21:58", updatedAt="Sat May 15 2021 01:39:51")
    comment1682b = Comment(videoId=392, channelId=96, content="Please put on these earmuffs because I can't you hear.", createdAt="Sat Oct 23 2021 21:18:24", updatedAt="Tue Feb 15 2022 13:21:00")
    comment1683b = Comment(videoId=388, channelId=94, content="It's important to remember to be aware of rampaging grizzly bears.", createdAt="Mon Jun 28 2021 01:41:07", updatedAt="Tue Aug 17 2021 00:57:07")
    comment1684b = Comment(videoId=203, channelId=86, content="I was offended by the suggestion that my baby brother was a jewel thief.", createdAt="Wed Jan 19 2022 13:17:25", updatedAt="Sun May 23 2021 00:21:15")
    comment1685b = Comment(videoId=671, channelId=95, content="The bug was having an excellent day until he hit the windshield.", createdAt="Wed Jun 30 2021 10:30:01", updatedAt="Tue Jun 08 2021 03:43:48")
    comment1686b = Comment(videoId=586, channelId=95, content="She had that tint of craziness in her soul that made her believe she could actually make a difference.", createdAt="Fri Aug 13 2021 20:48:20", updatedAt="Sat Jan 15 2022 20:59:03")
    comment1687b = Comment(videoId=442, channelId=90, content="He fumbled in the darkness looking for the light switch, but when he finally found it there was someone already there.", createdAt="Mon Nov 29 2021 19:43:43", updatedAt="Sat Sep 25 2021 02:53:23")
    comment1688b = Comment(videoId=610, channelId=86, content="The Great Dane looked more like a horse than a dog.", createdAt="Sun Mar 20 2022 16:21:33", updatedAt="Wed Apr 21 2021 12:31:04")
    comment1689b = Comment(videoId=178, channelId=88, content="The busker hoped that the people passing by would throw money, but they threw tomatoes instead, so he exchanged his hat for a juicer.", createdAt="Fri Oct 01 2021 02:55:19", updatedAt="Mon Oct 18 2021 13:46:56")
    comment1690b = Comment(videoId=415, channelId=97, content="I am happy to take your donation; any amount will be greatly appreciated.", createdAt="Sun Oct 31 2021 10:59:43", updatedAt="Wed Dec 15 2021 16:17:14")
    comment1691b = Comment(videoId=173, channelId=92, content="Everybody should read Chaucer to improve their everyday vocabulary.", createdAt="Thu Mar 31 2022 20:50:28", updatedAt="Sun Oct 10 2021 12:56:36")
    comment1692b = Comment(videoId=33, channelId=94, content="Honestly, I didn't care much for the first season, so I didn't bother with the second.", createdAt="Wed Oct 13 2021 02:10:22", updatedAt="Mon Feb 28 2022 01:54:25")
    comment1693b = Comment(videoId=185, channelId=87, content="Today arrived with a crash of my car through the garage door.", createdAt="Sat Nov 20 2021 12:47:27", updatedAt="Fri Nov 12 2021 07:58:47")
    comment1694b = Comment(videoId=469, channelId=96, content="Potato wedges probably are not best for relationships.", createdAt="Mon Dec 13 2021 14:16:19", updatedAt="Sun Oct 03 2021 02:05:46")
    comment1695b = Comment(videoId=723, channelId=95, content="He swore he just saw his sushi move.", createdAt="Mon Dec 20 2021 23:20:09", updatedAt="Tue Dec 28 2021 20:10:10")
    comment1696b = Comment(videoId=728, channelId=95, content="The Japanese yen for commerce is still well-known.", createdAt="Sat Dec 04 2021 07:32:22", updatedAt="Thu Jul 08 2021 11:37:53")
    comment1697b = Comment(videoId=493, channelId=86, content="She traveled because it cost the same as therapy and was a lot more enjoyable.", createdAt="Mon Apr 04 2022 01:53:03", updatedAt="Tue Nov 30 2021 03:26:52")
    comment1698b = Comment(videoId=645, channelId=91, content="Her life in the confines of the house became her new normal.", createdAt="Mon Aug 09 2021 09:18:48", updatedAt="Thu Jan 20 2022 06:32:01")
    comment1699b = Comment(videoId=273, channelId=90, content="I can't believe this is the eighth time I'm smashing open my piggy bank on the same day!", createdAt="Sun Sep 26 2021 04:01:38", updatedAt="Mon Aug 02 2021 06:20:42")
    comment1700b = Comment(videoId=281, channelId=87, content="He walked into the basement with the horror movie from the night before playing in his head.", createdAt="Wed Jul 28 2021 23:33:40", updatedAt="Tue Mar 29 2022 08:08:03")
    comment1701b = Comment(videoId=568, channelId=89, content="Cats are good pets, for they are clean and are not noisy.", createdAt="Mon Jun 14 2021 04:00:32", updatedAt="Thu Dec 16 2021 15:31:16")
    comment1702b = Comment(videoId=42, channelId=94, content="Boulders lined the side of the road foretelling what could come next.", createdAt="Mon May 03 2021 13:08:28", updatedAt="Thu Dec 23 2021 05:01:30")
    comment1703b = Comment(videoId=358, channelId=97, content="Random words in front of other random words create a random sentence.", createdAt="Mon Jul 12 2021 14:33:59", updatedAt="Thu Feb 03 2022 02:49:44")
    comment1704b = Comment(videoId=333, channelId=95, content="He wore the surgical mask in public not to keep from catching a virus, but to keep people away from him.", createdAt="Wed Jul 21 2021 23:14:46", updatedAt="Fri Nov 19 2021 21:57:48")
    comment1705b = Comment(videoId=248, channelId=94, content="She looked into the mirror and saw another person.", createdAt="Wed Feb 16 2022 13:12:42", updatedAt="Thu Mar 31 2022 01:41:41")
    comment1706b = Comment(videoId=661, channelId=91, content="Patricia found the meaning of life in a bowl of Cheerios.", createdAt="Sat Jun 12 2021 08:06:20", updatedAt="Sun Feb 06 2022 18:57:56")
    comment1707b = Comment(videoId=704, channelId=97, content="A good example of a useful vegetable is medicinal rhubarb.", createdAt="Sat Dec 11 2021 01:29:57", updatedAt="Tue Dec 07 2021 21:51:26")
    comment1708b = Comment(videoId=600, channelId=92, content="The shark-infested South Pine channel was the only way in or out.", createdAt="Tue Mar 01 2022 23:41:26", updatedAt="Sat Jul 03 2021 05:48:24")
    comment1709b = Comment(videoId=85, channelId=89, content="The waves were crashing on the shore; it was a lovely sight.", createdAt="Thu May 13 2021 22:42:33", updatedAt="Sun Jan 23 2022 11:52:26")
    comment1710b = Comment(videoId=136, channelId=93, content="He went back to the video to see what had been recorded and was shocked at what he saw.", createdAt="Tue Apr 27 2021 13:18:03", updatedAt="Thu Mar 17 2022 21:02:28")
    comment1711b = Comment(videoId=229, channelId=88, content="He fumbled in the darkness looking for the light switch, but when he finally found it there was someone already there.", createdAt="Tue Sep 21 2021 17:32:54", updatedAt="Sat Aug 07 2021 00:54:06")
    comment1712b = Comment(videoId=377, channelId=91, content="She had a difficult time owning up to her own crazy self.", createdAt="Fri Dec 10 2021 06:29:29", updatedAt="Thu Mar 24 2022 19:11:51")
    comment1713b = Comment(videoId=457, channelId=85, content="He didn’t want to go to the dentist, yet he went anyway.", createdAt="Fri Dec 10 2021 00:10:45", updatedAt="Wed Nov 03 2021 06:00:54")
    comment1714b = Comment(videoId=647, channelId=97, content="Plans for this weekend include turning wine into water.", createdAt="Mon Sep 13 2021 21:30:12", updatedAt="Mon Dec 06 2021 20:50:30")
    comment1715b = Comment(videoId=598, channelId=98, content="The clock within this blog and the clock on my laptop are 1 hour different from each other.", createdAt="Fri Oct 29 2021 23:10:45", updatedAt="Tue Sep 28 2021 18:37:11")
    comment1716b = Comment(videoId=674, channelId=90, content="He was an introvert that extroverts seemed to love.", createdAt="Tue Sep 21 2021 21:11:24", updatedAt="Mon Jan 10 2022 01:04:04")
    comment1717b = Comment(videoId=452, channelId=95, content="The sign said there was road work ahead so he decided to speed up.", createdAt="Mon Apr 12 2021 17:06:24", updatedAt="Mon Jan 31 2022 09:49:17")
    comment1718b = Comment(videoId=66, channelId=91, content="The shooter says goodbye to his love.", createdAt="Mon Mar 14 2022 08:12:25", updatedAt="Wed Dec 22 2021 02:17:14")
    comment1719b = Comment(videoId=762, channelId=86, content="She insisted that cleaning out your closet was the key to good driving.", createdAt="Tue May 04 2021 21:52:30", updatedAt="Sun Aug 29 2021 23:38:50")
    comment1720b = Comment(videoId=523, channelId=93, content="She was too short to see over the fence.", createdAt="Wed Nov 24 2021 23:39:48", updatedAt="Wed Jun 02 2021 21:43:08")
    comment1721b = Comment(videoId=435, channelId=92, content="The fog was so dense even a laser decided it wasn't worth the effort.", createdAt="Mon Nov 22 2021 16:31:41", updatedAt="Mon Jul 26 2021 02:41:00")
    comment1722b = Comment(videoId=726, channelId=90, content="The best key lime pie is still up for debate.", createdAt="Thu May 13 2021 18:15:45", updatedAt="Sun Oct 24 2021 11:20:21")
    comment1723b = Comment(videoId=580, channelId=87, content="I am happy to take your donation; any amount will be greatly appreciated.", createdAt="Thu Dec 23 2021 23:45:20", updatedAt="Thu Feb 17 2022 12:49:19")
    comment1724b = Comment(videoId=593, channelId=90, content="The golden retriever loved the fireworks each Fourth of July.", createdAt="Wed Jan 05 2022 05:23:17", updatedAt="Fri Jul 16 2021 23:00:55")
    comment1725b = Comment(videoId=107, channelId=98, content="The rusty nail stood erect, angled at a 45-degree angle, just waiting for the perfect barefoot to come along.", createdAt="Sat Jan 22 2022 06:19:27", updatedAt="Wed Apr 14 2021 20:45:57")
    comment1726b = Comment(videoId=140, channelId=90, content="The virus had powers none of us knew existed.", createdAt="Fri Jan 28 2022 12:53:52", updatedAt="Sat Feb 19 2022 06:51:56")
    comment1727b = Comment(videoId=287, channelId=92, content="Tomatoes make great weapons when water balloons aren’t available.", createdAt="Wed Jul 21 2021 17:33:42", updatedAt="Sat Feb 19 2022 03:40:51")
    comment1728b = Comment(videoId=674, channelId=94, content="Douglas figured the best way to succeed was to do the opposite of what he'd been doing all his life.", createdAt="Tue Jan 25 2022 13:15:28", updatedAt="Fri Aug 20 2021 16:09:16")
    comment1729b = Comment(videoId=664, channelId=90, content="Swim at your own risk was taken as a challenge for the group of Kansas City college students.", createdAt="Tue May 11 2021 20:51:31", updatedAt="Wed Jul 07 2021 17:55:07")
    comment1730b = Comment(videoId=3, channelId=97, content="The glacier came alive as the climbers hiked closer.", createdAt="Sat Jul 31 2021 07:37:07", updatedAt="Sat Feb 19 2022 08:27:02")
    comment1731b = Comment(videoId=704, channelId=91, content="It caught him off guard that space smelled of seared steak.", createdAt="Thu Jul 29 2021 03:36:24", updatedAt="Tue Dec 07 2021 18:16:16")
    comment1732b = Comment(videoId=429, channelId=88, content="The delicious aroma from the kitchen was ruined by cigarette smoke.", createdAt="Thu Mar 24 2022 01:25:11", updatedAt="Wed Apr 21 2021 05:44:08")
    comment1733b = Comment(videoId=605, channelId=87, content="I've always wanted to go to Tajikistan, but my cat would miss me.", createdAt="Thu Feb 03 2022 08:28:16", updatedAt="Sun Oct 24 2021 08:04:58")
    comment1734b = Comment(videoId=333, channelId=92, content="You bite up because of your lower jaw.", createdAt="Sun Jan 23 2022 05:47:05", updatedAt="Mon Aug 09 2021 08:26:04")
    comment1735b = Comment(videoId=339, channelId=95, content="She is never happy until she finds something to be unhappy about; then, she is overjoyed.", createdAt="Fri Oct 08 2021 15:34:58", updatedAt="Thu Mar 24 2022 20:23:14")
    comment1736b = Comment(videoId=663, channelId=92, content="The swirled lollipop had issues with the pop rock candy.", createdAt="Mon Nov 29 2021 03:04:13", updatedAt="Wed Sep 15 2021 20:09:05")
    comment1737b = Comment(videoId=712, channelId=86, content="Although it wasn't a pot of gold, Nancy was still enthralled at what she found at the end of the rainbow.", createdAt="Wed Feb 16 2022 16:52:07", updatedAt="Mon Apr 19 2021 17:16:33")
    comment1738b = Comment(videoId=649, channelId=92, content="Charles ate the french fries knowing they would be his last meal.", createdAt="Thu Mar 03 2022 21:42:34", updatedAt="Tue Dec 14 2021 06:10:20")
    comment1739b = Comment(videoId=168, channelId=88, content="She had a habit of taking showers in lemonade.", createdAt="Mon Jul 12 2021 16:56:18", updatedAt="Mon Oct 25 2021 13:15:18")
    comment1740b = Comment(videoId=133, channelId=98, content="The truth is that you pay for your lifestyle in hours.", createdAt="Fri Apr 30 2021 21:42:11", updatedAt="Wed Feb 23 2022 08:38:16")
    comment1741b = Comment(videoId=142, channelId=88, content="Nancy thought the best way to create a welcoming home was to line it with barbed wire.", createdAt="Thu Sep 02 2021 02:01:57", updatedAt="Fri Sep 24 2021 01:13:43")
    comment1742b = Comment(videoId=626, channelId=91, content="Happiness can be found in the depths of chocolate pudding.", createdAt="Tue Nov 16 2021 17:40:54", updatedAt="Sat Jan 15 2022 15:09:07")
    comment1743b = Comment(videoId=26, channelId=96, content="It's never been my responsibility to glaze the donuts.", createdAt="Sun Mar 06 2022 07:37:18", updatedAt="Mon Oct 18 2021 07:23:57")
    comment1744b = Comment(videoId=359, channelId=94, content="She was too busy always talking about what she wanted to do to actually do any of it.", createdAt="Sat Oct 30 2021 15:00:58", updatedAt="Fri Mar 11 2022 03:57:20")
    comment1745b = Comment(videoId=712, channelId=93, content="Her fragrance of choice was fresh garlic.", createdAt="Mon Jun 14 2021 09:59:25", updatedAt="Fri Aug 27 2021 11:48:16")
    comment1746b = Comment(videoId=407, channelId=87, content="Even though he thought the world was flat he didn’t see the irony of wanting to travel around the world.", createdAt="Mon Jan 03 2022 23:38:51", updatedAt="Tue Mar 29 2022 07:09:57")
    comment1747b = Comment(videoId=242, channelId=95, content="It was a slippery slope and he was willing to slide all the way to the deepest depths.", createdAt="Sat Jan 29 2022 17:12:28", updatedAt="Sun Oct 17 2021 07:04:14")
    comment1748b = Comment(videoId=280, channelId=91, content="She works two jobs to make ends meet; at least, that was her reason for not having time to join us.", createdAt="Tue Oct 05 2021 11:43:27", updatedAt="Tue Nov 30 2021 03:52:41")
    comment1749b = Comment(videoId=248, channelId=95, content="While on the first date he accidentally hit his head on the beam.", createdAt="Tue Dec 07 2021 13:19:07", updatedAt="Mon Mar 07 2022 01:47:20")
    comment1750b = Comment(videoId=578, channelId=97, content="When he asked her favorite number, she answered without hesitation that it was diamonds.", createdAt="Wed Feb 16 2022 08:45:10", updatedAt="Sat May 29 2021 06:25:55")
    comment1751b = Comment(videoId=335, channelId=92, content="Iguanas were falling out of the trees.", createdAt="Sat Sep 11 2021 21:10:03", updatedAt="Thu Dec 02 2021 13:28:54")
    comment1752b = Comment(videoId=770, channelId=85, content="Please put on these earmuffs because I can't you hear.", createdAt="Sun Jun 06 2021 06:51:33", updatedAt="Sat Mar 26 2022 01:20:15")
    comment1753b = Comment(videoId=353, channelId=90, content="He loved eating his bananas in hot dog buns.", createdAt="Thu Feb 24 2022 23:15:09", updatedAt="Fri Jun 11 2021 13:16:43")
    comment1754b = Comment(videoId=167, channelId=93, content="The heat", createdAt="Sun Jan 02 2022 10:16:54", updatedAt="Mon Jan 03 2022 08:23:11")
    comment1755b = Comment(videoId=464, channelId=87, content="It's always a good idea to seek shelter from the evil gaze of the sun.", createdAt="Sun Jul 11 2021 18:17:52", updatedAt="Mon Dec 06 2021 21:52:12")
    comment1756b = Comment(videoId=141, channelId=85, content="As he looked out the window, he saw a clown walk by.", createdAt="Sun Nov 28 2021 22:49:10", updatedAt="Mon Sep 06 2021 07:29:18")
    comment1757b = Comment(videoId=163, channelId=90, content="We have a lot of rain in June.", createdAt="Sat Jan 15 2022 18:55:55", updatedAt="Thu Jan 27 2022 09:22:17")
    comment1758b = Comment(videoId=441, channelId=85, content="It's much more difficult to play tennis with a bowling ball than it is to bowl with a tennis ball.", createdAt="Tue Mar 29 2022 02:09:43", updatedAt="Thu Nov 04 2021 08:37:48")
    comment1759b = Comment(videoId=712, channelId=96, content="Writing a list of random sentences is harder than I initially thought it would be.", createdAt="Mon Apr 26 2021 13:18:41", updatedAt="Sat May 08 2021 04:54:51")
    comment1760b = Comment(videoId=103, channelId=93, content="The crowd yells and screams for more memes.", createdAt="Fri Jun 25 2021 05:30:22", updatedAt="Thu Feb 24 2022 20:55:25")
    comment1761b = Comment(videoId=476, channelId=89, content="You're unsure whether or not to trust him, but very thankful that you wore a turtle neck.", createdAt="Sat Sep 18 2021 21:17:42", updatedAt="Sat Jan 08 2022 00:55:39")
    comment1762b = Comment(videoId=356, channelId=96, content="The father handed each child a roadmap at the beginning of the 2-day road trip and explained it was so they could find their way home.", createdAt="Mon Oct 11 2021 03:03:38", updatedAt="Thu Oct 07 2021 18:32:06")
    comment1763b = Comment(videoId=503, channelId=95, content="I always dreamed about being stranded on a desert island until it actually happened.", createdAt="Wed Oct 06 2021 04:34:36", updatedAt="Wed Nov 24 2021 08:02:14")
    comment1764b = Comment(videoId=37, channelId=85, content="People generally approve of dogs eating cat food but not cats eating dog food.", createdAt="Mon Nov 15 2021 09:55:42", updatedAt="Thu Nov 25 2021 17:19:08")
    comment1765b = Comment(videoId=245, channelId=86, content="The tree fell unexpectedly short.", createdAt="Sun Feb 20 2022 14:46:01", updatedAt="Sat Jan 22 2022 08:07:44")
    comment1766b = Comment(videoId=629, channelId=85, content="As he dangled from the rope deep inside the crevasse", createdAt="Tue Jan 04 2022 17:09:17", updatedAt="Mon Oct 25 2021 11:43:12")
    comment1767b = Comment(videoId=440, channelId=89, content="When transplanting seedlings, candied teapots will make the task easier.", createdAt="Sun Oct 10 2021 08:34:36", updatedAt="Fri Jul 23 2021 06:37:28")
    comment1768b = Comment(videoId=653, channelId=90, content="As you consider all the possible ways to improve yourself and the world, you notice John Travolta seems fairly unhappy.", createdAt="Sun Oct 10 2021 03:12:55", updatedAt="Sat Mar 05 2022 11:34:16")
    comment1769b = Comment(videoId=444, channelId=87, content="She couldn't understand why nobody else could see that the sky is full of cotton candy.", createdAt="Fri Jun 18 2021 18:04:12", updatedAt="Tue Mar 01 2022 15:47:02")
    comment1770b = Comment(videoId=166, channelId=88, content="He had a vague sense that trees gave birth to dinosaurs.", createdAt="Thu Mar 10 2022 18:02:46", updatedAt="Fri Dec 24 2021 05:36:24")
    comment1771b = Comment(videoId=779, channelId=88, content="Truth in advertising and dinosaurs with skateboards have much in common.", createdAt="Wed Mar 30 2022 00:54:32", updatedAt="Mon Aug 16 2021 03:06:51")
    comment1772b = Comment(videoId=193, channelId=96, content="The two walked down the slot canyon oblivious to the sound of thunder in the distance.", createdAt="Sat Mar 26 2022 03:15:54", updatedAt="Thu Mar 03 2022 14:10:57")
    comment1773b = Comment(videoId=281, channelId=87, content="It's a skateboarding penguin with a sunhat!", createdAt="Fri Jan 28 2022 05:45:14", updatedAt="Tue Jan 04 2022 11:12:09")
    comment1774b = Comment(videoId=554, channelId=89, content="He embraced his new life as an eggplant.", createdAt="Wed Nov 10 2021 07:00:05", updatedAt="Wed May 26 2021 13:19:24")
    comment1775b = Comment(videoId=572, channelId=87, content="He found the end of the rainbow and was surprised at what he found there.", createdAt="Thu May 27 2021 05:50:17", updatedAt="Thu Jul 01 2021 01:59:16")
    comment1777b = Comment(videoId=266, channelId=92, content="His son quipped that power bars were nothing more than adult candy bars.", createdAt="Sun Sep 26 2021 02:57:55", updatedAt="Sat Oct 09 2021 16:41:04")
    comment1778b = Comment(videoId=507, channelId=92, content="He used to get confused between soldiers and shoulders, but as a military man, he now soldiers responsibility.", createdAt="Wed Feb 23 2022 20:58:43", updatedAt="Mon May 31 2021 19:58:43")
    comment1779b = Comment(videoId=40, channelId=98, content="Little Red Riding Hood decided to wear orange today.", createdAt="Wed Aug 11 2021 18:21:59", updatedAt="Sat Feb 12 2022 12:34:31")
    comment1780b = Comment(videoId=128, channelId=85, content="It was her first experience training a rainbow unicorn.", createdAt="Sat Oct 09 2021 09:00:17", updatedAt="Fri May 21 2021 20:23:44")
    comment1781b = Comment(videoId=67, channelId=96, content="She couldn't decide of the glass was half empty or half full so she drank it.", createdAt="Thu Feb 03 2022 17:55:04", updatedAt="Thu Mar 31 2022 23:41:06")
    comment1782b = Comment(videoId=706, channelId=88, content="I liked their first two albums but changed my mind after that charity gig.", createdAt="Mon Sep 13 2021 05:43:21", updatedAt="Sat Apr 24 2021 14:04:50")
    comment1783b = Comment(videoId=668, channelId=91, content="They got there early, and they got really good seats.", createdAt="Sun Apr 11 2021 08:52:45", updatedAt="Sun Nov 21 2021 13:13:36")
    comment1784b = Comment(videoId=585, channelId=91, content="Joe made the sugar cookies; Susan decorated them.", createdAt="Fri Jan 28 2022 06:35:06", updatedAt="Sun Feb 13 2022 10:19:42")
    comment1785b = Comment(videoId=260, channelId=98, content="Flying fish flew by the space station.", createdAt="Wed Mar 30 2022 18:07:17", updatedAt="Fri Aug 06 2021 11:29:31")
    comment1786b = Comment(videoId=706, channelId=87, content="The heat", createdAt="Wed Feb 23 2022 18:41:07", updatedAt="Wed Sep 15 2021 06:21:53")
    comment1787b = Comment(videoId=625, channelId=93, content="We have young kids who often walk into our room at night for various reasons including clowns in the closet.", createdAt="Thu Sep 30 2021 00:38:02", updatedAt="Tue Jun 15 2021 07:35:55")
    comment1788b = Comment(videoId=662, channelId=88, content="His confidence would have bee admirable if it wasn't for his stupidity.", createdAt="Mon Aug 16 2021 16:58:21", updatedAt="Sat Jan 01 2022 14:15:31")
    comment1789b = Comment(videoId=409, channelId=85, content="He went on a whiskey diet and immediately lost three days.", createdAt="Thu Mar 03 2022 01:34:19", updatedAt="Sun Jan 30 2022 14:29:34")
    comment1790b = Comment(videoId=516, channelId=85, content="He watched the dancing piglets with panda bear tummies in the swimming pool.", createdAt="Wed Mar 09 2022 09:19:00", updatedAt="Tue Aug 31 2021 16:29:44")
    comment1791b = Comment(videoId=126, channelId=90, content="It was at that moment that he learned there are certain parts of the body that you should never Nair.", createdAt="Sun Jan 23 2022 02:42:11", updatedAt="Mon Apr 04 2022 03:19:47")
    comment1792b = Comment(videoId=235, channelId=89, content="He poured rocks in the dungeon of his mind.", createdAt="Tue Nov 09 2021 04:07:51", updatedAt="Wed Mar 23 2022 20:43:54")
    comment1793b = Comment(videoId=30, channelId=90, content="She found it strange that people use their cellphones to actually talk to one another.", createdAt="Sat Jan 29 2022 01:10:51", updatedAt="Sun Jul 18 2021 22:29:54")
    comment1794b = Comment(videoId=365, channelId=98, content="He decided that the time had come to be stronger than any of the excuses he'd used until then.", createdAt="Sat Aug 28 2021 22:58:13", updatedAt="Tue Apr 13 2021 22:15:08")
    comment1795b = Comment(videoId=690, channelId=87, content="The worst thing about being at the top of the career ladder is that there's a long way to fall.", createdAt="Wed Mar 16 2022 14:55:26", updatedAt="Sat Mar 05 2022 07:04:56")
    comment1796b = Comment(videoId=298, channelId=95, content="It didn't take long for Gary to detect the robbers were amateurs.", createdAt="Thu Aug 19 2021 09:16:55", updatedAt="Sun Oct 24 2021 03:02:30")
    comment1797b = Comment(videoId=698, channelId=88, content="Garlic ice-cream was her favorite.", createdAt="Wed Dec 01 2021 16:10:53", updatedAt="Wed Jun 30 2021 19:37:18")
    comment1798b = Comment(videoId=420, channelId=88, content="When nobody is around, the trees gossip about the people who have walked under them.", createdAt="Mon Jan 03 2022 18:33:13", updatedAt="Mon Jul 26 2021 06:35:21")
    comment1799b = Comment(videoId=234, channelId=95, content="A dead duck doesn't fly backward.", createdAt="Mon Oct 25 2021 19:45:27", updatedAt="Mon Jan 24 2022 23:08:30")
    comment1800b = Comment(videoId=258, channelId=85, content="I caught my squirrel rustling through my gym bag.", createdAt="Tue Apr 27 2021 09:42:55", updatedAt="Mon Jun 07 2021 17:26:48")
    comment1801b = Comment(videoId=164, channelId=86, content="When he asked her favorite number, she answered without hesitation that it was diamonds.", createdAt="Sat Aug 14 2021 21:29:44", updatedAt="Wed Dec 01 2021 18:24:50")
    comment1802b = Comment(videoId=735, channelId=93, content="It's never been my responsibility to glaze the donuts.", createdAt="Thu Jul 15 2021 00:18:23", updatedAt="Tue May 11 2021 23:45:31")
    comment1803b = Comment(videoId=82, channelId=87, content="Harrold felt confident that nobody would ever suspect his spy pigeon.", createdAt="Fri Oct 15 2021 10:42:45", updatedAt="Thu Jul 08 2021 15:38:14")
    comment1804b = Comment(videoId=416, channelId=93, content="The memory we used to share is no longer coherent.", createdAt="Mon Jul 19 2021 23:21:15", updatedAt="Mon Nov 15 2021 06:54:28")
    comment1805b = Comment(videoId=426, channelId=89, content="She learned that water bottles are no longer just to hold liquid, but they're also status symbols.", createdAt="Sun Oct 17 2021 16:19:53", updatedAt="Sat Jun 26 2021 23:18:47")
    comment1806b = Comment(videoId=353, channelId=95, content="Even with the snow falling outside, she felt it appropriate to wear her bikini.", createdAt="Thu Jun 10 2021 07:29:25", updatedAt="Thu Jun 17 2021 05:13:00")
    comment1807b = Comment(videoId=610, channelId=86, content="I met an interesting turtle while the song on the radio blasted away.", createdAt="Mon Mar 28 2022 08:51:40", updatedAt="Tue Apr 27 2021 22:59:20")
    comment1808b = Comment(videoId=21, channelId=96, content="Lets all be unique together until we realise we are all the same.", createdAt="Tue Mar 29 2022 08:05:11", updatedAt="Sat Dec 18 2021 13:20:10")
    comment1809b = Comment(videoId=294, channelId=85, content="There's a reason that roses have thorns.", createdAt="Sun Mar 13 2022 18:51:29", updatedAt="Tue Dec 07 2021 02:37:27")
    comment1811b = Comment(videoId=630, channelId=94, content="The golden retriever loved the fireworks each Fourth of July.", createdAt="Thu Aug 05 2021 12:38:52", updatedAt="Thu Dec 09 2021 09:37:21")
    comment1812b = Comment(videoId=699, channelId=90, content="Lucifer was surprised at the amount of life at Death Valley.", createdAt="Mon Sep 27 2021 19:14:37", updatedAt="Tue Nov 09 2021 13:17:48")
    comment1813b = Comment(videoId=294, channelId=96, content="He swore he just saw his sushi move.", createdAt="Thu Dec 09 2021 19:30:04", updatedAt="Mon Nov 08 2021 18:50:35")
    comment1814b = Comment(videoId=533, channelId=92, content="She traveled because it cost the same as therapy and was a lot more enjoyable.", createdAt="Mon Jan 31 2022 21:04:39", updatedAt="Sat Feb 12 2022 07:41:46")
    comment1815b = Comment(videoId=753, channelId=96, content="Thirty years later, she still thought it was okay to put the toilet paper roll under rather than over.", createdAt="Mon Oct 18 2021 06:35:19", updatedAt="Sun May 30 2021 00:20:00")
    comment1816b = Comment(videoId=281, channelId=92, content="We're careful about orange ping pong balls because people might think they're fruit.", createdAt="Thu Jun 10 2021 08:12:57", updatedAt="Mon May 17 2021 20:15:59")
    comment1817b = Comment(videoId=200, channelId=97, content="Smoky the Bear secretly started the fires.", createdAt="Thu Sep 09 2021 17:20:40", updatedAt="Fri Jun 25 2021 19:06:08")
    comment1818b = Comment(videoId=533, channelId=91, content="He decided to fake his disappearance to avoid jail.", createdAt="Wed Feb 02 2022 14:12:34", updatedAt="Sun Aug 29 2021 19:03:20")
    comment1820b = Comment(videoId=715, channelId=95, content="Flying fish flew by the space station.", createdAt="Mon Aug 09 2021 09:42:03", updatedAt="Wed Aug 11 2021 16:07:55")
    comment1821b = Comment(videoId=235, channelId=88, content="Please tell me you don't work in a morgue.", createdAt="Fri Dec 17 2021 18:16:48", updatedAt="Fri Apr 01 2022 19:03:53")
    comment1822b = Comment(videoId=602, channelId=88, content="They were excited to see their first sloth.", createdAt="Thu Apr 22 2021 00:28:10", updatedAt="Fri Mar 18 2022 03:07:28")
    comment1823b = Comment(videoId=733, channelId=96, content="In that instant, everything changed.", createdAt="Fri May 21 2021 02:17:32", updatedAt="Mon Jan 03 2022 00:51:42")
    comment1824b = Comment(videoId=595, channelId=93, content="He was willing to find the depths of the rabbit hole in order to be with her.", createdAt="Sun Nov 07 2021 14:44:43", updatedAt="Tue Aug 17 2021 06:56:23")
    comment1825b = Comment(videoId=575, channelId=85, content="All she wanted was the answer, but she had no idea how much she would hate it.", createdAt="Fri Jan 28 2022 17:34:23", updatedAt="Fri Jun 11 2021 16:30:20")
    comment1826b = Comment(videoId=215, channelId=94, content="The two walked down the slot canyon oblivious to the sound of thunder in the distance.", createdAt="Mon May 03 2021 14:48:34", updatedAt="Wed Feb 16 2022 16:32:44")
    comment1827b = Comment(videoId=402, channelId=88, content="Garlic ice-cream was her favorite.", createdAt="Sat Jan 08 2022 13:35:54", updatedAt="Wed Aug 18 2021 10:28:51")
    comment1828b = Comment(videoId=216, channelId=89, content="She learned that water bottles are no longer just to hold liquid, but they're also status symbols.", createdAt="Sat Oct 09 2021 14:11:28", updatedAt="Fri Dec 31 2021 15:57:44")
    comment1829b = Comment(videoId=719, channelId=88, content="She looked at the masterpiece hanging in the museum but all she could think is that her five-year-old could do better.", createdAt="Sat Oct 23 2021 19:03:26", updatedAt="Thu Feb 24 2022 11:34:06")
    comment1830b = Comment(videoId=244, channelId=91, content="The efficiency we have at removing trash has made creating trash more acceptable.", createdAt="Thu Oct 14 2021 03:02:40", updatedAt="Mon Feb 28 2022 14:02:49")
    comment1831b = Comment(videoId=59, channelId=88, content="They throw cabbage that turns your brain into emotional baggage.", createdAt="Sun Jan 16 2022 05:15:02", updatedAt="Mon Nov 08 2021 19:04:51")
    comment1832b = Comment(videoId=754, channelId=85, content="I want a giraffe, but I'm a turtle eating waffles.", createdAt="Sun Sep 05 2021 21:47:35", updatedAt="Wed May 12 2021 01:12:24")
    comment1833b = Comment(videoId=653, channelId=92, content="The sudden rainstorm washed crocodiles into the ocean.", createdAt="Sat May 29 2021 06:22:39", updatedAt="Sat Jan 15 2022 05:41:20")
    comment1834b = Comment(videoId=565, channelId=92, content="There aren't enough towels in the world to stop the sewage flowing from his mouth.", createdAt="Tue Jan 04 2022 15:24:03", updatedAt="Tue Feb 01 2022 09:38:38")
    comment1835b = Comment(videoId=98, channelId=89, content="The waitress was not amused when he ordered green eggs and ham.", createdAt="Mon Nov 01 2021 13:57:30", updatedAt="Wed Jun 30 2021 02:20:08")
    comment1836b = Comment(videoId=591, channelId=94, content="Erin accidentally created a new universe.", createdAt="Tue Jul 27 2021 20:12:36", updatedAt="Mon Dec 13 2021 04:16:18")
    comment1837b = Comment(videoId=529, channelId=93, content="The worst thing about being at the top of the career ladder is that there's a long way to fall.", createdAt="Sat Jun 26 2021 01:16:47", updatedAt="Mon Dec 20 2021 03:04:23")
    comment1838b = Comment(videoId=513, channelId=89, content="She saw no irony asking me to change but wanting me to accept her for who she is.", createdAt="Mon Aug 09 2021 03:32:00", updatedAt="Sun Jun 20 2021 16:31:55")
    comment1839b = Comment(videoId=225, channelId=85, content="Kevin embraced his ability to be at the wrong place at the wrong time.", createdAt="Mon Aug 09 2021 21:19:33", updatedAt="Sat Nov 06 2021 15:27:06")
    comment1840b = Comment(videoId=648, channelId=87, content="Random words in front of other random words create a random sentence.", createdAt="Wed Mar 09 2022 12:42:21", updatedAt="Mon Oct 04 2021 18:15:34")
    comment1841b = Comment(videoId=713, channelId=92, content="His get rich quick scheme was to grow a cactus farm.", createdAt="Sat Mar 26 2022 20:46:42", updatedAt="Sat Jun 19 2021 20:00:37")
    comment1842b = Comment(videoId=304, channelId=86, content="The furnace repairman indicated the heating system was acting as an air conditioner.", createdAt="Thu Dec 30 2021 08:08:11", updatedAt="Sat Apr 09 2022 21:43:06")
    comment1843b = Comment(videoId=494, channelId=89, content="The tortoise jumped into the lake with dreams of becoming a sea turtle.", createdAt="Tue Sep 21 2021 00:11:49", updatedAt="Thu Jun 24 2021 19:07:59")
    comment1844b = Comment(videoId=556, channelId=85, content="The chic gangster liked to start the day with a pink scarf.", createdAt="Thu Jul 29 2021 05:43:00", updatedAt="Sat Jul 24 2021 00:59:11")
    comment1845b = Comment(videoId=616, channelId=88, content="He had reached the point where he was paranoid about being paranoid.", createdAt="Sat Aug 21 2021 22:51:01", updatedAt="Wed Sep 01 2021 13:16:28")
    comment1846b = Comment(videoId=267, channelId=98, content="When she didn’t like a guy who was trying to pick her up, she started using sign language.", createdAt="Sat Aug 21 2021 11:17:53", updatedAt="Sun Jul 11 2021 05:54:15")
    comment1847b = Comment(videoId=59, channelId=94, content="He decided to live his life by the big beats manifesto.", createdAt="Mon Apr 19 2021 14:26:29", updatedAt="Thu Apr 29 2021 13:22:13")
    comment1848b = Comment(videoId=575, channelId=85, content="Courage and stupidity were all he had.", createdAt="Tue May 25 2021 22:21:24", updatedAt="Wed Sep 22 2021 18:01:29")
    comment1849b = Comment(videoId=775, channelId=94, content="Peter found road kill an excellent way to save money on dinner.", createdAt="Tue Oct 26 2021 12:30:36", updatedAt="Sun Sep 19 2021 06:26:19")
    comment1850b = Comment(videoId=447, channelId=96, content="I met an interesting turtle while the song on the radio blasted away.", createdAt="Mon Apr 19 2021 23:45:21", updatedAt="Fri Feb 04 2022 17:14:27")
    comment1851b = Comment(videoId=722, channelId=96, content="It caught him off guard that space smelled of seared steak.", createdAt="Sat Jan 22 2022 15:26:46", updatedAt="Wed Oct 13 2021 08:54:57")
    comment1852b = Comment(videoId=317, channelId=93, content="The light in his life was actually a fire burning all around him.", createdAt="Sat Jan 29 2022 14:17:10", updatedAt="Sat Aug 07 2021 18:25:16")
    comment1853b = Comment(videoId=335, channelId=93, content="She insisted that cleaning out your closet was the key to good driving.", createdAt="Sun Nov 07 2021 08:38:32", updatedAt="Wed Jun 09 2021 15:08:58")
    comment1854b = Comment(videoId=129, channelId=98, content="Never underestimate the willingness of the greedy to throw you under the bus.", createdAt="Wed Jul 28 2021 06:37:42", updatedAt="Fri Oct 08 2021 23:54:10")
    comment1855b = Comment(videoId=557, channelId=87, content="He would only survive if he kept the fire going and he could hear thunder in the distance.", createdAt="Sat Sep 25 2021 22:19:07", updatedAt="Sun Oct 03 2021 21:16:26")
    comment1856b = Comment(videoId=305, channelId=88, content="My secretary is the only person who truly understands my stamp-collecting obsession.", createdAt="Wed Apr 14 2021 20:53:48", updatedAt="Fri Nov 19 2021 14:27:01")
    comment1857b = Comment(videoId=248, channelId=98, content="Her hair was windswept as she rode in the black convertible.", createdAt="Thu Nov 18 2021 10:56:05", updatedAt="Sat Feb 12 2022 04:21:19")
    comment1858b = Comment(videoId=643, channelId=85, content="The blinking lights of the antenna tower came into focus just as I heard a loud snap.", createdAt="Sun Oct 31 2021 18:31:31", updatedAt="Thu Mar 10 2022 18:32:54")
    comment1859b = Comment(videoId=583, channelId=96, content="Henry couldn't decide if he was an auto mechanic or a priest.", createdAt="Sat Jul 10 2021 04:47:38", updatedAt="Tue Oct 19 2021 04:37:15")
    comment1860b = Comment(videoId=82, channelId=93, content="She moved forward only because she trusted that the ending she now was going through must be followed by a new beginning.", createdAt="Tue Feb 08 2022 08:00:14", updatedAt="Sat Jul 10 2021 09:59:58")
    comment1862b = Comment(videoId=136, channelId=96, content="Yeah, I think it's a good environment for learning English.", createdAt="Sun Oct 31 2021 00:53:58", updatedAt="Fri Feb 04 2022 06:20:13")
    comment1863b = Comment(videoId=49, channelId=86, content="The Guinea fowl flies through the air with all the grace of a turtle.", createdAt="Mon Aug 16 2021 08:15:09", updatedAt="Mon Sep 13 2021 17:08:57")
    comment1864b = Comment(videoId=210, channelId=92, content="The virus had powers none of us knew existed.", createdAt="Fri Apr 01 2022 22:02:13", updatedAt="Mon Mar 28 2022 01:08:20")
    comment1865b = Comment(videoId=68, channelId=85, content="Buried deep in the snow, he hoped his batteries were fresh in his avalanche beacon.", createdAt="Sun Dec 19 2021 07:31:23", updatedAt="Sat May 08 2021 21:37:05")
    comment1866b = Comment(videoId=770, channelId=87, content="Nobody questions who built the pyramids in Mexico.", createdAt="Tue Jun 01 2021 05:09:26", updatedAt="Fri Apr 23 2021 06:18:53")
    comment1867b = Comment(videoId=43, channelId=97, content="The bullet pierced the window shattering it before missing Danny's head by mere millimeters.", createdAt="Fri Mar 18 2022 15:38:18", updatedAt="Wed Oct 13 2021 20:39:32")
    comment1868b = Comment(videoId=293, channelId=93, content="Her daily goal was to improve on yesterday.", createdAt="Tue Oct 26 2021 05:36:14", updatedAt="Mon Nov 01 2021 04:55:46")
    comment1869b = Comment(videoId=310, channelId=96, content="My dentist tells me that chewing bricks is very bad for your teeth.", createdAt="Sun May 16 2021 22:00:55", updatedAt="Sat Jul 10 2021 19:17:51")
    comment1870b = Comment(videoId=582, channelId=85, content="Behind the window was a reflection that only instilled fear.", createdAt="Fri Jul 09 2021 18:31:19", updatedAt="Fri Dec 17 2021 04:36:22")
    comment1871b = Comment(videoId=625, channelId=95, content="Grape jelly was leaking out the hole in the roof.", createdAt="Sun Dec 26 2021 03:41:00", updatedAt="Sun Dec 19 2021 11:06:59")
    comment1872b = Comment(videoId=745, channelId=93, content="He had a wall full of masks so she could wear a different face every day.", createdAt="Wed Jun 23 2021 13:29:58", updatedAt="Mon Jan 24 2022 19:57:28")
    comment1873b = Comment(videoId=469, channelId=86, content="I was offended by the suggestion that my baby brother was a jewel thief.", createdAt="Fri Feb 04 2022 08:17:51", updatedAt="Wed Apr 14 2021 11:22:49")
    comment1874b = Comment(videoId=617, channelId=93, content="While all her friends were positive that Mary had a sixth sense, she knew she actually had a seventh sense.", createdAt="Mon Nov 08 2021 10:21:24", updatedAt="Mon Mar 07 2022 19:03:46")
    comment1875b = Comment(videoId=322, channelId=87, content="The father handed each child a roadmap at the beginning of the 2-day road trip and explained it was so they could find their way home.", createdAt="Tue Apr 13 2021 14:00:00", updatedAt="Tue Dec 14 2021 09:30:42")
    comment1876b = Comment(videoId=283, channelId=85, content="The Great Dane looked more like a horse than a dog.", createdAt="Mon Oct 18 2021 12:57:50", updatedAt="Wed Feb 16 2022 17:45:29")
    comment1877b = Comment(videoId=342, channelId=95, content="Toddlers feeding raccoons surprised even the seasoned park ranger.", createdAt="Sat Oct 02 2021 03:00:54", updatedAt="Mon Oct 25 2021 11:32:50")
    comment1878b = Comment(videoId=132, channelId=94, content="He wondered if it could be called a beach if there was no sand.", createdAt="Fri Sep 24 2021 20:16:51", updatedAt="Sun Nov 28 2021 04:25:04")
    comment1879b = Comment(videoId=124, channelId=86, content="The tumbleweed refused to tumble but was more than willing to prance.", createdAt="Sat Jun 19 2021 14:24:04", updatedAt="Wed Jan 26 2022 05:23:51")
    comment1880b = Comment(videoId=488, channelId=95, content="They got there early, and they got really good seats.", createdAt="Wed May 19 2021 14:31:14", updatedAt="Sun Jan 23 2022 04:13:57")
    comment1881b = Comment(videoId=552, channelId=92, content="He quietly entered the museum as the super bowl started.", createdAt="Sat Dec 18 2021 01:27:07", updatedAt="Thu Sep 16 2021 22:03:03")
    comment1882b = Comment(videoId=51, channelId=87, content="Lucifer was surprised at the amount of life at Death Valley.", createdAt="Mon Dec 27 2021 20:23:42", updatedAt="Fri Dec 03 2021 12:13:38")
    comment1883b = Comment(videoId=625, channelId=86, content="The delicious aroma from the kitchen was ruined by cigarette smoke.", createdAt="Sun Jul 04 2021 20:46:18", updatedAt="Mon Oct 18 2021 10:22:43")
    comment1884b = Comment(videoId=54, channelId=87, content="I want to buy a onesie… but know it won’t suit me.", createdAt="Sat Sep 04 2021 17:35:37", updatedAt="Wed Feb 23 2022 02:05:38")
    comment1885b = Comment(videoId=470, channelId=98, content="Courage and stupidity were all he had.", createdAt="Tue Nov 02 2021 06:22:50", updatedAt="Fri Feb 04 2022 18:35:54")
    comment1886b = Comment(videoId=483, channelId=89, content="It didn't take long for Gary to detect the robbers were amateurs.", createdAt="Thu May 20 2021 07:39:12", updatedAt="Fri Dec 03 2021 07:47:25")
    comment1887b = Comment(videoId=529, channelId=97, content="Bill ran from the giraffe toward the dolphin.", createdAt="Mon Mar 21 2022 12:54:49", updatedAt="Thu Nov 25 2021 12:25:57")
    comment1888b = Comment(videoId=574, channelId=88, content="The efficiency with which he paired the socks in the drawer was quite admirable.", createdAt="Fri Mar 11 2022 18:49:36", updatedAt="Fri Feb 18 2022 06:21:59")
    comment1889b = Comment(videoId=705, channelId=92, content="The toy brought back fond memories of being lost in the rain forest.", createdAt="Sun Oct 17 2021 03:15:43", updatedAt="Fri Sep 24 2021 20:34:06")
    comment1890b = Comment(videoId=185, channelId=90, content="In hopes of finding out the truth, he entered the one-room library.", createdAt="Fri Mar 04 2022 02:26:00", updatedAt="Wed Mar 02 2022 02:45:37")
    comment1891b = Comment(videoId=434, channelId=98, content="I’m working on a sweet potato farm.", createdAt="Sat Feb 05 2022 16:36:52", updatedAt="Wed Sep 01 2021 08:37:14")
    comment1892b = Comment(videoId=667, channelId=86, content="The urgent care center was flooded with patients after the news of a new deadly virus was made public.", createdAt="Mon Nov 29 2021 12:17:58", updatedAt="Fri Oct 01 2021 21:11:13")
    comment1893b = Comment(videoId=152, channelId=94, content="Iron pyrite is the most foolish of all minerals.", createdAt="Sun Sep 19 2021 10:44:18", updatedAt="Fri Nov 19 2021 04:15:38")
    comment1894b = Comment(videoId=221, channelId=95, content="No matter how beautiful the sunset, it saddened her knowing she was one day older.", createdAt="Sun Sep 12 2021 04:11:31", updatedAt="Mon Oct 18 2021 09:22:00")
    comment1895b = Comment(videoId=182, channelId=88, content="Nancy thought the best way to create a welcoming home was to line it with barbed wire.", createdAt="Sat May 01 2021 15:00:10", updatedAt="Sat Nov 27 2021 04:31:00")
    comment1896b = Comment(videoId=590, channelId=98, content="The elderly neighborhood became enraged over the coyotes who had been blamed for the poodle’s disappearance.", createdAt="Tue Dec 28 2021 13:03:23", updatedAt="Wed Apr 21 2021 00:21:35")
    comment1897b = Comment(videoId=123, channelId=95, content="At last", createdAt="Wed Mar 02 2022 21:21:51", updatedAt="Wed Aug 18 2021 06:11:19")
    comment1898b = Comment(videoId=575, channelId=87, content="That must be the tenth time I've been arrested for selling deep-fried cigars.", createdAt="Sun Jul 18 2021 22:58:24", updatedAt="Fri Feb 25 2022 07:03:15")
    comment1899b = Comment(videoId=400, channelId=97, content="When he had to picnic on the beach, he purposely put sand in other people’s food.", createdAt="Sat Jul 17 2021 16:45:17", updatedAt="Fri May 07 2021 13:32:30")
    comment1900b = Comment(videoId=424, channelId=97, content="We have young kids who often walk into our room at night for various reasons including clowns in the closet.", createdAt="Sun Aug 29 2021 04:52:41", updatedAt="Thu Jun 10 2021 04:26:18")
    comment1901b = Comment(videoId=244, channelId=98, content="Dan took the deep dive down the rabbit hole.", createdAt="Thu Sep 09 2021 20:52:06", updatedAt="Mon Oct 25 2021 03:46:55")
    comment1902b = Comment(videoId=655, channelId=87, content="The river stole the gods.", createdAt="Tue Jul 13 2021 21:15:27", updatedAt="Tue Dec 28 2021 17:36:29")
    comment1903b = Comment(videoId=486, channelId=93, content="There's a message for you if you look up.", createdAt="Mon Feb 21 2022 18:24:27", updatedAt="Fri Sep 10 2021 12:24:55")
    comment1904b = Comment(videoId=528, channelId=91, content="He enjoys practicing his ballet in the bathroom.", createdAt="Sun Jun 27 2021 07:05:59", updatedAt="Fri Dec 31 2021 13:14:54")
    comment1905b = Comment(videoId=260, channelId=89, content="Random words in front of other random words create a random sentence.", createdAt="Mon Dec 20 2021 21:21:41", updatedAt="Fri Jan 14 2022 05:46:13")
    comment1906b = Comment(videoId=591, channelId=87, content="She could hear him in the shower singing with a joy she hoped he'd retain after she delivered the news.", createdAt="Sat Aug 28 2021 10:15:23", updatedAt="Fri Oct 08 2021 14:07:19")
    comment1907b = Comment(videoId=716, channelId=86, content="The worst thing about being at the top of the career ladder is that there's a long way to fall.", createdAt="Mon Aug 09 2021 01:10:21", updatedAt="Sun Jul 25 2021 10:52:29")
    comment1908b = Comment(videoId=148, channelId=90, content="He was so preoccupied with whether or not he could that he failed to stop to consider if he should.", createdAt="Sat Oct 16 2021 13:34:23", updatedAt="Mon Mar 07 2022 22:16:04")
    comment1909b = Comment(videoId=282, channelId=92, content="My uncle's favorite pastime was building cars out of noodles.", createdAt="Mon Aug 09 2021 00:43:30", updatedAt="Sat Sep 25 2021 18:12:23")
    comment1910b = Comment(videoId=148, channelId=95, content="Everyone was curious about the large white blimp that appeared overnight.", createdAt="Wed Mar 30 2022 18:13:17", updatedAt="Tue Feb 15 2022 20:46:28")
    comment1911b = Comment(videoId=481, channelId=95, content="I am happy to take your donation; any amount will be greatly appreciated.", createdAt="Fri Jun 25 2021 06:14:41", updatedAt="Thu Jul 08 2021 02:08:42")
    comment1912b = Comment(videoId=89, channelId=86, content="Thigh-high in the water, the fisherman’s hope for dinner soon turned to despair.", createdAt="Fri Nov 05 2021 23:21:11", updatedAt="Sun Mar 13 2022 10:42:05")
    comment1913b = Comment(videoId=666, channelId=90, content="Shakespeare was a famous 17th-century diesel mechanic.", createdAt="Tue Feb 15 2022 05:10:00", updatedAt="Fri Mar 25 2022 04:57:20")
    comment1914b = Comment(videoId=417, channelId=90, content="I would be delighted if the sea were full of cucumber juice.", createdAt="Thu Aug 19 2021 11:53:43", updatedAt="Fri Dec 03 2021 02:22:34")
    comment1915b = Comment(videoId=113, channelId=95, content="They improved dramatically once the lead singer left.", createdAt="Fri Mar 18 2022 03:39:21", updatedAt="Fri Mar 18 2022 14:08:06")
    comment1916b = Comment(videoId=31, channelId=92, content="Watching the geriatric men’s softball team brought back memories of 3 yr olds playing t-ball.", createdAt="Thu Oct 14 2021 15:57:52", updatedAt="Fri Oct 01 2021 00:09:43")
    comment1917b = Comment(videoId=576, channelId=86, content="The lyrics of the song sounded like fingernails on a chalkboard.", createdAt="Wed Dec 22 2021 13:05:10", updatedAt="Sun May 09 2021 08:07:17")
    comment1918b = Comment(videoId=458, channelId=97, content="With a single flip of the coin, his life changed forever.", createdAt="Mon Oct 11 2021 01:42:29", updatedAt="Thu Dec 09 2021 13:25:14")
    comment1919b = Comment(videoId=529, channelId=87, content="I trust everything that's written in purple ink.", createdAt="Sun Jan 09 2022 00:22:20", updatedAt="Fri Feb 25 2022 18:50:20")
    comment1920b = Comment(videoId=192, channelId=86, content="I became paranoid that the school of jellyfish was spying on me.", createdAt="Thu Nov 04 2021 01:01:42", updatedAt="Fri Sep 03 2021 06:39:12")
    comment1921b = Comment(videoId=567, channelId=91, content="It was always dangerous to drive with him since he insisted the safety cones were a slalom course.", createdAt="Fri Jan 28 2022 20:20:00", updatedAt="Thu Dec 02 2021 01:16:06")
    comment1922b = Comment(videoId=575, channelId=86, content="It's never been my responsibility to glaze the donuts.", createdAt="Sun Jan 02 2022 15:45:29", updatedAt="Fri Feb 11 2022 07:08:10")
    comment1923b = Comment(videoId=132, channelId=91, content="The spa attendant applied the deep cleaning mask to the gentleman’s back.", createdAt="Wed Jul 07 2021 09:13:41", updatedAt="Mon Jun 28 2021 04:32:19")
    comment1924b = Comment(videoId=163, channelId=89, content="The fish dreamed of escaping the fishbowl and into the toilet where he saw his friend go.", createdAt="Sat May 08 2021 15:20:36", updatedAt="Sat Jan 22 2022 15:43:36")
    comment1925b = Comment(videoId=29, channelId=97, content="It didn't make sense unless you had the power to eat colors.", createdAt="Sat Sep 04 2021 21:03:13", updatedAt="Sat Aug 21 2021 16:13:59")
    comment1926b = Comment(videoId=107, channelId=85, content="I hear that Nancy is very pretty.", createdAt="Wed Dec 29 2021 03:43:27", updatedAt="Wed Dec 22 2021 11:57:38")
    comment1927b = Comment(videoId=509, channelId=98, content="Toddlers feeding raccoons surprised even the seasoned park ranger.", createdAt="Tue Dec 28 2021 21:51:51", updatedAt="Sun Jun 27 2021 14:10:06")
    comment1929b = Comment(videoId=104, channelId=92, content="I want more detailed information.", createdAt="Mon May 24 2021 23:46:20", updatedAt="Sun Sep 26 2021 03:32:16")
    comment1930b = Comment(videoId=331, channelId=94, content="Yeah, I think it's a good environment for learning English.", createdAt="Thu Jan 27 2022 03:16:49", updatedAt="Mon Apr 04 2022 13:55:50")
    comment1931b = Comment(videoId=120, channelId=89, content="The chic gangster liked to start the day with a pink scarf.", createdAt="Sun Nov 21 2021 07:30:30", updatedAt="Tue Jun 22 2021 13:10:14")
    comment1932b = Comment(videoId=48, channelId=88, content="He had decided to accept his fate of accepting his fate.", createdAt="Tue Nov 02 2021 21:00:56", updatedAt="Fri Aug 27 2021 18:59:31")
    comment1933b = Comment(videoId=383, channelId=92, content="This is a Japanese doll.", createdAt="Thu Feb 03 2022 07:21:01", updatedAt="Sat Oct 09 2021 18:06:25")
    comment1934b = Comment(videoId=272, channelId=88, content="There is no better feeling than staring at a wall with closed eyes.", createdAt="Fri Jul 09 2021 11:11:46", updatedAt="Sat Oct 02 2021 07:29:00")
    comment1935b = Comment(videoId=14, channelId=88, content="Iron pyrite is the most foolish of all minerals.", createdAt="Thu Apr 15 2021 10:59:30", updatedAt="Thu Feb 17 2022 08:02:19")
    comment1936b = Comment(videoId=633, channelId=87, content="If any cop asks you where you were, just say you were visiting Kansas.", createdAt="Wed May 26 2021 15:51:36", updatedAt="Sat Aug 21 2021 16:53:54")
    comment1937b = Comment(videoId=20, channelId=94, content="Two seats were vacant.", createdAt="Wed May 05 2021 19:27:41", updatedAt="Wed Apr 21 2021 12:28:40")
    comment1938b = Comment(videoId=486, channelId=92, content="If my calculator had a history, it would be more embarrassing than my browser history.", createdAt="Mon Apr 04 2022 05:59:19", updatedAt="Fri Dec 17 2021 05:57:26")
    comment1939b = Comment(videoId=732, channelId=97, content="It took him a while to realize that everything he decided not to change, he was actually choosing.", createdAt="Mon Mar 28 2022 17:49:05", updatedAt="Sat Nov 13 2021 18:33:03")
    comment1940b = Comment(videoId=348, channelId=91, content="The father handed each child a roadmap at the beginning of the 2-day road trip and explained it was so they could find their way home.", createdAt="Fri Dec 03 2021 22:48:02", updatedAt="Thu Aug 05 2021 08:34:58")
    comment1941b = Comment(videoId=266, channelId=94, content="At that moment she realized she had a sixth sense.", createdAt="Sat Apr 24 2021 14:03:47", updatedAt="Fri Jan 14 2022 10:58:56")
    comment1942b = Comment(videoId=716, channelId=87, content="It isn't true that my mattress is made of cotton candy.", createdAt="Mon Jul 05 2021 23:36:20", updatedAt="Wed Jul 21 2021 08:22:00")
    comment1943b = Comment(videoId=521, channelId=88, content="I'm not a party animal, but I do like animal parties.", createdAt="Mon May 17 2021 01:17:43", updatedAt="Fri Apr 16 2021 18:15:40")
    comment1944b = Comment(videoId=222, channelId=88, content="We have never been to Asia, nor have we visited Africa.", createdAt="Tue Mar 22 2022 01:33:47", updatedAt="Sun Aug 22 2021 12:19:12")
    comment1945b = Comment(videoId=743, channelId=89, content="At that moment he wasn't listening to music, he was living an experience.", createdAt="Wed Nov 24 2021 18:57:52", updatedAt="Wed Jan 19 2022 20:15:43")
    comment1946b = Comment(videoId=451, channelId=87, content="I thought red would have felt warmer in summer but I didn't think about the equator.", createdAt="Mon Jan 17 2022 15:26:51", updatedAt="Tue Sep 21 2021 21:50:16")
    comment1947b = Comment(videoId=366, channelId=91, content="After exploring the abandoned building, he started to believe in ghosts.", createdAt="Mon Apr 04 2022 12:27:55", updatedAt="Tue Dec 07 2021 13:18:56")
    comment1948b = Comment(videoId=726, channelId=97, content="Traveling became almost extinct during the pandemic.", createdAt="Mon Feb 21 2022 17:13:49", updatedAt="Tue Aug 10 2021 10:16:23")
    comment1949b = Comment(videoId=315, channelId=88, content="This is the last random sentence I will be writing and I am going to stop mid-sent", createdAt="Sun Sep 12 2021 04:40:52", updatedAt="Sat May 08 2021 07:34:46")
    comment1950b = Comment(videoId=682, channelId=91, content="He stepped gingerly onto the bridge knowing that enchantment awaited on the other side.", createdAt="Sun Sep 05 2021 04:36:11", updatedAt="Sun Dec 05 2021 12:16:07")
    comment1951b = Comment(videoId=636, channelId=88, content="100 years old is such a young age if you happen to be a bristlecone pine.", createdAt="Mon Nov 29 2021 17:47:30", updatedAt="Sat Jul 31 2021 01:15:25")
    comment1953b = Comment(videoId=349, channelId=90, content="his seven-layer cake only had six layers.", createdAt="Thu May 27 2021 21:06:43", updatedAt="Tue Jul 20 2021 18:39:25")
    comment1954b = Comment(videoId=207, channelId=98, content="He found rain fascinating yet unpleasant.", createdAt="Fri Dec 17 2021 03:12:04", updatedAt="Fri Sep 03 2021 05:10:10")
    comment1955b = Comment(videoId=98, channelId=91, content="It was her first experience training a rainbow unicorn.", createdAt="Mon Jun 21 2021 03:05:33", updatedAt="Mon Feb 14 2022 13:23:50")
    comment1956b = Comment(videoId=580, channelId=95, content="Nobody has encountered an explosive daisy and lived to tell the tale.", createdAt="Fri Oct 01 2021 12:22:46", updatedAt="Mon Apr 04 2022 08:02:11")
    comment1957b = Comment(videoId=215, channelId=85, content="Don't put peanut butter on the dog's nose.", createdAt="Sun Sep 05 2021 09:07:44", updatedAt="Mon Apr 04 2022 14:44:39")
    comment1958b = Comment(videoId=231, channelId=86, content="He fumbled in the darkness looking for the light switch, but when he finally found it there was someone already there.", createdAt="Mon May 10 2021 04:21:00", updatedAt="Tue Apr 05 2022 09:41:40")
    comment1959b = Comment(videoId=161, channelId=85, content="The pigs were insulted that they were named hamburgers.", createdAt="Fri Oct 08 2021 01:55:54", updatedAt="Fri Jun 11 2021 03:15:26")
    comment1960b = Comment(videoId=372, channelId=87, content="There were three sphered rocks congregating in a cubed room.", createdAt="Sun Oct 31 2021 02:25:25", updatedAt="Mon Jan 24 2022 19:14:04")
    comment1961b = Comment(videoId=745, channelId=94, content="The anaconda was the greatest criminal mastermind in this part of the neighborhood.", createdAt="Thu Sep 02 2021 04:10:37", updatedAt="Thu Oct 14 2021 09:49:04")
    comment1962b = Comment(videoId=91, channelId=96, content="Tom got a small piece of pie.", createdAt="Mon May 17 2021 16:17:12", updatedAt="Fri Sep 10 2021 05:25:18")
    comment1963b = Comment(videoId=59, channelId=98, content="Everybody should read Chaucer to improve their everyday vocabulary.", createdAt="Fri Sep 24 2021 14:48:52", updatedAt="Mon Nov 22 2021 04:30:37")
    comment1964b = Comment(videoId=299, channelId=95, content="The thick foliage and intertwined vines made the hike nearly impossible.", createdAt="Tue Dec 21 2021 20:11:10", updatedAt="Fri Sep 03 2021 05:23:46")
    comment1965b = Comment(videoId=44, channelId=89, content="The crowd yells and screams for more memes.", createdAt="Sun Nov 21 2021 17:01:26", updatedAt="Thu Jun 03 2021 06:28:44")
    comment1966b = Comment(videoId=148, channelId=97, content="He was the only member of the club who didn't like plum pudding.", createdAt="Fri Feb 25 2022 10:10:23", updatedAt="Wed Oct 20 2021 21:51:12")
    comment1967b = Comment(videoId=355, channelId=87, content="The tart lemonade quenched her thirst, but not her longing.", createdAt="Sun Sep 12 2021 15:08:07", updatedAt="Tue Dec 07 2021 20:50:24")
    comment1968b = Comment(videoId=738, channelId=95, content="The sudden rainstorm washed crocodiles into the ocean.", createdAt="Wed Apr 21 2021 16:54:41", updatedAt="Tue Jan 25 2022 03:28:59")
    comment1969b = Comment(videoId=35, channelId=88, content="There have been days when I wished to be separated from my body, but today wasn’t one of those days.", createdAt="Fri Jun 11 2021 18:07:52", updatedAt="Sun Jul 04 2021 09:54:36")
    comment1970b = Comment(videoId=653, channelId=93, content="Nobody loves a pig wearing lipstick.", createdAt="Thu Oct 14 2021 03:04:00", updatedAt="Mon May 24 2021 03:57:40")
    comment1971b = Comment(videoId=114, channelId=85, content="The estate agent quickly marked out his territory on the dance floor.", createdAt="Thu Jul 22 2021 22:00:31", updatedAt="Thu Oct 28 2021 13:29:07")
    comment1972b = Comment(videoId=471, channelId=90, content="She was too busy always talking about what she wanted to do to actually do any of it.", createdAt="Thu Jun 17 2021 08:29:55", updatedAt="Thu Dec 16 2021 18:24:01")
    comment1973b = Comment(videoId=413, channelId=88, content="Nothing seemed out of place except the washing machine in the bar.", createdAt="Wed Aug 11 2021 23:50:39", updatedAt="Thu Jul 15 2021 04:36:05")
    comment1974b = Comment(videoId=415, channelId=87, content="The paintbrush was angry at the color the artist chose to use.", createdAt="Tue Aug 24 2021 14:30:21", updatedAt="Sun Apr 03 2022 18:47:23")
    comment1975b = Comment(videoId=116, channelId=90, content="A quiet house is nice until you are ordered to stay in it for months.", createdAt="Thu Aug 19 2021 13:41:42", updatedAt="Wed Aug 11 2021 01:50:21")
    comment1976b = Comment(videoId=630, channelId=94, content="He played the game as if his life depended on it and the truth was that it did.", createdAt="Tue Jun 15 2021 12:01:12", updatedAt="Sat Apr 09 2022 20:25:51")
    comment1977b = Comment(videoId=775, channelId=96, content="Giving directions that the mountains are to the west only works when you can see them.", createdAt="Thu Jan 20 2022 00:21:37", updatedAt="Thu Oct 14 2021 23:03:59")
    comment1978b = Comment(videoId=689, channelId=97, content="There were white out conditions in the town; subsequently, the roads were impassable.", createdAt="Sat Aug 21 2021 17:14:02", updatedAt="Thu Dec 09 2021 06:34:21")
    comment1979b = Comment(videoId=128, channelId=85, content="Don't put peanut butter on the dog's nose.", createdAt="Sun Nov 14 2021 23:54:56", updatedAt="Mon Dec 06 2021 19:48:30")
    comment1980b = Comment(videoId=56, channelId=85, content="Be careful with that butter knife.", createdAt="Fri May 28 2021 18:53:03", updatedAt="Fri Dec 10 2021 22:26:06")
    comment1981b = Comment(videoId=470, channelId=91, content="He was surprised that his immense laziness was inspirational to others.", createdAt="Sun Aug 29 2021 14:49:18", updatedAt="Fri Aug 13 2021 18:28:29")
    comment1982b = Comment(videoId=595, channelId=92, content="Everyone was curious about the large white blimp that appeared overnight.", createdAt="Sun Oct 24 2021 21:36:23", updatedAt="Wed Nov 24 2021 08:31:01")
    comment1983b = Comment(videoId=338, channelId=96, content="Please wait outside of the house.", createdAt="Thu Sep 09 2021 07:15:28", updatedAt="Sun Feb 20 2022 02:33:50")
    comment1984b = Comment(videoId=669, channelId=86, content="The toy brought back fond memories of being lost in the rain forest.", createdAt="Tue Apr 20 2021 00:42:01", updatedAt="Tue Apr 27 2021 03:12:36")
    comment1985b = Comment(videoId=769, channelId=87, content="They wandered into a strange Tiki bar on the edge of the small beach town.", createdAt="Mon Nov 15 2021 13:07:49", updatedAt="Wed Mar 02 2022 09:32:02")
    comment1986b = Comment(videoId=346, channelId=91, content="Not all people who wander are lost.", createdAt="Sun Mar 06 2022 16:50:47", updatedAt="Tue Aug 17 2021 23:09:42")
    comment1987b = Comment(videoId=309, channelId=96, content="She discovered van life is difficult with 2 cats and a dog.", createdAt="Sat Apr 24 2021 06:46:40", updatedAt="Thu Sep 30 2021 13:24:49")
    comment1988b = Comment(videoId=452, channelId=86, content="A good example of a useful vegetable is medicinal rhubarb.", createdAt="Thu Feb 24 2022 10:20:08", updatedAt="Sun Aug 29 2021 03:06:27")
    comment1989b = Comment(videoId=631, channelId=95, content="I honestly find her about as intimidating as a basket of kittens.", createdAt="Sun Oct 17 2021 02:02:54", updatedAt="Thu Feb 24 2022 08:56:41")
    comment1990b = Comment(videoId=724, channelId=88, content="Everyone pretends to like wheat until you mention barley.", createdAt="Fri Oct 15 2021 21:38:13", updatedAt="Thu Sep 30 2021 21:25:44")
    comment1991b = Comment(videoId=370, channelId=92, content="I only enjoy window shopping when the windows are transparent.", createdAt="Sat May 22 2021 14:20:56", updatedAt="Tue Sep 07 2021 09:02:00")
    comment1992b = Comment(videoId=144, channelId=86, content="People who insist on picking their teeth with their elbows are so annoying!", createdAt="Sun Sep 05 2021 06:35:50", updatedAt="Fri Mar 18 2022 23:25:27")
    comment1993b = Comment(videoId=656, channelId=86, content="The sunblock was handed to the girl before practice, but the burned skin was proof she did not apply it.", createdAt="Tue Jun 08 2021 01:16:42", updatedAt="Tue Feb 15 2022 05:12:23")
    comment1994b = Comment(videoId=721, channelId=90, content="It didn't take long for Gary to detect the robbers were amateurs.", createdAt="Tue Apr 20 2021 14:00:52", updatedAt="Wed Feb 09 2022 23:32:00")
    comment1995b = Comment(videoId=587, channelId=97, content="He is good at eating pickles and telling women about his emotional problems.", createdAt="Thu Nov 11 2021 07:02:23", updatedAt="Mon Jun 21 2021 13:32:48")
    comment1996b = Comment(videoId=161, channelId=88, content="The most exciting eureka moment I've had was when I realized that the instructions on food packets were just guidelines.", createdAt="Tue Sep 21 2021 07:55:57", updatedAt="Fri Jul 23 2021 10:13:05")
    comment1997b = Comment(videoId=643, channelId=98, content="The fish dreamed of escaping the fishbowl and into the toilet where he saw his friend go.", createdAt="Sat Feb 26 2022 04:14:15", updatedAt="Wed Mar 09 2022 14:24:39")
    comment1998b = Comment(videoId=604, channelId=95, content="The minute she landed she understood the reason this was a fly-over state.", createdAt="Fri Mar 25 2022 09:03:04", updatedAt="Sat May 01 2021 16:02:01")
    comment1999b = Comment(videoId=589, channelId=93, content="She always speaks to him in a loud voice.", createdAt="Mon Dec 13 2021 06:06:05", updatedAt="Tue Aug 10 2021 20:41:54")
    comment2000b = Comment(videoId=414, channelId=98, content="I was very proud of my nickname throughout high school but today- I couldn’t be any different to what my nickname was.", createdAt="Fri Mar 25 2022 17:26:46", updatedAt="Mon Jan 24 2022 21:50:25")
    comment2001b = Comment(videoId=423, channelId=96, content="She moved forward only because she trusted that the ending she now was going through must be followed by a new beginning.", createdAt="Tue Oct 19 2021 04:58:23", updatedAt="Wed Aug 18 2021 14:50:40")
    comment2002b = Comment(videoId=611, channelId=86, content="Potato wedges probably are not best for relationships.", createdAt="Mon Nov 22 2021 16:17:57", updatedAt="Mon Jul 26 2021 00:07:34")
    comment2003b = Comment(videoId=9, channelId=95, content="The teenage boy was accused of breaking his arm simply to get out of the test.", createdAt="Thu Feb 03 2022 04:56:25", updatedAt="Mon May 03 2021 04:33:57")
    comment2004b = Comment(videoId=626, channelId=94, content="He kept telling himself that one day it would all somehow make sense.", createdAt="Fri Nov 19 2021 20:36:56", updatedAt="Mon Aug 23 2021 09:25:01")
    comment2005b = Comment(videoId=742, channelId=85, content="She works two jobs to make ends meet; at least, that was her reason for not having time to join us.", createdAt="Tue Nov 30 2021 21:06:17", updatedAt="Mon Oct 04 2021 21:27:27")
    comment2006b = Comment(videoId=347, channelId=96, content="My secretary is the only person who truly understands my stamp-collecting obsession.", createdAt="Sat Jun 05 2021 16:39:27", updatedAt="Mon Jun 21 2021 23:23:15")
    comment2007b = Comment(videoId=446, channelId=87, content="They say that dogs are man's best friend, but this cat was setting out to sabotage that theory.", createdAt="Mon Jan 10 2022 19:43:29", updatedAt="Thu Jul 15 2021 14:21:22")
    comment2008b = Comment(videoId=645, channelId=91, content="He had unknowingly taken up sleepwalking as a nighttime hobby.", createdAt="Sat Dec 18 2021 21:17:42", updatedAt="Sat Feb 05 2022 06:21:38")
    comment2009b = Comment(videoId=444, channelId=95, content="My uncle's favorite pastime was building cars out of noodles.", createdAt="Fri Oct 15 2021 22:16:12", updatedAt="Sat May 01 2021 20:56:14")
    comment2010b = Comment(videoId=286, channelId=97, content="On each full moon", createdAt="Sat Oct 16 2021 05:34:32", updatedAt="Mon Feb 28 2022 18:21:21")
    comment2011b = Comment(videoId=379, channelId=88, content="The teens wondered what was kept in the red shed on the far edge of the school grounds.", createdAt="Sat Jul 17 2021 08:08:48", updatedAt="Fri Nov 26 2021 07:48:37")
    comment2012b = Comment(videoId=129, channelId=89, content="The small white buoys marked the location of hundreds of crab pots.", createdAt="Sun Dec 05 2021 08:01:49", updatedAt="Sun Aug 01 2021 23:38:50")
    comment2013b = Comment(videoId=384, channelId=90, content="Each person who knows you has a different perception of who you are.", createdAt="Wed Jan 05 2022 22:57:08", updatedAt="Sat Apr 09 2022 12:45:07")
    comment2014b = Comment(videoId=405, channelId=92, content="The tree fell unexpectedly short.", createdAt="Mon Apr 04 2022 05:23:29", updatedAt="Thu Dec 23 2021 13:10:04")
    comment2015b = Comment(videoId=205, channelId=94, content="The thick foliage and intertwined vines made the hike nearly impossible.", createdAt="Sat Oct 09 2021 22:22:37", updatedAt="Wed May 05 2021 20:00:54")
    comment2016b = Comment(videoId=331, channelId=96, content="Italy is my favorite country; in fact, I plan to spend two weeks there next year.", createdAt="Sun Oct 10 2021 13:30:21", updatedAt="Mon Jul 26 2021 21:25:27")
    comment2017b = Comment(videoId=749, channelId=95, content="Today we gathered moss for my uncle's wedding.", createdAt="Thu Feb 17 2022 19:29:14", updatedAt="Mon Aug 16 2021 17:36:26")
    comment2018b = Comment(videoId=626, channelId=87, content="She had some amazing news to share but nobody to share it with.", createdAt="Sun Jul 18 2021 20:53:50", updatedAt="Mon May 03 2021 13:30:59")
    comment2019b = Comment(videoId=747, channelId=95, content="He hated that he loved what she hated about hate.", createdAt="Mon Oct 18 2021 01:26:19", updatedAt="Fri Nov 19 2021 10:57:15")
    comment2020b = Comment(videoId=766, channelId=97, content="The dead trees waited to be ignited by the smallest spark and seek their revenge.", createdAt="Mon Apr 04 2022 13:47:00", updatedAt="Tue Nov 09 2021 02:29:46")
    comment2021b = Comment(videoId=63, channelId=89, content="They wandered into a strange Tiki bar on the edge of the small beach town.", createdAt="Sun Jan 16 2022 06:56:21", updatedAt="Mon Apr 12 2021 09:03:20")
    comment2022b = Comment(videoId=458, channelId=96, content="This is a Japanese doll.", createdAt="Sat May 15 2021 21:39:52", updatedAt="Mon Jun 21 2021 14:16:07")
    comment2023b = Comment(videoId=779, channelId=95, content="He had unknowingly taken up sleepwalking as a nighttime hobby.", createdAt="Wed Oct 20 2021 17:14:04", updatedAt="Wed Nov 17 2021 18:15:44")
    comment2024b = Comment(videoId=620, channelId=97, content="The rusty nail stood erect, angled at a 45-degree angle, just waiting for the perfect barefoot to come along.", createdAt="Wed May 12 2021 09:31:53", updatedAt="Tue Oct 12 2021 20:13:55")
    comment2025b = Comment(videoId=723, channelId=92, content="Always bring cinnamon buns on a deep-sea diving expedition.", createdAt="Sun Jun 20 2021 10:58:21", updatedAt="Tue Mar 08 2022 09:19:27")
    comment2026b = Comment(videoId=501, channelId=89, content="Kevin embraced his ability to be at the wrong place at the wrong time.", createdAt="Wed Jun 23 2021 05:11:29", updatedAt="Sat Apr 24 2021 10:29:32")
    comment2027b = Comment(videoId=450, channelId=89, content="For some unfathomable reason, the response team didn't consider a lack of milk for my cereal as a proper emergency.", createdAt="Tue Oct 26 2021 11:26:55", updatedAt="Thu Dec 09 2021 15:18:34")
    comment2028b = Comment(videoId=245, channelId=91, content="The pet shop stocks everything you need to keep your anaconda happy.", createdAt="Fri Jan 07 2022 21:15:16", updatedAt="Sun Jan 30 2022 22:21:47")
    comment2029b = Comment(videoId=768, channelId=96, content="I purchased a baby clown from the Russian terrorist black market.", createdAt="Mon May 10 2021 20:04:06", updatedAt="Thu Apr 22 2021 00:30:30")
    comment2030b = Comment(videoId=598, channelId=97, content="The random sentence generator generated a random sentence about a random sentence.", createdAt="Sat Oct 16 2021 02:44:54", updatedAt="Mon Sep 13 2021 00:19:15")
    comment2031b = Comment(videoId=233, channelId=86, content="He wondered if she would appreciate his toenail collection.", createdAt="Tue Apr 13 2021 09:58:35", updatedAt="Sun Jan 02 2022 02:12:58")
    comment2032b = Comment(videoId=519, channelId=91, content="Someone I know recently combined Maple Syrup & buttered Popcorn thinking it would taste like caramel popcorn. It didn’t and they don’t recommend anyone else do it either.", createdAt="Thu May 27 2021 06:31:40", updatedAt="Thu Oct 21 2021 05:02:35")
    comment2033b = Comment(videoId=643, channelId=85, content="The toy brought back fond memories of being lost in the rain forest.", createdAt="Wed Oct 13 2021 05:40:10", updatedAt="Wed Jan 05 2022 09:42:11")
    comment2034b = Comment(videoId=66, channelId=90, content="Nancy thought the best way to create a welcoming home was to line it with barbed wire.", createdAt="Sat Aug 21 2021 23:06:34", updatedAt="Wed Sep 01 2021 16:30:16")
    comment2035b = Comment(videoId=707, channelId=88, content="The two walked down the slot canyon oblivious to the sound of thunder in the distance.", createdAt="Mon Sep 13 2021 11:05:07", updatedAt="Fri Jul 23 2021 19:57:10")
    comment2036b = Comment(videoId=687, channelId=89, content="Edith could decide if she should paint her teeth or brush her nails.", createdAt="Thu Dec 09 2021 09:16:14", updatedAt="Wed Apr 21 2021 11:04:41")
    comment2037b = Comment(videoId=129, channelId=93, content="You can't compare apples and oranges, but what about bananas and plantains?", createdAt="Fri Apr 30 2021 00:58:35", updatedAt="Mon Aug 16 2021 23:00:25")
    comment2038b = Comment(videoId=642, channelId=91, content="The tumbleweed refused to tumble but was more than willing to prance.", createdAt="Tue Jul 06 2021 21:28:29", updatedAt="Mon Oct 04 2021 11:35:22")
    comment2039b = Comment(videoId=153, channelId=85, content="Getting up at dawn is for the birds.", createdAt="Sat Jun 26 2021 18:18:38", updatedAt="Mon Feb 14 2022 18:10:29")
    comment2040b = Comment(videoId=371, channelId=92, content="The irony of the situation wasn't lost on anyone in the room.", createdAt="Mon Aug 02 2021 05:27:40", updatedAt="Sun Oct 03 2021 23:08:47")
    comment2041b = Comment(videoId=67, channelId=89, content="I've traveled all around Africa and still haven't found the gnu who stole my scarf.", createdAt="Tue Jun 22 2021 09:00:41", updatedAt="Thu Mar 03 2022 05:50:14")
    comment2043b = Comment(videoId=299, channelId=86, content="If my calculator had a history, it would be more embarrassing than my browser history.", createdAt="Sat Sep 18 2021 01:24:35", updatedAt="Thu Mar 31 2022 06:43:03")
    comment2044b = Comment(videoId=674, channelId=93, content="Her hair was windswept as she rode in the black convertible.", createdAt="Mon Jul 19 2021 19:00:44", updatedAt="Wed May 26 2021 16:47:26")
    comment2045b = Comment(videoId=53, channelId=98, content="She insisted that cleaning out your closet was the key to good driving.", createdAt="Thu Dec 30 2021 04:42:24", updatedAt="Tue Apr 20 2021 22:02:27")
    comment2046b = Comment(videoId=582, channelId=91, content="On a scale from one to ten, what's your favorite flavor of random grammar?", createdAt="Mon Jan 10 2022 19:47:10", updatedAt="Sat Dec 04 2021 05:50:58")
    comment2047b = Comment(videoId=234, channelId=87, content="They throw cabbage that turns your brain into emotional baggage.", createdAt="Fri Dec 31 2021 19:15:12", updatedAt="Fri May 07 2021 20:01:43")
    comment2048b = Comment(videoId=380, channelId=85, content="She always had an interesting perspective on why the world must be flat.", createdAt="Tue Apr 13 2021 03:57:11", updatedAt="Tue Jun 01 2021 01:03:56")
    comment2049b = Comment(videoId=483, channelId=91, content="They improved dramatically once the lead singer left.", createdAt="Thu Aug 12 2021 09:42:13", updatedAt="Sun Feb 20 2022 01:43:05")
    comment2050b = Comment(videoId=570, channelId=95, content="I may struggle with geography, but I'm sure I'm somewhere around here.", createdAt="Wed Apr 21 2021 14:08:02", updatedAt="Fri Dec 31 2021 03:53:39")
    comment2051b = Comment(videoId=609, channelId=89, content="There was no ice cream in the freezer, nor did they have money to go to the store.", createdAt="Mon Mar 14 2022 08:48:54", updatedAt="Wed Aug 18 2021 10:42:32")
    comment2052b = Comment(videoId=244, channelId=87, content="His get rich quick scheme was to grow a cactus farm.", createdAt="Thu Feb 24 2022 21:10:49", updatedAt="Mon Oct 04 2021 14:20:48")
    comment2053b = Comment(videoId=767, channelId=86, content="Her daily goal was to improve on yesterday.", createdAt="Sat May 15 2021 13:05:23", updatedAt="Sun Apr 10 2022 15:54:18")
    comment2054b = Comment(videoId=143, channelId=89, content="He poured rocks in the dungeon of his mind.", createdAt="Wed Nov 10 2021 13:27:06", updatedAt="Fri Jun 04 2021 05:09:45")
    comment2055b = Comment(videoId=746, channelId=90, content="It's never been my responsibility to glaze the donuts.", createdAt="Mon Jul 12 2021 15:12:37", updatedAt="Wed May 19 2021 10:48:37")
    comment2056b = Comment(videoId=749, channelId=86, content="The snow-covered path was no help in finding his way out of the back-country.", createdAt="Fri May 14 2021 02:25:53", updatedAt="Wed Feb 16 2022 01:18:29")
    comment2057b = Comment(videoId=278, channelId=86, content="After fighting off the alligator, Brian still had to face the anaconda.", createdAt="Thu Jun 24 2021 09:54:53", updatedAt="Tue Dec 28 2021 16:33:44")
    comment2058b = Comment(videoId=634, channelId=85, content="I've always wanted to go to Tajikistan, but my cat would miss me.", createdAt="Wed Sep 01 2021 03:32:13", updatedAt="Thu Sep 30 2021 11:40:20")
    comment2059b = Comment(videoId=345, channelId=90, content="Beach-combing replaced wine tasting as his new obsession.", createdAt="Sat Apr 17 2021 11:36:31", updatedAt="Tue Oct 12 2021 09:41:33")
    comment2060b = Comment(videoId=84, channelId=86, content="The elephant didn't want to talk about the person in the room.", createdAt="Tue Jul 27 2021 06:21:00", updatedAt="Fri Oct 15 2021 03:37:53")
    comment2061b = Comment(videoId=457, channelId=87, content="The waves were crashing on the shore; it was a lovely sight.", createdAt="Tue Oct 12 2021 04:30:49", updatedAt="Mon Nov 15 2021 21:21:41")



    comments = [
        comment1, comment2, comment3, comment4, comment5, comment6, comment7, comment8, comment9, comment10, comment11, comment12, comment13, comment14, comment15, comment16, comment17, comment18, comment19, comment20, comment21, comment22, comment23, comment24, comment25, comment26,
        comment27, comment28, comment29, comment30, comment31, comment32, comment33, comment34, comment35, comment37, comment38, comment39, comment40, comment41, comment42, comment43, comment44, comment45, comment46, comment47, comment48, comment49, comment50, comment51, comment52,
        comment53, comment54, comment55, comment56, comment57, comment58, comment59, comment60, comment61, comment62, comment63, comment64, comment65, comment66, comment67, comment68, comment69, comment70, comment71, comment72, comment73, comment74, comment75, comment76, comment77, comment78,
        comment79, comment80, comment81, comment82, comment83, comment84, comment85, comment86, comment87, comment88, comment89, comment90, comment91, comment92, comment93, comment94, comment95, comment96, comment97, comment98, comment99, comment100, comment101, comment102, comment103, comment104,
        comment105, comment106, comment107, comment108, comment109, comment110, comment111, comment112, comment113, comment114, comment115, comment116, comment117, comment118, comment119, comment120, comment121, comment122, comment123, comment124, comment125, comment126, comment127, comment128,
        comment129, comment130, comment131, comment132, comment133, comment134, comment135, comment136, comment137, comment138, comment139, comment140, comment141, comment142, comment143, comment144, comment145, comment146, comment147, comment149, comment150, comment151, comment152,
        comment153, comment154, comment155, comment156, comment157, comment158, comment160, comment161, comment162, comment163, comment164, comment165, comment166, comment167, comment168, comment169, comment170, comment171, comment172, comment173, comment174, comment175, comment176,
        comment177, comment178, comment179, comment180, comment181, comment182, comment183, comment184, comment185, comment186, comment187, comment188, comment189, comment190, comment191, comment192, comment193, comment194, comment195, comment196, comment197, comment198, comment199, comment200,
        comment201, comment202, comment203, comment204, comment205, comment206, comment207, comment208, comment209, comment210, comment211, comment212, comment213, comment214, comment215, comment216, comment217, comment218, comment219, comment220, comment222, comment223, comment224,
        comment225, comment226, comment227, comment228, comment229, comment230, comment231, comment232, comment233, comment234, comment235, comment236, comment237, comment238, comment239, comment240, comment241, comment242, comment243, comment244, comment245, comment246, comment247, comment248,
        comment249, comment250, comment251, comment252, comment253, comment254, comment255, comment256, comment257, comment258, comment259, comment260, comment261, comment262, comment263, comment264, comment265, comment266, comment267, comment268, comment269, comment270, comment271, comment272,
        comment273, comment274, comment275, comment276, comment277, comment278, comment279, comment280, comment281, comment282, comment283, comment284, comment285, comment286, comment287, comment288, comment289, comment290, comment291, comment292, comment293, comment294, comment295, comment296,
        comment297, comment298, comment299, comment300, comment301, comment302, comment303, comment304, comment305, comment306, comment307, comment308, comment309, comment310, comment311, comment312, comment313, comment314, comment315, comment316, comment317, comment318, comment319, comment320,
        comment321, comment322, comment323, comment324, comment325, comment326, comment327, comment328, comment329, comment330, comment331, comment332, comment333, comment334, comment335, comment336, comment337, comment338, comment339, comment340, comment341, comment342, comment343, comment344,
        comment345, comment346, comment347, comment348, comment349, comment350, comment351, comment352, comment353, comment354, comment355, comment356, comment357, comment358, comment359, comment360, comment362, comment363, comment364, comment365, comment366, comment367, comment368,
        comment369, comment370, comment371, comment372, comment373, comment374, comment375, comment376, comment377, comment378, comment379, comment380, comment381, comment382, comment383, comment384, comment385, comment386, comment387, comment388, comment389, comment390, comment391, comment392,
        comment393, comment394, comment395, comment396, comment397, comment398, comment399, comment400, comment401, comment402, comment403, comment404, comment405, comment406, comment407, comment408, comment409, comment410, comment411, comment412, comment413, comment414, comment415, comment416,
        comment417, comment418, comment419, comment420, comment421, comment422, comment423, comment424, comment425, comment426, comment427, comment428, comment429, comment430, comment431, comment432, comment433, comment434, comment435, comment436, comment437, comment438, comment439, comment440,
        comment441, comment442, comment443, comment444, comment445, comment446, comment447, comment449, comment450, comment451, comment452, comment453, comment454, comment455, comment456, comment457, comment458, comment459, comment460, comment461, comment462, comment463, comment464,
        comment465, comment466, comment467, comment468, comment469, comment470, comment471, comment472, comment473, comment474, comment475, comment476, comment477, comment479, comment480, comment481, comment482, comment483, comment484, comment485, comment486, comment487, comment488,
        comment489, comment490, comment491, comment492, comment493, comment494, comment495, comment496, comment497, comment498, comment499, comment500, comment501, comment502, comment503, comment504, comment505, comment506, comment507, comment508, comment509, comment510, comment511, comment512,
        comment513, comment514, comment515, comment516, comment517, comment518, comment519, comment520, comment521, comment522, comment523, comment524, comment525, comment526, comment527, comment528, comment529, comment530, comment531, comment533, comment534, comment535, comment536,
        comment537, comment538, comment539, comment540, comment541, comment542, comment543, comment544, comment545, comment546, comment547, comment548, comment549, comment550, comment551, comment552, comment553, comment554, comment555, comment556, comment558, comment559, comment560,
        comment561, comment562, comment563, comment564, comment565, comment566, comment567, comment568, comment569, comment570, comment571, comment572, comment573, comment574, comment575, comment576, comment577, comment578, comment579, comment580, comment581, comment582, comment583, comment584,
        comment585, comment586, comment588, comment589, comment590, comment591, comment592, comment593, comment594, comment595, comment596, comment597, comment598, comment599, comment600, comment601, comment602, comment603, comment604, comment605, comment606, comment607, comment608,
        comment609, comment610, comment611, comment612, comment613, comment614, comment615, comment616, comment617, comment618, comment619, comment620, comment621, comment622, comment623, comment624, comment625, comment626, comment627, comment628, comment629, comment630, comment631, comment632,
        comment633, comment634, comment635, comment636, comment637, comment638, comment639, comment641, comment642, comment643, comment646, comment647, comment648, comment649, comment650, comment651, comment652, comment653, comment654, comment655, comment656,
        comment657, comment658, comment659, comment660, comment661, comment662, comment663, comment665, comment666, comment667, comment668, comment669, comment670, comment671, comment672, comment673, comment674, comment675, comment676, comment677, comment678, comment679, comment680,
        comment681, comment682, comment683, comment684, comment685, comment686, comment687, comment688, comment689, comment690, comment692, comment693, comment694, comment695, comment696, comment697, comment698, comment699, comment700, comment701, comment702, comment703, comment704,
        comment705, comment706, comment707, comment708, comment709, comment710, comment711, comment712, comment713, comment714, comment715, comment716, comment717, comment718, comment719, comment720, comment721, comment722, comment723, comment724, comment725, comment726, comment727, comment728,
        comment729, comment730, comment731, comment732, comment733, comment734, comment735, comment736, comment737, comment738, comment739, comment740, comment741, comment742, comment743, comment744, comment745, comment746, comment747, comment748, comment749, comment750, comment751, comment752,
        comment753, comment754, comment755, comment756, comment757, comment758, comment759, comment760, comment761, comment762, comment763, comment764, comment765, comment766, comment767, comment768, comment769, comment770, comment771, comment772, comment773, comment774, comment775, comment776,
        comment777, comment778, comment779, comment780, comment781, comment782, comment783, comment785, comment786, comment787, comment788, comment789, comment790, comment791, comment792, comment793, comment794, comment795, comment796, comment797, comment798, comment799, comment800,
        comment801, comment802, comment803, comment804, comment805, comment806, comment807, comment808, comment809, comment810, comment811, comment812, comment813, comment814, comment815, comment816, comment817, comment818, comment819, comment820, comment821, comment822, comment823, comment824,
        comment825, comment826, comment827, comment828, comment829, comment830, comment831, comment832, comment833, comment834, comment835, comment836, comment837, comment838, comment839, comment840, comment841, comment842, comment843, comment844, comment845, comment846, comment847, comment848,
        comment849, comment850, comment851, comment852, comment853, comment854, comment856, comment857, comment858, comment859, comment860, comment861, comment862, comment863, comment864, comment865, comment866, comment867, comment868, comment869, comment870, comment871, comment872,
        comment873, comment874, comment875, comment876, comment877, comment878, comment879, comment880, comment881, comment882, comment883, comment884, comment885, comment886, comment887, comment888, comment889, comment890, comment891, comment892, comment893, comment894, comment895, comment896,
        comment897, comment898, comment899, comment900, comment901, comment902, comment903, comment904, comment905, comment906, comment907, comment908, comment909, comment910, comment911, comment912, comment913, comment914, comment915, comment916, comment917, comment918, comment919, comment920,
        comment921, comment922, comment923, comment924, comment925, comment926, comment927, comment928, comment929, comment930, comment931, comment932, comment933, comment934, comment935, comment936, comment937, comment938, comment939, comment940, comment941, comment942, comment943, comment944,
        comment945, comment946, comment947, comment948, comment949, comment950, comment952, comment953, comment954, comment955, comment956, comment958, comment959, comment960, comment961, comment962, comment963, comment964, comment965, comment966, comment967, comment968,
        comment969, comment970, comment971, comment972, comment973, comment974, comment975, comment976, comment977, comment978, comment979, comment981, comment982, comment983, comment984, comment985, comment986, comment987, comment988, comment989, comment990, comment991, comment992,
        comment993, comment994, comment995, comment996, comment997, comment998, comment999, comment1000, comment1001, comment1003, comment1004, comment1005, comment1006, comment1007, comment1008, comment1009, comment1010, comment1011, comment1012, comment1013, comment1014, comment1015,
        comment1016, comment1017, comment1018, comment1019, comment1020, comment1021, comment1022, comment1023, comment1024, comment1025, comment1026, comment1027, comment1028, comment1029, comment1030, comment1031, comment1032, comment1033, comment1034, comment1035, comment1036, comment1037,
        comment1038, comment1039, comment1040, comment1041, comment1042, comment1043, comment1044, comment1045, comment1046, comment1047, comment1048, comment1049, comment1050, comment1051, comment1052, comment1054, comment1055, comment1056, comment1057, comment1058, comment1059,
        comment1060, comment1061, comment1062, comment1063, comment1064, comment1065, comment1066, comment1067, comment1068, comment1069, comment1070, comment1071, comment1072, comment1074, comment1075, comment1076, comment1077, comment1078, comment1079, comment1080, comment1081,
        comment1082, comment1083, comment1084, comment1085, comment1086, comment1087, comment1088, comment1089, comment1090, comment1091, comment1092, comment1093, comment1094, comment1095, comment1096, comment1097, comment1098, comment1099, comment1100, comment1101, comment1102, comment1103,
        comment1104, comment1105, comment1106, comment1107, comment1108, comment1109, comment1110, comment1111, comment1112, comment1113, comment1114, comment1115, comment1116, comment1117, comment1118, comment1119, comment1120, comment1121, comment1122, comment1123, comment1124, comment1125,
        comment1126, comment1127, comment1128, comment1129, comment1130, comment1131, comment1132, comment1133, comment1134, comment1135, comment1136, comment1137, comment1138, comment1139, comment1140, comment1141, comment1142, comment1143, comment1144, comment1145, comment1146, comment1147,
        comment1148, comment1149, comment1150, comment1151, comment1152, comment1153, comment1155, comment1157, comment1158, comment1159, comment1160, comment1161, comment1162, comment1163, comment1164, comment1165, comment1166, comment1167, comment1168, comment1169,
        comment1170, comment1171, comment1172, comment1173, comment1174, comment1175, comment1176, comment1178, comment1179, comment1180, comment1181, comment1182, comment1183, comment1184, comment1185, comment1186, comment1187, comment1188, comment1189, comment1190, comment1191,
        comment1192, comment1194, comment1195, comment1196, comment1197, comment1198, comment1199, comment1200, comment1201, comment1202, comment1204, comment1205, comment1206, comment1207, comment1208, comment1209, comment1210, comment1211, comment1212, comment1213,
        comment1214, comment1215, comment1216, comment1217, comment1218, comment1219, comment1220, comment1221, comment1222, comment1223, comment1224, comment1225, comment1226, comment1228, comment1229, comment1230, comment1231, comment1232, comment1233, comment1234, comment1235,
        comment1236, comment1237, comment1238, comment1239, comment1240, comment1241, comment1242, comment1243, comment1244, comment1245, comment1246, comment1247, comment1248, comment1249, comment1250, comment1251, comment1252, comment1253, comment1254, comment1255, comment1256, comment1257,
        comment1258, comment1259, comment1260, comment1261, comment1262, comment1263, comment1264, comment1265, comment1266, comment1267, comment1268, comment1269, comment1270, comment1271, comment1272, comment1273, comment1274, comment1275, comment1276, comment1277, comment1278, comment1279,
        comment1280, comment1281, comment1282, comment1283, comment1284, comment1285, comment1287, comment1288, comment1289, comment1290, comment1291, comment1292, comment1293, comment1294, comment1295, comment1296, comment1297, comment1298, comment1299, comment1300, comment1301,
        comment1302, comment1303, comment1304, comment1305, comment1306, comment1307, comment1308, comment1309, comment1310, comment1311, comment1312, comment1313, comment1314, comment1315, comment1316, comment1317, comment1318, comment1319, comment1320, comment1321, comment1322, comment1323,
        comment1324, comment1325, comment1326, comment1327, comment1329, comment1330, comment1331, comment1332, comment1333, comment1334, comment1335, comment1336, comment1337, comment1338, comment1339, comment1340, comment1341, comment1342, comment1343, comment1344, comment1345,
        comment1346, comment1347, comment1348, comment1349, comment1350, comment1351, comment1352, comment1353, comment1354, comment1355, comment1356, comment1357, comment1358, comment1359, comment1360, comment1361, comment1362, comment1364, comment1365, comment1366, comment1367,
        comment1368, comment1369, comment1370, comment1371, comment1372, comment1373, comment1374, comment1375, comment1376, comment1377, comment1378, comment1380, comment1381, comment1382, comment1384, comment1385, comment1386, comment1387, comment1388, comment1389,
        comment1390, comment1391, comment1392, comment1393, comment1394, comment1395, comment1396, comment1397, comment1398, comment1399, comment1400, comment1401, comment1402, comment1403, comment1404, comment1406, comment1407, comment1408, comment1409, comment1410, comment1411,
        comment1412, comment1413, comment1414, comment1415, comment1416, comment1417, comment1418, comment1419, comment1420, comment1421, comment1422, comment1423, comment1424, comment1425, comment1426, comment1427, comment1428, comment1429, comment1430, comment1431, comment1432, comment1433,
        comment1434, comment1435, comment1436, comment1437, comment1438, comment1439, comment1440, comment1441, comment1442, comment1444, comment1445, comment1446, comment1447, comment1448, comment1449, comment1450, comment1451, comment1452, comment1453, comment1454, comment1455,
        comment1457, comment1458, comment1459, comment1460, comment1461, comment1462, comment1463, comment1464, comment1465, comment1466, comment1467, comment1468, comment1469, comment1470, comment1471, comment1472, comment1473, comment1475, comment1476, comment1477,
        comment1478, comment1479, comment1480, comment1481, comment1482, comment1483, comment1484, comment1485, comment1486, comment1487, comment1488, comment1489, comment1490, comment1491, comment1492, comment1493, comment1494, comment1495, comment1496, comment1497, comment1498, comment1499,
        comment1500, comment1501, comment1502, comment1503, comment1504, comment1505, comment1506, comment1507, comment1508, comment1509, comment1510, comment1511, comment1512, comment1513, comment1514, comment1515, comment1516, comment1517, comment1518, comment1519, comment1520, comment1521,
        comment1522, comment1523, comment1524, comment1525, comment1526, comment1527, comment1528, comment1529, comment1530, comment1531, comment1532, comment1533, comment1534, comment1535, comment1536, comment1537, comment1538, comment1539, comment1540, comment1541, comment1542, comment1543,
        comment1544, comment1545, comment1546, comment1547, comment1548, comment1549, comment1550, comment1551, comment1552, comment1553, comment1554, comment1556, comment1557, comment1558, comment1560, comment1561, comment1562, comment1563, comment1564, comment1565,
        comment1566, comment1567, comment1568, comment1569, comment1570, comment1571, comment1573, comment1574, comment1575, comment1576, comment1577, comment1578, comment1579, comment1580, comment1581, comment1582, comment1583, comment1584, comment1585, comment1586, comment1587,
        comment1588, comment1589, comment1590, comment1591, comment1592, comment1593, comment1594, comment1595, comment1596, comment1597, comment1598, comment1600, comment1601, comment1602, comment1603, comment1604, comment1605, comment1606, comment1607, comment1608, comment1609,
        comment1610, comment1611, comment1612, comment1613, comment1614, comment1615, comment1616, comment1617, comment1618, comment1619, comment1620, comment1621, comment1622, comment1623, comment1624, comment1625, comment1626, comment1627, comment1628, comment1629, comment1631,
        comment1632, comment1633, comment1634, comment1635, comment1636, comment1637, comment1638, comment1639, comment1640, comment1641, comment1642, comment1643, comment1644, comment1645, comment1646, comment1647, comment1648, comment1649, comment1650, comment1651, comment1652, comment1653,
        comment1654, comment1655, comment1656, comment1657, comment1658, comment1659, comment1660, comment1661, comment1662, comment1663, comment1664, comment1665, comment1666, comment1667, comment1668, comment1669, comment1670, comment1671, comment1672, comment1673, comment1674, comment1675,
        comment1676, comment1677, comment1678, comment1679, comment1680, comment1681, comment1682, comment1683, comment1684, comment1685, comment1686, comment1687, comment1688, comment1689, comment1690, comment1691, comment1692, comment1693, comment1694, comment1695, comment1696, comment1697,
        comment1698, comment1699, comment1700, comment1701, comment1702, comment1703, comment1704, comment1705, comment1706, comment1707, comment1708, comment1709, comment1710, comment1711, comment1712, comment1713, comment1714, comment1715, comment1716, comment1717, comment1718, comment1719,
        comment1720, comment1721, comment1722, comment1723, comment1724, comment1725, comment1726, comment1727, comment1728, comment1729, comment1730, comment1731, comment1732, comment1733, comment1734, comment1735, comment1736, comment1737, comment1738, comment1739, comment1740, comment1741,
        comment1742, comment1743, comment1744, comment1745, comment1746, comment1747, comment1748, comment1749, comment1750, comment1751, comment1752, comment1753, comment1754, comment1755, comment1756, comment1757, comment1758, comment1759, comment1760, comment1761, comment1762, comment1763,
        comment1764, comment1765, comment1766, comment1767, comment1768, comment1769, comment1770, comment1771, comment1772, comment1773, comment1774, comment1775, comment1776, comment1777, comment1778, comment1779, comment1780, comment1781, comment1782, comment1783, comment1784, comment1785,
        comment1786, comment1787, comment1788, comment1789, comment1790, comment1791, comment1792, comment1793, comment1794, comment1795, comment1796, comment1797, comment1798, comment1799, comment1800, comment1801, comment1802, comment1803, comment1804, comment1805, comment1806, comment1807,
        comment1808, comment1809, comment1811, comment1812, comment1813, comment1814, comment1815, comment1816, comment1817, comment1818, comment1819, comment1820, comment1821, comment1822, comment1823, comment1824, comment1825, comment1826, comment1827, comment1828, comment1829,
        comment1830, comment1832, comment1833, comment1834, comment1835, comment1836, comment1837, comment1838, comment1839, comment1840, comment1841, comment1842, comment1843, comment1844, comment1845, comment1846, comment1847, comment1848, comment1849, comment1850, comment1851,
        comment1852, comment1853, comment1854, comment1855, comment1856, comment1857, comment1858, comment1859, comment1860, comment1862, comment1863, comment1864, comment1865, comment1866, comment1867, comment1868, comment1869, comment1870, comment1871, comment1872, comment1873,
        comment1874, comment1875, comment1876, comment1877, comment1878, comment1879, comment1880, comment1881, comment1882, comment1883, comment1885, comment1886, comment1887, comment1888, comment1889, comment1890, comment1891, comment1892, comment1893, comment1894, comment1895,
        comment1896, comment1897, comment1898, comment1899, comment1900, comment1901, comment1902, comment1903, comment1904, comment1905, comment1906, comment1907, comment1908, comment1909, comment1910, comment1911, comment1912, comment1913, comment1914, comment1915, comment1916, comment1917,
        comment1918, comment1919, comment1920, comment1921, comment1922, comment1924, comment1925, comment1926, comment1927, comment1928, comment1929, comment1930, comment1931, comment1932, comment1933, comment1934, comment1935, comment1936, comment1937, comment1938, comment1939,
        comment1940, comment1941, comment1942, comment1943, comment1944, comment1945, comment1946, comment1947, comment1948, comment1949, comment1950, comment1951, comment1952, comment1953, comment1954, comment1955, comment1956, comment1957, comment1958, comment1959, comment1960, comment1961,
        comment1962, comment1963, comment1964, comment1965, comment1966, comment1968, comment1969, comment1970, comment1971, comment1972, comment1973, comment1974, comment1975, comment1976, comment1977, comment1978, comment1979, comment1980, comment1981, comment1982, comment1983,
        comment1984, comment1985, comment1986, comment1987, comment1988, comment1990, comment1991, comment1992, comment1993, comment1994, comment1995, comment1996, comment1997, comment1998, comment1999, comment2000, comment2001, comment2002, comment2003, comment2004, 
        comment2006, comment2007, comment2009, comment2010, comment2011, comment2012, comment2013, comment2014, comment2015, comment2016, comment2017, comment2018, comment2019, comment2020, comment2021, comment2022, comment2024, comment2025, comment2026, comment2027,
        comment2028, comment2029, comment2030, comment2031, comment2032, comment2033, comment2034, comment2035, comment2037, comment2038, comment2039, comment2040, comment2041, comment2042, comment2043, comment2044, comment2045, comment2046, comment2047, comment2048, comment2049,
        comment2050, comment2051, comment2052, comment2053, comment2054, comment2055, comment2056, comment2058, comment2059, comment2060, comment2061,
        
        # DUPLICATE COMMENTS:
        comment1b,
        comment2b,
        comment3b,
        comment4b,
        comment5b,
        comment6b,
        comment7b,
        comment8b,
        comment9b,
        comment10b,
        comment11b,
        comment12b,
        comment13b,
        comment14b,
        comment15b,
        comment16b,
        comment17b,
        comment18b,
        comment19b,
        comment20b,
        comment21b,
        comment22b,
        comment23b,
        comment24b,
        comment25b,
        comment26b,
        comment27b,
        comment28b,
        comment29b,
        comment30b,
        comment31b,
        comment32b,
        comment33b,
        comment34b,
        comment35b,
        comment36b,
        comment37b,
        comment38b,
        comment39b,
        comment40b,
        comment41b,
        comment42b,
        comment43b,
        comment44b,
        comment45b,
        comment46b,
        comment47b,
        comment48b,
        comment49b,
        comment50b,
        comment51b,
        comment52b,
        comment53b,
        comment54b,
        comment55b,
        comment56b,
        comment57b,
        comment58b,
        comment59b,
        comment60b,
        comment61b,
        comment62b,
        comment63b,
        comment64b,
        comment65b,
        comment66b,
        comment67b,
        comment68b,
        comment69b,
        comment70b,
        comment71b,
        comment72b,
        comment73b,
        comment74b,
        comment75b,
        comment76b,
        comment77b,
        comment78b,
        comment79b,
        comment80b,
        comment81b,
        comment82b,
        comment83b,
        comment84b,
        comment85b,
        comment86b,
        comment87b,
        comment88b,
        comment89b,
        comment90b,
        comment91b,
        comment92b,
        comment94b,
        comment95b,
        comment96b,
        comment97b,
        comment98b,
        comment99b,
        comment100b,
        comment101b,
        comment104b,
        comment105b,
        comment106b,
        comment107b,
        comment108b,
        comment109b,
        comment110b,
        comment111b,
        comment112b,
        comment113b,
        comment114b,
        comment115b,
        comment116b,
        comment117b,
        comment118b,
        comment119b,
        comment120b,
        comment121b,
        comment122b,
        comment123b,
        comment124b,
        comment125b,
        comment126b,
        comment127b,
        comment128b,
        comment129b,
        comment130b,
        comment131b,
        comment132b,
        comment134b,
        comment135b,
        comment136b,
        comment137b,
        comment138b,
        comment139b,
        comment140b,
        comment141b,
        comment142b,
        comment143b,
        comment144b,
        comment145b,
        comment146b,
        comment147b,
        comment148b,
        comment149b,
        comment150b,
        comment151b,
        comment152b,
        comment153b,
        comment154b,
        comment155b,
        comment156b,
        comment157b,
        comment158b,
        comment159b,
        comment160b,
        comment161b,
        comment162b,
        comment163b,
        comment164b,
        comment165b,
        comment166b,
        comment167b,
        comment168b,
        comment169b,
        comment170b,
        comment171b,
        comment172b,
        comment173b,
        comment174b,
        comment175b,
        comment176b,
        comment177b,
        comment178b,
        comment179b,
        comment180b,
        comment181b,
        comment182b,
        comment183b,
        comment184b,
        comment185b,
        comment186b,
        comment187b,
        comment188b,
        comment189b,
        comment190b,
        comment191b,
        comment192b,
        comment193b,
        comment194b,
        comment195b,
        comment196b,
        comment197b,
        comment198b,
        comment200b,
        comment201b,
        comment202b,
        comment203b,
        comment204b,
        comment205b,
        comment206b,
        comment207b,
        comment208b,
        comment209b,
        comment210b,
        comment212b,
        comment214b,
        comment215b,
        comment216b,
        comment217b,
        comment218b,
        comment219b,
        comment220b,
        comment221b,
        comment222b,
        comment223b,
        comment224b,
        comment225b,
        comment226b,
        comment227b,
        comment228b,
        comment229b,
        comment230b,
        comment231b,
        comment234b,
        comment235b,
        comment236b,
        comment237b,
        comment238b,
        comment239b,
        comment240b,
        comment241b,
        comment242b,
        comment243b,
        comment244b,
        comment245b,
        comment246b,
        comment247b,
        comment248b,
        comment249b,
        comment250b,
        comment251b,
        comment252b,
        comment253b,
        comment254b,
        comment255b,
        comment256b,
        comment257b,
        comment258b,
        comment259b,
        comment260b,
        comment261b,
        comment262b,
        comment263b,
        comment264b,
        comment265b,
        comment266b,
        comment268b,
        comment269b,
        comment270b,
        comment271b,
        comment272b,
        comment273b,
        comment274b,
        comment276b,
        comment277b,
        comment278b,
        comment280b,
        comment281b,
        comment282b,
        comment283b,
        comment284b,
        comment285b,
        comment286b,
        comment287b,
        comment288b,
        comment289b,
        comment290b,
        comment291b,
        comment292b,
        comment293b,
        comment294b,
        comment295b,
        comment296b,
        comment297b,
        comment298b,
        comment299b,
        comment300b,
        comment301b,
        comment302b,
        comment303b,
        comment304b,
        comment305b,
        comment306b,
        comment307b,
        comment308b,
        comment309b,
        comment310b,
        comment311b,
        comment312b,
        comment313b,
        comment314b,
        comment315b,
        comment316b,
        comment317b,
        comment319b,
        comment320b,
        comment321b,
        comment322b,
        comment323b,
        comment324b,
        comment326b,
        comment327b,
        comment328b,
        comment329b,
        comment330b,
        comment331b,
        comment332b,
        comment333b,
        comment334b,
        comment335b,
        comment336b,
        comment337b,
        comment338b,
        comment339b,
        comment340b,
        comment341b,
        comment342b,
        comment343b,
        comment344b,
        comment345b,
        comment346b,
        comment347b,
        comment348b,
        comment349b,
        comment350b,
        comment351b,
        comment352b,
        comment353b,
        comment354b,
        comment355b,
        comment356b,
        comment357b,
        comment358b,
        comment359b,
        comment360b,
        comment361b,
        comment362b,
        comment363b,
        comment364b,
        comment365b,
        comment366b,
        comment367b,
        comment368b,
        comment369b,
        comment371b,
        comment372b,
        comment373b,
        comment374b,
        comment375b,
        comment376b,
        comment377b,
        comment378b,
        comment379b,
        comment380b,
        comment381b,
        comment382b,
        comment383b,
        comment384b,
        comment385b,
        comment386b,
        comment387b,
        comment388b,
        comment389b,
        comment390b,
        comment391b,
        comment392b,
        comment393b,
        comment394b,
        comment395b,
        comment396b,
        comment397b,
        comment398b,
        comment399b,
        comment400b,
        comment401b,
        comment402b,
        comment403b,
        comment404b,
        comment405b,
        comment407b,
        comment408b,
        comment409b,
        comment410b,
        comment411b,
        comment412b,
        comment413b,
        comment414b,
        comment415b,
        comment416b,
        comment417b,
        comment418b,
        comment419b,
        comment420b,
        comment421b,
        comment422b,
        comment423b,
        comment424b,
        comment425b,
        comment426b,
        comment427b,
        comment428b,
        comment429b,
        comment430b,
        comment431b,
        comment432b,
        comment433b,
        comment434b,
        comment435b,
        comment436b,
        comment437b,
        comment438b,
        comment439b,
        comment440b,
        comment441b,
        comment442b,
        comment443b,
        comment444b,
        comment445b,
        comment446b,
        comment447b,
        comment448b,
        comment449b,
        comment450b,
        comment451b,
        comment452b,
        comment453b,
        comment454b,
        comment455b,
        comment456b,
        comment457b,
        comment458b,
        comment459b,
        comment460b,
        comment461b,
        comment462b,
        comment463b,
        comment464b,
        comment465b,
        comment466b,
        comment467b,
        comment468b,
        comment469b,
        comment470b,
        comment471b,
        comment472b,
        comment473b,
        comment474b,
        comment475b,
        comment476b,
        comment477b,
        comment478b,
        comment479b,
        comment481b,
        comment482b,
        comment483b,
        comment484b,
        comment485b,
        comment486b,
        comment487b,
        comment488b,
        comment489b,
        comment490b,
        comment491b,
        comment492b,
        comment493b,
        comment494b,
        comment495b,
        comment496b,
        comment497b,
        comment498b,
        comment499b,
        comment500b,
        comment501b,
        comment502b,
        comment503b,
        comment504b,
        comment505b,
        comment506b,
        comment507b,
        comment508b,
        comment509b,
        comment510b,
        comment511b,
        comment512b,
        comment513b,
        comment514b,
        comment515b,
        comment516b,
        comment517b,
        comment518b,
        comment519b,
        comment520b,
        comment521b,
        comment522b,
        comment523b,
        comment524b,
        comment525b,
        comment526b,
        comment527b,
        comment528b,
        comment529b,
        comment531b,
        comment532b,
        comment533b,
        comment534b,
        comment535b,
        comment536b,
        comment537b,
        comment538b,
        comment539b,
        comment541b,
        comment542b,
        comment543b,
        comment544b,
        comment545b,
        comment546b,
        comment547b,
        comment548b,
        comment549b,
        comment550b,
        comment551b,
        comment553b,
        comment554b,
        comment555b,
        comment556b,
        comment557b,
        comment558b,
        comment559b,
        comment560b,
        comment561b,
        comment562b,
        comment563b,
        comment564b,
        comment565b,
        comment566b,
        comment567b,
        comment568b,
        comment569b,
        comment570b,
        comment571b,
        comment572b,
        comment573b,
        comment574b,
        comment575b,
        comment576b,
        comment577b,
        comment578b,
        comment579b,
        comment580b,
        comment581b,
        comment582b,
        comment583b,
        comment584b,
        comment585b,
        comment586b,
        comment587b,
        comment588b,
        comment589b,
        comment590b,
        comment591b,
        comment592b,
        comment593b,
        comment594b,
        comment595b,
        comment596b,
        comment598b,
        comment599b,
        comment600b,
        comment601b,
        comment602b,
        comment603b,
        comment604b,
        comment605b,
        comment606b,
        comment607b,
        comment608b,
        comment609b,
        comment610b,
        comment611b,
        comment612b,
        comment613b,
        comment614b,
        comment615b,
        comment617b,
        comment619b,
        comment620b,
        comment621b,
        comment622b,
        comment623b,
        comment624b,
        comment625b,
        comment626b,
        comment627b,
        comment628b,
        comment629b,
        comment630b,
        comment631b,
        comment632b,
        comment633b,
        comment634b,
        comment635b,
        comment636b,
        comment637b,
        comment638b,
        comment639b,
        comment640b,
        comment641b,
        comment642b,
        comment643b,
        comment644b,
        comment645b,
        comment646b,
        comment647b,
        comment648b,
        comment649b,
        comment650b,
        comment651b,
        comment652b,
        comment653b,
        comment654b,
        comment655b,
        comment656b,
        comment657b,
        comment658b,
        comment659b,
        comment660b,
        comment661b,
        comment662b,
        comment663b,
        comment664b,
        comment665b,
        comment666b,
        comment667b,
        comment668b,
        comment669b,
        comment670b,
        comment671b,
        comment672b,
        comment673b,
        comment674b,
        comment675b,
        comment676b,
        comment677b,
        comment678b,
        comment679b,
        comment680b,
        comment681b,
        comment682b,
        comment683b,
        comment684b,
        comment685b,
        comment686b,
        comment687b,
        comment688b,
        comment689b,
        comment690b,
        comment691b,
        comment692b,
        comment693b,
        comment694b,
        comment695b,
        comment696b,
        comment697b,
        comment698b,
        comment699b,
        comment700b,
        comment701b,
        comment702b,
        comment703b,
        comment704b,
        comment705b,
        comment706b,
        comment707b,
        comment708b,
        comment709b,
        comment710b,
        comment711b,
        comment712b,
        comment713b,
        comment714b,
        comment715b,
        comment716b,
        comment717b,
        comment718b,
        comment719b,
        comment720b,
        comment721b,
        comment722b,
        comment723b,
        comment724b,
        comment725b,
        comment726b,
        comment727b,
        comment728b,
        comment729b,
        comment730b,
        comment731b,
        comment732b,
        comment733b,
        comment734b,
        comment735b,
        comment736b,
        comment737b,
        comment738b,
        comment739b,
        comment740b,
        comment741b,
        comment742b,
        comment743b,
        comment744b,
        comment745b,
        comment746b,
        comment747b,
        comment748b,
        comment749b,
        comment750b,
        comment751b,
        comment752b,
        comment753b,
        comment754b,
        comment755b,
        comment756b,
        comment757b,
        comment759b,
        comment760b,
        comment761b,
        comment762b,
        comment763b,
        comment764b,
        comment765b,
        comment766b,
        comment767b,
        comment768b,
        comment769b,
        comment770b,
        comment771b,
        comment772b,
        comment773b,
        comment774b,
        comment775b,
        comment776b,
        comment777b,
        comment778b,
        comment779b,
        comment780b,
        comment781b,
        comment782b,
        comment783b,
        comment784b,
        comment785b,
        comment786b,
        comment787b,
        comment789b,
        comment790b,
        comment791b,
        comment792b,
        comment793b,
        comment794b,
        comment795b,
        comment796b,
        comment797b,
        comment798b,
        comment799b,
        comment800b,
        comment801b,
        comment802b,
        comment803b,
        comment804b,
        comment805b,
        comment806b,
        comment807b,
        comment808b,
        comment809b,
        comment810b,
        comment811b,
        comment812b,
        comment813b,
        comment814b,
        comment815b,
        comment816b,
        comment817b,
        comment818b,
        comment819b,
        comment820b,
        comment821b,
        comment822b,
        comment823b,
        comment824b,
        comment825b,
        comment826b,
        comment828b,
        comment829b,
        comment830b,
        comment831b,
        comment832b,
        comment833b,
        comment834b,
        comment835b,
        comment836b,
        comment837b,
        comment838b,
        comment839b,
        comment840b,
        comment841b,
        comment842b,
        comment843b,
        comment844b,
        comment845b,
        comment846b,
        comment847b,
        comment848b,
        comment849b,
        comment850b,
        comment852b,
        comment853b,
        comment854b,
        comment855b,
        comment856b,
        comment857b,
        comment858b,
        comment859b,
        comment860b,
        comment861b,
        comment862b,
        comment863b,
        comment864b,
        comment865b,
        comment866b,
        comment867b,
        comment868b,
        comment869b,
        comment870b,
        comment871b,
        comment872b,
        comment873b,
        comment874b,
        comment875b,
        comment876b,
        comment877b,
        comment878b,
        comment879b,
        comment880b,
        comment881b,
        comment882b,
        comment883b,
        comment884b,
        comment885b,
        comment886b,
        comment887b,
        comment888b,
        comment889b,
        comment890b,
        comment891b,
        comment892b,
        comment893b,
        comment894b,
        comment895b,
        comment896b,
        comment897b,
        comment898b,
        comment899b,
        comment900b,
        comment901b,
        comment902b,
        comment903b,
        comment904b,
        comment905b,
        comment906b,
        comment907b,
        comment908b,
        comment909b,
        comment910b,
        comment911b,
        comment912b,
        comment913b,
        comment914b,
        comment915b,
        comment916b,
        comment917b,
        comment918b,
        comment919b,
        comment920b,
        comment921b,
        comment922b,
        comment924b,
        comment925b,
        comment926b,
        comment927b,
        comment928b,
        comment929b,
        comment930b,
        comment931b,
        comment932b,
        comment933b,
        comment934b,
        comment935b,
        comment936b,
        comment937b,
        comment938b,
        comment939b,
        comment940b,
        comment941b,
        comment942b,
        comment943b,
        comment944b,
        comment945b,
        comment946b,
        comment947b,
        comment948b,
        comment949b,
        comment950b,
        comment952b,
        comment953b,
        comment954b,
        comment955b,
        comment956b,
        comment957b,
        comment958b,
        comment959b,
        comment960b,
        comment961b,
        comment962b,
        comment963b,
        comment964b,
        comment965b,
        comment966b,
        comment967b,
        comment968b,
        comment969b,
        comment970b,
        comment971b,
        comment972b,
        comment973b,
        comment974b,
        comment975b,
        comment976b,
        comment977b,
        comment978b,
        comment979b,
        comment980b,
        comment981b,
        comment982b,
        comment983b,
        comment984b,
        comment985b,
        comment986b,
        comment987b,
        comment988b,
        comment989b,
        comment990b,
        comment991b,
        comment992b,
        comment993b,
        comment994b,
        comment995b,
        comment996b,
        comment997b,
        comment998b,
        comment999b,
        comment1000b,
        comment1001b,
        comment1005b,
        comment1006b,
        comment1007b,
        comment1008b,
        comment1009b,
        comment1010b,
        comment1011b,
        comment1012b,
        comment1013b,
        comment1014b,
        comment1015b,
        comment1016b,
        comment1017b,
        comment1018b,
        comment1019b,
        comment1021b,
        comment1022b,
        comment1023b,
        comment1024b,
        comment1025b,
        comment1026b,
        comment1027b,
        comment1028b,
        comment1029b,
        comment1030b,
        comment1031b,
        comment1032b,
        comment1033b,
        comment1034b,
        comment1035b,
        comment1036b,
        comment1037b,
        comment1038b,
        comment1039b,
        comment1040b,
        comment1041b,
        comment1042b,
        comment1043b,
        comment1044b,
        comment1045b,
        comment1046b,
        comment1047b,
        comment1048b,
        comment1049b,
        comment1050b,
        comment1051b,
        comment1052b,
        comment1054b,
        comment1056b,
        comment1057b,
        comment1058b,
        comment1059b,
        comment1060b,
        comment1061b,
        comment1062b,
        comment1063b,
        comment1064b,
        comment1065b,
        comment1066b,
        comment1067b,
        comment1068b,
        comment1069b,
        comment1070b,
        comment1071b,
        comment1072b,
        comment1073b,
        comment1074b,
        comment1075b,
        comment1076b,
        comment1077b,
        comment1078b,
        comment1079b,
        comment1080b,
        comment1081b,
        comment1082b,
        comment1083b,
        comment1084b,
        comment1085b,
        comment1086b,
        comment1087b,
        comment1088b,
        comment1089b,
        comment1090b,
        comment1091b,
        comment1092b,
        comment1093b,
        comment1094b,
        comment1095b,
        comment1096b,
        comment1097b,
        comment1098b,
        comment1099b,
        comment1100b,
        comment1101b,
        comment1102b,
        comment1103b,
        comment1104b,
        comment1105b,
        comment1106b,
        comment1107b,
        comment1108b,
        comment1109b,
        comment1110b,
        comment1111b,
        comment1112b,
        comment1113b,
        comment1114b,
        comment1115b,
        comment1116b,
        comment1117b,
        comment1118b,
        comment1119b,
        comment1120b,
        comment1121b,
        comment1122b,
        comment1123b,
        comment1124b,
        comment1125b,
        comment1126b,
        comment1127b,
        comment1128b,
        comment1129b,
        comment1130b,
        comment1131b,
        comment1132b,
        comment1133b,
        comment1134b,
        comment1135b,
        comment1136b,
        comment1137b,
        comment1138b,
        comment1139b,
        comment1140b,
        comment1141b,
        comment1142b,
        comment1143b,
        comment1144b,
        comment1145b,
        comment1146b,
        comment1147b,
        comment1148b,
        comment1149b,
        comment1150b,
        comment1151b,
        comment1152b,
        comment1153b,
        comment1155b,
        comment1156b,
        comment1157b,
        comment1158b,
        comment1159b,
        comment1160b,
        comment1161b,
        comment1162b,
        comment1163b,
        comment1164b,
        comment1165b,
        comment1166b,
        comment1167b,
        comment1168b,
        comment1169b,
        comment1170b,
        comment1171b,
        comment1172b,
        comment1173b,
        comment1174b,
        comment1175b,
        comment1176b,
        comment1177b,
        comment1178b,
        comment1179b,
        comment1180b,
        comment1181b,
        comment1182b,
        comment1183b,
        comment1184b,
        comment1185b,
        comment1186b,
        comment1187b,
        comment1188b,
        comment1189b,
        comment1190b,
        comment1191b,
        comment1192b,
        comment1193b,
        comment1194b,
        comment1195b,
        comment1196b,
        comment1197b,
        comment1198b,
        comment1199b,
        comment1200b,
        comment1201b,
        comment1202b,
        comment1203b,
        comment1204b,
        comment1205b,
        comment1206b,
        comment1207b,
        comment1208b,
        comment1209b,
        comment1210b,
        comment1211b,
        comment1212b,
        comment1213b,
        comment1214b,
        comment1215b,
        comment1216b,
        comment1217b,
        comment1218b,
        comment1219b,
        comment1220b,
        comment1221b,
        comment1222b,
        comment1223b,
        comment1224b,
        comment1225b,
        comment1226b,
        comment1227b,
        comment1228b,
        comment1229b,
        comment1230b,
        comment1231b,
        comment1232b,
        comment1233b,
        comment1234b,
        comment1235b,
        comment1236b,
        comment1237b,
        comment1238b,
        comment1239b,
        comment1240b,
        comment1241b,
        comment1242b,
        comment1243b,
        comment1245b,
        comment1246b,
        comment1247b,
        comment1248b,
        comment1249b,
        comment1250b,
        comment1251b,
        comment1252b,
        comment1253b,
        comment1254b,
        comment1255b,
        comment1256b,
        comment1257b,
        comment1258b,
        comment1259b,
        comment1260b,
        comment1261b,
        comment1262b,
        comment1263b,
        comment1264b,
        comment1265b,
        comment1266b,
        comment1267b,
        comment1268b,
        comment1269b,
        comment1270b,
        comment1271b,
        comment1272b,
        comment1273b,
        comment1274b,
        comment1275b,
        comment1276b,
        comment1277b,
        comment1278b,
        comment1279b,
        comment1280b,
        comment1281b,
        comment1282b,
        comment1283b,
        comment1284b,
        comment1285b,
        comment1286b,
        comment1287b,
        comment1288b,
        comment1289b,
        comment1290b,
        comment1291b,
        comment1292b,
        comment1293b,
        comment1294b,
        comment1295b,
        comment1296b,
        comment1297b,
        comment1298b,
        comment1299b,
        comment1300b,
        comment1301b,
        comment1302b,
        comment1303b,
        comment1304b,
        comment1305b,
        comment1306b,
        comment1307b,
        comment1308b,
        comment1309b,
        comment1310b,
        comment1311b,
        comment1312b,
        comment1313b,
        comment1314b,
        comment1315b,
        comment1316b,
        comment1317b,
        comment1318b,
        comment1319b,
        comment1320b,
        comment1321b,
        comment1322b,
        comment1323b,
        comment1324b,
        comment1325b,
        comment1326b,
        comment1327b,
        comment1328b,
        comment1329b,
        comment1330b,
        comment1331b,
        comment1332b,
        comment1333b,
        comment1334b,
        comment1335b,
        comment1336b,
        comment1337b,
        comment1338b,
        comment1339b,
        comment1340b,
        comment1341b,
        comment1342b,
        comment1343b,
        comment1344b,
        comment1345b,
        comment1346b,
        comment1347b,
        comment1348b,
        comment1349b,
        comment1350b,
        comment1351b,
        comment1352b,
        comment1353b,
        comment1354b,
        comment1355b,
        comment1356b,
        comment1357b,
        comment1358b,
        comment1359b,
        comment1360b,
        comment1361b,
        comment1362b,
        comment1363b,
        comment1364b,
        comment1365b,
        comment1366b,
        comment1367b,
        comment1368b,
        comment1370b,
        comment1371b,
        comment1372b,
        comment1373b,
        comment1374b,
        comment1375b,
        comment1376b,
        comment1377b,
        comment1378b,
        comment1379b,
        comment1380b,
        comment1381b,
        comment1382b,
        comment1383b,
        comment1384b,
        comment1386b,
        comment1387b,
        comment1388b,
        comment1389b,
        comment1390b,
        comment1391b,
        comment1392b,
        comment1393b,
        comment1394b,
        comment1395b,
        comment1396b,
        comment1397b,
        comment1398b,
        comment1399b,
        comment1400b,
        comment1401b,
        comment1402b,
        comment1404b,
        comment1406b,
        comment1407b,
        comment1408b,
        comment1409b,
        comment1410b,
        comment1411b,
        comment1412b,
        comment1413b,
        comment1414b,
        comment1415b,
        comment1418b,
        comment1419b,
        comment1420b,
        comment1421b,
        comment1422b,
        comment1423b,
        comment1424b,
        comment1425b,
        comment1426b,
        comment1427b,
        comment1428b,
        comment1429b,
        comment1430b,
        comment1431b,
        comment1432b,
        comment1433b,
        comment1434b,
        comment1435b,
        comment1436b,
        comment1437b,
        comment1438b,
        comment1439b,
        comment1440b,
        comment1441b,
        comment1442b,
        comment1443b,
        comment1444b,
        comment1445b,
        comment1446b,
        comment1447b,
        comment1448b,
        comment1449b,
        comment1450b,
        comment1451b,
        comment1452b,
        comment1453b,
        comment1454b,
        comment1455b,
        comment1458b,
        comment1459b,
        comment1460b,
        comment1461b,
        comment1462b,
        comment1463b,
        comment1464b,
        comment1465b,
        comment1466b,
        comment1467b,
        comment1468b,
        comment1469b,
        comment1470b,
        comment1471b,
        comment1472b,
        comment1473b,
        comment1474b,
        comment1475b,
        comment1476b,
        comment1477b,
        comment1478b,
        comment1479b,
        comment1480b,
        comment1481b,
        comment1482b,
        comment1483b,
        comment1484b,
        comment1485b,
        comment1486b,
        comment1487b,
        comment1488b,
        comment1489b,
        comment1490b,
        comment1491b,
        comment1492b,
        comment1493b,
        comment1494b,
        comment1495b,
        comment1496b,
        comment1497b,
        comment1498b,
        comment1499b,
        comment1500b,
        comment1501b,
        comment1502b,
        comment1503b,
        comment1504b,
        comment1505b,
        comment1506b,
        comment1507b,
        comment1508b,
        comment1509b,
        comment1510b,
        comment1511b,
        comment1512b,
        comment1513b,
        comment1514b,
        comment1515b,
        comment1516b,
        comment1517b,
        comment1518b,
        comment1519b,
        comment1520b,
        comment1521b,
        comment1522b,
        comment1523b,
        comment1524b,
        comment1525b,
        comment1526b,
        comment1527b,
        comment1528b,
        comment1529b,
        comment1530b,
        comment1531b,
        comment1532b,
        comment1533b,
        comment1534b,
        comment1535b,
        comment1536b,
        comment1537b,
        comment1538b,
        comment1539b,
        comment1540b,
        comment1541b,
        comment1543b,
        comment1544b,
        comment1545b,
        comment1546b,
        comment1548b,
        comment1549b,
        comment1550b,
        comment1551b,
        comment1552b,
        comment1553b,
        comment1554b,
        comment1555b,
        comment1556b,
        comment1557b,
        comment1558b,
        comment1561b,
        comment1562b,
        comment1563b,
        comment1564b,
        comment1565b,
        comment1566b,
        comment1567b,
        comment1568b,
        comment1569b,
        comment1570b,
        comment1571b,
        comment1572b,
        comment1573b,
        comment1574b,
        comment1575b,
        comment1576b,
        comment1577b,
        comment1578b,
        comment1579b,
        comment1580b,
        comment1581b,
        comment1582b,
        comment1583b,
        comment1584b,
        comment1585b,
        comment1586b,
        comment1587b,
        comment1588b,
        comment1589b,
        comment1590b,
        comment1591b,
        comment1592b,
        comment1593b,
        comment1594b,
        comment1595b,
        comment1596b,
        comment1597b,
        comment1598b,
        comment1599b,
        comment1600b,
        comment1601b,
        comment1602b,
        comment1603b,
        comment1604b,
        comment1605b,
        comment1606b,
        comment1607b,
        comment1608b,
        comment1609b,
        comment1610b,
        comment1611b,
        comment1612b,
        comment1613b,
        comment1614b,
        comment1615b,
        comment1616b,
        comment1617b,
        comment1618b,
        comment1619b,
        comment1620b,
        comment1621b,
        comment1622b,
        comment1623b,
        comment1624b,
        comment1625b,
        comment1626b,
        comment1627b,
        comment1628b,
        comment1629b,
        comment1630b,
        comment1631b,
        comment1632b,
        comment1633b,
        comment1634b,
        comment1635b,
        comment1636b,
        comment1637b,
        comment1638b,
        comment1639b,
        comment1640b,
        comment1641b,
        comment1642b,
        comment1643b,
        comment1644b,
        comment1645b,
        comment1646b,
        comment1647b,
        comment1648b,
        comment1649b,
        comment1650b,
        comment1651b,
        comment1652b,
        comment1653b,
        comment1654b,
        comment1655b,
        comment1656b,
        comment1657b,
        comment1658b,
        comment1659b,
        comment1660b,
        comment1661b,
        comment1662b,
        comment1663b,
        comment1664b,
        comment1665b,
        comment1666b,
        comment1667b,
        comment1668b,
        comment1669b,
        comment1670b,
        comment1671b,
        comment1672b,
        comment1673b,
        comment1674b,
        comment1675b,
        comment1676b,
        comment1677b,
        comment1678b,
        comment1679b,
        comment1680b,
        comment1681b,
        comment1682b,
        comment1683b,
        comment1684b,
        comment1685b,
        comment1686b,
        comment1687b,
        comment1688b,
        comment1689b,
        comment1690b,
        comment1691b,
        comment1692b,
        comment1693b,
        comment1694b,
        comment1695b,
        comment1696b,
        comment1697b,
        comment1698b,
        comment1699b,
        comment1700b,
        comment1701b,
        comment1702b,
        comment1703b,
        comment1704b,
        comment1705b,
        comment1706b,
        comment1707b,
        comment1708b,
        comment1709b,
        comment1710b,
        comment1711b,
        comment1712b,
        comment1713b,
        comment1714b,
        comment1715b,
        comment1716b,
        comment1717b,
        comment1718b,
        comment1719b,
        comment1720b,
        comment1721b,
        comment1722b,
        comment1723b,
        comment1724b,
        comment1725b,
        comment1726b,
        comment1727b,
        comment1728b,
        comment1729b,
        comment1730b,
        comment1731b,
        comment1732b,
        comment1733b,
        comment1734b,
        comment1735b,
        comment1736b,
        comment1737b,
        comment1738b,
        comment1739b,
        comment1740b,
        comment1741b,
        comment1742b,
        comment1743b,
        comment1744b,
        comment1745b,
        comment1746b,
        comment1747b,
        comment1748b,
        comment1749b,
        comment1750b,
        comment1751b,
        comment1752b,
        comment1753b,
        comment1754b,
        comment1755b,
        comment1756b,
        comment1757b,
        comment1758b,
        comment1759b,
        comment1760b,
        comment1761b,
        comment1762b,
        comment1763b,
        comment1764b,
        comment1765b,
        comment1766b,
        comment1767b,
        comment1768b,
        comment1769b,
        comment1770b,
        comment1771b,
        comment1772b,
        comment1773b,
        comment1774b,
        comment1775b,
        comment1777b,
        comment1778b,
        comment1779b,
        comment1780b,
        comment1781b,
        comment1782b,
        comment1783b,
        comment1784b,
        comment1785b,
        comment1786b,
        comment1787b,
        comment1788b,
        comment1789b,
        comment1790b,
        comment1791b,
        comment1792b,
        comment1793b,
        comment1794b,
        comment1795b,
        comment1796b,
        comment1797b,
        comment1798b,
        comment1799b,
        comment1800b,
        comment1801b,
        comment1802b,
        comment1803b,
        comment1804b,
        comment1805b,
        comment1806b,
        comment1807b,
        comment1808b,
        comment1809b,
        comment1811b,
        comment1813b,
        comment1814b,
        comment1815b,
        comment1816b,
        comment1817b,
        comment1818b,
        comment1820b,
        comment1821b,
        comment1822b,
        comment1823b,
        comment1824b,
        comment1825b,
        comment1826b,
        comment1827b,
        comment1828b,
        comment1829b,
        comment1830b,
        comment1831b,
        comment1832b,
        comment1833b,
        comment1834b,
        comment1835b,
        comment1836b,
        comment1837b,
        comment1838b,
        comment1839b,
        comment1840b,
        comment1841b,
        comment1842b,
        comment1843b,
        comment1844b,
        comment1845b,
        comment1846b,
        comment1847b,
        comment1848b,
        comment1849b,
        comment1850b,
        comment1851b,
        comment1852b,
        comment1853b,
        comment1854b,
        comment1855b,
        comment1856b,
        comment1857b,
        comment1858b,
        comment1859b,
        comment1860b,
        comment1862b,
        comment1863b,
        comment1865b,
        comment1866b,
        comment1867b,
        comment1868b,
        comment1869b,
        comment1870b,
        comment1871b,
        comment1872b,
        comment1873b,
        comment1874b,
        comment1875b,
        comment1876b,
        comment1877b,
        comment1878b,
        comment1879b,
        comment1880b,
        comment1881b,
        comment1882b,
        comment1883b,
        comment1884b,
        comment1885b,
        comment1886b,
        comment1887b,
        comment1888b,
        comment1889b,
        comment1890b,
        comment1891b,
        comment1892b,
        comment1893b,
        comment1894b,
        comment1895b,
        comment1896b,
        comment1897b,
        comment1898b,
        comment1899b,
        comment1900b,
        comment1901b,
        comment1902b,
        comment1903b,
        comment1904b,
        comment1905b,
        comment1906b,
        comment1907b,
        comment1908b,
        comment1909b,
        comment1910b,
        comment1911b,
        comment1912b,
        comment1913b,
        comment1914b,
        comment1915b,
        comment1916b,
        comment1917b,
        comment1918b,
        comment1919b,
        comment1920b,
        comment1921b,
        comment1922b,
        comment1923b,
        comment1924b,
        comment1925b,
        comment1926b,
        comment1927b,
        comment1929b,
        comment1930b,
        comment1931b,
        comment1932b,
        comment1933b,
        comment1934b,
        comment1935b,
        comment1936b,
        comment1937b,
        comment1938b,
        comment1939b,
        comment1940b,
        comment1941b,
        comment1942b,
        comment1943b,
        comment1944b,
        comment1945b,
        comment1946b,
        comment1947b,
        comment1948b,
        comment1949b,
        comment1950b,
        comment1951b,
        comment1953b,
        comment1954b,
        comment1955b,
        comment1956b,
        comment1957b,
        comment1958b,
        comment1959b,
        comment1960b,
        comment1961b,
        comment1962b,
        comment1963b,
        comment1964b,
        comment1965b,
        comment1966b,
        comment1967b,
        comment1968b,
        comment1969b,
        comment1970b,
        comment1971b,
        comment1972b,
        comment1973b,
        comment1974b,
        comment1975b,
        comment1976b,
        comment1977b,
        comment1978b,
        comment1979b,
        comment1980b,
        comment1981b,
        comment1982b,
        comment1983b,
        comment1984b,
        comment1985b,
        comment1986b,
        comment1987b,
        comment1988b,
        comment1989b,
        comment1990b,
        comment1991b,
        comment1992b,
        comment1993b,
        comment1994b,
        comment1995b,
        comment1996b,
        comment1997b,
        comment1998b,
        comment1999b,
        comment2000b,
        comment2001b,
        comment2002b,
        comment2003b,
        comment2004b,
        comment2005b,
        comment2006b,
        comment2007b,
        comment2008b,
        comment2009b,
        comment2010b,
        comment2011b,
        comment2012b,
        comment2013b,
        comment2014b,
        comment2015b,
        comment2016b,
        comment2017b,
        comment2018b,
        comment2019b,
        comment2020b,
        comment2021b,
        comment2022b,
        comment2023b,
        comment2024b,
        comment2025b,
        comment2026b,
        comment2027b,
        comment2028b,
        comment2029b,
        comment2030b,
        comment2031b,
        comment2032b,
        comment2033b,
        comment2034b,
        comment2035b,
        comment2036b,
        comment2037b,
        comment2038b,
        comment2039b,
        comment2040b,
        comment2041b,
        comment2043b,
        comment2044b,
        comment2045b,
        comment2046b,
        comment2047b,
        comment2048b,
        comment2049b,
        comment2050b,
        comment2051b,
        comment2052b,
        comment2053b,
        comment2054b,
        comment2055b,
        comment2056b,
        comment2057b,
        comment2058b,
        comment2059b,
        comment2060b,
        comment2061b,
    ]



    for comment in comments:
        db.session.add(comment)

    db.session.commit()


# Uses a raw SQL query to TRUNCATE the users table.
# SQLAlchemy doesn't have a built in function to do this
# TRUNCATE Removes all the data from the table, and RESET IDENTITY
# resets the auto incrementing primary key, CASCADE deletes any
# dependent entities
def undo_comments():
    db.session.execute('TRUNCATE comments RESTART IDENTITY CASCADE;')
    db.session.commit()
