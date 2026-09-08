"""Beginner voice assistant for the Oasis Infobyte Python internship."""

from __future__ import annotations

import argparse
from datetime import datetime
from typing import Optional
from urllib.parse import quote_plus
import webbrowser

try:
    import speech_recognition as sr
except ImportError:  # pragma: no cover - depends on the user's environment
    sr = None

try:
    import pyttsx3
except ImportError:  # pragma: no cover - depends on the user's environment
    pyttsx3 = None


class VoiceAssistant:
    """Handle speech input and useful beginner-level commands."""

    def __init__(self) -> None:
        self.recognizer = sr.Recognizer() if sr is not None else None
        self.speech_engine = pyttsx3.init() if pyttsx3 is not None else None

    def speak(self, message: str) -> None:
        """Print and speak a response when text-to-speech is available."""
        print(f"Assistant: {message}")
        if self.speech_engine is not None:
            self.speech_engine.say(message)
            self.speech_engine.runAndWait()

    def listen(self) -> Optional[str]:
        """Capture one microphone request and convert it to text."""
        if self.recognizer is None:
            self.speak("Speech recognition is not installed. Run pip install -r requirements.txt.")
            return None

        try:
            with sr.Microphone() as microphone:
                self.speak("Listening...")
                self.recognizer.adjust_for_ambient_noise(microphone, duration=0.5)
                audio = self.recognizer.listen(microphone, timeout=5, phrase_time_limit=8)
            return self.recognizer.recognize_google(audio)
        except sr.WaitTimeoutError:
            self.speak("I did not hear anything. Please try again.")
        except sr.UnknownValueError:
            self.speak("I could not understand that. Please repeat the command.")
        except sr.RequestError:
            self.speak("The speech recognition service is unavailable. Please try again later.")
        except OSError:
            self.speak("No working microphone was found. You can use text mode instead.")
        return None

    def process_command(self, command: str) -> bool:
        """Perform a command and return False when the assistant should stop."""
        normalized = command.lower().strip()

        if any(greeting in normalized for greeting in ("hello", "hi", "hey")):
            self.speak("Hello! How can I help you?")
        elif "time" in normalized:
            current_time = datetime.now().strftime("%I:%M %p")
            self.speak(f"The current time is {current_time}.")
        elif "date" in normalized or "today" in normalized:
            current_date = datetime.now().strftime("%A, %B %d, %Y")
            self.speak(f"Today is {current_date}.")
        elif normalized.startswith(("search for ", "search ", "google ")):
            topic = normalized.removeprefix("search for ").removeprefix("search ").removeprefix("google ").strip()
            if topic:
                webbrowser.open(f"https://www.google.com/search?q={quote_plus(topic)}")
                self.speak(f"I opened a web search for {topic}.")
            else:
                self.speak("Please tell me what you want to search for.")
        elif normalized in {"exit", "quit", "stop", "goodbye"}:
            self.speak("Goodbye!")
            return False
        else:
            self.speak("I do not know that command. Please try again.")
        return True

    def run(self) -> None:
        """Listen continuously until the user says stop or goodbye."""
        self.speak("Voice assistant started. Say hello, ask for the time or date, or say search followed by a topic.")
        while True:
            command = self.listen()
            if command is not None:
                print(f"You: {command}")
                if not self.process_command(command):
                    break


def run_text_demo(assistant: VoiceAssistant) -> None:
    """Run the same command logic without requiring a microphone."""
    assistant.speak("Text demo started. Type a command, or type stop to exit.")
    while True:
        command = input("You: ").strip()
        if not command:
            assistant.speak("Please enter a command.")
            continue
        if not assistant.process_command(command):
            break


def main() -> None:
    parser = argparse.ArgumentParser(description="A beginner Python voice assistant")
    parser.add_argument("--text", action="store_true", help="Use keyboard input instead of a microphone")
    arguments = parser.parse_args()

    assistant = VoiceAssistant()
    if arguments.text:
        run_text_demo(assistant)
    else:
        assistant.run()


if __name__ == "__main__":
    main()