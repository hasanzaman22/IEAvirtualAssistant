#                           Hasan Zamanli [English With AI] [Adriana]
# Libaries for use my tool
# pip install SpeechRecognition
# pip install pyaudio
# pip install pywhatkit
# pip install gtts
# pip install playsound
# pip install openai
# For Linux: if playsound give some error, install this libary - sudo apt install python3-gst-1.0
# If alsa give error, install and import this libary - python3 -m pip install sounddevice

import os
import speech_recognition as sr
import pyaudio
import pywhatkit
from gtts import gTTS
from playsound import playsound
import sounddevice
import openai
import time
from datetime import date, datetime

openai.api_key = "YOUR_API_KEY"


while True:
    def speech(text):
        print(text)
        language = "en"
        output = gTTS(text=text, lang=language, slow=False)

        output.save("../sounds/records.mp3")
        playsound("../sounds/records.mp3")


    r = sr.Recognizer()

    def get_audio():
        while True:
            with sr.Microphone() as source:
                r.energy_threshold = 400
                r.adjust_for_ambient_noise(source)
                r.dynamic_energy_threshold = True
                audio = r.listen(source)
            try:
                speech_text = r.recognize_google(audio, language="en-EN")
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
            elif "my name" in text.lower():
                speech("\tYour name is Hasan.")
            elif "your name" in text.lower():
                speech("\tMy name is Adriana.")
            elif "which day" in text.lower() or "what day" in text.lower():
                toDay = time.strftime("%A")
                speech(f"\t {toDay}")
            elif "what time" in text.lower():
                speech(datetime.now().strftime("%H:%M"))
            elif "sleep mode" in text.lower():
                speech("\tHow many seconds continue?")
                sec = float(get_audio())
                speech(f"\tOkay, {sec} sleep mode goes seconds.")
                sleep = time.sleep(sec)
                speech("\tSleep mode ended.")
            elif "keep note" in text.lower():
                speech("What name the file name?")
                txtFile = get_audio() + ".txt"
                speech("Note keeping...")
                texT = get_audio()
                filE = open(txtFile, "w", encoding='utf-8')
                filE.writelines(texT)
                filE.close()
            elif "close program" in text.lower():
                exit()
            else:
                response = openai.Completion.create(
                    model="text-davinci-002",
                    prompt=f'{text}: Hello, who are you?\n\tAI: I am an AI created by OpenAI. How can I help you today?'
                           f'\n{text}:',
                    temperature=0.9,
                    max_tokens=150,
                    top_p=1,
                    frequency_penalty=0,
                    presence_penalty=0.6,
                    stop=[f'{text}:', "AI:"]
                )

                start_sequence = response
                restart_sequence = text

                speech(f'{response["choices"][0]["text"]}')

                continue
    else:
        speech("Call Adriana first.")
        continue

    # answer = input("Do you want to continue? y/n\n")
    # if answer == "y":
    #     continue
    # else:
    #     exit()