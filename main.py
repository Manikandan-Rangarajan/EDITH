import datetime

import pyttsx3
import requests
import speech_recognition
import webbrowser
from bs4 import BeautifulSoup

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)
engine.setProperty("rate", 200)


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
        if "alpha" in query:
            from GreetMe import greetMe
            greetMe()

            while True:
                query = takeCommand().lower()
                if "hold" in query:
                    speak("Ok sir, I'm on hold.")
                    break

                elif "intro" in query:
                    intro = "I am EDITH. I am Joker Panda's personal virtual assistant"
                    speak(intro)

                elif "open" in query or "launch" in query:
                    from DictApp import openAppWeb
                    openAppWeb(query)

                elif "close" in query or "scrap" in query:
                    from DictApp import closeAppWeb
                    closeAppWeb(query)

                elif "google" in query:
                    from SearchFile import searchGoogle
                    searchGoogle(query)

                elif "youtube" in query:
                    from SearchFile import searchYoutube
                    searchYoutube(query)

                elif "wikipedia" in query:
                    from SearchFile import searchWikipedia
                    searchWikipedia(query)

                elif "temperature" in query:
                    search = "temperature in chennai"
                    url = f"https://www.google.com/search?q={search}"
                    r = requests.get(url)
                    data = BeautifulSoup(r.text,"html.parser")
                    temp_key = data.find("div", class_ = "BNeawe").text
                    speak(f"the current {search} is {temp_key}")

                elif "weather" in query:
                    search = "weather in chennai"
                    url = f"https://www.google.com/search?q={search}"
                    r = requests.get(url)
                    data = BeautifulSoup(r.text,"html.parser")
                    temp_key = data.find("div", class_ = "BNeawe").text
                    speak(f"the current {search} is {temp_key}")

                elif "time" in query:
                    hour = datetime.datetime.now().strftime("%H")
                    mint = datetime.datetime.now().strftime("%M")
                    print(hour + ":" + mint)
                    speak(f"the time is {hour} hours and {mint}minutes")

                elif "code exit" in query:
                    speak("Ok sir, See you again..")
                    exit()
