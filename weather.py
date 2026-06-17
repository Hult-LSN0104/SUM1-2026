from flask import Flask, render_template, request
import requests

app = Flask(__name__)


API_KEY = "38592b16570a05063a4fe96854a6cb8f"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"


@app.route("/", methods=["GET", "POST"])
def home():
    weather = None
    error = None

    # Print API Key to console
    print(f"Your API KEY is {API_KEY}")

    if request.method == "POST":
        city = request.form.get("city", "").strip()

        if not city:
            error = "Please enter a city name."
        else:
            params = {
                "q": city,
                "appid": API_KEY,
                "units": "metric",  # switch to "imperial" for Fahrenheit
            }
            try:
                response = requests.get(BASE_URL, params=params, timeout=5)
                data = response.json()

                if response.status_code == 200:
                    weather = {
                        "city": data["name"],
                        "country": data["sys"]["country"],
                        "temp": round(data["main"]["temp"]),
                        "feels_like": round(data["main"]["feels_like"]),
                        "humidity": data["main"]["humidity"],
                        "description": data["weather"][0]["description"].title(),
                        "icon": data["weather"][0]["icon"],
                        "wind": data["wind"]["speed"],
                    }
                else:
                    # OpenWeatherMap returns a helpful "message" field on errors
                    error = data.get("message", "City not found.").title()
            except requests.exceptions.RequestException:
                error = "Could not reach the weather service. Please try again."

    return render_template("weather.html", weather=weather, error=error)


if __name__ == "__main__":
    app.run(debug=True)