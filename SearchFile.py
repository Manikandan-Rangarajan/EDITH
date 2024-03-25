import webbrowser

import pyttsx3
import pywhatkit
import speech_recognition as sr
import wikipedia
from bs4 import BeautifulSoup


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
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

query = takeCommand().lower()


engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)
engine.setProperty("rate", 170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def searchGoogle(query):
    if "google" in query:
        import wikipedia as googleScrap
        query = query.replace("edith","")
        query = query.replace("google","")
        query = query.replace("google search","")
        speak("This is What I found.")

        try:
            pywhatkit.search(query)
            result = googleScrap.summary(query,2)
            speak(result)
            print(result)
        except Exception as e:
            speak("No matches found")

def searchYoutube(query):
    if "youtube" in query:
        import wikipedia as googleScrap
        query = query.replace("edith","")
        query = query.replace("youtube","")
        query = query.replace("youtube search","")
        web = "https://www.youtube.com/results?search_query=" + query
        webbrowser.open(web)
        speak("This is What I found.")

        try:
            pywhatkit.playonyt(query)
            speak("Done, Boss!")
        except Exception as e:
            speak("No matches found")


def searchWikipedia(query):
    if "wikipedia" in query:
        speak("Searching from wikipedia")
        query = query.replace("wikipedia","")
        query = query.replace("wikipedia search","")
        query = query.replace("edith","")
        result = wikipedia.summary(query,sentences = 2)
        speak("According to wikipedia")
        print(result)
        speak(result)
