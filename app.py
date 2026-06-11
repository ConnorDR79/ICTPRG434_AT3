from flask import Flask, render_template
from main import getTemp, getWind, getHum

app = Flask(__name__)

getTemp()
getWind()
getHum()

@app.route("/")
def index():
    return render_template("base.html")

if __name__ == "__main__":
    app.run()