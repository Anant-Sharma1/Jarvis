from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from os import getcwd

Link = fr"{getcwd()}\Body\voice.html"
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--use-fake-ui-for-media-stream")
chrome_options.add_argument("--use-fake-device-for-media-stream")
chrome_options.add_argument("--headless=new")
chrome_driver_path = 'DataBase\\chromedriver.exe'
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service, options=chrome_options)

def SpeechRecognitionModel():
    driver.get(url=Link)
    driver.find_element(by=By.ID, value='start').click()
    print("Listening...")
    while True:
        try:
            Text=driver.find_element(by=By.ID, value='output').text
            if Text != "":
                print("You : " + Text)
                driver.find_element(by=By.ID, value='end').click()
                return Text
        except Exception as e:
            print(e)

if __name__=="__main__":
    while True:
        SpeechRecognitionModel()