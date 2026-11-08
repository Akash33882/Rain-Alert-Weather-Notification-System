from dotenv import load_dotenv
import os   
load_dotenv()

import requests

my_lat = 12.295810
my_lng = 76.639381
API_KEY = os.environ.get("API_KEY")

prmts = {
    "lat" : my_lat,
    "lon" : my_lng,
    "appid" : API_KEY,
    "cnt" : 4
}

responce = requests.get(url=f"https://api.openweathermap.org/data/2.5/forecast", params=prmts)
responce.raise_for_status()
whether_data = responce.json()

is_raining = False
for data in whether_data["list"]:
    whether_code = data["weather"][0]["id"] < 700
    if whether_code:
        is_raining = True

if is_raining:
    print("Carry the Umbrella.")
