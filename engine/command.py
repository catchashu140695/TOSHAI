import json
import os
import pyttsx3  #text-to-speech
import speech_recognition as sr #speech recognition audio to text
import eel
from engine.features import *
from engine.config import Assistant_Name
import time
from engine.web_automations import web_automations



@eel.expose()
def speak(text):
    engine = pyttsx3.init("sapi5")
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
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
        print("After hearing : " + query)     
        eel.DisplayMessage(query)        
    except Exception as e:
        return ""  
    
    return query.lower()

@eel.expose
def allCommand():
    try:
        #query=takecommand();
        query="upload shots"
        eel.DisplayMessage(query)
        if "open" in query: 
            command=query.replace(Assistant_Name,"")
            command=query.replace("open","")        
            openCommand(command)
        elif "on youtube" in query:
            search_term=extract_yt_term(query)        
            PlayYoutube(search_term)
        elif "write" in query:
            command=query.replace(Assistant_Name,"")
            command=query.replace("using openai","")     
            res=web_automations.chatgpt3(command)
            eel.DisplayMessage(res)
            speak(res)
        elif "upload news" in query:  
            speak("Sir, News will be uploaded to your youtube channel. I will notify you with status for this process.")                     
            NewsAutomation()
        elif "update shots table" in query:
            while True:
                speak("shorts upload sequence initiated.")
                prompt="give 5  youtube title,description and tags for generic funny youtube shorts (not specific topic) in json format that you have never created before where the keys will be title,description and tags. give the tags '#' initiated and space separated. Also add #shorts #youtube #youtubeshorts to every"
                res=web_automations.chatgpt3(prompt)       
                res1=push_shorts_title_desc_tags(res)
                if res1=="1":
                    speak("successfully inserted to database")
                else:
                    speak("Failure inserrting to database.")                
            
        else:
            eel.DisplayMessage("I'm sorry, I didn't understand your message.")
            speak("I'm sorry, I didn't understand your message.")
        time.sleep(2)
        eel.DisplayMessage('')
        eel.showhood()
    except Exception as e:
        print("Error Messsage" + e)
    
def extract_yt_term(command):
    pattern=r'play\s+(.*?)\s+on\s+youtube'
    match=re.search(pattern,command,re.IGNORECASE)
    return match.group(1) if match else None


    
    
    
        







