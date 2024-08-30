import requests
from typing import Final

API_KEY: Final = '822ccea99e830f652ac3eec191bf60ef'


def get_weather_infos(city: str):
    response = requests.get(
        f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&lang=tr&units=metric'
    )
    data = response.json()
    if response.status_code == 200:
        return data
    else:
        print(f"Error {data['cod']}: {data['message']}")
        return None
