from flask import Flask, render_template
from main import getTemp, getWind, getHum, getRain, data
from datetime import datetime

#Create Flask application instance
app = Flask(__name__)


#Define the route for the home page
#When a user visits "/", Flask render the webpage.html template
@app.route("/")
def index():
    #Generate weather graphs when the application starts
    getTemp()
    getWind()
    getHum()
    getRain()

    #Get last update date and time
    last_updated = data["observations"]["data"][0]["local_date_time"]

    # Extract current conditions for the webpage boxes
    current_temp = data["observations"]["data"][0]["air_temp"]
    current_humidity = data["observations"]["data"][0]["rel_hum"]
    current_wind_spd = data["observations"]["data"][0]["wind_spd_kmh"]
    current_rain = data["observations"]["data"][0]["rain_trace"]

    # Pass all variables to fill the HTML
    return render_template(
        "webpage.html", 
        last_updated=last_updated,
        current_temp=current_temp,
        current_humidity=current_humidity,
        current_wind_spd=current_wind_spd,
        current_rain=current_rain,
    )

#Start the Flask developmenmt server
if __name__ == "__main__":
    app.run(debug=True)