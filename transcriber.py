import whisper
import os


def transcribe(stop_event, recordings_queue, transcript_queue):
    print("Transcribing...")

    MODEL = whisper.load_model("base")

    while not stop_event.is_set() or not recordings_queue.empty():
        # Get the filepath from the queue
        filepath = recordings_queue.get()

        # Load audio and pad or trim to 1 second
        audio = whisper.load_audio(filepath)
        audio = whisper.pad_or_trim(audio)
        mel = whisper.log_mel_spectrogram(audio).to(MODEL.device)
        options = whisper.DecodingOptions(language="en", fp16=False)

        result = whisper.decode(MODEL, mel, options)

        if result.no_speech_prob < 0.5:
            # Add transcript to queue
            transcript_queue.put(result.text)

        # Delete the file
        os.remove(filepath)

    print("Stopped transcribing")
