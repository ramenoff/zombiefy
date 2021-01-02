from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

MAX_VIDEOS = 5000

flow = InstalledAppFlow.from_client_secrets_file(
    "client_secrets.json", scopes = ["https://www.googleapis.com/auth/youtube"]
)

credentials = flow.run_console()

youtube = build('youtube', 'v3', credentials = credentials)

def returnPlaylist(playListID):

  response = youtube.playlistItems().list(
    part = 'contentDetails',
    playlistId = playListID,
    maxResults = MAX_VIDEOS
  ).execute()

  playlistItems = response['items']
  nextPageToken = response.get('nextPageToken')

  return playlistItems
