#                              Hasan Zamanli [English] [Adriana]
# Libaries for use my tool
# pip install SpeechRecognition
# pip install pyaudio
# pip install pywhatkit
# pip install gtts
# pip install playsound
# For Linux: if playsound give some error, install this libary - sudo apt install python3-gst-1.0
# If alsa give error, install and import this libary - python3 -m pip install sounddevice

import os
import speech_recognition as sr
import pyaudio
import pywhatkit
from gtts import gTTS
from playsound import playsound
import sounddevice
import time
from datetime import date, datetime


while True:
    def speech(text):
        print(text)
        language = "en"
        output = gTTS(text=text, lang=language, slow=False)

        output.save("../sounds/records.mp3")
        playsound("../sounds/records.mp3")


    recorder = sr.Recognizer()

    def get_audio():
        while True:
            with sr.Microphone() as source:
                audio = recorder.listen(source)
            try:
                speech_text = recorder.recognize_google(audio, language="en-EN")
                print(speech_text)
            except sr.UnknownValueError:
                speech("I don't understand.")
                continue
            except sr.RequestError:
                speech("System not working.")

            return speech_text

    first_text = get_audio()

    if "adriana" in first_text.lower():
        speech("\tHow can I help you?")
        while True:
            text = get_audio()
            if "youtube" in text.lower():
                speech("\tOkay, i will open this on YouTube for you.")
                pywhatkit.playonyt(text)
                time.sleep(10)
                pass
            elif "spotify" in text.lower():
                speech("\tOkay, i will open Spotify for you.")
                os.system("spotify")
                time.sleep(10)
                pass
            elif "search" in text.lower():
                speech("\tOkay, i will search this on Google for you")
                pywhatkit.search(text)
                time.sleep(10)
                pass
            elif "info" in text.lower():
                speech(f"\tYou can read below {text}:")
                pywhatkit.info(text, lines=4)
            elif "my name" in text.lower():
                speech("\tYour name is Hasan.")
            elif "your name" in text.lower():
                speech("\tMy name is Adriana.")
            elif "how are you" in text.lower():
                speech("\tThanks to god, you?")
            elif "am good" in text.lower() or "am nice" in text.lower() or "I'm nice" in text.lower() or "I'm good" in text.lower():
                speech("\tAlways be happy")
            elif "am bad" in text.lower() or "am sad" in text.lower() or "I'm bad" in text.lower() or "I'm sad" in text.lower():
                speech("\tGo and work.")
            elif "who are you" in text.lower():
                speech("\tI'm Adriana. I'm Hasan's virtual voice assistant.")
            elif "what are you doing" in text.lower():
                speech("\tI'm at your service, what are you doing?")
            elif "which day" in text.lower() or "what day" in text.lower():
                toDay = time.strftime("%A")
                speech(f"\t {toDay}")
            elif "what time" in text.lower():
                speech(datetime.now().strftime("%H:%M"))
            elif "sleep mode" in text.lower() or "off" in text.lower():
                speech("\tHow many seconds?")
                sec = float(get_audio())
                speech(f"\tOkay, I'm going into {sec} second sleep mode.")
                sleep = time.sleep(sec)
                speech("\tSleep mode is over.")
            elif "keep note" in text.lower() or "adriana write" in text.lower():
                speech("What should the file name be?")
                txtFile = get_audio() + ".txt"
                speech("I am writing...")
                texT = get_audio()
                filE = open(txtFile, "w", encoding='utf-8')
                filE.writelines(texT)
                filE.close()
            elif "thank" in text.lower() or "thanks" in text.lower() or "appreciation" in text.lower():
                speech("\tYou're welcome.")
            elif "shutdown" in text.lower() or "shut up" in text.lower() or "off" in text.lower():
                exit()
            else:
                speech("I don't have an answer to that question yet.")
                continue
    else:
        speech("Call Adriana first.")
        continue

    # question = speech("Do you want to continue?\n")
    # answer = get_audio()
    # if answer == "hə" or "bəli":
    #     continue
    # else:
    #     exit()