import discord


class Client(discord.Client):
    async def on_ready(self):
        print(f'Logged as: {self.user}')

    async def on_message(self, message):
        print(f'Message from {message.author}: {message.content}')


intents = discord.Intents.all()

client = Client(intents=intents)
client.run('token')