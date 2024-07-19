def kelvin_to_celsius(kelvin):
    return round(kelvin - 273.15, 1)


def kelvin_to_fahrenheit(kelvin):
    return round((kelvin - 273.15) * 1.8 + 32, 1)


def ms_to_kph(ms):
    return round(ms * 3.6, 2)


def ms_to_mph(ms):
    return round((ms * 3.6) / 1.6, 2)
