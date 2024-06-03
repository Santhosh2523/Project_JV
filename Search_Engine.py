import speech_recognition
import pyttsx3
import pywhatkit
import wikipedia
import webbrowser


def takeCommand():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        # print(speech_recognition.Microphone.list_microphone_names())
        print("Listening....")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source, 0, 4)

    try:
        print("Understanding....")
        query = r.recognize_google(audio, language='en-in')
        print(f"You said : {query}")
    except Exception as e:
        print(f"Say that again {e}")
        return "None"
    return query


query = takeCommand().lower()

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
engine.setProperty("rate", 170)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def SearchGoogle(query):
    if "google" in query:
        import wikipedia as googleScrap
        query = query.replace("Jarvis", "")
        query = query.replace("google Search...", "")
        query = query.replace("google", "")
        speak("This is what i found an google")

        try:
            pywhatkit.search(query)
            result = googleScrap.summary(query, 1)
            speak(result)
        except:
            speak("No Speakable output available")


def SearchYoutube(query):
    if "youtube" in query:
        speak("This what i found for your search!")
        query = query.replace("youtube Search", "")
        query = query.replace("Youtube", "")
        query = query.replace("jarvis", "")

        web = "https://www.youtube.com/results?search_query=" + query
        webbrowser.open(web)
        pywhatkit.playonyt(query)
        speak("Done , sir")


def SearchWikipedia(query):
    if "wikipedia" in query:
        speak("Searching from Wikipedia..")
        query = query.replace("Wikipedia", "")
        query = query.replace("Search Wikipedia", "")
        query = query.replace("Jarvis", "")
        results = wikipedia.summary(query, sentences=2)
        speak("According to wikipedia")
        print(results)
        speak(results)
