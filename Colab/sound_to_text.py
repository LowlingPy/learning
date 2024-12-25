# pip install speechrecognition pydub

from pydub import AudioSegment
import speech_recognition as sr


def split_audio(file_path, chunk_length_ms=60000):  # Default to 1 minute chunks
    audio = AudioSegment.from_file(file_path)
    chunks = []
    for i in range(0, len(audio), chunk_length_ms):
        chunk = audio[i:i + chunk_length_ms]
        chunks.append(chunk)
    return chunks


# Split the audio file
audio_path = "Your File"  # Your audio file path
chunks = split_audio(audio_path)

# Process each chunk separately
recognizer = sr.Recognizer()

# Open a text file to write the transcriptions
with open("transcription.txt", "w", encoding="utf-8") as f:
    for i, chunk in enumerate(chunks):
        chunk_path = f"chunk_{i}.wav"
        chunk.export(chunk_path, format="wav")

        with sr.AudioFile(chunk_path) as source:
            audio_data = recognizer.record(source)
            try:
                text = recognizer.recognize_google(audio_data, language="fa-IR")
                f.write(f"\n{text}\n")  # Save the transcription to the text file
                print(text)
            except sr.RequestError as e:
                f.write(f"Chunk {i}: Could not request results from Google Speech Recognition service; {e}\n\n")
            except sr.UnknownValueError:
                f.write(f"Chunk {i}: Google Speech Recognition could not understand audio.\n\n")

print("Transcription saved to transcription.txt")
