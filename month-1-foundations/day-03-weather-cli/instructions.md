# Day 3: Weather CLI

## What You're Building
A command-line weather tool. Type a city name, get the current temperature and conditions. Uses a real API (OpenWeather) and a third-party Python package (`requests`).

## What You'll Learn
- `pip install` — installing packages
- `import` — using third-party libraries
- `requests` library — making HTTP requests
- API keys — what they are and how to use them
- `.env` files — keeping secrets out of your code
- JSON responses — parsing API data

## Setup
1. Get a free OpenWeather API key: https://openweathermap.org/api (sign up, go to API Keys)
2. Install packages: `pip install requests python-dotenv`
3. Create a `.env` file in this folder with: `OPENWEATHER_API_KEY=your_key_here`
4. Add `.env` to your `.gitignore` (NEVER commit API keys!)

## Requirements
Build `weather.py` that:

1. **Asks for a city name** (or accepts it as a command-line argument)
2. **Calls the OpenWeather API** using `requests.get()`
3. **Displays:**
   - City name and country
   - Temperature (in Fahrenheit and Celsius)
   - Weather description (sunny, cloudy, rainy, etc.)
   - Humidity percentage
4. **Handles errors:**
   - City not found (API returns 404)
   - No internet connection
   - Invalid/missing API key
   - Empty input

## API Endpoint
```
https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=imperial
```

## How to Work
- First, get `requests` working with a simple API call
- Then parse the JSON response
- Then add error handling
- Then add the .env file for the API key

## Stretch Goals
- Add a 5-day forecast option
- Support zip codes
- Cache results so the same city doesn't hit the API twice in a row
- Display with colored output using `rich`

## When You're Done
```
git add .
git commit -m "Day 3: Weather CLI with requests and API keys"
git push
```
