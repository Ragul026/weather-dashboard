"""
main.py
-------
Command-line Weather Dashboard.

Features:
- Current weather for any city
- 5-day forecast
- Search history (saved locally to a JSON file)
- Clean error handling for bad input / network issues / invalid cities

Run: python main.py
"""

import json
import os
from datetime import datetime
from weather_api import get_current_weather, get_forecast, WeatherAPIError

HISTORY_FILE = "search_history.json"


def load_history() -> list:
    """Load past searches from a JSON file. Returns empty list if none exist."""
    if not os.path.exists(HISTORY_FILE):
        return []
    try:
        with open(HISTORY_FILE, "r") as f:
            return json.load(f)
    except (json.JSONDecodeError, FileNotFoundError):
        return []


def save_history(history: list) -> None:
    """Persist search history to a JSON file."""
    with open(HISTORY_FILE, "w") as f:
        json.dump(history, f, indent=2)


def add_to_history(city: str) -> None:
    """Add a searched city (with timestamp) to history, avoiding immediate duplicates."""
    history = load_history()
    entry = {
        "city": city,
        "searched_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    history.append(entry)
    # Keep only the last 10 searches
    history = history[-10:]
    save_history(history)


def display_current_weather(weather: dict) -> None:
    """Pretty-print current weather data to the console."""
    print("\n" + "=" * 40)
    print(f"  Weather in {weather['city']}, {weather['country']}")
    print("=" * 40)
    print(f"  Condition     : {weather['description']}")
    print(f"  Temperature   : {weather['temperature']}°C")
    print(f"  Feels Like    : {weather['feels_like']}°C")
    print(f"  Min / Max     : {weather['temp_min']}°C / {weather['temp_max']}°C")
    print(f"  Humidity      : {weather['humidity']}%")
    print(f"  Pressure      : {weather['pressure']} hPa")
    print(f"  Wind Speed    : {weather['wind_speed']} m/s")
    print("=" * 40 + "\n")


def display_forecast(forecast: list, city: str) -> None:
    """Pretty-print a multi-day forecast to the console."""
    print(f"\n5-Day Forecast for {city}")
    print("-" * 40)
    for day in forecast:
        print(f"  {day['date']}: {day['temp']}°C, {day['description']} "
              f"(Humidity: {day['humidity']}%)")
    print("-" * 40 + "\n")


def display_history() -> None:
    """Show the last few searched cities."""
    history = load_history()
    if not history:
        print("\nNo search history yet.\n")
        return
    print("\nRecent Searches")
    print("-" * 40)
    for entry in reversed(history):
        print(f"  {entry['city']}  —  {entry['searched_at']}")
    print("-" * 40 + "\n")


def main_menu() -> None:
    """Main interactive loop for the CLI dashboard."""
    print("\n🌦️   WEATHER DASHBOARD  🌦️")

    while True:
        print("\nWhat would you like to do?")
        print("  1. Get current weather")
        print("  2. Get 5-day forecast")
        print("  3. View search history")
        print("  4. Exit")

        choice = input("Enter choice (1-4): ").strip()

        if choice == "1":
            city = input("Enter city name: ").strip()
            if not city:
                print("City name cannot be empty.")
                continue
            try:
                weather = get_current_weather(city)
                display_current_weather(weather)
                add_to_history(weather["city"])
            except WeatherAPIError as e:
                print(f"\nError: {e}\n")

        elif choice == "2":
            city = input("Enter city name: ").strip()
            if not city:
                print("City name cannot be empty.")
                continue
            try:
                forecast = get_forecast(city)
                display_forecast(forecast, city)
                add_to_history(city)
            except WeatherAPIError as e:
                print(f"\nError: {e}\n")

        elif choice == "3":
            display_history()

        elif choice == "4":
            print("\nGoodbye!\n")
            break

        else:
            print("Invalid choice. Please enter 1-4.")


if __name__ == "__main__":
    main_menu()
