import random
import speech_recognition as sr
import pyttsx3
import winsound
from datetime import datetime
from tkinter import Tk, Label, Button, Text, Scrollbar, END, Frame
from googletrans import Translator, LANGUAGES  # Import Translator and LANGUAGES
import wikipedia

# Initialize the text-to-speech engine
engine = pyttsx3.init()

def speak(text):
    """
    Converts text to speech.
    Arguments:
    text -- The text to be spoken by the assistant.
    """
    engine.setProperty('rate', 150)  # Set speech rate (words per minute)
    engine.say(text)  # Speak the text
    engine.runAndWait()  # Wait for the speech to finish

# Initialize the recognizer and translator
recognizer = sr.Recognizer()
translator = Translator()  # Initialize the translator

def play_beep():
    """
    Plays a beep sound.
    This is used to signal that the assistant is starting or performing an action.
    """
    frequency = 1000  # Frequency of the beep in Hz
    duration = 500    # Duration of the beep in milliseconds
    winsound.Beep(frequency, duration)  # Play the beep sound

# Intents and responses: These are mappings of user queries to appropriate responses or actions.
intents = {
    "greeting": ["hello", "hi", "hey", "good morning", "good evening"],
    "farewell": ["bye", "goodbye", "see you later", "take care"],
    "thanks": ["thank you", "thanks", "appreciate it"],
    "time_query": ["what time is it", "tell me the time", "current time"],
    "date_query": ["what's the date", "tell me today's date", "current date"],
    "joke": ["tell me a joke", "make me laugh", "say something funny"],
    "weather_query": ["what's the weather", "how's the weather", "is it raining", "weather forecast"],
    "reminder": ["set a reminder", "remind me to", "can you set a reminder"],
    "news_query": ["what's the news", "latest news", "news updates"],
    "calculation": ["what is", "calculate", "solve this", "do the math"],
    "quote": ["give me a quote", "inspire me", "motivate me"],
    "how_are_you": ["how are you", "how's it going", "what's up"],
    "small_talk": ["tell me something interesting", "say something", "talk to me"],
    "alarm_set": ["set an alarm", "wake me up at", "can you set an alarm"],
    "time_check": ["how much time is left", "how much time", "time remaining"],
    "translate": ["translate", "can you translate", "what's the translation for"],
    "stop": ["stop"]
}

responses = {
    "greeting": ["Hello! How can I assist you today?", "Hi there! What do you need?", "Hey! How's it going?"],
    "farewell": ["Goodbye! Have a great day!", "See you later!", "Take care!"],
    "thanks": ["You're welcome! Happy to help.", "No problem at all!", "Anytime!"],
    "time_query": [
        f"The current time is {datetime.now().strftime('%I:%M %p')}.",
        f"It's now {datetime.now().strftime('%H:%M')}.",
        f"The time is {datetime.now().strftime('%I:%M %p')}."
    ],
    "date_query": [
        f"Today is {datetime.now().strftime('%A, %B %d, %Y')}.",
        f"It's {datetime.now().strftime('%B %d, %Y')}.",
        f"The date is {datetime.now().strftime('%A, %d %B %Y')}."
    ],
    "joke": [
        "Why don’t scientists trust atoms? Because they make up everything!",
        "Why was the math book sad? It had too many problems.",
        "What do you call fake spaghetti? An impasta!"
    ],
    "translate": [
        "Sure! What do you need translated?",
        "Let me know what you want translated, and I’ll assist you.",
        "I can help with translations! Just tell me what you need."
    ],
    "stop": ["stop"]
}

def get_intent(user_input):
    """
    Determines the intent behind the user input.
    Arguments:
    user_input -- The input from the user (text).
    
    Returns:
    intent -- The identified intent (as a string), or None if no intent is found.
    """
    for intent, phrases in intents.items():
        if any(phrase in user_input for phrase in phrases):
            return intent
    
    # Detect knowledge-based questions more flexibly
    knowledge_keywords = [
        "who is", "what is", "tell me about", "do you know", "explain", "define", 
        "what's", "how does", "how is", "can you explain", "can you tell me", "describe", 
        "give me information about", "give me details on", "what does", "what are", "what's the meaning of", 
        "what do you know about", "how does it work", "how is it", "what's the definition of"
    ]
    
    if any(keyword in user_input for keyword in knowledge_keywords):
        return "knowledge_query"
    
    return None

def respond_to_intent(intent):
    """
    Responds based on the detected intent.
    Arguments:
    intent -- The identified intent (string).
    
    Returns:
    response -- A random response from the defined responses for the given intent.
    """
    if intent in responses:
        return random.choice(responses[intent])
    else:
        return "I'm sorry, I didn't understand that."

