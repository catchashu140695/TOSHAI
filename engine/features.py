from playsound import playsound
import eel

@eel.expose()
def playAssistantSound():
    opening_sound="www\\assets\\audio\\siri_start.MP3"
    playsound(opening_sound)
    