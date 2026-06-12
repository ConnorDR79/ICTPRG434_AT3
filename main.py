import requests
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import matplotlib.dates as mdates

#HTTP header that identifies the application when requesting data from BOM API
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

#Request the latest weather observations from BOM
response = requests.get(f"https://www.bom.gov.au/fwo/IDV60801/IDV60801.94857.json", headers=headers)

#If above request succeeds, convert JSON response into python dictionary
#Added error handling
data = {}   #Initialize default empty dictionary

if response.status_code == 200:
    data = response.json()
else:
    print("API Failed!")

#Function to generate Temperature Graph
def getTemp():
    #Initialise list variables to store x-axis (Time) and y-axis values (Temperature)
    x = []
    y = []

    #Retrieve weather observations from BOM
    observations = data["observations"]["data"]

    #Determine the timestamp of most recent observation
    latest = datetime.strptime(observations[0]["local_date_time_full"], "%Y%m%d%H%M%S")

    #Calculate timestamp from 12 hours ago
    last_time = latest - timedelta(hours=12)

    #Collect Temperature reading from the last 12 hours
    for observation in observations:
        observation_time = datetime.strptime(observation["local_date_time_full"], "%Y%m%d%H%M%S")

        if observation_time >= last_time:
            x.append(observation_time)
            y.append(observation["air_temp"])

    #Reverse list so that the graphs read in order, from oldest to newest
    x.reverse()
    y.reverse()

    #Create and format the graph itself
    #With smaller markers
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(x, y, color='#1f77b4', marker='.', markersize=6, linewidth=1.5)

    #Display time labels for every 2 hours to stop overlapping
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%I:%M %p'))
    ax.xaxis.set_major_locator(mdates.HourLocator(interval=2))

    #Clean borders (Removes the unnecessary top/right box outlines)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    #Label graph and it axes
    ax.set_title("Temperature - Last 12 Hours")
    ax.set_xlabel("Time")
    ax.set_ylabel("Temp (Celcius)")

    #Plot the graph and save the image to display
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("static/temp_graph.png")
    plt.close()

#Function to generate Wind Graph
def getWind():
    #Initialise list variables to store x-axis (Time) and y-axis values (Wind)
    x = []
    y = []

    #Retrieve weather observations from BOM
    observations = data["observations"]["data"]

    #Determine the timestamp of most recent observation
    latest = datetime.strptime(observations[0]["local_date_time_full"], "%Y%m%d%H%M%S")

    #Calculate timestamp from 12 hours ago
    last_time = latest - timedelta(hours=12)

    #Collect Wind reading from the last 12 hours
    for observation in observations:
        observation_time = datetime.strptime(observation["local_date_time_full"], "%Y%m%d%H%M%S")

        wind_speed = observation.get("wind_spd_kmh")

        if observation_time >= last_time and wind_speed is not None:
            x.append(observation_time)
            y.append(wind_speed)

    #Reverse list so that the graphs read in order, from oldest to newest
    x.reverse()
    y.reverse()

    #Create and format the graph itself
    #With smaller markers
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(x, y, color='#1f77b4', marker='.', markersize=6, linewidth=1.5)

    #Display time labels for every 2 hours to stop overlapping
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%I:%M %p'))
    ax.xaxis.set_major_locator(mdates.HourLocator(interval=2))

    #Clean borders (Removes the unnecessary top/right box outlines)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    #Label graph and it axes
    ax.set_ylim(bottom=0)
    ax.set_title("Wind Speed - Last 12 Hours")
    ax.set_xlabel("Time")
    ax.set_ylabel("Wind (km/h)")

    #Plot the graph and save the image to display
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("static/wind_graph.png")
    plt.close()

#Function to generate Humidity Graph
def getHum():
    #Initialise list variables to store x-axis (Time) and y-axis values (Humidity)
    x = []
    y = []

    #Retrieve weather observations from BOM
    observations = data["observations"]["data"]

    #Determine the timestamp of most recent observation
    latest = datetime.strptime(observations[0]["local_date_time_full"], "%Y%m%d%H%M%S")

    #Calculate timestamp from 12 hours ago
    last_time = latest - timedelta(hours=12)

    #Collect Humidity reading from the last 12 hours
    for observation in observations:
        observation_time = datetime.strptime(observation["local_date_time_full"], "%Y%m%d%H%M%S")

        humidity = observation.get("rel_hum")

        if observation_time >= last_time and humidity is not None:
            x.append(observation_time)
            y.append(humidity)

    #Reverse list so that the graphs read in order, from oldest to newest
    x.reverse()
    y.reverse()

    #Create and format the graph itself
    #With smaller markers
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(x, y, color='#1f77b4', marker='.', markersize=6, linewidth=1.5)

    #Display time labels for every 2 hours to stop overlapping
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%I:%M %p'))
    ax.xaxis.set_major_locator(mdates.HourLocator(interval=2))

    #Clean borders (Removes the unnecessary top/right box outlines)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    #Label graph and it axes
    ax.set_ylim(0, 100)
    ax.set_title("Relative Humidity - Last 12 Hours")
    ax.set_xlabel("Time")
    ax.set_ylabel("Humidity (%)")

    #Plot the graph and save the image to display
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("static/humidity_graph.png")
    plt.close()

#Function to generate Rainfall Graph
def getRain():
    #Initialise list variables to store x-axis (Time) and y-axis values (Rainfall)
    x = []
    y = []

    #Retrieve weather observations from BOM
    observations = data["observations"]["data"]

    #Determine the timestamp of most recent observation
    latest = datetime.strptime(observations[0]["local_date_time_full"], "%Y%m%d%H%M%S")

    #Calculate timestamp from 12 hours ago
    last_time = latest - timedelta(hours=12)

    #Collect Humidity reading from the last 12 hours
    for observation in observations:
        observation_time = datetime.strptime(observation["local_date_time_full"], "%Y%m%d%H%M%S")

        rain = float(observation.get("rain_trace", 0))

        if observation_time >= last_time:
            x.append(observation_time)
            y.append(rain)

    #Reverse list so that the graphs read in order, from oldest to newest
    x.reverse()
    y.reverse()

    #Create and format the graph itself with narrow bars
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.bar(x, y, width=timedelta(minutes=20), color='#1f77b4', edgecolor='black')

    #Display time labels for every hour of the last 12 hours
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%I:%M %p'))
    ax.xaxis.set_major_locator(mdates.HourLocator(interval=1))

    #Label graph and it axes
    ax.set_ylim(bottom=0)
    ax.set_title("Rainfall - Last 12 Hours")
    ax.set_xlabel("Time")
    ax.set_ylabel("Rain (mm)")

    #Plot the graph and save the image to display
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("static/rain_graph.png")
    plt.close()