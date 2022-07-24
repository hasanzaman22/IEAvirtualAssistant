#                              Hasan Zamanli [Turkish] [Esra]
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

        tts.save("../sounds/records.mp3")
        playsound("../sounds/records.mp3")
        os.remove("../sounds/records.mp3")


    recorder = sr.Recognizer()

    def get_audio():
        while True:
            with sr.Microphone() as source:
                audio = recorder.listen(source)
            try:
                speech_text = recorder.recognize_google(audio, language="tr-TR")
                print(speech_text)
            except sr.UnknownValueError:
                speech("Anlamadım.")
                continue
            except sr.RequestError:
                speech("Sistem çalışmıyor.")

            return speech_text

    first_text = get_audio()

    if "esra" in first_text.lower():
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
            elif "ara" in text.lower():
                speech("\tTamam, senin için bunu arıyorum.")
                pywhatkit.search(text)
                time.sleep(10)
                pass
            elif "benim adım" in text.lower():
                speech("\tSenin adın Hasan.")
            elif "senin adın" in text.lower():
                speech("\tBenim adım İsrafil.")
            elif "nasılsın" in text.lower():
                speech("\tŞükürler olsun, sen nasılsın?")
            elif "iyiyim" in text.lower():
                speech("\tHep iyi ol.")
            elif "şükür" in text.lower():
                speech("\tŞükürler içinde ol.")
            elif "öptüm" in text.lower():
                speech("\tBende öptüm.")
            elif "kimsin" in text.lower():
                speech("\tBen İsrafil. Hasan'ın sanal sesli asistanıyım.")
            elif "ne yapıyorsun" in text.lower():
                speech("\tEmrindeyim, sen ne yapıyorsun?")
            elif "hangi gündeyiz" in text.lower():
                toDay = time.strftime("%A")
                toDay.capitalize()
                if toDay == "Monday":
                    toDay = "\tPazartesi"
                elif toDay == "Tuesday":
                    toDay = "\tSalı"
                elif toDay == "Wednesday":
                    toDay = "\tÇarşamba"
                elif toDay == "Thursday":
                    toDay = "\tPerşembe"
                elif toDay == "Friday":
                    toDay = "\tCuma"
                elif toDay == "Saturday":
                    toDay = "\tCumartesi"
                elif toDay == "Sunday":
                    toDay = "\tPazar"
                speech(toDay)
            elif "saat kaç" in text.lower():
                speech(datetime.now().strftime("%H:%M"))
            elif "uykuya geç" in text.lower() or "uyku modu" in text.lower() or "uyku moduna geç" in text.lower() \
                    or "uyu" in text.lower():
                speech("\tKaç saniyelik?")
                sec = float(get_audio())
                speech(f"\tTamam, {sec} saniyelik uyku moduna geçiyorum.")
                sleep = time.sleep(sec)
                speech("\tUyku modu bitti.")
            elif "not tut" in text.lower() or "esra yaz" in text.lower() or "not al" in text.lower():
                speech("Dosyanın ismi ne olsun?")
                txtFile = get_audio() + ".txt"
                speech("Yazıyorum...")
                texT = get_audio()
                filE = open(txtFile, "w", encoding='utf-8')
                filE.writelines(texT)
                filE.close()
            elif "sağol" in text.lower() or "sağolun" in text.lower() or "teşekkür" in text.lower() or "teşekkürler" in text.lower():
                speech("\tÖnemli değil.")
            elif "programı kapat" in text.lower():
                exit()
            else:
                speech("Öyle bir soruya henüz cevabım yok.")
                continue
    else:
        speech("Önce Esra'yı çağır.")

    # question = speech("Devam etmek istiyor musunuz?\n")
    # answer = get_audio()
    # if answer == "evet" or "tabii":
    #     continue
    # else:
    #     exit()