import speech_recognition as sr
import pyttsx3 as p

from speech2 import *
from web_auto1 import *
from web_auto2 import *
from web_auto3 import *
import win32api

r = sr.Recognizer()
engine = p.init()
engine.say("hello, how are you doing?")
engine.runAndWait()

with sr.Microphone() as s:
    text = r.listen(s)
    try:
        recognized_text = r.recognize_google(text)
        print(recognized_text)
    except sr.UnknownValueError:
        print("unknown")
    except sr.RequestError as e:
        print("error")
doing()
