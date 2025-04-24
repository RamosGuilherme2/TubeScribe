from download_audio import baixar_audio
from transcribe_audio import transcrever_audio
from summarize_text import gerar_resumo
from save_summary import salvar_resumo
import os

def processar_video(url):
    try:
        audio_path = baixar_audio(url)
        print("Transcrevendo o áudio completo...")
        texto_transcrito = transcrever_audio(audio_path)
        print("Gerando resumo do texto transcrito...")
        resumo = gerar_resumo(texto_transcrito)
        print("Resumo gerado com sucesso!")
        print(f"\nResumo:\n{resumo}")
        salvar_resumo(resumo, "resumo.txt")

        print("Resumo salvo em resumo.txt!")
    except Exception as e:
       print(f"Ocorreu um erro: {e}")
    finally:
        if os.path.exists(audio_path):
         os.remove(audio_path)
         print("Arquivos temporarios removidos com sucesso!")

if __name__ == "__main__":
    url = input("Insira o URL do vídeo do YouTube: ")
    processar_video(url)
