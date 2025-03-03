import os
import yt_dlp  # Biblioteca usada para baixar vídeos do YouTube

# Define o caminho do ffmpeg.exe na mesma pasta onde o script está localizado
ffmpeg_path = os.path.join(os.path.dirname(__file__), "ffmpeg.exe")

# Configura o ambiente para que o yt_dlp utilize o FFmpeg corretamente
os.environ["FFMPEG_BINARY"] = ffmpeg_path  # Define a variável de ambiente do FFmpeg
os.environ["PATH"] += os.pathsep + os.path.dirname(ffmpeg_path)  # Adiciona o diretório do FFmpeg ao PATH do sistema

def progress_hook(d, progress_callback=None):
    """
    Função de callback que monitora o progresso do download.

    Parâmetros:
    - d: Dicionário de informações do yt_dlp sobre o estado do download.
    - progress_callback: Função opcional para atualizar a interface gráfica com o progresso.
    """
    if d['status'] == 'downloading':  # Verifica se o download está em andamento
        downloaded = d.get('downloaded_bytes', 0)  # Obtém a quantidade de bytes já baixados
        total = d.get('total_bytes', 1)  # Obtém o tamanho total do arquivo (evita divisão por zero)
        progress = downloaded / total  # Calcula a porcentagem concluída do download

        if progress_callback:
            progress_callback(progress)  # Atualiza a interface gráfica, se uma função de callback foi fornecida
        
        print(f"Progresso: {progress * 100:.2f}%")  # Exibe o progresso no console

    elif d['status'] == 'finished':  # Se o download for concluído, exibe uma mensagem
        print("Download concluído!")

def download_video(url, quality, format, output_path, progress_callback=None):
    """
    Realiza o download de um vídeo do YouTube com base nas configurações fornecidas.

    Parâmetros:
    - url: Link do vídeo do YouTube.
    - quality: Qualidade máxima desejada para o vídeo (exemplo: "720p").
    - format: Tipo do arquivo a ser baixado ("Vídeo" ou "Áudio").
    - output_path: Caminho onde o arquivo será salvo.
    - progress_callback: Função opcional para atualizar o progresso na interface gráfica.
    """
    
    # Configuração das opções para o yt_dlp
    ydl_opts = {
        'format': 'bestaudio/best' if format == 'Audio' else f'bestvideo[height<={quality}]+bestaudio/best',
        # Define o nome do arquivo de saída baseado no título do vídeo
        'outtmpl': os.path.join(output_path, '%(title)s.%(ext)s'),
        # Adiciona a função de monitoramento de progresso
        'progress_hooks': [lambda d: progress_hook(d, progress_callback)], 
        # Se o usuário escolheu apenas áudio, converte para MP3 com qualidade 192kbps usando FFmpeg
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }] if format == 'Audio' else [],
    }

    # Inicializa o yt_dlp e executa o download do vídeo/áudio
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
