#pip install requests
#pip install bs4
import requests
from bs4 import BeautifulSoup
from Body.Speak import speak

classes=["zCubwf","hgKElc","LTKOO sY7ric","Z0LcW","gsrt vk_bk FzvWSb YwPhnf","pclqee","tw-Data-text tw-text-small tw-ta",
    "IZ6rdc","O5uR6d LTKOO","vlzY6d","webanswers-webanswers_table__webanswers-table",
    "dDoNo ikb4Bb gsrt","sXLaOe","LWkfKe","VQF4g","qv3Wpe","kno-rdesc"]

useragent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36'

#scrape data from google search results
def Online_Scraper(query,PRINT=True):
    query=query.replace(" + "," plus ")
    query=query.replace(" - "," minus ")   
    URL = "https://www.google.co.in/search?q=" + query
    headers = {'User-Agent': useragent}

    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')

    for i in classes:
        try:
            result=soup.find(class_=i).get_text()
            if PRINT:
                print(f"by class {i}")
            return result
        except Exception:
            pass
    return None

def Temperature():
    search = "temperature in kolkata"
    url = f"https://www.google.com/search?q={search}"
    r = requests.get(url)
    data = BeautifulSoup(r.text,"html.parser")
    temperature = data.find("div",class_="BNeawe").text
    speak(f"{search} is {temperature}")

if __name__=="__main__":
    Temperature()