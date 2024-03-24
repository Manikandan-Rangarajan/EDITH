import pyttsx3
import speech_recognition
import webbrowser

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)
engine.setProperty("rate", 170)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def takeCommand():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.8
        r.energy_threshold = 700
        audio = r.listen(source, 0, 3)

    try:
        print("Understanding...")
        query = r.recognize_google(audio, language='en-in')
        print(f"You said: {query}\n")
    except Exception as e:
        print("Say that again...")
        return "None"
    return query


if __name__ == "__main__":
    while True:
        query = takeCommand().lower()
        if "code alpha" in query:
            from GreetMe import greetMe
            greetMe()

            while True:
                query = takeCommand().lower()
                if "hold" in query:
                    speak("Ok sir, I'm on hold.")
                    break

                elif "intro" in query.lower():
                    intro = "I am Blaze. I am Joker Panda's personal virtual assistant"
                    speak(intro)

                elif "google" in query.lower():
                    from SearchFile import searchGoogle
                    searchGoogle(query)

                elif "youtube" in query.lower():
                    from SearchFile import searchYoutube
                    searchYoutube(query)

                elif "code exit" in query.lower():
                    speak("Ok sir, See you again..")
                    exit()
