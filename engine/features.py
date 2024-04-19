from engine.config import Assistant_Name
from playsound import playsound
import eel
import os
import pywhatkit as kit
import re
import sqlite3
import pyttsx3
import webbrowser


conn=sqlite3.connect("jarvis.db")
cursor=conn.cursor()


@eel.expose()
def playAssistantSound():
    opening_sound="www\\assets\\audio\\siri_start.MP3"
    playsound(opening_sound)

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

def openCommand(query):
    app_name=query.replace(Assistant_Name,"")
    app_name=query.replace("open","")
    app_name=query.lower().strip()    
    if app_name != "":
        try:
            cursor.execute(
                'select path from sys_command where name in (?)',(app_name,)
            )
            results=cursor.fetchall()            
            if(len(results)!=0):
                speak("opening " + query)
                os.startfile(results[0][0])
            elif len(results) == 0:
                cursor.execute(
                'select url from web_command where name in (?)',(app_name,)
                )
                results=cursor.fetchall()
                
                if len(results) != 0:
                     speak("opening " + query)
                     webbrowser.open(results[0][0])
                else:
                    speak("opening " + query)
                    try:
                        os.system("start " + query)
                    except:
                        speak("Not Found !!!")
        except:
            speak("Something went wrong !!!")                
                

        
def PlayYoutube(search_term): 
    speak("Playing "+ search_term + " on youtube.")   
    kit.playonyt(search_term)
    

    