import discord, datetime
from data import api_data


def parse_aqi_data(lat, lon, ctx):
    data = api_data.get_aqi_data(lat, lon)

    description = f"""
    ```
Air Quality Index: {data['list'][0]['main']['aqi']}

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
        title=f"Air Quality Index for location:",
        description=description
    )

    embed.set_footer(text=f"Requested by {ctx.author} • API provided by OpenWeatherMap")
    embed.timestamp = datetime.datetime.utcnow()
    return embed