import discord
import wolfram_language_functions as wlf
import configparser

intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)

user_datasets = {} # Initialize user_datasets to empty dict, it has not been populated yet

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
    if message.content.startswith('!predict'):
        # starting a message with !predict will, first time, build the datasets
        # If the datasets are already built, it will just use that
        print("Original content:", message.content[9:])
        predicted = await predict_text(message.author.id, message.guild, message.content[9:])
        print("Predicted next word:", predicted)


async def predict_text(user, guild, phrase, channels=False):  #TODO: Change this to predict_text
    """
    This will run on each channel of the specified guild, 
    or if channels is specified 
    it will only run on the specified ones.
    
    If datasets is already specified, it will not go through the process
    of re-creating a new one.
    
    Read the message history, and return a dictionary with one dataset 
    for each user--a dictionary with the list of messages they've sent
    {user1: [message1, message2, message3], user2: ...}
    
    TODO: Maybe separate into different datasets for different channels?
    
    Return value: string (predicted next word/phrase)
    """
    global user_datasets
    if not user_datasets:
        user_ids = [user.id for user in guild.members]
        for user_id in user_ids:
            user_datasets[user_id] = []
            for channel in (channels or guild.text_channels):
                messages = await channel.history(limit=5).flatten()
                for i in range(len(messages)): # Could maybe delete item as it is matched to user, but for now that causes problems
                    if messages[i].author.id == user_id:
                        user_datasets[user_id].append(messages[i].content)
    return wlf.predict_next_word(user_datasets, user, phrase, True)
    
  

client.run(config['DISCORD']['APIKey'])
