import requests

url = "https://ipinfo.io/"
response = requests.get(url)
# print(response.text)  # Data looks like a json...

data = response.json()
print("City:", data["city"])
print("Region:", data["region"])
print("location:", data["loc"])

