import requests 

url = "https://api.chucknorris.io/jokes/random"

response = requests.get(url) 

joke = response.json() 

print(f"Here's a joke:\n{joke['value']}")