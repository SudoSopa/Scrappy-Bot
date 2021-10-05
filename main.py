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
	modlog = client.get_channel(611980801969487882) 
	fakemodlog = client.get_channel(859678510780121098) #for testing
	message = await channel.fetch_message(payload.message_id)
	"""
	await channel.send('Reaction detected!\n' + \
			   'Message ID: ' + str(payload.message_id) +'\n' +  \
			   'Reacting User\'s ID: ' + str(payload.user_id) +'\n'+ \
			   'Emoji Name: ' + payload.emoji.name)
	print(payload.emoji.name)
	"""

	if payload.emoji.name == '🛑':
		await message.clear_reaction('🛑')
		await modlog.send('<@&370637282648260608> <@&894752798305038386>\n🚨 Message Reported! 🚨') 
		#await modlog.send('Message reported! {}'.format(message.format.mention)) #Currently pings author message, change to Bot dev, then Mod role later

		# Build embed fields then send
		embedDescription = '**Reported message sent by {} '.format(message.author.mention) + \
			     	   'in {}**'.format(message.channel.mention) +  '\n' + \
			     	   message.content + '\n\n' + \
			     '[Jump to Message](' + message.jump_url + ')' 

		embedReport = discord.Embed(description=embedDescription, color=discord.Colour.red())
		embedReport.add_field(name='Report sent by', value=payload.member.mention, inline=False)
	
		#await modlog.send(embed=embedReport)
		await modlog.send(embed=embedReport)

		""" #Keep this to have necessary data
		await modlog.send('Message reported!\n' + \
			   'Message Contents ' + message.content + '\n' + \
			   'Message Link: ' + message.jump_url +'\n' +  \
			   'Channel ID: ' + str(client.get_channel(payload.channel_id)) + '\n' + \
			   'Reacting User\'s ID: ' + str(payload.user_id))
		"""

	
@client.event
async def on_message(message):
	
	fakemodlog = client.get_channel(859678510780121098) #for testing
	modlog = client.get_channel(611980801969487882) #for the real deal

	#if DM message
	if not message.guild:
		await fakemodlog.send("DM received!\n\n")
		
		#Build embed
		embedDescription = message.content

		#init embed
		embedDM = discord.Embed(description=embedDescription)

		#send embed
		await modlog.send(embed=embedDM)
	

	#await fakemodlog.send("Message received! No DM check.")


load_dotenv('.env')
client.run(os.getenv('BOT_TOKEN'))
