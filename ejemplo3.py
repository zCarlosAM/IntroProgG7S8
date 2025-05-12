import pyttsx3
import win32com.client
import time

engine = pyttsx3.init()
engine.setProperty('rate', 150)
engine.setProperty('volume', 0.9)
engine.setProperty('language', 'es')

for i in range(5):
    j = 0
    while j < 5:
        text = f"i: {i}, j: {j}"
        speaker = win32com.client.Dispatch("SAPI.SpVoice")
        
        speaker.Speak(text)
        time.sleep(3)