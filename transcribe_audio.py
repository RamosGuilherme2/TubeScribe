import whisper

def transcrever_audio(audio_path="audio.mp3"):
    modelo = whisper.load_model("small")
    resultado = modelo.transcribe(audio_path)
    return resultado["text"]
