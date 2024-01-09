import discord

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self,message):
        if message.author == client.user:
            return

        if message.content.startswith('$hello'):
            await message.channel.send('Hello!')

        if message.content.startswith('$qual seu nome?'):
            await message.channel.send("joaozin delas")

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run('MTE5NDQyMzczODUwMzAyNDc1MA.GXcQvJ.x42OanmPNBmeQdY2BK7F4A_BxwT8NXSlUAvI_4')