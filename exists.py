import requests

url = "https://icanhazdadjoke.com/search"
res = requests.get(url).status_code
print(f"HTTP status code is: {res}")
