import json
from googleapiclient.discovery import build

channels1 = [
"UCUaT_39o1x6qWjz7K2pWcgw",
"UCo8bcnLyZH8tBIH9V1mLgqQ",
"UCSReacwdlGHHyTIyuROhVdQ",
"UCWWyv3cV6dH1Q8rdGFu10hQ",
"UCaT7afn2Tgc0a70U3x11Dgg",
"UCfLkhIbGHcY_GSb9HFW9oeQ",
"UCgnazDE-yCm8gqymB1lQ8pw",
"UCc7r84eB_n8f3Ke4GrYua1g",
"UCHEf6T_gVq4tlW5i91ESiWg",
"UCVge8FcdNub_Lc4gqPjYyDg",
"UCyoEZ7icpGsUlki08Is8v9g",
"UCxt9Pvye-9x_AIcb1UtmF1Q",
"UCgioULMzcmu7m4NVMKt98LA",
"UCDRmGMSgrtZkOsh_NQl4_xw",
"UCE28rwYoaV7jvU6GVzdu_GQ",
"UCwLkHYmrX8Mkw0lY9fcVkKg",
"UCrLamXyxmMYuhJGKMzmzjAg",
"UCcgqSM4YEo5vVQpqwN-MaNw",
"UCIwFjwMjI0y7PDBVEO9-bkQ",
"UC3jOd7GUMhpgJRBhiLzuLsg",
"UCuHzBCaKmtaLcRAOoazhCPA",
"UC0BletW9phE4xHFM44q4qKA",
"UCzLaQ6eeTVuAltzTrN7fzyg",
"UCAY_M9HyJb8oMKPV1utQQyA",
"UCDlQwv99CovKafGvxyaiNDA",
]

channels2 = [
"UCXGgrKt94gR6lmN4aN3mYTg",
"UCgyqtNWZmIxTx3b6OxTSALw",
"UChd1FPXykD4pust3ljzq6hQ",
"UC-lHJZR3Gqxm24_Vd_AJ5Yw",
"UC-kOXc3gBwksVfmndSEz7jg",
"UC73Us1H9hxv__5oobyLDOyw",
"UChzM3rKP9jGZgSgERC3W8LA",
"UCvBtKQaoDhsHkrvtLjSAhyw",
"UCHn2-DNS5t4tEXqBK5bHmTQ",
"UCmoX4QULJ9MB00xW4coMiOw",
"UCbpMy0Fg74eXXkvxJrtEn3w",
"UCzqbfYjQmf9nLQPMxVgPhiA",
"UCu-x3zDk9Otg5Gr1-9UW8cg",
"UC49ta0RHXJUiID5KWRkcySw",
"UCIivy92qQoJnnjrdBOSqc8g",
"UC3sezeaHPsJW9-TRGnQXlRg",
"UCvthuVsurPaVz2a7_4LepGg",
"UCGwPbAQdGA3_88WBuGtg9tw",
"UCblxOYgXdlcQqoSEY3fhHFw",
"UCm0f2zUj2eSEKfH8IpyHV3Q",
"UCxOeBwl01LMHuXpP3CpJfCw",
"UCZb_nifUWnRfydzWaCsEswg",
"UC-5Kr2sFSJf8jGjyRJ-4H8Q",
"UCJb7_Qsz9pNQDcOA4YA6TxA",
"UClhEIA4NgUey4ty9h8AllHw",
]

channels3 = [
"UCR-QYzXrZF8yFarK8wZbHog",
"UCgPClNr5VSYC3syrDUIlzLw",
"UCp6etHEelnOOd3m9CFsCSgg",
"UCrOgQZYG0olMJaMlNQPjLYw",
"UCq8jp0E99ELBvmBxjJ-JLgA",
"UCGMEwmTEHMhRZg1revBjxzw",
"UCpGimyrbwRtrcJ-CIiRDXbA",
"UCVp3nfGRxmMadNDuVbJSk8A",
"UCoUM-UJ7rirJYP8CQ0EIaHA",
"UCYvmuw-JtVrTZQ-7Y4kd63Q",
"UCfM3zsQsOnfWNUppiycmBuw",
"UC9CoOnJkIBMdeijd9qYoT_g",
]

