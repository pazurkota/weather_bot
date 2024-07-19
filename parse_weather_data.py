import discord, api_data, datetime
from parse_units import kelvin_to_celsius, kelvin_to_fahrenheit, ms_to_kph, ms_to_mph


def parse_weather_data(lat, lon, ctx):
    data = api_data.get_weather_data(lat, lon)

    description = f"""
    ```
Current temperature: {kelvin_to_celsius(data['main']['temp'])}°C ({kelvin_to_fahrenheit(data['main']['temp'])}°F) 
Temperature range: {kelvin_to_celsius(data['main']['temp_min'])}°C-{kelvin_to_celsius(data['main']['temp_max'])}°C ({kelvin_to_fahrenheit(data['main']['temp_min'])}°F-{kelvin_to_fahrenheit(data['main']['temp_max'])}°F)
Air pressure: {data['main']['pressure']}hPa
Humidity: {show_humidity(data)}%

Wind speed: {show_wind_speed(data)}m/s ({ms_to_kph(show_wind_speed(data))}kph or {ms_to_mph(show_wind_speed(data))}mph)
Wind direction: {data['wind']['deg']}°
Wind gusts: {show_wind_gusts(data)}m/s ({ms_to_kph(show_wind_gusts(data))}kph or {ms_to_mph(show_wind_gusts(data))}mph)

Rain volume for the last hour: {show_rain(data)}mm
Cloudiness: {show_cloudiness(data)}%```
    """

    embed = discord.Embed(
        colour=discord.Colour.green(),
        title=f"Weather for {data['name']}, {data['sys']['country']}:",
        description=description
    )

    embed.set_footer(text=f"Requested by {ctx.author} • API provided by OpenWeatherMap")
    embed.timestamp = datetime.datetime.utcnow()
    return embed


def show_humidity(data):
    if 'humidity' in data['main']:
        return data['main']['humidity']
    else:
        return 0


def show_wind_gusts(data):
    if 'gust' in data['wind']:
        return data['wind']['gust']
    else:
        return 0


def show_rain(data):
    if 'rain' in data:
        return data['rain']['1h']
    else:
        return 0


def show_cloudiness(data):
    if 'clouds' in data:
        return data['clouds']['all']
    else:
        return 0


def show_wind_speed(data):
    if 'speed' in data['wind']:
        return data['wind']['speed']
    else:
        return 0
