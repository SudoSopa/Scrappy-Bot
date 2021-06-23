# main.py

import discord
from dotenv import load_dotenv # Using env vars to hide token
import os # Reads .env to get token

intents = discord.Intents(guild_messages=True, guild_reactions=True)

client = discord.Client()

@client.event
async def on_ready():
	print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
	if message.author == client.user: #Prevents bot replying to its own msg
		return

	if message.content.startswith('hello'):
		await message.channel.send('Hello from Scrappy!')

@client.event
async def on_raw_reaction_add(payload):
	#print("Reaction detected!")
	channel = client.get_channel(payload.channel_id)
	await channel.send('Reaction detected!\n' + \
			   'Message ID: ' + str(payload.message_id) +'\n' +  \
			   'Reacting User\'s ID: ' + str(payload.user_id))


load_dotenv('.env')
client.run(os.getenv('BOT_TOKEN'))
