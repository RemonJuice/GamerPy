import discord
import re
import random
import glob


client = discord.Client()
#discord.opus.load_opus("opuslib")

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    print(discord.opus.is_loaded())
@client.event

async def on_message(message):
    _Random = random.randint(0,3)
    mentions = message.mentions


    if client.user in mentions:
        if _Random == 0:
            await client.send_message(message.channel,"あっ"+message.author.name+"さん、何でしょうか?")
        elif _Random == 1:
            await client.send_message(message.channel,"何でしょうか？")
        elif _Random == 2:
            await client.send_message(message.channel,"ん？なんですか？")
        elif _Random == 3:
            await client.send_message(message.channel,"はい、なんでしょうか")


    if message.content.startswith("join") and client.user in mentions:
        _Specified_Channel = message.content.split(":")[1]
        _Channels = message.channel.server.channels
        for c in _Channels:
            if c.name == _Specified_Channel:
                if client.user in c.voice_members:
                    voice = client.voice_client_in(message.server)
                else:
                    voice = await client.join_voice_channel(c)
                player = voice.create_ffmpeg_player("test.mp3")
                player.start()
    if message.content.startswith("leave"):
        voice = client.voice_client_in(message.server)
        await voice.disconnect()        
                
             
       
client.run("NDY1MTE3MDQxOTg1MTkxOTM2.DiI1pA.HhjQZ_7IqrmErNBfyjB_ajctW9s")