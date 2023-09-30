# api https://api.kanye.rest
import requests

url = "https://api.kanye.rest"

response = requests.get(url)
response.raise_for_status()

data = response.json()
quote = data['quote']
print(quote)