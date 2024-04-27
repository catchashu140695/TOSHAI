import os
import eel
from engine.features import *
from engine.command import *

def start():
    eel.init('www')    
    playAssistantSound()    
    os.system('start chrome.exe --app="http://localhost:8000/index.html"')
    eel.start('index.html', mode=None, host='localhost', block=True, size=(1920, 1080))
