from dotenv import load_dotenv
import openai
import os


def interpret(stop_event, transcript_queue, narrate_queue):
    print("Interpreting...")

    # Load environment variables from .env
    load_dotenv()

    openai.api_key = os.getenv("OPENAI_API_KEY")

    MAX_TOKENS = 128
    TEMPERATURE = 0.8

    while not (stop_event.is_set() and transcript_queue.empty()):
        # Get the transcript from the queue
        transcript = transcript_queue.get()

        # If the transcript is -E-X-I-T-, stop narrating
        if transcript == "-E-X-I-T-":
            break

        prompt = f"One sentence answer: {transcript}"

        completion = openai.Completion.create(
            model="text-davinci-003",
            prompt=prompt,
            max_tokens=MAX_TOKENS,
            temperature=TEMPERATURE,
            top_p=1.0,
            frequency_penalty=0.0,
            presence_penalty=0.0,
        )

        # Trim and clean the message choice
        message = completion.choices[0].text.strip()

        narrate_queue.put(message)

    print("Stopped interpreting")
