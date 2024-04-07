import sounddevice as sd
import numpy as np

threshold = 100
Clap = False

def detect_clap(indata,frames,time,status):
    global Clap
    volume_norm = np.linalg.norm(indata) * 10
    if volume_norm>threshold:
        print("Clapped!")
        Clap = True

def Listen_for_claps():
    with sd.InputStream(callback=detect_clap):
        return sd.sleep(1000)
    
def MainClapExe():
    print("Waiting for Clap To Run Jarvis")
    while True:
        Listen_for_claps()
        if Clap==True:
            break
        else:
            pass
        
MainClapExe()