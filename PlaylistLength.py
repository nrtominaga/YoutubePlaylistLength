import argparse
import isodate

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# your API key here
API_SERVICE_NAME = 'youtube'
API_VERSION = 'v3'
API_KEY = "AIzaSyCglRrhkgaiC6b3Bc6oW9Zb9XEVMbR2Yro"
youtube = build(API_SERVICE_NAME, API_VERSION, developerKey=API_KEY)

HOUR = 3600
MINUTE = 60


def get_playlist_info(playlist_id):
    # playlist info
    part = "contentDetails"
    max_results = 50
    playlist_response = youtube.playlistItems().list(part=part, maxResults=max_results, playlistId=playlist_id).execute()
    return playlist_response


def get_video_info(ids):
    vid_input = ','.join(ids)
    return youtube.videos().list(id=vid_input, part='contentDetails').execute()


def calculate_playlist_length(ids):
    video_response = get_video_info(ids)
    length = 0
    for video in video_response['items']:
        time = isodate.parse_duration(video['contentDetails']['duration'])
        length += time.total_seconds()
    return length


def get_video_ids(playlist_info):
    vids = []
    for video in playlist_info['items']:
        vids.append(video['contentDetails']['videoId'])
    return vids


def print_time(seconds):
    hours = seconds // HOUR
    seconds = seconds % HOUR
    minutes = seconds // MINUTE
    seconds = seconds % 60
    print("HOURS: " + str(hours) + " MINUTES: " + str(minutes) + " SECONDS: " + str(seconds))


if __name__ == "__main__":
    playlistId = input("Please input the playlist url: ")

    playlist = get_playlist_info(playlistId)
    vid_ids = get_video_ids(playlist)
    length = calculate_playlist_length(vid_ids)
    print_time(length)