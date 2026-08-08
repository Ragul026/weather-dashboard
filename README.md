# 🌦️ Weather Dashboard

A Python weather dashboard that fetches live weather data and 5-day forecasts
using the OpenWeatherMap API. Includes both a CLI version and an optional
Streamlit GUI.

## Features
- Current weather lookup by city name
- 5-day forecast (simplified to one reading per day)
- Local search history (saved to `search_history.json`)
- Robust error handling (invalid city, bad API key, no internet, timeout)
- Clean separation between API logic (`weather_api.py`) and UI logic (`main.py` / `streamlit_app.py`)

## Tech Stack
- Python 3
- `requests` — for HTTP calls to the OpenWeatherMap REST API
- `json` — for parsing API responses and storing local search history
- `streamlit` + `pandas` — optional GUI and data table/chart display

## Setup

1. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

2. **Get a free API key**
   - Sign up at https://openweathermap.org/api
   - Copy your API key from "My API Keys"
   - Paste it into `config.py`:
     ```python
     API_KEY = "your_key_here"
     ```
   - Note: new keys can take 10–15 minutes to activate.

3. **Run the CLI version**
   ```bash
   python main.py
   ```

4. **Run the GUI version (optional)**
   ```bash
   streamlit run streamlit_app.py
   ```

## Project Structure
```
weather_dashboard/
├── config.py           # API key & settings
├── weather_api.py       # All API calls + parsing + custom exceptions
├── main.py               # CLI application (menu-driven)
├── streamlit_app.py      # Optional GUI version
├── requirements.txt
└── README.md
```

## How It Works
1. User enters a city name.
2. `weather_api.py` builds a request to OpenWeatherMap's `/weather` or
   `/forecast` endpoint with the city and API key as query parameters.
3. The raw JSON response is parsed down to only the fields the app needs.
4. Errors (invalid city, bad key, network issues) are caught and raised as
   a custom `WeatherAPIError` so the calling code can display a clean message
   instead of crashing.
5. Each successful search is logged to `search_history.json` with a timestamp.

## Possible Extensions (good to mention in an interview as "future work")
- Cache responses (e.g. with `functools.lru_cache` or Redis) to reduce API calls
- Add unit tests with `pytest` + `unittest.mock` for the API layer
- Support multiple cities in one view (comparison dashboard)
- Add a database (SQLite) instead of JSON for search history
- Deploy the Streamlit app (Streamlit Community Cloud / Render) for a live demo link

## Interview Talking Points
- **Why `requests`?** Simple, widely-used HTTP library; handles query params,
  timeouts, and status codes cleanly.
- **Why a custom exception (`WeatherAPIError`)?** Keeps error handling
  consistent and lets the UI layer catch one exception type instead of
  guessing what could go wrong.
- **Why separate `weather_api.py` from `main.py`?** Separation of concerns —
  the API layer could be reused by a CLI, a GUI, or a Flask backend without
  changes.
- **How would you scale this?** Add caching, rate-limit handling, and swap
  JSON file storage for a real database.
