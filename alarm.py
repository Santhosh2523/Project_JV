import pyttsx3
import datetime
import os

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
engine.setProperty("rate", 170)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


extractedtime = open("alarm_text", "rt")
time = extractedtime.read()
Time = str(time)
extractedtime.close()

deletetime = open("alarm_text", "r+")
deletetime.truncate(0)
deletetime.close()


def ring(time_):
    timeset = str(time_)
    timenow = timeset.replace("Jarvis", "")
    timenow = timenow.replace("set an alarm", "")
    timenow = timenow.replace(" and ", "")
    Alarmtime = str(timenow)
    print(Alarmtime)
    while True:
        currenttime = datetime.datetime.now().strftime("%H:%M:%S")

        if currenttime == Alarmtime:
            speak("Alarm ringing")
            os.startfile('Vaa Senthaazhini.mp3')
        elif currenttime + "00:00:30" == Alarmtime:
            exit()


ring(time)
