import discord
import re
import glob
import time
import threading
import asyncio

client = discord.Client()

@client.event
async def on_ready():
	print('Logged in as')
	print(client.user.name)
	print(client.user.id)
	print('------')

@client.event

async def on_message(message):
	_Message_Text = message.content
	timepoint = time.time()
	
	######timer start#######
	if _Message_Text.startswith('/start'):
		timefile = open('Timerlog.txt','w')
		timefile.write(str(timepoint))
		timefile.close()

		await asyncio.sleep(5)

		readfile = open('Timerlog.txt','r')
		savedtime = readfile.read()
		readfile.close()

		if savedtime!='stop':
			await client.send_message(message.channel,'5s')

	######timer stop#######
	if _Message_Text.startswith('/stop'):
		readfile = open('Timerlog.txt','r')
		savedtime = readfile.read()
		readfile.close()

		timefile = open('Timerlog.txt','w')
		timefile.write('stop')
		timefile.close()

		await client.send_message(message.channel,'timer stop')
		await client.send_message(message.channel,'time='+str(timepoint-float(savedtime)))

client.run()

    
