import pyttsx3 as p
import requests
from api import*
engine = p.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', 130)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
def speak(text):
  engine.say(text)
  engine.runAndWait()



def get_weather(city_name):
    url = f"http://api.weatherapi.com/v1/current.json?key=6cab4af42db34f41b69162201232710&q={city_name}&aqi=yes"

    try:
        response = requests.get(url)
        data = response.json()

        if 'error' in data:
            speak(f"City '{city_name}' not found.")
        else:
            current = data['current']
            temperature = current['temp_c']
            pressure = current['pressure_mb']
            humidity = current['humidity']
            weather_description = current['condition']['text']

            speak(f"Temperature: {temperature}°C")
            speak(f"Pressure: {pressure} hPa")
            speak(f"Humidity: {humidity}%")
            speak(f"Description: {weather_description}")

    except requests.exceptions.RequestException as e:
        print("An error occurred:", e)
        speak("Sorry, I couldn't fetch the weather information at the moment.")

# Example usage:
# get_weather("London")  # Replace "London" with the desired city name



# Example usage:
# get_weather("London")  # Replace "London" with the desired city name
