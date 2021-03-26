import discord
import os
from main import *

PHRASES = ['IN MY HEAD IN MY HEAD', 'IN MY HEAD, IN MY HEAD', 'IN YOUR HEAD IN YOUR HEAD', 'IN YOUR HEAD, IN YOUR HEAD']

RESPONSE = "Zombie, Zombie, Zombie-ie-ie-ie"

lines = open(FILE_NAME, "r")
zombie_triggers = lines.read().splitlines()
lines.close()

client = discord.Client()


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event

async def on_message(message):

    if message.author == client.user:
        return

    if any([(phrase.lower() in message.content.lower()) for phrase in zombie_triggers]):
        zombie_link = returnVideo()
        await message.channel.send(zombie_link)

    if any(ext in message.content.upper() for ext in phrases):
        await message.channel.send(RESPONSE)

client.run(KEY)