from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from time import sleep

Link = "https://readloud.net/english/british/1-male-voice-brian.html"
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3")
chrome_options.add_argument("--headless=new")
chrome_driver_path = 'DataBase\\chromedriver.exe'
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service, options=chrome_options)
driver.get(Link)

script = """function mediaElementIsPlaying(el) {
  return el && el.currentTime > 0 && !el.paused && !el.ended && el.readyState > 2;
}

// Check if any audio element is playing
const audioIsPlaying = !![...document.getElementsByTagName('audio')].find((el) => mediaElementIsPlaying(el));

// If either audio or video is playing, return true
return audioIsPlaying;"""

def speak(Text):
    try:
        textarea = driver.find_element(By.NAME, "but1")
        textarea.clear()
        textarea.send_keys(Text)

        submit = driver.find_element(By.NAME, "butt0")
        submit.click()

        while 1:
            playing = driver.execute_script(script)
            if not playing:
                break
            sleep(0.1)

    except Exception as e:
        print(e)
        print("Restarting website")
        driver.get(Link)
        speak(Text)



if __name__ == "__main__":
    while 1:
        text = input(">>>  ")
        speak(text)