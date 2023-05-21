import os
import datetime
import pyaudio
import wave
import librosa
import numpy as np

def listen(stop_event, recordings_path):
    # Matching whisper settings
    FORMAT = pyaudio.paInt16
    # OpenAI whisper uses 1 channel by default
    CHANNELS = 1
    # OpenAI whisper uses 16kHz sample rate by default
    RATE = 16000
    # Set the sample duration
    FRAME_LENGTH = RATE // 10
    # Proportion of the frame length to be considered as silence
    CHUNK_SILENT_THRESHOLD = 0.5
    # Silence RMS ceiling
    SILENCE_RMS_CEILING = 64

    # Initialize PyAudio
    audio = pyaudio.PyAudio()

    # Open microphone stream
    stream = audio.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=FRAME_LENGTH)

    print('Listening...')
    while not stop_event.is_set():
        frames = []
        silent_frames = 0

        while True:
            # Read audio data from the stream
            data = stream.read(FRAME_LENGTH)
            frames.append(data)

            # Check for silence
            chunk = np.frombuffer(data, dtype=np.int16)
            rms_features = librosa.feature.rms(y=chunk, frame_length=FRAME_LENGTH, hop_length=FRAME_LENGTH)
            rms = np.average(rms_features)

            # If the audio is silent, increment the silent frame count
            if rms < SILENCE_RMS_CEILING:
                silent_frames += 1
            else:
                silent_frames = 0
            
            # If there are consecutive silent frames, stop recording
            if silent_frames >= CHUNK_SILENT_THRESHOLD:
                break
        
        # If all frames are silent, skip saving the file
        if len(frames) == silent_frames:
            continue

        # Save the recorded audio to a WAV file
        ts = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        filename = f"{ts}.wav"
        file_path = os.path.join(recordings_path, filename)

        with wave.open(file_path, 'wb') as wf:
            wf.setnchannels(CHANNELS)
            wf.setsampwidth(audio.get_sample_size(FORMAT))
            wf.setframerate(RATE)
            wf.writeframes(b"".join(frames))

    # Close the stream
    stream.stop_stream()
    stream.close()
    audio.terminate()

    print('Stopped listening')