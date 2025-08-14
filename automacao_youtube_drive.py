import os.path
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import yt_dlp

def baixar_video(link):
    ydl_opts = {
        'outtmpl': "video.mp4", 
        'format': '18',            
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([link])
    
    return ydl_opts['outtmpl']

SCOPES = ['https://www.googleapis.com/auth/drive.file']

def autenticar_drive():
    creds = None
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    if not creds or not creds.valid:
        flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
        creds = flow.run_local_server(port=0)
        with open('token.json', 'w') as token:
            token.write(creds.to_json())
    service = build('drive', 'v3', credentials=creds)
    return service


service= autenticar_drive()