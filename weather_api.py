"""
weather_api.py
--------------
Handles all communication with the OpenWeatherMap API.
Separated from main.py so the API logic is reusable and testable
(good practice to mention in interviews: "separation of concerns").
"""

import requests
from config import API_KEY, BASE_URL, FORECAST_URL, UNITS


class WeatherAPIError(Exception):
    """Custom exception for weather API related errors."""
    pass


def get_current_weather(city: str) -> dict:
    """
    Fetch current weather data for a given city.

    Args:
        city (str): Name of the city, e.g. "Chennai" or "London,UK"

    Returns:
        dict: Parsed and simplified weather data.

    Raises:
        WeatherAPIError: If the request fails or city is not found.
    """
    params = {
        "q": city,
        "appid": API_KEY,
        "units": UNITS
    }

    try:
        response = requests.get(BASE_URL, params=params, timeout=10)
    except requests.exceptions.ConnectionError:
        raise WeatherAPIError("No internet connection. Please check your network.")
    except requests.exceptions.Timeout:
        raise WeatherAPIError("Request timed out. Try again later.")
    except requests.exceptions.RequestException as e:
        raise WeatherAPIError(f"An unexpected error occurred: {e}")

    if response.status_code == 401:
        raise WeatherAPIError("Invalid API key. Check config.py.")
    elif response.status_code == 404:
        raise WeatherAPIError(f"City '{city}' not found. Check the spelling.")
    elif response.status_code != 200:
        raise WeatherAPIError(f"API error (status code {response.status_code}).")

    data = response.json()

    # Parse only the fields we care about — keeps calling code clean
    return {
        "city": data["name"],
        "country": data["sys"]["country"],
        "temperature": data["main"]["temp"],
        "feels_like": data["main"]["feels_like"],
        "temp_min": data["main"]["temp_min"],
        "temp_max": data["main"]["temp_max"],
        "humidity": data["main"]["humidity"],
        "pressure": data["main"]["pressure"],
        "description": data["weather"][0]["description"].title(),
        "icon": data["weather"][0]["icon"],
        "wind_speed": data["wind"]["speed"],
        "sunrise": data["sys"]["sunrise"],
        "sunset": data["sys"]["sunset"],
        "timezone": data["timezone"],
    }


def get_forecast(city: str) -> list:
    """
    Fetch a 5-day / 3-hour interval forecast for a given city,
    then reduce it to one entry per day (simplified forecast).

    Args:
        city (str): Name of the city.

    Returns:
        list[dict]: One summarized forecast entry per day.
    """
    params = {
        "q": city,
        "appid": API_KEY,
        "units": UNITS
    }

    try:
        response = requests.get(FORECAST_URL, params=params, timeout=10)
    except requests.exceptions.RequestException as e:
        raise WeatherAPIError(f"Could not fetch forecast: {e}")

    if response.status_code != 200:
        raise WeatherAPIError(f"API error (status code {response.status_code}).")

    data = response.json()
    daily_data = {}

    # The API returns data every 3 hours; we pick the midday (12:00) entry
    # for each date to represent that day's forecast.
    for entry in data["list"]:
        date, time = entry["dt_txt"].split(" ")
        if time == "12:00:00":
            daily_data[date] = {
                "date": date,
                "temp": entry["main"]["temp"],
                "description": entry["weather"][0]["description"].title(),
                "humidity": entry["main"]["humidity"],
            }

    return list(daily_data.values())
