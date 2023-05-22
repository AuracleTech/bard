import threading
import keyboard
import os
from queue import Queue
import recorder
import transcriber
import interpreter


def clear_queue(queue):
    while not queue.empty():
        queue.get()


# Create stop event
stop_event = threading.Event()

# Create paths
recordings_path = "recordings"
if not os.path.exists(recordings_path):
    os.makedirs(recordings_path)

# Create queues
recordings_queue = Queue()
transcript_queue = Queue()

# Start the threads
thread1 = threading.Thread(
    target=recorder.listen, args=(stop_event, recordings_path, recordings_queue)
)
thread2 = threading.Thread(
    target=transcriber.transcribe, args=(stop_event, recordings_queue, transcript_queue)
)
thread3 = threading.Thread(
    target=interpreter.interpret, args=(stop_event, transcript_queue)
)
# TODO add thread4 for commands & speaker

thread1.start()
thread2.start()
thread3.start()

print("Press 's' to stop")
keyboard.wait("s")
print("Stopping...")
stop_event.set()

print("Waiting for threads to finish...")
thread1.join()
thread2.join()
thread3.join()

print("Clearing queues...")
clear_queue(recordings_queue)
clear_queue(transcript_queue)

print("Deleting recordings...")
for filename in os.listdir(recordings_path):
    os.remove(os.path.join(recordings_path, filename))
os.rmdir(recordings_path)

exit(0)
