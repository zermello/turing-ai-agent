import requests

def get_weather(city):
    url = f"https://geocoding-api.open-meteo.com/v1/search?name={city}&count=10&language=en&format=json"

    response = requests.get(url)
    data = response.json()

    latitude = data["results"][0]["latitude"]
    longitude = data["results"][0]["longitude"]

    weather_url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m"
    response = requests.get(weather_url)
    data = response.json()
    weather = data["current"]["temperature_2m"]
    return f"Currently, it's {weather}C in {city}"

get_weather("india")