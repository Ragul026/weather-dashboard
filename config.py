"""
   Configuration file for Weather Dashboard.
   """

   import os

   try:
       import streamlit as st
       API_KEY = st.secrets["API_KEY"]
   except Exception:
       API_KEY = os.environ.get("API_KEY", "YOUR_API_KEY_HERE")

   BASE_URL = "https://api.openweathermap.org/data/2.5/weather"
   FORECAST_URL = "https://api.openweathermap.org/data/2.5/forecast"

   UNITS = "metric"