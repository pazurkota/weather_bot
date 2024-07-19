import discord, parse_weather_data
from data import api_data, read_json
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)


@bot.event
async def on_ready():
    print(f'Successfully logged in as {bot.user}')


@bot.command()
async def weather(ctx, arg):
    city = api_data.get_geolocation(arg)
    await ctx.send(embed=parse_weather_data.parse_weather_data(city[0], city[1], ctx))


@bot.command()
async def aqi(ctx, arg):
    await ctx.send('AQI data is not available at this time.')

bot.run(read_json.get_token())
