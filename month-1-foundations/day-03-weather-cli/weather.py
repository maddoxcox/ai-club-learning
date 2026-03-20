# Day 3: Weather CLI
# Get weather data for any city using the OpenWeather API.

import os

import requests
from dotenv import load_dotenv



def get_api_key():
    load_dotenv()
    key = os.getenv("OPENWEATHER_API_KEY")
    if key is None:
        raise ValueError("API key not found. Check your .env file.")
    return key



def fetch_weather(city, key):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={key}&units=imperial"
    try:
        response = requests.get(url)
    except requests.exceptions.ConnectionError:
        print("No internet connection.")
        return None
    if response.status_code == 200:
        return response.json()
    elif response.status_code == 404:
        print(f"City '{city}' not found.")
        return None





def display_weather(data):
    city = data["name"]
    country = data["sys"]["country"]
    temp_f = data["main"]["temp"]
    temp_c = (temp_f - 32) * 5 / 9
    humidity = data["main"]["humidity"]
    description = data["weather"][0]["description"]

    print(f'{city}, {country}')
    print(f'{temp_f}°F / {temp_c:.1f}°C')
    print(f'{description}')
    print(f'Humidity: {humidity}%')


def main():
    key = get_api_key()
    city = input("Enter a city: ")
    if not city:
        print("Please enter a city name.")
        return
    data = fetch_weather(city, key)
    if data is None:
        return
    display_weather(data)


if __name__ == "__main__":
    main()