api_key = "AIzaSyDWpRXqmeXAlCEGrwPbO6K_8SNIwSDYJEI"
yt_api = build("youtube", "v3", developerKey=api_key)

# CHANNELS ########################################################################################
for channelId in channels3:
    request = yt_api.channels().list(
        part="brandingSettings, snippet",
        id=channelId
    )
    response = request.execute()

    # CHANNELS PRINT 0UT ######################################
    # this for loop doesn't need to exist but i'm too lazy to refactor from how i did it before
    for channel in response["items"]:
        channelName = channel["brandingSettings"]["channel"]["title"]
        profileImageUrl = channel["snippet"]["thumbnails"]["high"]["url"]
        bannerImageUrl = channel["brandingSettings"]["image"]["bannerExternalUrl"]
        try:
            channelTrailerId = channel["brandingSettings"]["channel"]["unsubscribedTrailer"]
        except:
            channelTrailerId = None
        createdAt = channel["snippet"]["publishedAt"]
        try:
            about = channel["brandingSettings"]["channel"]["description"]
        except:
            about = None
        
        print('\n\n')
        print(f"""{channelName.split()[0]} = Channel(channelName="{channelName}", profileImageUrl="{profileImageUrl}", bannerImageUrl="{bannerImageUrl}", channelTrailerId="{channelTrailerId}", createdAt="{createdAt}", email="{'_'.join(channelName.lower().split())}@{'_'.join(channelName.lower().split())}.com", about='''{about}''')""")
    
    
    
# NOTE: THESE ARE NOT IN THE SAME ORDER AS THE channelsX ARRAY!!
channels1uploadsPlaylistIds = ['UUHEf6T_gVq4tlW5i91ESiWg', 'UUAY_M9HyJb8oMKPV1utQQyA', 'UUyoEZ7icpGsUlki08Is8v9g', 'UUUaT_39o1x6qWjz7K2pWcgw', 'UUWWyv3cV6dH1Q8rdGFu10hQ', 'UUDRmGMSgrtZkOsh_NQl4_xw', 'UUIwFjwMjI0y7PDBVEO9-bkQ', 'UUwLkHYmrX8Mkw0lY9fcVkKg', 'UUxt9Pvye-9x_AIcb1UtmF1Q', 'UU0BletW9phE4xHFM44q4qKA', 'UUcgqSM4YEo5vVQpqwN-MaNw', 'UU3jOd7GUMhpgJRBhiLzuLsg', 'UUuHzBCaKmtaLcRAOoazhCPA', 'UUrLamXyxmMYuhJGKMzmzjAg', 'UUfLkhIbGHcY_GSb9HFW9oeQ', 'UUDlQwv99CovKafGvxyaiNDA', 'UUo8bcnLyZH8tBIH9V1mLgqQ', 'UUaT7afn2Tgc0a70U3x11Dgg', 'UUgioULMzcmu7m4NVMKt98LA', 'UUc7r84eB_n8f3Ke4GrYua1g', 'UUVge8FcdNub_Lc4gqPjYyDg', 'UUSReacwdlGHHyTIyuROhVdQ', 'UUE28rwYoaV7jvU6GVzdu_GQ', 'UUgnazDE-yCm8gqymB1lQ8pw', 'UUzLaQ6eeTVuAltzTrN7fzyg']  
channels2uploadsPlaylistIds = ['UUGwPbAQdGA3_88WBuGtg9tw', 'UUZb_nifUWnRfydzWaCsEswg', 'UUmoX4QULJ9MB00xW4coMiOw', 'UUbpMy0Fg74eXXkvxJrtEn3w', 'UU73Us1H9hxv__5oobyLDOyw', 'UUvBtKQaoDhsHkrvtLjSAhyw', 'UUzqbfYjQmf9nLQPMxVgPhiA', 'UUhd1FPXykD4pust3ljzq6hQ', 'UUvthuVsurPaVz2a7_4LepGg', 'UUXGgrKt94gR6lmN4aN3mYTg', 'UU49ta0RHXJUiID5KWRkcySw', 'UU3sezeaHPsJW9-TRGnQXlRg', 'UUJb7_Qsz9pNQDcOA4YA6TxA', 'UUxOeBwl01LMHuXpP3CpJfCw', 'UU-lHJZR3Gqxm24_Vd_AJ5Yw', 'UUm0f2zUj2eSEKfH8IpyHV3Q', 'UUgyqtNWZmIxTx3b6OxTSALw', 'UUHn2-DNS5t4tEXqBK5bHmTQ', 'UUu-x3zDk9Otg5Gr1-9UW8cg', 'UU-kOXc3gBwksVfmndSEz7jg', 'UU-5Kr2sFSJf8jGjyRJ-4H8Q', 'UUlhEIA4NgUey4ty9h8AllHw', 'UUIivy92qQoJnnjrdBOSqc8g', 'UUblxOYgXdlcQqoSEY3fhHFw', 'UUhzM3rKP9jGZgSgERC3W8LA']   
channels3uploadsPlaylistIds = ['UUR-QYzXrZF8yFarK8wZbHog', 'UUfM3zsQsOnfWNUppiycmBuw', 'UUq8jp0E99ELBvmBxjJ-JLgA', 'UUp6etHEelnOOd3m9CFsCSgg', 'UUgPClNr5VSYC3syrDUIlzLw', 'UUVp3nfGRxmMadNDuVbJSk8A', 'UUYvmuw-JtVrTZQ-7Y4kd63Q', 'UUGMEwmTEHMhRZg1revBjxzw', 'UU9CoOnJkIBMdeijd9qYoT_g', 'UUoUM-UJ7rirJYP8CQ0EIaHA', 'UUrOgQZYG0olMJaMlNQPjLYw', 'UUpGimyrbwRtrcJ-CIiRDXbA']

