import os.path
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from googleapiclient.http import MediaFileUpload
import yt_dlp

def baixar_video(link):
    
    ydl_opts = {
        'outtmpl': "%(title)s.%(ext)s", 
        'format': '18',            
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(link, download=True)
        caminho_final = ydl.prepare_filename(info)    
    
    return caminho_final

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


def enviar_para_drive(caminho_arquivo):
    service = autenticar_drive()
    nome_no_drive = os.path.basename(caminho_arquivo)

    
    media = MediaFileUpload(caminho_arquivo, mimetype='video/mp4', resumable=True)
    arquivo = service.files().create(
        body={'name': nome_no_drive},
        media_body=media,
        fields='id'
    ).execute()

    service.permissions().create(
        fileId=arquivo['id'],
        body={'type': 'anyone', 'role': 'reader'}
    ).execute()

    link = f"https://drive.google.com/file/d/{arquivo['id']}/view"
    return link


if __name__ == "__main__":
    link_youtube = str(input('Digite o link do vídeo:'))
    link_youtube = link_youtube.strip()
    arquivo_baixado = baixar_video(link_youtube)
    link_drive = enviar_para_drive(arquivo_baixado)
    print(f'O seu vídeo foi salvo em: {link_drive}')