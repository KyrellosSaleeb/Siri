# Siri Voice Assistant

A simple voice assistant built with Python that can perform various tasks like telling the time, answering questions, translating text, and more. It uses speech recognition, text-to-speech, and Wikipedia for knowledge queries.

## Features

- **Speech Recognition**: Converts speech to text using the microphone.
- **Text-to-Speech (TTS)**: Converts text into spoken words using `pyttsx3`.
- **Intents Handling**: Responds to different intents like greetings, jokes, weather queries, and more.
- **Knowledge Queries**: Fetches answers from Wikipedia for general queries.
- **Translation**: Translates text to different languages using the Google Translate API.
- **Graphical User Interface (GUI)**: Built with `Tkinter` for easy interaction.

## Requirements

Ensure you have the following libraries installed:

- `speechrecognition`
- `pyttsx3`
- `winsound` (Windows only)
- `googletrans`
- `wikipedia`
- `tkinter` (for GUI)

You can install the required dependencies via `pip`:
pip install speechrecognition pyttsx3 googletrans wikipedia

## Note:

winsound is included by default in Windows. On macOS and Linux, you may need to use another library to play sounds.

## How to Run the Program
- Clone this repository or download the Python script (assistant.py).
- Install the dependencies listed above.
- Run the Python script:
    python assistant.py
- The program will open a GUI window with buttons for listening and stopping the assistant.
- Press "Start Listening" to begin issuing voice commands.
- Press "Stop Assistant" to exit the assistant.


## Features Walkthrough
- Greeting: If the user says "hello," "hi," or similar, the assistant responds with a greeting.
- Farewell: If the user says "goodbye" or "bye," the assistant will respond with a farewell message.
- Time & Date: The assistant can respond with the current time and date.
- Jokes: You can ask the assistant to tell a joke.
- Knowledge Queries: You can ask the assistant "What is [something]?" and it will fetch information from Wikipedia.
- Translation: The assistant can translate text into another language. You can say "translate hello to Spanish" or similar.
- Stop Assistant: Use the command to stop the assistant and quit the program.

## Example Usage
Commands:
- Greeting: "Hello", "Hi", "Good morning"
- Farewell: "Goodbye", "See you later"
- Time: "What time is it?", "Tell me the time"
- Date: "What’s the date?", "Today’s date"
- Jokes: "Tell me a joke", "Say something funny"
- Knowledge Queries: "What is Python?", "Who is Albert Einstein?"
- Translation: "Translate hello to French", "What’s the translation for apple in Spanish?"

## GUI Interface:

- Start Listening: Press to start voice recognition.
- Stop Assistant: Press to end the session.
- Technologies Used
- Speech Recognition: speechrecognition library for converting speech to text.
- Text-to-Speech: pyttsx3 for text-to-speech functionality.
- GUI: tkinter for the graphical interface.
- Translation: Google Translate API via googletrans library.
- Knowledge Base: Wikipedia API via wikipedia library.

## Limitations
- This assistant is currently limited to handling a predefined set of commands (intents).
- Works best with clear speech and in relatively quiet environments.

![image](https://github.com/user-attachments/assets/f6927a7b-cdd8-48a2-849b-5e09e8f58cb5)
![image](https://github.com/user-attachments/assets/96ced69f-35d5-4af2-9b04-a29c51e24c48)
![image](https://github.com/user-attachments/assets/0b49f967-3b68-4b17-8258-a4d193d1df13)
![image](https://github.com/user-attachments/assets/b30c72ed-669c-4705-b27c-1e13828f53d7)

