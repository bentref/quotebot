import discord
from . import wolfram_language_functions as wlf

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    elif wlf.bad_vibe(message.content):
        user_id = message.author.id
        await message.channel.send(f"<@!{user_id}> That's not a very positive vibe :((((((((")
    

client.run('Nzg1OTk4NjUzODcyOTMwODE3.X9AASg.TY1Ja9qKidLqyodwfog1NGJRSFE')
