from googleapiclient.discovery import build

api_key = "AIzaSyDWpRXqmeXAlCEGrwPbO6K_8SNIwSDYJEI"


yt_api = build("youtube", "v3", developerKey=api_key)

request = yt_api.channels().list(
    part="statistics",
    forUsername="schafer5"
)

response = request.execute()

print(response)
