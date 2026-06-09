import requests 

API_KEY = "b589bf07fdcccfb9d127da7fdb95de49" 
city = input("Enter a city name: ") 
response = requests.get(f"https://api.openweathermap.org/data/2.5/weather",
  params={ 
     "q": city, 
     "appid": API_KEY, 
     "units": "metric" } ) 
if response.status_code == 200: 
    weather_data = response.json() 
    print(f"Temperature in {city}: {weather_data['main']['temp']}°C") 
else: 
    print("Error fetching weather data.")