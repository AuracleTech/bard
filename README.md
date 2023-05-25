![Command](https://cdn.dribbble.com/users/2665918/screenshots/11996965/media/87e5b5088f4d3a7f1ddef27db699410b.gif)

# Bard

###### a python AI Voice Command Assistant

Bard stands for **B**ackend **A**I **R**esponse **D**ialog. This project uses 4 agents working in parallel.

1. The **Recorder** which records vocal inputs and saves them to the recordings folder.
2. A **Transcriber** which transcribes the recordings and passes them to the interpreter.
3. An **Interpreter** which interprets the transcribed questions and passes the results to the narrator.
4. The **Narrator** which narrates the answers or results to the user.

## Usage

1. Install requirements

- [OpenAI API Key](https://beta.openai.com/)
- [git](https://git-scm.com/downloads)
- [FFmpeg](https://ffmpeg.org/download.html)
- [Python 3.11](https://www.python.org/downloads/release/python-3113/)

2. Clone this repository to your local machine using the following command

```shell
git clone https://github.com/AuracleTech/bard.git
```

3. Navigate to the project directory

```shell
cd bard
```

4. Install OpenAi Whisper

```shell
pip install -U openai-whisper
```

5. Install pipreqs to generates the dependencies

```shell
pip install pipreqs
```

6. Use pipreqs to generate the dependencies

```shell
pipreqs . --force
```

7. Install the required dependencies by running the following command

```shell
pip install -r requirements.txt
```

8. Create a .env file in the root directory and add the following variables

```shell
OPENAI_API_KEY=your-openai-api-key-here
```

9. Launch the app

```shell
python src/main.py
```

10. Ask Bard your questions by including its name

- **Bard**, Do you know any library in python to play sound effects?

- So you're telling me that OpenAI is called Open but is actually Closed source, **Bard**?

- Hey **Bard** what's the name of the entry point file in python?

## Help

Feel free to open an [issue](/issues) if you have any questions or suggestions.
