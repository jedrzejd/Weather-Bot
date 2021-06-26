import json

import requests
from tokens import WEATHER_TOKEN


def get_current_weather_from_city_name(city_name):
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&units=metric&lang=pl&appid={WEATHER_TOKEN}'
    data = json.loads(requests.get(url).content)
    return parse_data(data)


def parse_data(data):
    data = data['main']
    return data