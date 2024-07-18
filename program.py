import discord, read_json, api_data
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
    data = api_data.get_weather_data(city[0], city[1])
    await ctx.send(data)


@bot.command()
async def aqi(ctx, arg):
    city = api_data.get_geolocation(arg)
    data = api_data.get_aqi_data(city[0], city[1])
    await ctx.send(data)

bot.run(read_json.get_token())
