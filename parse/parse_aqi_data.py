import discord, datetime
from data import api_data


def parse_aqi_data(lat, lon, ctx):
    data = api_data.get_aqi_data(lat, lon)
    city = api_data.get_city_name(lat, lon)

    description = f"""
    ```
Air Quality Index: {data['list'][0]['main']['aqi']} ({show_aqi_index_desc(data['list'][0]['main']['aqi'])})

Concentration of CO: {data['list'][0]['components']['co']}µg/m³
Concentration of NO: {data['list'][0]['components']['no']}µg/m³
Concentration of NO₂: {data['list'][0]['components']['no2']}µg/m³
Concentration of O₃: {data['list'][0]['components']['o3']}µg/m³
Concentration of SO₂: {data['list'][0]['components']['so2']}µg/m³
Concentration of PM₂.₅: {data['list'][0]['components']['pm2_5']}µg/m³
Concentration of PM₁₀: {data['list'][0]['components']['pm10']}µg/m³
Concentration of NH₃: {data['list'][0]['components']['nh3']}µg/m³```
    """

    embed = discord.Embed(
        colour=discord.Colour.green(),
        title=f"Air Quality Index {city[0]}, {city[1]}",
        description=description
    )

    embed.set_footer(text=f"Requested by {ctx.author} • API provided by OpenWeatherMap")
    embed.timestamp = datetime.datetime.utcnow()
    return embed


def show_aqi_index_desc(aqi_index):
    if aqi_index == 1:
        return "Good"
    elif aqi_index == 2:
        return "Fair"
    elif aqi_index == 3:
        return "Moderate"
    elif aqi_index == 4:
        return "Poor"
    elif aqi_index == 5:
        return "Very Poor"
    else:
        return "Unknown"