import datetime
import os
import pyautogui
import pyttsx3
import requests
import speech_recognition
from bs4 import BeautifulSoup
from speech_recognition import Recognizer

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
engine.setProperty("rate", 170)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def takeCommand():
    r: Recognizer = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        # speak(speech_recognition.Microphone.list_microphone_names())
        print("Listening....")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source, 0, 4)

    try:
        print("Understanding....")
        query = r.recognize_google(audio, language='en-in')
        query = query.lower()
        print(f"You said : {query}")
    except Exception as e:
        print(f"Say that again {e}")
        return "None"
    return query


def alarm(query_1):
    timehere = open("alarm_text", "a")
    timehere.write(query_1)
    timehere.close()
    os.startfile("alarm.py")


if __name__ == "__main__":
    from GreetME import greetMe

    greetMe()
    while True:
        query = takeCommand().lower()
        if "wake up" in query:
            from GreetME import greetMe

            greetMe()

        elif "go to sleep" in query:
            speak("ok sir , you can call me any time")
            break

        elif "hello" in query:
            speak("Hello sir I am Jarvis,How are you ?")

        elif "i am fine" in query:
            speak("that's great , sir")

        elif "how are you" in query:
            speak("Prefect sir")

        elif "thank you" in query:
            speak("you are welcome , sir")

        elif "pause" in query:
            pyautogui.press("k")
            speak("video passed")

        elif "play" in query:
            pyautogui.press("k")
            speak("Video playing")

        elif "mute" in query:
            pyautogui.press("m")
            speak("video are mute")

        elif "unmute" in query:
            pyautogui.press("m")
            speak("Video are unmute")

        elif "volume up" in query:
            from keyboard import volumeup

            speak("Turning volume up , sir")
            volumeup()

        elif "volume down" in query:
            from keyboard import volumedown

            speak("Turning volume down , sir")
            volumedown()

        elif "open" in query:
            from Dictapp import openappweb

            openappweb(query)

        elif "close" in query:
            from Dictapp import closeappweb

            closeappweb(query)

        elif "google" in query:
            from Search_Engine import SearchGoogle

            SearchGoogle(query)

        elif "youtube" in query:
            from Search_Engine import SearchYoutube

            SearchYoutube(query)

        elif "wikipedia" in query:
            from Search_Engine import SearchWikipedia

            SearchWikipedia(query)

        elif "news" in query:
            from NewsRead import latestnews

            latestnews()

        elif "temperature" in query:
            search = "Hyderabad in temperature"
            url = f"https://www.google.com/search?q={search}"
            r = requests.get(url)
            data = BeautifulSoup(r.text, "html.parser")
            temp = data.find("div", class_="BNeawe").text
            speak(f"current{search} is {temp}")

        elif "weather" in query:
            search = "Hyderabad in weather"
            url = f"https://www.google.com/search?q={search}"
            r = requests.get(url)
            data = BeautifulSoup(r.text, "html.parser")
            temp = data.find("div", class_="BNeawe").text
            speak(f"current{search} is {temp}")

        elif "set an alarm" in query:
            speak("input time Example:- 10 and 10 and 10")
            speak("set the time")
            a = input("Please tell the time :- ")
            alarm(a)
            speak("done sir")

        elif "the time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M")
            speak(f"sir,the time is {strTime}")

        elif "finally sleep" in query:
            speak("Going to sleep ,sir")
            exit()

        elif "remember that" in query:
            remember_Message = query.replace("remember that", "")
            # remember_Message = query.replace("jarvis", "")
            speak("You told me to remember that " + remember_Message)
            remember = open("remember_text", "w")
            remember.write(remember_Message)
            remember.close()

        elif "what do you remember" in query:
            remember = open("remember_text", "r")
            speak("you told me to remember that " + remember.read())
