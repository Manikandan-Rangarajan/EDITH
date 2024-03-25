import datetime
import pyttsx3

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)
engine.setProperty("rate", 170)


def speak(query):
    engine.say(query)
    engine.runAndWait()


def greetMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour <= 12:
        speak("Good Morning Boss.")
    elif hour > 12 and hour <= 18:
        speak("Good Afternoon Boss")
    else:
        speak("Good Evening Boss.")
    speak("What is today's task Boss?")

def iAmUp():
    speak("Yes Boss, I'm raring to go")
    speak("What's the task now Boss.")
