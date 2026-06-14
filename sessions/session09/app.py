import requests
from flask import Flask, render_template, request

from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()
API_KEY = os.getenv("API_KEY")
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

app = Flask(__name__)

# data = response.json()  # JSON → Python dict

@app.route("/", methods=["GET", "POST"])
def home():
    weather = None
    if request.method == "POST":
        city = request.form["city"]
        response = requests.get(BASE_URL, params={
            "q": city,
            "appid": API_KEY,
            "units": "imperial"
        })
        data = response.json()
        if data.get("cod") == 200:  # Check for valid response
            weather = {
                "city": data["name"],
                "temp": data["main"]["temp"],
                "description": data["weather"][0]["description"]
            }
    return render_template("index.html", weather=weather)

@app.route("/tail", methods=["GET", "POST"])
def tail():
    weather = None
    if request.method == "POST":
        city = request.form["city"]
        response = requests.get(BASE_URL, params={
            "q": city,
            "appid": API_KEY,
            "units": "imperial"
        })
        data = response.json()
        if data.get("cod") == 200:  # Check for valid response
            weather = {
                "city": data["name"],
                "temp": data["main"]["temp"],
                "description": data["weather"][0]["description"]
            }
    return render_template("tailwind.html", weather=weather)

if __name__ == "__main__":
    app.run(debug=True)
