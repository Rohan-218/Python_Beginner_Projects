import pyttsx3  # Text-to-speech conversion library
import speech_recognition as sr  # Speech recognition library
import webbrowser  # For opening web pages
import datetime  # For getting the current time
import pyjokes  # For generating jokes
import os  # For interacting with the operating system (e.g., listing files)
from ttsvoice import tts  # Custom module for text-to-speech conversion

def sp_text():
    """
    Captures audio from the microphone and converts it to text using Google's speech recognition.
    """
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("\nSpeak...")  # Prompt in English: "Speak, I am listening..."
        tx_speech("Speak...")
        recognizer.adjust_for_ambient_noise(source)  # Adjust for ambient noise
        audio = recognizer.listen(source)  # Listen for audio
        try:
            print("Let me understand...")  # Prompt in English: "Let me understand..."
            data = recognizer.recognize_google(audio)  # Recognize speech using Google API
            print(data)  # Print the recognized text
            return data  # Return the recognized text
        except sr.UnknownValueError:  # Handle unrecognized speech
            print("Did you even say anything?")  # Prompt in English: "Did you even say anything?"

def tx_speech(data):
    """
    Converts text to speech using pyttsx3.
    """
    engine = pyttsx3.init()
    voices = engine.getProperty("voices")
    engine.setProperty("voice", voices[0].id)  # Set the voice
    engine.setProperty("rate", 170)  # Set the speaking rate
    engine.say(data)
    engine.runAndWait()
    # print("\n---->  Executed Successfully\n")

def txt_speech(string):
    """
    Converts text to speech using a custom tts function from the ttsvoice module.
    """
    tts(string, "male")
    print("\n---->  Executed Successfully\n")

def handle_command(command):
    """
    Processes the recognized command and performs the corresponding action.
    """
    command = command.lower()  # Convert to lowercase for easier comparison

    if "your name" in command:  # Respond to a query about the program's name
        name = " My name is Bablu. "
        print(name)
        tx_speech(name)

    elif "my name" in command:  # Respond to a query about the user's name
        m_name = " Your name is Nikhil."
        print(m_name)
        tx_speech(m_name)

    elif "time" in command:  # Provide the current time
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        print(current_time)
        tx_speech(current_time)

    elif "youtube" in command:  # Open YouTube in the web browser
        print("Open YouTube")
        webbrowser.open("https://www.youtube.com/")

    elif "instagram" in command:  # Open Instagram in the web browser
        print("Opening Instagram")
        webbrowser.open("https://www.instagram.com/?utm_source=pwa_homescreen&__pwa=1")

    elif "joke" in command:  # Tell a joke
        joke = pyjokes.get_joke(language='en', category='neutral')
        print(joke)
        tx_speech(joke)

    elif "play song" in command:  # Play a song from a specified directory
        directory = "C:\\Voiceover\\songs"
        try:
            songs = os.listdir(directory)
            if songs:
                print(songs)  # Print the list of songs
                os.startfile(os.path.join(directory, songs[0]))  # Play the first song
            else:
                print("No songs found in the directory.")
                tx_speech("No songs found in the directory.")
        except FileNotFoundError:
            print(f"Directory '{directory}' not found.")
            tx_speech(f"Directory '{directory}' not found.")
        except Exception as e:
            print(f"An error occurred: {e}")
            tx_speech(f"An error occurred: {e}")

    elif "exit" in command:  # Exit the program
        tx_speech("Exiting\nThank you")
        return False  # Indicate that we should exit the loop

    else:  # Handle unrecognized commands
        print("Didn't understand, please repeat")  # Prompt in English: "Didn't understand, please repeat"
        tx_speech("Didn't understand, please repeat")

    return True  # Indicate that we should continue the loop

def main():
    data1 = sp_text()  # Capture and recognize speech input

    if data1:  # If speech was recognized
        data1 = data1.lower()  # Convert the recognized text to lowercase for easier comparison

        if "listen" in data1:  # Check if the recognized text contains the word "listen"
            while True:
                data2 = sp_text()  # Capture additional speech input
                if data2:
                    if not handle_command(data2):  # Process the command and check if we should exit
                        break
                else:
                    print("Say something...")  # Prompt in English: "Say something..."
                    tx_speech("Say something...")
        elif "stop" in data1:
            print("----> Program stopped.")
            tx_speech("Program stopped.")
        else:
            print('''You need to say " listen" for me to start executing commands.''')  # Prompt in English: '''You need to say " listen" for me to start executing commands'''
            tx_speech('''You need to say " listen" for me to start executing commands.''')
            main()
    else:
        print("Say something...")  # Prompt in English: "Say something..."
        tx_speech("Say something...")
        main()

if __name__ == '__main__':
    main()
# Uncomment the following lines to test specific functionality
# time = datetime.datetime.now().strftime("%I:%M %p")
# print(time)
# txt_speech(time)
# txt_speech("Rak")
# joke_1 = pyjokes.get_joke(language= 'en', category= 'neutral')
# print(joke_1)
# txt_speech(joke_1)
# add = "C:\\Voiceover\\songs"
# listsong = os.listdir(add)
# print(listsong)
# os.startfile(os.path.join(add,listsong[0]))
# time.sleep(5)
