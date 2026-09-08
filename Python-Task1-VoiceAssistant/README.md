# Python Voice Assistant

A beginner-friendly voice assistant built for the Oasis Infobyte Python Programming internship.

## Features

- Captures commands from a microphone using `SpeechRecognition`.
- Responds to greetings with a predefined message.
- Reports the current time and date.
- Opens a Google search for a spoken topic.
- Uses `pyttsx3` for spoken responses.
- Handles silence, misunderstood speech, unavailable speech services, and missing microphones gracefully.
- Includes a text mode for testing on computers without a microphone.

## Setup

```powershell
py -m pip install -r requirements.txt
py -m pip install PyAudio
```

If PyAudio does not install on your system, use the text mode to test the command logic. Microphone mode requires a working microphone and an internet connection for Google's speech recognition service.

## Run

Microphone mode:

```powershell
py main.py
```

Text demo mode:

```powershell
py main.py --text
```

Try these commands:

- `hello`
- `what is the time`
- `what is today's date`
- `search for Python tutorials`
- `stop`

## Privacy

In microphone mode, audio is captured only while the assistant is listening and is sent to the Google speech recognition service through the `SpeechRecognition` library for transcription. The project does not store audio, transcripts, or personal information. Text mode keeps input local. Browser searches are sent to Google when the user requests a search.

## Project Structure

```text
Python-Task1-VoiceAssistant/
|-- main.py
|-- README.md
`-- requirements.txt
```