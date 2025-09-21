import os
from dotenv import load_dotenv
import requests

load_dotenv()

api_key = os.getenv("API_KEY")



def get_weather(city):
    base_url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    responce = requests.get(base_url)
    
    return responce.json()

city = "Tashkent"
info = get_weather(city)

print(f"City: {info['name']}")
print(f"Weather: {info['weather'][0]['main']}")
print(f"Description: {info['weather'][0]['description']}")
print(f"Temperature: {info['main']['temp']}°C")
print(f"Humidity: {info['main']['humidity']}%")