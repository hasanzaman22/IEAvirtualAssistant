#                              Hasan Zamanli [Azerbaijani] [İsrafil]
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
import time
from datetime import date, datetime


while True:
    def speech(text):
        print(text)
        language = "tr"
        output = gTTS(text=text, lang=language, slow=False)

        output.save("../sounds/records.mp3")
        playsound("../sounds/records.mp3")


    recorder = sr.Recognizer()

    def get_audio():
        while True:
            with sr.Microphone() as source:
                audio = recorder.listen(source)
            try:
                speech_text = recorder.recognize_google(audio, language="az-AZ")
                print(speech_text)
            except sr.UnknownValueError:
                speech("Anlamadım.")
                continue
            except sr.RequestError:
                speech("Sistem çalışmıyor.")

            return speech_text

    first_text = get_audio()

    if "israfil" in first_text.lower():
        speech("\tDinliyorum...")
        while True:
            text = get_audio()
            if "youtube" in text.lower():
                speech("\tTamam, senin için youtubeda bunu açıyorum.")
                pywhatkit.playonyt(text)
                time.sleep(10)
                pass
            elif "spotify" in text.lower():
                speech("\tSpotify açılıyor...")
                os.system("spotify")
                time.sleep(10)
                pass
            elif "axtar" in text.lower():
                speech("\tTamam, senin için bunu arıyorum.")
                pywhatkit.search(text)
                time.sleep(10)
                pass
            elif "mənim adım" in text.lower():
                speech("\tSenin adın Hasan.")
            elif "sənin adın" in text.lower():
                speech("\tBenim adım İsrafil.")
            elif "necəsən" in text.lower():
                speech("\tŞükürler olsun, sen nasılsın?")
            elif "nə edirsən" in text.lower():
                speech("\tEmrindeyim, sen ne yapıyorsun?")
            elif "yaxşıyam" in text.lower():
                speech("\tHep iyi ol.")
            elif "şükür" in text.lower():
                speech("\tŞükürler içinde ol.")
            elif "maçı" in text.lower():
                speech("\tMaç")
            elif "kimsən" in text.lower():
                speech("\tBen İsrafil. Hasan'ın sanal, sesli asistanıyım.")
            elif "öpürəm" in text.lower():
                speech("\tBende öpüyorum.")
            elif "hansı gündəyik" in text.lower() or "neçənci gündəyik" in text.lower() or "neçənci gündü" in text.lower():
                toDay = time.strftime("%A")
                toDay.capitalize()
                if toDay == "Monday":
                    toDay = "\tBirinci gün"
                elif toDay == "Tuesday":
                    toDay = "\tİkinci gün"
                elif toDay == "Wednesday":
                    toDay = "\tÜçüncü gün"
                elif toDay == "Thursday":
                    toDay = "\tDördüncü gün"
                elif toDay == "Friday":
                    toDay = "\tBeşinci gün"
                elif toDay == "Saturday":
                    toDay = "\tAltıncı gün"
                elif toDay == "Sunday":
                    toDay = "\tYedinci gün"
                speech(toDay)
            elif "saat neçədir" in text.lower():
                speech(datetime.now().strftime("%H:%M"))
            elif "yuxuya keç" in text.lower() or "yuxuya get" in text.lower() or "yat" in text.lower():
                speech("\tKaç saniyelik?")
                sec = float(get_audio())
                speech(f"\tTamam, {sec} saniyelik uyku moduna geçiyorum.")
                sleep = time.sleep(sec)
                speech("\tUyku modu bitti.")
            elif "qeyd et" in text.lower() or "israfil yaz" in text.lower():
                speech("\tDosyanın ismi ne olsun?")
                txtFile = get_audio() + ".txt"
                speech("\tYazıyorum...")
                texT = get_audio()
                filE = open(txtFile, "w", encoding='utf-8')
                filE.writelines(texT)
                filE.close()
                speech("\tYazdım.")
            elif "sağol" in text.lower() or "sağolun" in text.lower() or "təşəkkür" in text.lower() or "təşəkkürlər" in text.lower():
                speech("\tÖnemli değil.")
            elif "proqramı bağla" in text.lower() or "proqramdan çıx" in text.lower() or "proqramı söndür" in text.lower():
                exit()
            else:
                speech("\tÖyle bir soruya henüz cevabım yok.")
                continue
    else:
        speech("\tÖnce İsrafili çağır koçum.")
        continue

    # question = speech("Devam etmek istiyor musunuz?\n")
    # answer = get_audio()
    # if answer == "hə" or "bəli":
    #     continue
    # else:
    #     exit()