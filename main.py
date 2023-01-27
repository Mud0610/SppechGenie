import speech_recognition as sr
from time import ctime
import webbrowser
import time
import os
import datetime
import subprocess

r = sr.Recognizer()


def record_audio(ask=False):
    with sr.Microphone() as source:
        if ask:
            print(ask)
        print("Listening")
        r.pause_threshold = 1
        r.energy_threshold = 3000
        audio = r.listen(source)
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio)
        except sr.UnknownValueError:
            print("Sorry ! I did'nt get that.")
        except sr.RequestError:
            print("Sorry, my speech service is down.")
        return voice_data


def note(text):
    date = datetime.datetime.now()
    file_name = str(date).replace(":", "-")+"-note.txt"
    with open(file_name, "w") as f:
        f.write(text)

    subprocess.Popen(["notepad.exe", file_name])


def vscode(code):
    date = datetime.datetime.now()
    file_name = str(date).replace(":", "-")+"-note.txt"
    with open(file_name, "w") as f:
        f.write(code)

    subprocess.Popen(
        ["C:\\Users\\user\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe", file_name])


def respond(voice_data):
    if "what is your name" in voice_data:
        print("My name is SpeechGenie.")

    if "what is the time" in voice_data:
        print(ctime())

    if "search" in voice_data:
        search = record_audio("What do you want to search for ?")
        url = "https://google.com/search?q=" + search
        webbrowser.get().open(url)
        print("Here it what I found for "+search)

    if "find location" in voice_data:
        location = record_audio("What is the location ?")
        url = "https://google.nl/maps/place/" + location + "/&amp"
        webbrowser.get().open(url)
        print("Here is the location of "+location)

    if "open code" in voice_data:
        codePath = "C:\\Users\\user\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
        os.startfile(codePath)

    if "make a note" in voice_data:
        note_text = record_audio("What would you like me to write down ?")
        note(note_text)
        print("I've made a note of it.")

    # if "continue" in voice_data:
    #     note_text_again = record_audio(
    #         "What would you like me to write down ?")
    #     with open(file_name, "w") as f:
    #         f.write(note_text_again)
    #     subprocess.Popen(
    #         ["C:\\Users\\user\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe", file_name])

    if "write the code" in voice_data:
        code_text = record_audio("What would you like me to write down ?")
        vscode(code_text)
        print("I've made a note of it.")

    if "exit" in voice_data:
        exit()


time.sleep(1)
print("How can I help you ?")

while 1:
    voice_data = record_audio()
    respond(voice_data)
