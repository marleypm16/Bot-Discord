import discord
import os
from config import TOKEN

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    # hello to a new member

    async def on_member_join(self,member):
        channel_name ='heavy-choices'
        channel = discord.utils.get(member.guild.channels, name=channel_name)

        if channel is not None:
            welcome_message = f'Mais um merda no servidor,{member.mention}! Seja bem-vindo'
            await channel.send(welcome_message)
    
    # music bot
    


    # mensagens no geral  
    
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
