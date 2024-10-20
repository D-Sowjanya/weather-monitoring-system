import sqlite3
from datetime import datetime

# Initialize a SQLite database to store weather data
conn = sqlite3.connect('weather_data.db')
cursor = conn.cursor()

# Create a table to store the weather data
cursor.execute('''CREATE TABLE IF NOT EXISTS weather (
                    city TEXT, 
                    temp REAL, 
                    feels_like REAL, 
                    main TEXT, 
                    timestamp INTEGER
                 )''')
conn.commit()


# Function to insert data into the database
def insert_weather_data(city, temp, feels_like, main, timestamp):
    cursor.execute('INSERT INTO weather (city, temp, feels_like, main, timestamp) VALUES (?, ?, ?, ?, ?)',
                   (city, temp, feels_like, main, timestamp))
    conn.commit()


# Function to calculate daily rollups (average, max, min temperature)
def daily_summary(city, date):
    start_timestamp = int(datetime.strptime(date, '%Y-%m-%d').timestamp())
    end_timestamp = start_timestamp + 86400  # 24 hours later

    cursor.execute('''SELECT AVG(temp), MAX(temp), MIN(temp), main 
                      FROM weather 
                      WHERE city = ? AND timestamp BETWEEN ? AND ?''',
                   (city, start_timestamp, end_timestamp))
    result = cursor.fetchone()

    if result:
        avg_temp, max_temp, min_temp, main_condition = result
        print(
            f"City: {city}, Date: {date}, Avg Temp: {avg_temp}°C, Max Temp: {max_temp}°C, Min Temp: {min_temp}°C, Main Condition: {main_condition}")
    else:
        print(f"No data available for {city} on {date}")


# Test data insertion and summary
if __name__ == "__main__":
    insert_weather_data('Hyderabad', 28.5, 30.0, 'Clear', int(datetime.now().timestamp()))
    daily_summary('Hyderabad', '2024-10-20')
