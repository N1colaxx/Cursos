

import yt_dlp

url = 'https://www.youtube.com/watch?v=9Azyhn2UUyw'

# Defina as opções para o download, incluindo o User-Agent e o novo caminho de saída
ydl_opts = {
    'outtmpl': r'D:\Progamas\Cursos\Curso_em_Video\python\pastaDonwload\%(title)s.%(ext)s',  # Novo caminho de saída
    'format': 'best',  # Melhor qualidade
    'headers': {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
    }
}

# Tente baixar o vídeo com yt-dlp
try:
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    print("Download concluído!")
except Exception as e:
    print(f'Ocorreu um erro: {e}')
