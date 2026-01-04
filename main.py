import time
import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import requests

# pip install pocketsphinx

recognizer=sr.Recognizer()
engine = pyttsx3.init()

newsapi="2d37fadd71a14e7b868c8471db94e412"

def speak(text):
    print(text)
    engine.say(text)
    engine.runAndWait()

def processComand(c):
    if "open google" in c.lower():
        webbrowser.open("https://www.google.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://www.youtube.com")
    elif "open LinkedIn" in c.lower():
        webbrowser.open("https://www.linkedin.com")
    elif "open github" in c.lower():
        webbrowser.open("https://www.github.com")
    elif c.lower().startswith("play"):
        song=c.lower().split(" ")[1]
        link=musicLibrary.music[song]
        webbrowser.open(link)
        
    elif "news" in c.lower():
            response = requests.get("https://newsapi.org/v2/top-headlines?sources=bbc-news&apiKey=2d37fadd71a14e7b868c8471db94e412")
            data = response.json()  # converts to dictionary
            titles = [article["title"] for article in data["articles"] if article.get("title")]

            if titles:
                speak("Here are the top news headlines from BBC News.")
                for i, title in enumerate(titles[:5], start=1):
                    print(f"{i}. {title}")
                    speak(f"Headline {i}: {title}")
                    time.sleep(1)
    else:
        # let openAI handle the request
        pass
if __name__=="__main__":
    speak("Initializing Jarvis")
    while True:
        # Listen for the wake word "Jarvis"
        # obtain audio from the microphone
        r = sr.Recognizer()

        # recognization speech using Google Web Speech API
        print("Recognizing...")
        try:
            with sr.Microphone() as source:
                print("I'm listening... Speak something, Miss Saranya 🎙️...")
                # recognizer.adjust_for_ambient_noise(source, duration=1)  # helps reduce noise
                audio = r.listen(source, timeout=5, phrase_time_limit=10)
            word = r.recognize_google(audio)
            print("You said:", word)
            command = r.recognize_google(audio)
            processComand(command)

        except Exception as e:
            print("Error; {0}".format(e))
    