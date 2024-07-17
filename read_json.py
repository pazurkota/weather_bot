import json


def read_json():
    file = open('data.json')
    data = json.load(file)
    return data


def get_api_key():
    return read_json()['api']


def get_token():
    return read_json()['token']
