import requests
import time

# Define your API key and the base URL for OpenWeatherMap API
API_KEY = 'your_api_key'
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'

# List of cities to monitor
CITIES = ['Delhi', 'Mumbai', 'Chennai', 'Bangalore', 'Kolkata', 'Hyderabad']

# Function to fetch weather data from the API
def fetch_weather(city):
    params = {
        'q': city,
        'appid': API_KEY,
        'units': 'metric'  # Temperature in Celsius
    }
    response = requests.get(BASE_URL, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error fetching data for {city}: {response.status_code}")
        return None

# Test the API call
if __name__ == "__main__":
    for city in CITIES:
        weather_data = fetch_weather(city)
        if weather_data:
            print(f"City: {city}, Temp: {weather_data['main']['temp']}°C")
        time.sleep(1)  # Avoid rapid API calls
