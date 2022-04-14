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
"UCXGgrKt94gR6lmN4aN3mYTg",
]

channels2 = [
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
"UCR-QYzXrZF8yFarK8wZbHog",
]

channels3 = [
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

request = yt_api.channels().list(
    part="brandingSettings, snippet",
    id="UC9CoOnJkIBMdeijd9qYoT_g"
)

response = request.execute()
print(json.dumps(response, sort_keys=True, indent=4))

# for channel in response["items"]:
#     channelName = channel["brandingSettings"]["channel"]["title"]
#     profileImageUrl = channel["snippet"]["thumbnails"]["high"]["url"]
#     bannerImageUrl = channel["brandingSettings"]["image"]["bannerExternalUrl"]
#     try:
#         channelTrailerId = channel["brandingSettings"]["channel"]["unsubscribedTrailer"]
#     except:
#         channelTrailerId = None
#     createdAt = channel["snippet"]["publishedAt"]
#     try:
#         about = channel["brandingSettings"]["channel"]["description"]
#     except:
#         about = None
    
#     print(f"""{channelName.split()[0]} = Channel(channelName="{channelName}", profileImageUrl="{profileImageUrl}", bannerImageUrl="{bannerImageUrl}", channelTrailerId="{channelTrailerId}", createdAt="{createdAt}", email="{'_'.join(channelName.lower().split())}@{'_'.join(channelName.lower().split())}.com", about='''{about}''')""")
    