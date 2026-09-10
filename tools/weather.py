import requests
import logging

def get_weather(city):
    try:
        url = f"https://geocoding-api.open-meteo.com/v1/search?name={city}&count=10&language=en&format=json"

        response = requests.get(url, timeout=5)
        data = response.json()

        if not data.get("results"):
         return f"I couldn't find the location '{city}'."

        latitude = data["results"][0]["latitude"]
        longitude = data["results"][0]["longitude"]

        weather_url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m"
        response = requests.get(weather_url, timeout=10)
        data = response.json()
        weather = data["current"]["temperature_2m"]
        return f"Currently, it's {weather}C in {city}"
    except requests.exceptions.RequestException as err:
       logging.error("fERROR: {err}")
       return "The API/internet could not be reached"
    except Exception as err:
        logging.error(f"ERROR: {err}")
        return f"The give city is spelled wrong or not found"

