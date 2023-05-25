import transcriber
import interpreter
import threading
import recorder
import narrator
import config
import os
from queue import Queue

# Create stop event
stop_event = threading.Event()

# Create queues
recordings_queue = Queue()
transcript_queue = Queue()
narrate_queue = Queue()

# Start the threads
thread_transcribe = threading.Thread(
    target=transcriber.transcribe, args=(stop_event, recordings_queue, transcript_queue)
)
thread_interpret = threading.Thread(
    target=interpreter.interpret, args=(stop_event, transcript_queue, narrate_queue)
)
thread_narrate = threading.Thread(
    target=narrator.narrate, args=(stop_event, narrate_queue)
)


def clear_queue(queue):
    while not queue.empty():
        queue.get()


try:
    print("Starting...")
    if not os.path.exists(config.RECORDINGS_PATH):
        os.makedirs(config.RECORDINGS_PATH)

    thread_narrate.start()
    thread_interpret.start()
    thread_transcribe.start()

    recorder.listen(stop_event, config.RECORDINGS_PATH, recordings_queue)

except KeyboardInterrupt:
    print("Stopping...")

    print("Setting stop event...")
    stop_event.set()

    print("Clearing queues...")
    clear_queue(recordings_queue)
    clear_queue(transcript_queue)
    clear_queue(narrate_queue)

    print("Send exit code to all queues...")
    recordings_queue.put(config.EXIT_CODE)
    transcript_queue.put(config.EXIT_CODE)
    narrate_queue.put(config.EXIT_CODE)

    print("Waiting for threads to finish...")
    thread_transcribe.join()
    thread_interpret.join()
    thread_narrate.join()

    print("Deleting recordings...")
    for filename in os.listdir(config.RECORDINGS_PATH):
        os.remove(os.path.join(config.RECORDINGS_PATH, filename))
    os.rmdir(config.RECORDINGS_PATH)

    print("Done")
    exit(0)
