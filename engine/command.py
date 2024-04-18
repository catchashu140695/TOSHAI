import os
import pyttsx3  #text-to-speech
import speech_recognition as sr #speech recognition audio to text
import eel
from engine.features import *
from engine.config import Assistant_Name
import time


@eel.expose()
def speak(text):
    engine = pyttsx3.init("sapi5")
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.setProperty('volume',1.0)
    engine.setProperty('rate', 174)
    """Saving Voice to a file"""
    # On linux make sure that 'espeak' and 'ffmpeg' are installed
    #engine.save_to_file('Hello World', 'test.mp3')
    
    engine.say(text)
    engine.runAndWait()
    
    
def takecommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        playAssistantSound()       
        eel.DisplayMessage('I am listening......')
        r.pause_threshold=1
        r.adjust_for_ambient_noise(source)
        audio=r.listen(source,10,6)
        
    try:       
        eel.DisplayMessage('recognizing....')
        query = r.recognize_google(audio,language="en-in")       
        eel.DisplayMessage(query)        
    except Exception as e:
        return ""  
    
    return query.lower()

@eel.expose
def allCommand():
    query=takecommand();
    eel.DisplayMessage(query)
    if "open" in query: 
        command=query.replace(Assistant_Name,"")
        command=query.replace("open","")  
        speak("opening "+command)     
        openCommand(query)        
    else:
        eel.DisplayMessage("I'm sorry, I didn't understand your message.")
        speak("I'm sorry, I didn't understand your message.")
    time.sleep(3)
    eel.DisplayMessage('')
    eel.showhood()
        







