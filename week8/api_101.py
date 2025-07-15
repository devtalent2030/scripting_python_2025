import requests

responce = requests.get("https://catfact.ninja/fact")
data = responce.json()

print(data["fact"])