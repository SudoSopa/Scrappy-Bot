# main.py

# TODO - Use environmental variables to keep bot token a secret when uploading to github

import discord

client = discord.Client()

@client.event
async def on_ready():
	print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
	if message.author == client.user: #Prevents bot replying to its own msg
		return

	if message.content.startswith('$hello'):
		await message.channel.send('Hello from Scrappy!')

client.run('Bot token here')
