import pyttsx3
import config


def narrate(narrate_queue):
    print("Narrating...")

    engine = pyttsx3.init()  # object creation
    engine.setProperty("rate", 170)
    engine.setProperty("volume", 1.0)
    VOICES = engine.getProperty("voices")
    engine.setProperty("voice", VOICES[0].id)

    while True:
        # Get the transcript from the queue
        message = narrate_queue.get()

        # If we receive exit code, stop
        if message == config.EXIT_CODE:
            break

        print("Narrating: " + message)
        engine.say(message)
        engine.runAndWait()

    print("Stopped narrating")
