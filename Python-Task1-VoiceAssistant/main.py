# Simple Python Voice Assistant

import pyttsx3
from datetime import datetime
import webbrowser


# Create the voice engine
speaker = pyttsx3.init()


# Function to make the assistant speak
def speak(message):
    print("Assistant:", message)
    speaker.say(message)
    speaker.runAndWait()


# Function to handle commands
def process_command(command):

    command = command.lower()

    if command == "hello":
        speak("Hello! How can I help you?")

    elif "time" in command:
        current_time = datetime.now().strftime("%I:%M %p")
        speak("The current time is " + current_time)

    elif "date" in command:
        current_date = datetime.now().strftime("%d %B %Y")
        speak("Today's date is " + current_date)

    elif "google" in command:
        speak("Opening Google")
        webbrowser.open("https://www.google.com")

    elif command == "stop":
        speak("Goodbye!")
        return False

    else:
        speak("Sorry, I don't understand that command.")

    return True


# Main program
speak("Hello! I am your voice assistant.")

while True:

    command = input("You: ")

    if process_command(command) == False:
        break