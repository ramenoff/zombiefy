import discord
from main import *

FILE_NAME = "zombieways.txt"

PHRASE_1A = "IN MY HEAD IN MY HEAD"
PHRASE_1B = "IN MY HEAD, IN MY HEAD"
PHRASE_2A = "IN YOUR HEAD IN YOUR HEAD"
PHRASE_2B = "IN YOUR HEAD, IN YOUR HEAD"

RESPONSE_1 = "Zombie, Zombie, Zombie-ie-ie-ie"

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

    
    if (PHRASE_1A in message.content.upper() or PHRASE_1B in message.content.upper()  or PHRASE_2A in message.content.upper()  or PHRASE_2B in message.content.upper()) :
        await message.channel.send(RESPONSE_1)

client.run('NzUxMTQ3NTg4ODg3MTE3OTQ2.X1E2tA.5aCwIzJHWDgor1z1GspMPcKsxVE')