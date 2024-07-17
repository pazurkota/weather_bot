import requests as req, json, read_json


# https://www.weatherapi.com/docs/
def get_request_data():
    request = f'/weather?lat=51.107883&lon=17.038538&appid={read_json.get_api_key()}'
    response = req.get(f'https://api.openweathermap.org/data/3.0{request}')
    return response.json()
