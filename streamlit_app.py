"""
streamlit_app.py
-----------------
Optional GUI version of the Weather Dashboard using Streamlit.
Great for demoing live in an interview — looks polished with minimal effort.

Run: streamlit run streamlit_app.py
"""

import streamlit as st
import pandas as pd
from weather_api import get_current_weather, get_forecast, WeatherAPIError

st.set_page_config(page_title="Weather Dashboard", page_icon="🌦️", layout="centered")

st.title("🌦️ Weather Dashboard")
st.write("Get real-time weather and 5-day forecasts using the OpenWeatherMap API.")

city = st.text_input("Enter a city name", placeholder="e.g. Chennai, London, Tokyo")

col1, col2 = st.columns(2)
current_clicked = col1.button("Get Current Weather", use_container_width=True)
forecast_clicked = col2.button("Get 5-Day Forecast", use_container_width=True)

if current_clicked:
    if not city.strip():
        st.warning("Please enter a city name.")
    else:
        try:
            with st.spinner("Fetching weather..."):
                weather = get_current_weather(city)

            st.subheader(f"{weather['city']}, {weather['country']}")
            icon_url = f"https://openweathermap.org/img/wn/{weather['icon']}@2x.png"
            st.image(icon_url, width=80)
            st.write(f"**Condition:** {weather['description']}")

            m1, m2, m3 = st.columns(3)
            m1.metric("Temperature", f"{weather['temperature']}°C")
            m2.metric("Feels Like", f"{weather['feels_like']}°C")
            m3.metric("Humidity", f"{weather['humidity']}%")

            m4, m5, m6 = st.columns(3)
            m4.metric("Min Temp", f"{weather['temp_min']}°C")
            m5.metric("Max Temp", f"{weather['temp_max']}°C")
            m6.metric("Wind Speed", f"{weather['wind_speed']} m/s")

        except WeatherAPIError as e:
            st.error(str(e))

if forecast_clicked:
    if not city.strip():
        st.warning("Please enter a city name.")
    else:
        try:
            with st.spinner("Fetching forecast..."):
                forecast = get_forecast(city)

            if forecast:
                df = pd.DataFrame(forecast)
                st.subheader(f"5-Day Forecast for {city}")
                st.dataframe(df, use_container_width=True, hide_index=True)
                st.line_chart(df.set_index("date")["temp"])
            else:
                st.info("No forecast data available.")

        except WeatherAPIError as e:
            st.error(str(e))

st.markdown("---")
st.caption("Built with Python, Requests, and the OpenWeatherMap API.")
