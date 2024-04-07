from Functions.Tools.ImgGen import Generate_Images
from Body.Speak import speak
import requests, json

# Your API key and city ID
api_key = "YOUR_API_KEY"
city_id = "YOUR_CITY_ID"

# URL for the weather API
url = f"https://api.openweathermap.org/data/2.5/weather?id={city_id}&appid={api_key}"

# Get the weather data
response = requests.get(url)
if response.status_code == 200:
    data = json.loads(response.text)
    current_temp = data["main"]["temp"] - 273.15
    speak(f"The current temperature in {data['name']} is {current_temp:.2f} degrees Celsius.")
else:
    speak("Error: Invalid API key or city ID.")