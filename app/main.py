import os

import requests
from fastapi import FastAPI

app = FastAPI()

URL = "http://api.weatherapi.com/v1/current.json?"
API_KEY = os.environ.get("API_KEY")
CITY = "Paris"


@app.get("/weather")
def get_weather() -> any:
    response = requests.get(URL + f"key={API_KEY}&q={CITY}")

#   if api_key is invalid
    if response.status_code != 200:
        return {"error": f"Failed to fetch weather data: {response.text}"}
    data = response.json()
    if "location" in data and "name" in data["location"]:
        location_name = data["location"]["name"]
    else:
        return {"error": "Invalid response structure", "raw_data": data}
    temperature = data["current"]["temp_c"]
    condition = data["current"]["condition"]["text"]

    return {
        "city": location_name,
        "temperature": temperature,
        "condition": condition
    }
