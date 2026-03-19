# Day 3: Weather CLI
# Get weather data for any city using the OpenWeather API.

import os

# TODO: pip install requests python-dotenv
# Then uncomment these:
# import requests
# from dotenv import load_dotenv

# Load environment variables from .env file
# load_dotenv()


def get_api_key():
    """Get the API key from environment variables."""
    # TODO: Load from .env
    # TODO: Raise error if not found
    pass


def fetch_weather(city, api_key):
    """Fetch weather data for a city from OpenWeather API."""
    # API endpoint
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=imperial"

    # TODO: Make the request with requests.get()
    # TODO: Check response status code
    # TODO: Parse the JSON response
    # TODO: Handle network errors
    pass


def display_weather(data):
    """Display weather data in a nice format."""
    # TODO: Extract city name, country, temp, description, humidity from data
    # TODO: Print formatted output
    # The JSON response looks like:
    # {
    #   "name": "London",
    #   "sys": {"country": "GB"},
    #   "main": {"temp": 55.4, "humidity": 72},
    #   "weather": [{"description": "scattered clouds"}]
    # }
    pass


def main():
    """Main program."""
    # TODO: Get API key
    # TODO: Ask user for city (or use sys.argv)
    # TODO: Fetch and display weather
    # TODO: Handle all errors gracefully
    pass


if __name__ == "__main__":
    main()
