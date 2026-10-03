import speech_recognition as sr
import webbrowser
import win32com.client
import os
import music_librerary
import credentials
import requests
from openai import OpenAI

speaker = win32com.client.Dispatch("SAPI.SpVoice")
client = OpenAI(api_key=credentials.openai_key)
history = [
    {"role": "system", "content": "You are Jarvis, a voice assistant. Reply in 1-3 short sentences, plain text only, no markdown or lists."}
]

def speak(text):
    speaker.Speak(text)

def get_news():
    try:
        res = requests.get(
            "https://newsapi.org/v2/top-headlines",
            params={"country": "us", "apiKey": credentials.newsapi},
            timeout=10,
        )
        data = res.json()
        print("News response:", data.get("status"), data.get("message"))
        if data.get("status") != "ok":
            speak("Could not fetch the news")
            return
        speak("Here are the top headlines")
        for a in data["articles"][:5]:
            print(a["title"])
            speak(a["title"])
    except Exception as e:
        print("News error:", e)
        speak("Could not fetch the news")

def ask_ai(question):
    history.append({"role": "user", "content": question})
    try:
        res = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=history[:1] + history[-10:],
            max_tokens=300,
        )
        answer = res.choices[0].message.content
        history.append({"role": "assistant", "content": answer})
        print("AI:", answer)
        speak(answer)
    except Exception as e:
        print("AI error:", e)
        history.pop()
        speak("Could not reach AI")

def processCommand(c):
    c = c.lower()
    print("Heard:", c)
    if "open google" in c:
        speak("Opening Google")
        webbrowser.open("https://www.google.com")
    elif "open youtube" in c:
        speak("Opening YouTube")
        webbrowser.open("https://www.youtube.com")
    elif "open openleaf" in c:
        speak("Opening Openleaf")
        webbrowser.open("https://www.openleaf.ai")
    elif "open facebook" in c:
        speak("Opening Facebook")
        webbrowser.open("https://www.facebook.com")
    elif "open twitter" in c:
        speak("Opening Twitter")
        webbrowser.open("https://www.twitter.com")
    elif "open instagram" in c:
        speak("Opening Instagram")
        webbrowser.open("https://www.instagram.com")
    elif "open linkedin" in c:
        speak("Opening LinkedIn")
        webbrowser.open("https://www.linkedin.com")
    elif "open github" in c:
        speak("Opening GitHub")
        webbrowser.open("https://www.github.com")
    elif "ytm" in c:
        speak("Opening YouTube Music")
        webbrowser.open("https://music.youtube.com")
    elif "open gmail" in c:
        speak("Opening Gmail")
        webbrowser.open("https://mail.google.com")
    elif "notepad" in c:
        speak("Opening Notepad")
        os.system("notepad.exe")
    elif "calculator" in c:
        speak("Opening Calculator")
        os.system("calc.exe")
    elif "command prompt" in c:
        speak("Opening Command Prompt")
        os.system("cmd.exe")
    elif "file explorer" in c:
        speak("Opening File Explorer")
        os.system("explorer.exe")
    elif "open chrome" in c:
        speak("Opening Google Chrome")
        os.system("start chrome")
    elif "open edge" in c:
        speak("Opening Microsoft Edge")
        os.system("start msedge")
    elif "open brave" in c:
        speak("Opening Brave Browser")
        os.system("start brave")
    elif "open spotify" in c:
        speak("Opening Spotify")
        os.system("start spotify")
    elif "open vscode" in c:
        speak("Opening Visual Studio Code")
        os.system("start code")
    elif "open whatsapp" in c or "open watsapp" in c:
        speak("Opening WhatsApp")
        os.system("start whatsapp:")
    elif "open telegram" in c:
        speak("Opening Telegram")
        os.system("start telegram")
    elif c.startswith("play"):
        song = c.replace("play", "", 1).strip()
        link = music_librerary.music.get(song)
        if link:
            speak(f"Playing {song}")
            webbrowser.open(link)
        else:
            speak("Song not found")
    elif "news" in c:
        get_news()
    else:
        ask_ai(c)

if __name__ == "__main__":
    speak("Hello Sir, I am Jarvis. How can I assist you today?")
    r = sr.Recognizer()

    while True:
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source, timeout=3, phrase_time_limit=3)
            word = r.recognize_google(audio)

            if word.lower() == "jarvis":
                speak("Yes Sir, what can I do for you?")
                with sr.Microphone() as source:
                    print("Jarvis Active...")
                    audio = r.listen(source, timeout=5, phrase_time_limit=5)
                command = r.recognize_google(audio)
                processCommand(command)

        except (sr.WaitTimeoutError, sr.UnknownValueError):
            pass
        except Exception as e:
            print("Error:", e)