import discord
import os
from config import TOKEN

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        if message.author == self.user:
            return

        if message.content.startswith('$hello'):
            await message.channel.send('Hello!')

        if message.content.startswith('$qual seu nome?'):
            await message.channel.send("joaozin delas")

intents = discord.Intents.default()
intents.messages = True

client = MyClient(intents=intents)
client.run(TOKEN)
