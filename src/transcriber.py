import whisper
import os
import config


def transcribe(stop_event, recordings_queue, transcript_queue):
    print("Transcribing...")

    MODEL = whisper.load_model("base")
    MIN_AMOUNT_OF_SPEECH_CERTAINTY = 0.8

    while not (stop_event.is_set() and recordings_queue.empty()):
        # Get the filepath from the queue
        filepath = recordings_queue.get()

        # If we receive exit code, stop
        if filepath == config.EXIT_CODE:
            break

        # Load audio and pad or trim to 1 second
        audio = whisper.load_audio(filepath)
        audio = whisper.pad_or_trim(audio)
        mel = whisper.log_mel_spectrogram(audio).to(MODEL.device)
        options = whisper.DecodingOptions(
            language=config.WHISPERING_LANGUAGE, fp16=False
        )

        result = whisper.decode(MODEL, mel, options)

        if result.no_speech_prob < MIN_AMOUNT_OF_SPEECH_CERTAINTY:
            print(f"DEBUG: {result.text}")

            # If the text contains the word "bart", "bard" or "barred" or "bored"
            lowercase_compare = result.text.lower()
            if (
                (lowercase_compare.find("bart") != -1)
                or (lowercase_compare.find("bard") != -1)
                or (lowercase_compare.find("barred") != -1)
                or (lowercase_compare.find("bored") != -1)
                or (lowercase_compare.find("Vard") != -1)
            ):
                # Add transcript to queue
                transcript_queue.put(result.text)
                config.play_transcribed_sound()

        # Delete the file
        os.remove(filepath)

    print("Stopped transcribing")
