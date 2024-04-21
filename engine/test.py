import pvporcupine
import pyaudio
import time
import struct
import pyautogui as autogui

porcupine = None
paud = None
audio_stream = None

try:
    # pretrained keywords
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
            print("Hotword detected")
            autogui.hotkey('win', 'j')
            time.sleep(2)

except KeyboardInterrupt:
    print("Exiting...")

finally:
    if porcupine is not None:
        porcupine.delete()
    if audio_stream is not None:
        audio_stream.close()
    if paud is not None:
        paud.terminate()