def handle_knowledge_query(user_input):
    """
    Fetches answers to general knowledge queries using Wikipedia.
    Arguments:
    user_input -- The input from the user (text), usually a question.
    
    Returns:
    summary -- A short Wikipedia summary of the query, or an error message if no information is found.
    """
    try:
        # Extract query by removing common question phrases
        query = user_input.replace("do you know", "").replace("what is", "").replace("who is", "").replace("tell me about", "").strip()

        if not query:
            return "Please specify what you want to know more about."

        # Search Wikipedia
        summary = wikipedia.summary(query, sentences=2)
        
        return summary  # Only return the summary here, TTS will happen later in handle_input.
        
    except wikipedia.exceptions.DisambiguationError as e:
        return f"Your query is too broad. Please try being more specific: {str(e.options[:5])}"
    except wikipedia.exceptions.PageError:
        return "Sorry, I couldn't find any information on that topic."
    except Exception as e:
        return f"An error occurred: {str(e)}"

def handle_translation(user_input):
    """
    Handles translation requests.
    Arguments:
    user_input -- The input from the user, e.g., "translate hello to Spanish."
    
    Returns:
    translation_output -- The translated text or an error message.
    """
    try:
        # Example input: "translate hello to spanish"
        parts = user_input.split("translate")[1].strip().split(" to ")
        text_to_translate = parts[0].strip()
        target_language_name = parts[1].strip().lower()

        # Convert language name to code
        target_language_code = next(
            (code for code, name in LANGUAGES.items() if name.lower() == target_language_name),
            None
        )

        if not target_language_code:
            return f"Sorry, I couldn't find the language '{target_language_name}'. Please try again."

        # Perform the translation
        translated_text = translator.translate(text_to_translate, dest=target_language_code).text
        
        # Write the translation to the GUI and speak it
        translation_output = f"The translation is: {translated_text}"
        display_text(translation_output)  # Display the translation
        speak(translated_text)           # Speak the translation
        return translation_output
    except IndexError:
        return "Please specify the text and target language, e.g., 'translate hello to Spanish'."
    except Exception as e:
        return f"An error occurred during translation: {str(e)}"

def recognize_speech():
    """
    Converts speech to text using the microphone.
    Returns:
    text -- The recognized speech as text, or an empty string if no speech is detected.
    """
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source, duration=1)
        display_text("Listening...")
        try:
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=10)
            display_text("Recognizing...")
            text = recognizer.recognize_google(audio)
            display_text(f"You said: {text}")
            return text.lower()
        except sr.UnknownValueError:
            display_text("Sorry, I could not understand. Please try again.")
            return ""
        except sr.RequestError:
            display_text("Sorry, unable to process the request.")
            return ""
        except sr.WaitTimeoutError:
            display_text("No speech detected within the timeout period.")
            return ""

def handle_input():
    """
    Handles the input received from the user (speech-to-text, intent recognition, and response generation).
    """
    play_beep()  # Play a beep to signal that the assistant is listening
    user_input = recognize_speech()  # Get the user's speech input
    if user_input:
        intent = get_intent(user_input)  # Determine the intent of the input
        if intent == "translate":
            response = handle_translation(user_input)  # Handle translation request
        elif intent == "knowledge_query":
            response = handle_knowledge_query(user_input)  # Handle knowledge query (Wikipedia search)
        else:
            response = respond_to_intent(intent)  # Handle other intents like greetings, jokes, etc.
        
        display_text(f"Siri: {response}")  # Display the response in the GUI
        speak(response)  # Speak the response out loud

        # If the intent is "stop", close the application
        if intent == "stop":
            stop_assistant()

def display_text(text):
    """
    Displays text in the GUI.
    Arguments:
    text -- The text to display in the output box.
    """
    output_box.insert(END, text + "\n")
    output_box.see(END)
    output_box.insert(END, "\n")

def stop_assistant():
    """
    Stops the assistant and closes the application.
    """
    display_text("Siri stopped.")  # Display that the assistant has stopped
    speak("Goodbye!")  # Speak goodbye message
    app.quit()  # Close the application

# GUI Setup
app = Tk()
app.title("Siri")
app.geometry("500x500")

frame = Frame(app)
frame.pack(pady=10)

Label(frame, text="Siri", font=("Helvetica", 16)).pack(pady=10)

output_box = Text(frame, height=20, width=60, wrap="word")
output_box.pack(pady=10)

scrollbar = Scrollbar(frame, command=output_box.yview)
scrollbar.pack(side="right", fill="y")
output_box.config(yscrollcommand=scrollbar.set)

Button(frame, text="Start Listening", command=handle_input, font=("Helvetica", 12)).pack(pady=5)
Button(frame, text="Stop Assistant", command=stop_assistant, font=("Helvetica", 12), fg="red").pack(pady=5)

app.mainloop()