import discord
import wolfram_language_functions as wlf
import configparser

client = discord.Client()

config = configparser.ConfigParser()
config.read('config.ini')

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
    

client.run(config['DISCORD']['APIKey'])
