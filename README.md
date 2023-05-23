# Python AI Voice Command Interpreter

This repository contains a Python 3.11-based AI project that can interpret and execute vocal commands. The program records vocal inputs, transcribes them, and then interprets them using another AI model and narrates the results.

## Installation

To use this voice command interpreter, please follow these steps:

1. Clone this repository to your local machine using the following command:

```bash
git clone https://github.com/AuracleTech/command-vocal-interpreter.git
```

2. Navigate to the project directory:

```bash
cd voice-command-interpreter
```

3. Install the required dependencies by running the following command:

```bash
pip install -r requirements.txt
```

## Usage

1. Run the main.py file using Python 3.11:

```bash
python main.py
```

The voice command interpreter will now simultaneously run four threads:

1. Record vocal commands and save them to the recordings folder.
2. Transcribe the recordings and save the transcriptions to the transcriptions folder.
3. Interpret the commands and save the interpreted commands to the commands folder.
4. Execute the commands and vocalize the results.
