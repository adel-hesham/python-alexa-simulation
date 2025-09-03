import speech_recognition as sr
import pyttsx3
import webbrowser as wb

# Initialize voice engine once
voice = pyttsx3.init()

def speak(text):
    voice.say(text)
    voice.runAndWait()

def capture_audio():
    rec = sr.Recognizer()
    speak("Say something")

    with sr.Microphone() as src:
        rec.pause_threshold = 1
        print("Listening...")
        audio = rec.listen(src)

        try:
            text = rec.recognize_google(audio)
            print(f"You said: {text}")
            return text.lower()
        except sr.UnknownValueError:
            print("Sorry, I did not understand that.")
            return None
        except sr.RequestError as e:
            print(f"Could not request results; {e}")
            return None

def respond(audio):
    if audio in ['open chrome', 'open google chrome', 'open google']:
        speak("Opening Google Chrome")
        print("Opening Google Chrome")
        wb.open('https://www.google.com', new=2)

    elif audio in ['facebook', 'open facebook']:
        speak("Opening Facebook")
        print("Opening Facebook")
        wb.open('https://www.facebook.com', new=2)

    elif audio in ['youtube', 'open youtube']:
        speak("Opening YouTube")
        print("Opening YouTube")
        wb.open('https://www.youtube.com', new=2)

    elif audio in ['exit', 'close']:
        speak("Bye")
        quit()

    else:
        speak("I can't understand you")
        print("I can't understand you")

def main():
    while True:
        my_voice = capture_audio()
        if my_voice:
            respond(my_voice)

if __name__ == '__main__':
    main()
