#Importing all files
#/modules

from Body.Speak import speak
from Body.Listen import SpeechRecognitionModel
from Functions.XTRA.Wish import Greetings
from Brain.ExecCode import ExecCode

from Brain.Gemini import Gemini
from Brain.Filter import Filter

from Brain import KnowApps,GoodMsg,Inspections

import pygetwindow as gw
import keyboard
import random
import time
import pyperclip as pi

speak(Greetings())
del Greetings

def Execution():
    while 1:          
        Q=SpeechRecognitionModel()
        Q=Q.replace("Anand","Anant")
        QL=Q.lower()
        # LQ=len(Q.split(" "))
        # SQ=Q.split(" ")[0]
        # EQ=Q.split(" ")[-1]
        NQ=QL.removeprefix("jarvis")
        CURRENT_APP=""
        try:
            CURRENT_APP = gw.getActiveWindowTitle()
        except:
            CURRENT_APP = ""
        try:
            CURRENT_APP_NAME=CURRENT_APP.split(" - ")[-1]
        except:
            CURRENT_APP_NAME=""

        if NQ in ['optimize this code',"write code for this","optimise this code"]:
            keyboard.press_and_release("ctrl + c")
            time.sleep(1)
            clipboard_data = pi.paste()
            r=Gemini(f"{clipboard_data} **{NQ}**")
            r=Filter(r)
            print(r)
            if r==None:
                speak("I can't do that sir")
            else:
                pi.copy(r)
                keyboard.press_and_release("ctrl + v")
                speak(random.choice(GoodMsg))

        elif QL.find("read my selection")==0 or QL.find("read my selected text")==0:
            speak("sure sir reading our selected data")
            keyboard.press_and_release("ctrl + c")
            time.sleep(1)
            clipboard_data = pi.paste()
            speak(clipboard_data)

        elif "read data from my clipboard" in QL or "read my clipboard" in QL or "read clipboard" in QL or "copy data from my clipboard" in QL:
            query = QL.replace("read data from my clipboard","")
            query = query.replace("read my clipboard","")
            query = query.replace("read clipboard","")
            keyboard.press_and_release("ctrl + c")
            speak("ok just give me a second")
            jo = pi.paste()
            Gemini(jo)
            speak("data copied")

        elif CURRENT_APP_NAME in KnowApps:

            Func_=KnowApps[CURRENT_APP_NAME]
            Output = Func_(QL)
            if Output != False:
                keyboard.press_and_release(Output)
            else:
                response = Gemini(Q)
                code = Filter(response)
                if code!=None:
                    if "from Functions.Tools.ImgGen import Generate_Image" in code or "from Functions.Tools.Alarm import" in code or "from Functions.Osrc.Nasa_News import Nasa" in code:
                        exec(code)
                    elif "from Functions.Osrc.DataOnline import Online_Scraper" in code:
                        "from Body.Speak import speak\n"+code
                        code = code.replace("print", "speak")
                        exec(code)
                    else:
                        Done=ExecCode(code)
                        print(Done)
                        if Done:
                            pass
                        else:
                            for i in range(3):
                                with open(r"error.log", "r") as f:
                                    res = f.read()
                                    if res != "":
                                        code = Gemini(f"{res} /n" + "**fix this and write full code again. with different approach**")
                                        code = Filter(code)
                                        if code==None:
                                            break
                                        Done=ExecCode(code)
                                        if Done==True:
                                            speak(random.choice(GoodMsg))
                                            break
                                    else:
                                        break

                else:
                    if len(response) > 280:
                        speak(random.choice(Inspections))                    
                        print(response)
                    else:
                        speak(response)

        else:
            response = Gemini(Q)
            code = Filter(response)
            if code!=None:
                if "from Functions.Tools.ImgGen import Generate_Image" in code or "from Functions.Tools.Alarm import" in code or "from Functions.Osrc.Nasa_News import Nasa" in code:
                    exec(code)
                elif "from Functions.Osrc.DataOnline import Online_Scraper" in code or "from Functions.Osrc.DataOnline import Temperature" in code:
                    "from Body.Speak import speak\n"+code
                    code = code.replace("print", "speak")
                    exec(code)
                else:
                    Done=ExecCode(code)
                    print(Done)
                    if Done:
                        pass
                    else:
                        for i in range(3):
                            with open(r"error.log", "r") as f:
                                res = f.read()
                                if res != "":
                                    code = Gemini(f"{res} /n" + "**fix this and write full code again. with different approach**")
                                    code = Filter(code)
                                    if code==None:
                                        break
                                    Done=ExecCode(code)
                                    if Done==True:
                                        speak(random.choice(GoodMsg))
                                        break
                                else:
                                    break

            else:
                if len(response) > 280:
                    speak(random.choice(Inspections))                    
                    print(response)
                else:
                    speak(response)

Execution()
