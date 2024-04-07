from PIL import Image
import requests
import os
from Body.Speak import speak
from time import sleep

Api_key = "3iX7wpWihuZSNcUxKnCWI7lUP2XyGm7ZDuL7fFWG"

def NasaNews(Date):
    speak("Extracting Space News.")
    Url = "https://api.nasa.gov/planetary/apod?api_key=" +str(Api_key)
    Params = {'date':str(Date)}
    r = requests.get(Url, params=Params)
    
    Data = r.json()
    Info = Data['explanation']
    Title = Data['title']
    Image_Url = Data['url']

    Explanation = str(Info.split('.')[:2])

    Image_r = requests.get(Image_Url)
    FileName = str(Date) + '.jpg'

    with open(FileName, 'wb') as f:
        f.write(Image_r.content)

    Path_1 = "E:\\Python\\AI JARVIS USING PYTHON\\" + str(FileName)
    Path_2 = "DataBase\\NasaDatabase\\" + str(FileName)

    img = Image.open(Path_1)
    img.show()
    img.close()  # Close the image after displaying it

    os.rename(Path_1, Path_2)

    speak(f"Title: {Title}")
    sleep(0.5)
    speak("Sir Check This.")
    # print(f"According to Nasa : {Info}")
    speak(f"According to Nasa : {Explanation}")

def DateConverter():

    from datetime import date

    # Get today's date
    today = date.today()

    # Extract year, month, and day components
    year = today.year
    month = today.month
    day = today.day

    # Convert to the desired format
    formatted_date = f"{year:04d}-{month:02d}-{day:02d}"

    return formatted_date

def Nasa():
    date = DateConverter()
    NasaNews(date)