import matplotlib.pyplot as plt
from database import cursor
import datetime


# Function to plot temperature trends for a city
def plot_city_weather(city):
    cursor.execute('''SELECT timestamp, temp FROM weather WHERE city = ?''', (city,))
    data = cursor.fetchall()

    dates = [datetime.datetime.fromtimestamp(row[0]) for row in data]
    temps = [row[1] for row in data]

    plt.plot(dates, temps, label='Temperature (°C)')
    plt.title(f'Temperature Trend for {city}')
    plt.xlabel('Time')
    plt.ylabel('Temperature (°C)')
    plt.xticks(rotation=45)
    plt.legend()
    plt.show()


# Test plotting function
if __name__ == "__main__":
    plot_city_weather('Hyderabad')
