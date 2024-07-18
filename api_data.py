import requests as req, json, read_json


# https://openweathermap.org/api
def get_weather_data(lat, lon):
    request = f'/weather?lat={lat}&lon={lon}&appid={read_json.get_api_key()}'
    response = req.get(f'https://api.openweathermap.org/data/2.5{request}')
    return response.json()


def get_aqi_data(lat, lon):
    request = f'/air_pollution?lat={lat}&lon={lon}&appid={read_json.get_api_key()}'
    response = req.get(f'https://api.openweathermap.org/data/2.5{request}')
    return response.json()


def get_geolocation(location):
    request = f"/direct?q=\'{location}\'&limit=1&appid={read_json.get_api_key()}"
    response = req.get(f'https://api.openweathermap.org/geo/1.0{request}')

    latitude = response.json()[0]['lat']
    longitude = response.json()[0]['lon']

    return [latitude, longitude]
