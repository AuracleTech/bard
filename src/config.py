import hashlib
import random
import os
import simpleaudio as sa


def play_sound(filename):
    path = os.path.join(ASSETS_PATH, filename + AUDIO_EXT)
    wave_obj = sa.WaveObject.from_wave_file(path)
    wave_obj.play()


def generate_random_hash():
    random_data = str(random.getrandbits(256)).encode("utf-8")
    hash_value = hashlib.sha256(random_data).hexdigest()
    return hash_value


def delete_recordings():
    for filename in os.listdir(RECORDINGS_PATH):
        os.remove(os.path.join(RECORDINGS_PATH, filename))
        os.rmdir(RECORDINGS_PATH)


# Generate exit code
EXIT_CODE = generate_random_hash()

# Paths
ASSETS_PATH = "assets"
AUDIO_EXT = ".wav"
RECORDINGS_PATH = "recordings"

# Whispering language
WHISPERING_LANGUAGE = "en"

# Create recordings directory
if not os.path.exists(RECORDINGS_PATH):
    os.makedirs(RECORDINGS_PATH)
