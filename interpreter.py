def interpret(stop_event, transcript_queue):
    print("Interpreting...")

    while not (stop_event.is_set() and transcript_queue.empty()):
        # Get the transcript from the queue
        transcript = transcript_queue.get()

        print("Interpreting: " + transcript)

    print("Stopped interpreting")
