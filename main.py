import requests
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import matplotlib.dates as mdates

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

response = requests.get(f"https://www.bom.gov.au/fwo/IDV60801/IDV60801.94857.json", headers=headers)

if response.status_code == 200:
    data = response.json()

def getTemp():
    x = []
    y = []

    observations = data["observations"]["data"]

    latest = datetime.strptime(observations[0]["local_date_time_full"], "%Y%m%d%H%M%S")

    last_time = latest - timedelta(hours=12)

    for observation in observations:
        observation_time = datetime.strptime(observation["local_date_time_full"], "%Y%m%d%H%M%S")

        if observation_time >= last_time:
            x.append(observation_time)
            y.append(observation["air_temp"])

    x.reverse()
    y.reverse()

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(x, y, marker='o', linewidth=2)

    ax.xaxis.set_major_formatter(mdates.DateFormatter('%I:%M %p'))
    ax.xaxis.set_major_locator(mdates.HourLocator(interval=2))

    ax.set_title("Temperature - Last 12 Hours")
    ax.set_xlabel("Time")
    ax.set_ylabel("Temp (Celcius")

    plt.xticks(rotation=45)
    plt.grid(True)
    plt.tight_layout()

    plt.savefig("static/temp_graph.png")
    plt.close()

def getWind():
    x = []
    y = []

    observations = data["observations"]["data"]

    latest = datetime.strptime(observations[0]["local_date_time_full"], "%Y%m%d%H%M%S")

    last_time = latest - timedelta(hours=12)

    for observation in observations:
        observation_time = datetime.strptime(observation["local_date_time_full"], "%Y%m%d%H%M%S")

        wind_speed = observation.get("wind_spd_kmh")

        if observation_time >= last_time and wind_speed is not None:
            x.append(observation_time)
            y.append(wind_speed)

    x.reverse()
    y.reverse()

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(x, y, marker='o', linewidth=2)

    ax.xaxis.set_major_formatter(mdates.DateFormatter('%I:%M %p'))
    ax.xaxis.set_major_locator(mdates.HourLocator(interval=2))

    ax.set_ylim(bottom=0)
    ax.set_title("Wind Speed - Last 12 Hours")
    ax.set_xlabel("Time")
    ax.set_ylabel("Wind (km/h)")

    plt.xticks(rotation=45)
    plt.grid(True)
    plt.tight_layout()

    plt.savefig("static/wind_graph.png")
    plt.close()

def getHum():
    x = []
    y = []

    observations = data["observations"]["data"]

    latest = datetime.strptime(observations[0]["local_date_time_full"], "%Y%m%d%H%M%S")

    last_time = latest - timedelta(hours=12)

    for observation in observations:
        observation_time = datetime.strptime(observation["local_date_time_full"], "%Y%m%d%H%M%S")

        humidity = observation.get("rel_hum")

        if observation_time >= last_time and humidity is not None:
            x.append(observation_time)
            y.append(humidity)

    x.reverse()
    y.reverse()

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(x, y, marker='o', linewidth=2)

    ax.xaxis.set_major_formatter(mdates.DateFormatter('%I:%M %p'))
    ax.xaxis.set_major_locator(mdates.HourLocator(interval=2))

    ax.set_ylim(0, 100)
    ax.set_title("Relative Humidity - Last 12 Hours")
    ax.set_xlabel("Time")
    ax.set_ylabel("Humidity (%)")

    plt.xticks(rotation=45)
    plt.grid(True)
    plt.tight_layout()

    plt.savefig("static/humidity_graph.png")
    plt.close()