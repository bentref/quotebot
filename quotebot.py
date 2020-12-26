import discord
import wolfram_language_functions as wlf

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    msg_hist = await read_message_history(client.guilds[0])
    print(msg_hist)
    
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    elif wlf.bad_vibe(message.content):
        user_id = message.author.id
        await message.channel.send(f"<@!{user_id}> That's not a very positive vibe :((((((((")
        
async def read_message_history(guild, channels=False):
    """
    This will run on each channel of the specified guild, 
    or if channels is specified 
    it will only run on the specified ones.
    
    Read the message history, and return a dictionary with one dataset 
    for each user--a dictionary with the list of messages they've sent
    {user1: [message1, message2, message3], user2: ...}
    
    TODO: Need to separate into different datasets for diff channels
    """
    datasets = {}
    user_ids = [user.id for user in guild.members]
    print(guild.members)
    for user_id in user_ids:
        datasets[user_id] = []
        for channel in (channels or guild.text_channels):
            messages = await channel.history(limit=10).flatten()
            for i in range(len(messages)): # Could maybe delete item as it is matched to user, but for now that causes problems
                if messages[i].author.id == user_id:
                    # print(messages[i].content)
                    datasets[user_id].append(messages[i])
                    # del messages[i]
    return datasets
  

client.run('Nzg1OTk4NjUzODcyOTMwODE3.X9AASg.TY1Ja9qKidLqyodwfog1NGJRSFE')
