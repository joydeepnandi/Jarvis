import pyttsx3  # pip install pyttsx3
import speech_recognition as sr  # pip install speechRecognition
import datetime
import wikipedia  # pip install wikipedia
import webbrowser as wb
import os
import smtplib
import selenium

chrome_path = "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\chrome"
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[0].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening! ")

    speak("Hello Sir! I am Jarvis. Please tell me how may I help you.")


def takeCommand():
    # Takes microphone input from the user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source, duration=0.5)
        r.pause_threshold = 1
        r.energy_threshold = 500
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-in")
        query = query.lower()
        print(query)
        if ('jarvis' in query):
            speak("Ok sir")
            print("User Said : ", query)
        else:
            speak("Say that again please")
            return ("None")
    except Exception as e:
        speak("Say that again please")
        print("Say that again please...")
        return ("None")
    return (query)


def continuecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 2000
        audio = r.listen(source)
    try:

        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        speak("ok sir")
        print(query)

    except Exception as e:
        speak("Say that again please")
        print("Say that again please...")
        return ("None")
    return (query)


def stopcommand():
    query = ""
    while ("jarvis" not in query):
        print(query)
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            r.adjust_for_ambient_noise(source, duration=0.5)
            r.pause_threshold = 1
            r.energy_threshold = 500
            audio = r.listen(source)
        try:
            query = r.recognize_google(audio, language='en-in')
            query = query.lower()
            print(query)
        except Exception as e:
            print('no')
            pass
    return


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('joydeep.nandi9@gmail.com', 'abcdefghi')
    server.sendmail('xyzg@gmail.com', to, content)
    server.close()


if __name__ == "__main__":
    wishMe()
    while True:
        # if 1:
        query = takeCommand().lower()
        query = query.replace("jarvis", "")
        if query == "None":
            continue
        elif "hi" in query or "hello" in query:
            speak("Hello Joydeep!")
        elif "stop" in query:
            speak("Wake me up by saying Jarvis")
            stopcommand()
            speak("I am awake Sir")
        elif 'wikipedia' in query:
            speak('Searching in wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'search' in query:
            query = query.replace('search', '')
            query = query.replace('Jarvis', '')
            query = query.replace('jarvis', '')
            wb.open_new_tab('https://www.google.com/search?source=hp&ei=xhHoXNviIMjJrQHyvonQAw&q=' + query)

        elif 'open' in query and 'youtube' in query:
            speak("Which video do you want to play")
            while (True):
                if (query == "None"):
                    continue
                else:
                    query = continuecommand().lower()
                    print(query)
                    try:
                        query = query.replace("play", "")
                    except:
                        query = query
                    wb.open_new_tab("https://www.youtube.com/results?search_query=" + query)
                    break
        elif 'open google' in query:
            wb.open_new_tab("http://www.google.com")

        elif 'open stackoverflow' in query:
            wb.open_new_tab("http://www.stackoverflow.com")
        elif 'open leetcode' in query:
            wb.open_new_tab("https://leetcode.com")
        elif 'open codechef' in query:
            wb.open_new_tab("http://www.codechef.com")
        elif 'open hackerearth' in query:
            wb.open_new_tab("http://www.hackerearth.com")
        elif 'open whatsapp' in query:
            wb.open_new_tab("https://web.whatsapp.com")



        elif 'open python' in query:
            # copy and paste python idle's path
            python = 'C:\\Users\\Win10\\AppData\\Local\\Programs\\Python\\Python36-32\\Lib\\idlelib\\idle.pyw'
            os.startfile(python)
        elif 'close python' in query:
            os.system("TASKKILL /F /IM pythonw.exe")


        elif 'open spotify' in query:
            #copy and paste the path here
            spotify = 'C:\\Users\\Win10\\AppData\\Roaming\\Spotify\\Spotify.exe'
            os.startfile(spotify)
        elif 'close spotify' in query:
            os.system("TASKKILL /F /IM spotify.exe")

        elif 'close chrome' in query:
            os.system("TASKKILL /F /IM chrome.exe")

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'email to' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "xyzg@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry Sir. I am not able to send this email")
        elif 'shutdown' in query:
            speak("Bye Sir")
            os.system("shutdown /s /t 1")
        elif 'restart' in query:
            speak("See you in a while")
            os.system("shutdown /r /t 1")