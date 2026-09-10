# Python Voice Assistant

A simple beginner-friendly Python voice assistant built for the Oasis Infobyte Python Programming internship.

## Features

* Responds to a greeting.
* Tells the current time.
* Tells today's date.
* Opens Google in the web browser.
* Uses `pyttsx3` to speak responses.
* Takes commands from the keyboard.
* Stops when the user types `stop`.

## Technologies Used

* Python
* `pyttsx3`
* `datetime`
* `webbrowser`

## Installation

Install the `pyttsx3` package using:

```powershell
py -m pip install pyttsx3
```

The other modules used in this project (`datetime` and `webbrowser`) are included with Python.

## How to Run

Open the project folder in VS Code or a terminal and run:

```powershell
py main.py
```

Then type a command when you see:

```text
You:
```

## Available Commands

Try these commands:

* `hello`
* `what is the time`
* `what is the date`
* `google`
* `stop`

## Example

```text
Assistant: Hello! I am your voice assistant.

You: hello
Assistant: Hello! How can I help you?

You: what is the time
Assistant: The current time is 10:30 PM

You: what is the date
Assistant: Today's date is 11 September 2026

You: google
Assistant: Opening Google

You: stop
Assistant: Goodbye!
```

## Project Structure

```text
Python-Task1-VoiceAssistant/
|-- main.py
`-- README.md
```

## How It Works

1. The program starts the voice assistant.
2. The user enters a command using the keyboard.
3. The program checks the command using `if`, `elif`, and `else`.
4. The assistant performs the requested action.
5. The assistant continues until the user types `stop`.
