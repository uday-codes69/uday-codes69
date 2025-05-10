import requests
import json
import os
city = input("Enter the name of city\n")

url = f"https://api.weatherapi.com/v1/current.json?key=cc2e38694b874b29ac595813251005&q={city}"

r = requests.get(url)
# print(r.text)

wdic = json.loads(r.text)
w = wdic["current"]["temp_c"]

os.system(f"say 'The current weather in {city} is {w} degrees'")

print(wdic["current"]["temp_c"])