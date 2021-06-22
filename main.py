# main.py


import discord
from dotenv import load_dotenv # Using env vars to hide token
import os # Reads .env to get token

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

load_dotenv('.env')
client.run(os.getenv('BOT_TOKEN'))
