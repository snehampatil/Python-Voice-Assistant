import speech_recognition as sr
import pyttsx3 as p
from web_auto import *
import win32api
from web_auto1 import *
from web_auto2 import *
from web_auto3 import *
import os


def doing():
    r = sr.Recognizer()
    r1 = sr.Recognizer()
    r2 = sr.Recognizer()
    r3 = sr.Recognizer()
    engine = p.init()
    engine.say("what do you want me to do?")
    engine.runAndWait()
    with sr.Microphone() as s:
        text = r.listen(s)

        try:
            recognized_text = r.recognize_google(text)
            print(recognized_text)

            if "information" in recognized_text:
                engine.say("information about what?")
                engine.runAndWait()
                with sr.Microphone() as source1:
                    audio1 = r1.listen(source1)
                    try:
                        information = r1.recognize_google(audio1)
                        bot = info()
                        bot.get_info(information)
                    except sr.UnknownValueError:
                        print("")
                    except sr.RequestError as e:
                        print("")
            elif "review" in recognized_text:
                engine.say("Which movie?")
                engine.runAndWait()
                with sr.Microphone() as source1:
                    audio1 = r1.listen(source1)
                    try:
                        information = r1.recognize_google(audio1)
                        bot = Movie()
                        bot.movie_review(information)
                    except sr.UnknownValueError:
                        print("")
                    except sr.RequestError as e:
                        print("")
            elif "song" in recognized_text:
                engine.say("Which artist?")
                engine.runAndWait()
                with sr.Microphone() as source1:
                    audio1 = r1.listen(source1)
                    try:
                        information = r1.recognize_google(audio1)
                        bot = Song()
                        bot.play(information)
                    except sr.UnknownValueError:
                        print("")
                    except sr.RequestError as e:
                        print("")
            elif "PowerPoint" in recognized_text:
                engine.say("opening Microsoft Powerpoint")
                engine.runAndWait()
                os.startfile("C:\Program Files\Microsoft Office\Office15\POWERPNT.EXE")

            elif "Notepad" in recognized_text:
                engine.say("opening Notepad")
                engine.runAndWait()
                os.startfile("C:\Windows\System32\notepad.exe")

            elif "text" in recognized_text:
                engine.say("What should be the name of the text file?")
                engine.runAndWait()
                with sr.Microphone() as source1:
                    audio1 = r1.listen(source1)
                    name = r.recognize_google(audio1)
                    print(name)
                    f = open(name, "w+")
                    engine.say("What should be written in the text file?")
                    engine.runAndWait()
                    with sr.Microphone() as source2:
                        audio2 = r1.listen(source2)
                        content = r.recognize_google(audio2)
                        print(content)
                        f.write(content)
                        f.close()

            elif "word" in recognized_text:
                engine.say("opening Microsoft word")
                engine.runAndWait()
                os.startfile("C:\Program Files\Microsoft Office\Office15\WINWORD.EXE")

            else:
                engine.say("Sorry i couldnt get you")
                engine.runAndWait()




        except sr.UnknownValueError:
            print("unknown")
        except sr.RequestError as e:
            print("error")
