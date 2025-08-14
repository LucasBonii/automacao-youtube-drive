import yt_dlp

def baixar_video(link):
    ydl_opts = {
        'outtmpl': "video.mp4", 
        'format': '18',            
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([link])
    
    return ydl_opts['outtmpl']


arquivo = baixar_video("https://www.youtube.com/watch?v=DfcXJYv_dxE")
print("Vídeo baixado:", arquivo)
