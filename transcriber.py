import subprocess
import whisper
import os

# Function to extract audio from video using ffmpeg
def extract_audio(video_path: str, audio_path: str = "temp_audio.wav") -> str:
    if os.path.exists(audio_path):
        os.remove(audio_path)  

    # ffmpeg command to extract audio
    command = [
        "ffmpeg",
        "-i", video_path,     # input video file
        "-q:a", "0",          # best audio quality
        "-map", "a",          # select only audio streams
        audio_path,
        "-y"                  # overwrite output file without asking
    ]
    
    subprocess.run(command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
    return audio_path

# Function to transcribe the audio using Whisper
def transcribe_audio(audio_path: str, model_size: str = "base") -> str:
    model = whisper.load_model(model_size)      # Load Whisper model
    result = model.transcribe(audio_path)       # Transcribe audio
    transcript = result["text"]                 # Extract text
    return transcript
