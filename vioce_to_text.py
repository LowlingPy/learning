import speech_recognition as sr
from pydub import AudioSegment

# Convert the audio file to wav format
audio_path = "Recording.m4a"  # Upload your file to Colab
wav_path = "Recording.wav"
audio = AudioSegment.from_file(audio_path)
audio.export(wav_path, format="wav")

# Transcribe the audio file
recognizer = sr.Recognizer()
with sr.AudioFile(wav_path) as source:
    audio_data = recognizer.record(source)
    text = recognizer.recognize_google(audio_data, language="fa-IR")

print(text)
