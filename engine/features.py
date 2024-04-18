from playsound import playsound
import eel
from engine.config import Assistant_Name
import os
from engine.command import *

@eel.expose()
def playAssistantSound():
    opening_sound="www\\assets\\audio\\siri_start.MP3"
    playsound(opening_sound)

def openCommand(query):
    command=query.replace(Assistant_Name,"")
    command=query.replace("open","")

    if(query != ""):       
        speak("opening "+query) 
        os.system("start "+ command.lower())
    else:
        print("No App Found !!!")
    