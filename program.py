import discord, read_json, api_data


class Client(discord.Client):
    async def on_ready(self):
        print(f'Logged as: {self.user}')

    async def on_message(self, message):
        if message.content.startswith('$json'):
            city = api_data.get_geolocation('Berlin')
            await message.channel.send(api_data.get_weather_data(city[0], city[1]))
            await message.channel.send(api_data.get_aqi_data(city[0], city[1]))


intents = discord.Intents.all()

client = Client(intents=intents)
client.run(read_json.get_token())
