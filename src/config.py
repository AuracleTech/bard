import hashlib
import random
import os
import pyaudio
import wave


def load_wav_file(file_path):
    with wave.open(file_path, "rb") as wav_file:
        # Get the audio file's properties
        num_channels = wav_file.getnchannels()
        sample_width = wav_file.getsampwidth()
        sample_rate = wav_file.getframerate()
        num_frames = wav_file.getnframes()
        audio_data = wav_file.readframes(num_frames)

    return audio_data, sample_rate, sample_width, num_channels


def generate_random_hash():
    random_data = str(random.getrandbits(256)).encode("utf-8")
    hash_value = hashlib.sha256(random_data).hexdigest()
    return hash_value


# Generate exit code
EXIT_CODE = generate_random_hash()

# Paths
ASSETS_PATH = "assets"
RECORDINGS_PATH = "recordings"

# Whispering language
WHISPERING_LANGUAGE = "en"

# Sound effects settings
SFX_FILE = "transcribed.wav"
SFX_FULL_PATH = os.path.join(ASSETS_PATH, SFX_FILE)
SFX_DATA, SFX_RATE, SFX_WIDTH, SFX_NB_CHANNEL = load_wav_file(SFX_FULL_PATH)


# Transcribed SFX
def play_transcribed_sound():
    p = pyaudio.PyAudio()

    # Open a stream
    stream = p.open(
        format=p.get_format_from_width(SFX_WIDTH),
        channels=SFX_NB_CHANNEL,
        rate=SFX_RATE,
        output=True,
    )

    # Play the audio by writing the data to the stream in chunks
    chunk_size = 1024
    start_index = 0
    while start_index < len(SFX_DATA):
        end_index = start_index + chunk_size
        chunk = SFX_DATA[start_index:end_index]
        stream.write(chunk)
        start_index = end_index

    # Stop and close the stream
    stream.stop_stream()
    stream.close()

    # Terminate the PyAudio instance
    p.terminate()
