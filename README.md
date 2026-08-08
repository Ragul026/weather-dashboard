# 🌦️ Weather Dashboard

A Python-based weather dashboard that displays current weather information and a 5-day forecast for any city using the OpenWeatherMap API.

## 🚀 Features

* Search weather by city name
* Display current weather information
* Show a 5-day weather forecast
* Store recent search history
* Handle invalid city names and API errors
* CLI version for terminal usage
* Streamlit GUI for a simple web interface

## 🛠️ Technologies Used

* Python
* Requests
* JSON
* Streamlit
* Pandas
* OpenWeatherMap API

## 📂 Project Structure

```text
weather-dashboard/
│
├── main.py
├── weather_api.py
├── streamlit_app.py
├── config.example.py
├── requirements.txt
├── README.md
└── .gitignore
```

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/Ragul026/weather-dashboard.git
cd weather-dashboard
```

### 2. Install required packages

```bash
pip install -r requirements.txt
```

### 3. Configure the API key

Create a `config.py` file and add your OpenWeatherMap API key:

```python
API_KEY = "your_api_key_here"
```

Keep your API key private and do not upload `config.py` to GitHub.

## ▶️ Run the Project

### Command Line Version

```bash
python main.py
```

### Streamlit Version

```bash
streamlit run streamlit_app.py
```

## 🔄 How It Works

1. The user enters a city name.
2. The application sends a request to the OpenWeatherMap API.
3. The API returns weather information in JSON format.
4. Python processes the required weather data.
5. The application displays the current weather and forecast.
6. Successful searches are stored in the search history.

## 📸 Project Preview

*Add screenshots of the working application here.*

## 📌 Learning Outcomes

Through this project, I practiced:

* Working with REST APIs
* Sending HTTP requests using Python
* Processing JSON data
* Handling errors and exceptions
* Working with Python modules
* Building a simple Streamlit application
* Using Git and GitHub for project management

## 🔮 Future Improvements

* Add weather charts
* Compare weather between multiple cities
* Add a database for search history
* Deploy the application online
