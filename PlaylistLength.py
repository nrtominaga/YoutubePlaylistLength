import argparse

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# your API key here
API_SERVICE_NAME = 'youtube'
API_VERSION = 'v3'
API_KEY = "AIzaSyCglRrhkgaiC6b3Bc6oW9Zb9XEVMbR2Yro"


def get_playlist_info(playlist_id):
    # playlist info
    youtube = build(API_SERVICE_NAME, API_VERSION, developerKey=API_KEY)
    part = "contentDetails"
    max_results = 50
    playlist_response = youtube.playlistItems().list(part=part, maxResults=max_results, playlistId=playlist_id).execute()
    return playlist_response


def get_video_info():
    print("hi")


def get_playlist_length(playlistInfo, client):
    print("what")


if __name__ == "__main__":
    playlistId = input("Please input the playlist url: ")
    print(playlistId)

    playlist = get_playlist_info(playlistId)
    print(playlist)