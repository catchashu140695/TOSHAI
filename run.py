import multiprocessing
import multiprocessing.process

def start_jarvis():    
    from main import start
    start()
    
def listen_hotword():   
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
    

