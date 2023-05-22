import simpleaudio as sa
import os

ASSETS_LOCATION = "assets"
EXTENSION = ".wav"


def play_sound(filename):
    path = os.path.join(ASSETS_LOCATION, filename + EXTENSION)
    wave_obj = sa.WaveObject.from_wave_file(path)
    wave_obj.play()
