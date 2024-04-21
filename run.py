import multiprocessing

def start_jarvis():
    print("Jarvis started !!!")
    from main import start
    start()
    
def listen_hotword():
    print("Background listening is enabled. Wake me up by saying Jarvis")
    from engine.features import hotword
    hotword()

if __name__ == "__main__":
    p1 = multiprocessing.Process(target=start_jarvis)
    p2 = multiprocessing.Process(target=listen_hotword)
    p1.start()
    p2.start()
    p1.join()
    
    if p2.is_alive():
        p2.terminate()
        p2.join()
    
    print("Jarvis shut down")
