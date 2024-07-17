import requests as req, json, read_json


# https://www.weatherapi.com/docs/
def get_request_data():
    request = f'/current.json?key={read_json.get_api_key()}q=\'Warsaw\''
    response = req.get(f'https://api.weatherapi.com/v1{request}')
    return response.json()


def get_json():
    return json.load(get_request_data())

