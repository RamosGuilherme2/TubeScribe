import os
import subprocess
import shutil

def baixar_audio(url, output_path="audio.mp3"):
    comando = f'yt-dlp -f bestaudio --extract-audio --audio-format mp3 "{url}" -o "{output_path}"'
    resultado = subprocess.run(comando, shell=True, capture_output=True, text=True)

    if resultado.returncode != 0:
        raise RuntimeError(f"Erro ao baixar áudio: {resultado.stderr}")
    
    print(f"Áudio baixado: {output_path}")
    return output_path