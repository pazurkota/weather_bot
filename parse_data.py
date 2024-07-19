import discord, api_data


def parse_weather_data(lat, lon):
    data = api_data.get_weather_data(lat, lon)

    description = f"""
    ```
Current temperature: {kelvin_to_celsius(data['main']['temp'])}°C ({kelvin_to_fahrenheit(data['main']['temp'])}°F) 
Temperature range: {kelvin_to_celsius(data['main']['temp_min'])}°C-{kelvin_to_celsius(data['main']['temp_max'])}°C ({kelvin_to_fahrenheit(data['main']['temp_min'])}°F-{kelvin_to_fahrenheit(data['main']['temp_max'])}°F)
Air pressure: {data['main']['pressure']}hPa
Humidity: {data['main']['humidity']}%

Wind speed: {data['wind']['speed']}m/s ({ms_to_kph(data['wind']['speed'])}kph or {ms_to_mph(data['wind']['speed'])}mph)
Wind direction: {data['wind']['deg']}°
Wind gusts: {data['wind']['gust']}m/s ({ms_to_kph(data['wind']['gust'])}kph or {ms_to_mph(data['wind']['gust'])}mph)

Rain volume for the last hour: {data['rain']['1h']}mm
Cloudiness: {data['clouds']['all']}%
    ```
    """

    embed = discord.Embed(
        colour=discord.Colour.green(),
        title=f"Weather for {data['name']}, {data['sys']['country']}:",
        description=description
    )
    return embed


def kelvin_to_celsius(kelvin):
    return round(kelvin - 273.15, 1)


def kelvin_to_fahrenheit(kelvin):
    return round((kelvin - 273.15) * 1.8 + 32, 1)


def ms_to_kph(ms):
    return round(ms * 3.6, 2)


def ms_to_mph(ms):
    return round((ms * 3.6) / 1.6, 2)


    