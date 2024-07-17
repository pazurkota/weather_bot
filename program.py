import discord, read_json, api_data


class Client(discord.Client):
    async def on_ready(self):
        print(f'Logged as: {self.user}')

    async def on_message(self, message):
        if message.content.startswith('$json'):
            await message.channel.send(api_data.get_request_data())


intents = discord.Intents.all()

client = Client(intents=intents)
client.run(read_json.get_token())