# VIDEOS ########################################################################################
# request = yt_api.channels().list(
#     part="contentDetails",
#     id=channels3
# )
# response = request.execute()
# uploadsPlaylistIds = [channel["contentDetails"]["relatedPlaylists"]["uploads"]  for channel in response["items"]] # ["contentDetails"]["relatedPlaylists"]["uploads"]
# print(uploadsPlaylistIds) # this will be channelsX's 'uploads' playlist id array (these are not in the same order as they were when the request was sent off)

# # NOTE: get the videos in each playlist (by playlist id)
# for playlistId in channels1uploadsPlaylistIds:
#     request = yt_api.playlistItems().list(
#         part="contentDetails, snippet",
#         playlistId=playlistId,
#         maxResults=10
#     )
#     response = request.execute()
#     # print(json.dumps(response, sort_keys=True, indent=4))
#     # print('\n\n\n\n')
        
#     # VIDEOS PRINT OUT ######################################
#     allChannels = channels1 + channels2 + channels3
#     for video in response["items"]:
#         channelId = allChannels.index(video["snippet"]["channelId"]) + 1
#         title = video["snippet"]["title"]
#         description = video["snippet"]["description"]
#         videoUrl = video["contentDetails"]["videoId"]
#         try:
#             thumbnailUrl = video["snippet"]["thumbnails"]["maxres"]["url"]
#         except:
#             thumbnailUrl = video["snippet"]["thumbnails"]["high"]["url"]
            
#         createdAt = video["snippet"]["publishedAt"]
        
#         print('\n\n\n')
#         print(f"""{title.split()[0]} = Video(channelId="{channelId}", title='''{title}''', description='''{description}''', videoUrl="{videoUrl}", thumbnailUrl="{thumbnailUrl}", createdAt="{createdAt}")""")
