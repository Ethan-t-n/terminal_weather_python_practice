import requests
import config

def get_weather(city, api_key):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    response = requests.get(url)
    data = response.json()
    print(data)  

    if "cod" in data and data["cod"] == "404":
        return "City not found."
    elif "weather" in data and isinstance(data["weather"], list) and len(data["weather"]) > 0:
        weather = data["weather"][0]["description"]
        temperature = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        return f"Weather: {weather}, Temperature: {temperature} K, Humidity: {humidity}%"
    else:
        return "Unable to fetch weather data."

api_key = config.weather_key
city = input("Enter a city name: ")
print(get_weather(city, api_key))

