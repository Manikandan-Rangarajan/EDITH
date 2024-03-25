import os
import pyautogui
import webbrowser
import pyttsx3
from time import sleep


engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)
engine.setProperty("rate", 170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

dictApp = {"commandPrompt":"cmd","word":"winword","excel":"excel","pycharm":"pc","visualStudiocode":"code","hyperTerminal":"terminal","settings":"tings"}

def  openAppWeb(query):
    speak("Launching Boss")
    if ".com" in query or ".co.in" in query or ".org" in query or ".in" in query:
        query = query.replace("open","")
        query = query.replace("edith","")
        query = query.replace("launch","")
        query = query.replace(" ","")

        webbrowser.open(f"https://www.{query}")

    else:
        keys = list(dictApp.keys())
        for app in keys:
            if app in query:
                os.system(f"start {dictApp[app]}")

def closeAppWeb(query):
    speak("Right away boss")
    if "one tab" in query or "1 tab" in query:
        pyautogui.hotkey("ctrl","w")

    elif "two tabs" in query:
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        speak("All tabs closed")

    elif "three tabs" in query:
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        speak("All tabs closed")

    elif "four tabs" in query:
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        speak("All tabs closed")

    else:
        keys = list(dictApp.keys())
        for app in keys:
            if app in query:
                os.system(f"taskkill /f /im {dictApp[app]}.exe")
