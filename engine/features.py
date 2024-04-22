from engine.config import Assistant_Name
from playsound import playsound
import eel
import os
import pywhatkit as kit
import re
import sqlite3
import pyttsx3
import webbrowser
import pvporcupine
import pyaudio
import struct
import time
import pyautogui as autogui
import json
import pyodbc
from newsapi import NewsApiClient
from datetime import datetime, timedelta



conn=sqlite3.connect("jarvis.db")
cursor=conn.cursor()


@eel.expose()
def playAssistantSound():
    opening_sound="www\\assets\\audio\\siri_start.MP3"
    playsound(opening_sound)

def print(text):
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
    
def hotword():
    """
    Listens for specific hotwords ("jarvis" and "alexa") and performs an action
    when one of them is detected (e.g., pressing Windows key + J).
    """
    porcupine = None
    paud = None
    audio_stream = None

    try:
        # Pretrained keywords
        porcupine = pvporcupine.create(keywords=["jarvis", "alexa"])
        paud = pyaudio.PyAudio()
        audio_stream = paud.open(rate=porcupine.sample_rate,
                                 channels=1,
                                 format=pyaudio.paInt16,
                                 input=True,
                                 frames_per_buffer=porcupine.frame_length)

        while True:
            keyword = audio_stream.read(porcupine.frame_length)
            keyword = struct.unpack_from("h" * porcupine.frame_length, keyword)

            keyword_index = porcupine.process(keyword)

            if keyword_index >= 0:
                # print("Hotword detected")
                autogui.keyDown("win")
                autogui.press("j")
                time.sleep(2)
                autogui.keyUp("win")

    except KeyboardInterrupt:
        # Handle Ctrl+C
        print("Interrupted by user")

    except Exception as e:
        # Handle specific exception during PyAudio operation
        print("Error:", e)

    finally:
        # Clean up resources
        if porcupine is not None:
            porcupine.delete()
        if audio_stream is not None:
            audio_stream.close()
        if paud is not None:
            paud.terminate()

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
                print("opening " + query)
                os.startfile(results[0][0])
            elif len(results) == 0:
                cursor.execute(
                'select url from web_command where name in (?)',(app_name,)
                )
                results=cursor.fetchall()
                
                if len(results) != 0:
                     print("opening " + query)
                     webbrowser.open(results[0][0])
                else:
                    print("opening " + query)
                    try:
                        os.system("start " + query)
                    except:
                        print("Not Found !!!")
        except:
            print("Something went wrong !!!")                
                

        
def PlayYoutube(search_term): 
    print("Playing "+ search_term + " on youtube.")   
    kit.playonyt(search_term)
    
    
# Import necessary libraries
from newsapi import NewsApiClient
from datetime import datetime, timedelta
import json
import pyodbc

def NewsAutomation():
    newsapi = NewsApiClient(api_key="43cd03efd7434c8faddab5e95dbb60d")
    categories = ["bollywood", "sports", "science"]
    # Calculate yesterday's date
    yesterday_date = datetime.now() - timedelta(days=1)
    yesterday_str = yesterday_date.strftime('%Y-%m-%d')

    for category in categories:
        print("Now fetching " + category + " news.")
        # Fetch articles from News API
        try:
            articles_response = newsapi.get_everything(q=category,
                                                       from_param=yesterday_str,
                                                       to=yesterday_str,
                                                       language='en',
                                                       sort_by='relevancy',
                                                       )
        except Exception as e:
            print(f"Failed to fetch articles: {str(e)}")
            continue  # Use continue instead of exit to try next category

        # Convert response to JSON string
        json_string = json.dumps(articles_response)

        # Parse JSON string
        data = json.loads(json_string)

        # Establish connection to SQL Server
        try:
            conn = pyodbc.connect('DRIVER={SQL Server};SERVER=TOSHWORKSTATION\SQLEXPRESS;DATABASE=ToshAI;Trusted_Connection=yes;')
            cursor = conn.cursor()
        except Exception as e:
            print(f"Failed to connect to the database: {str(e)}")
            continue  # Use continue to attempt the next category

        # Iterate through articles and insert into database
        for article in data['articles']:
            source_name = article['source']['name']
            author = article['author']
            title = article['title']
            description = article.get('description', None)
            url = article['url']
            url_to_image = article.get('urlToImage', None)
            published_at = article['publishedAt']
            content = article.get('content', None)
            
            try:
                # Execute stored procedure or SQL insert statement
                cursor.execute("EXEC USP_NewsArticle ?,?,?,?,?,?,?,?,?", 
                               (source_name, author, title, description, url, url_to_image, published_at, content, category))
            except Exception as e:
                print(f"Failed to insert article into database: {str(e)}")
                # Consider adding a rollback or other error handling here

        # Commit the transaction and close the cursor after all inserts
        conn.commit()
        cursor.close()
        print(f"Success! News fetched and inserted into the database for {category}")


    
  