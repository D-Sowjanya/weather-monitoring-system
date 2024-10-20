from apscheduler.schedulers.blocking import BlockingScheduler
from weather_fetcher import fetch_weather
from database import insert_weather_data
from datetime import datetime

scheduler = BlockingScheduler()


# Fetch and store weather data for all cities every 5 minutes
def job():
    CITIES = ['Delhi', 'Mumbai', 'Chennai', 'Bangalore', 'Kolkata', 'Hyderabad']
    for city in CITIES:
        weather_data = fetch_weather(city)
        if weather_data:
            temp = weather_data['main']['temp']
            feels_like = weather_data['main']['feels_like']
            main = weather_data['weather'][0]['main']
            timestamp = int(datetime.now().timestamp())

            insert_weather_data(city, temp, feels_like, main, timestamp)
            print(f"Stored data for {city}: {temp}°C at {datetime.now()}")


# Schedule the job every 5 minutes
scheduler.add_job(job, 'interval', minutes=5)

# Start the scheduler
scheduler.start()
