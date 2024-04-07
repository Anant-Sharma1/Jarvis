import os
from playsound import playsound
import requests
from bs4 import BeautifulSoup

def TTS(query):

    url = "https://readloud.net/english/british/1-male-voice-brian.html"

    headers = {
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"

    }

    payload= {
        "but1":query,
        "but5":"0",
        "butP":"0",
        "butPauses":"0",
        'butt0':"submit"
    }

    response = requests.post(url,headers=headers,data=payload)

    if response.status_code==200:
        return response.text
    else:
        print("Failed to retrive data Statur code : ", response.status_code)

def url_extracter(text):

    soup = BeautifulSoup(text,'html.parser')

    audio_element = soup.find('audio')

    if audio_element:
        source_url = audio_element.find('source')['src']
        return source_url
    else:
        print("No audio element found")

def audio_downloader(source_url):

    headers = {
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"

    }

    response = requests.get(f"https://readloud.net{source_url}",headers=headers)

    if response.status_code==200:
        file_name = 'audio.mp3'
        with open(file_name,"wb") as f:
            f.write(response.content)

    else:
        print("failed to retrive MP3 file Status code: ", response.status_code)

    playsound(file_name)
    os.remove(file_name)


def speak(text):
    textual_response = TTS(text)
    source_url = url_extracter(textual_response)
    print()
    print(f"AI : {text}")
    print()
    audio_downloader(source_url=source_url)

if __name__ == "__main__":
    while 1:
        text = input(">>>  ")
        speak(text)