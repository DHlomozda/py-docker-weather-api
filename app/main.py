import os

import requests
from dotenv import load_dotenv
from fastapi import FastAPI
app = FastAPI()
load_dotenv()

URL = "http://api.weatherapi.com/v1/current.json?"
API_KEY = os.getenv("API_KEY")
CITY = "Paris"


@app.get("/weather")
def get_weather() -> any:
    response = requests.get(URL + f"key={API_KEY}&q={CITY}")
    data = response.json()
    location_name = data["location"]["name"]
    temperature = data["current"]["temp_c"]
    condition = data["current"]["condition"]["text"]

    return {
        "city": location_name,
        "temperature": temperature,
        "condition": condition
    }
