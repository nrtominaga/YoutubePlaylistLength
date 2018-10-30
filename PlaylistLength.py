import os

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from google_auth_oauthlib.flow import InstalledAppFlow


SCOPES = ['https://www.googleapis.com/auth/youtube.force-ssl']

# your API key here
API_SERVICE_NAME = 'youtube'
API_VERSION = 'v3'
API_KEY = "AIzaSyCglRrhkgaiC6b3Bc6oW9Zb9XEVMbR2Yro"

# The CLIENT_SECRETS_FILE variable specifies the name of a file that contains
# the OAuth 2.0 information for this application, including its client_id and
# client_secret.
CLIENT_SECRETS_FILE = "client_secret.json"

def get_authenticated_service():
    flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRETS_FILE, SCOPES)
    credentials = flow.run_console()
    return build(API_SERVICE_NAME, API_VERSION, credentials=credentials)

def get_playlist_info(playlist_id):
    # playlist info
    part = "contentDetails"
    max_results = 50
    API_ENDPOINT = "https://www.googleapis.com/youtube/v3/playlistItems?part=" + part + "&maxResults=" + max_results + "&playlistId=" + playlist_id + "&key=" + API_KEY


if __name__ == "__main__":
    playlist = input("Please input the playlist url: ")
    print(playlist)