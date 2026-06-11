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


    return render_template("webpage.html", last_updated=last_updated)

#Start the Flask developmenmt server
if __name__ == "__main__":
    app.run()