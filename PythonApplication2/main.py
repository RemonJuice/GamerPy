import discord
import re
import random
import glob
from time import sleep

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

    if message.content.startswith("PlayingGame"):
        await client.send_message(message.channel,message.mentions[0].game.name+message.mentions[0].id)

    if message.content.startswith("pic:"):
                await client.send_file(message.channel,"C:\\ProgwwwramTmp\\"+_Message_Text.split(":")[1]+".jpg")

    if message.content.startswith("start:"):
        if client.user != message.author:
            _Specified_Channel = _Message_Text.split(":")[1]
            _Channels = message.channel.server.channels
            _Team1 = []
            _Team2 = []
            _SpecifiedMembers = message.mentions

            for c in _Channels:
                if c.name == _Specified_Channel:
                    _Members = c.voice_members


            for m in _SpecifiedMembers:
               _Team1 = _Team1 + [m.name]
               delnum = _Members.index(m)
               print(delnum)
               del _Members[delnum]

            for i in range(len(_Members)):
                if _Members[i].name != "Rythm" :
                    _UnderNum = 0
                    _TextFileR = open(_Specified_Channel+"_"+_Members[i].name+".txt",'r')
                    _PlayedNum = int(_TextFileR.readline())
                    _TextFileR.close()
                    for j in range(len(_Members)):
                        if _Members[j].name != "Rythm":
                            _TextFileR = open(_Specified_Channel+"_"+_Members[j].name+".txt",'r')
                            if _PlayedNum > int(_TextFileR.readline()):
                                _UnderNum = _UnderNum + 1
                                _TextFileR.close()

                    if _UnderNum < 5 - len(_Team1):
                        _Team1 = _Team1 + [_Members[i].name]
                    else:
                        _Team2 = _Team2 + [_Members[i].name]

            if (len(_Team1) < 5) & (len(_Team2) > 0):
                for i in range(5-len(_Team1)):
                    _Team1 = _Team1 + [_Team2[0]]
                    del _Team2[0]

            await client.send_message(message.channel,"-------------チーム1-------------")
            for m in _Team1:
                await client.send_message(message.channel,m)
                _TextFileR = open(_Specified_Channel+"_"+m+".txt",'r')
                _PlayedNum = int(_TextFileR.read())
                print(_PlayedNum)
                _TextFileR.close()
                _TextFileW = open(_Specified_Channel+"_"+m+".txt",'w')
                _TextFileW.write(str(_PlayedNum + 1))
                _TextFileW.close()
            await client.send_message(message.channel,"-------------チーム2-------------")
            for m in _Team2:
                await client.send_message(message.channel,m)
            await client.send_message(message.channel,"--------------------------------")


    if message.content.startswith("set:"):
        _Specified_Channel = _Message_Text.split(":")[1]
        _SpecifiedMembers = message.mentions
        for member in _SpecifiedMembers:
            _TextFileW = open(_Specified_Channel+"_"+member.name+".txt",'w')
            _TextFileW.write("0")
            _TextFileW.close()

    if message.content.startswith("playnum"):
        _Specified_Channel = _Message_Text.split(":")[1]
        _SpecifiedMembers = message.mentions
            

        for m in _SpecifiedMembers:
            _TextFileR = open(_Specified_Channel+"_"+m.name+".txt",'r')
            await client.send_message(message.channel,m.name+":"+_TextFileR.readline())
            _TextFileR.close()

    if message.content.startswith("playnum_ch:"):
        _Specified_Channel = _Message_Text.split(":")[1]
        path = "C:\\Users\\さはら\\source\\repos\\PythonApplication2\\PythonApplication2\\r6s_*.txt"
        files = glob.glob(path)

        for f in files:
            _FileName = f.split("\\")[7]
            _TextFileR = open(_FileName)
            _UserName = _FileName.split("_")[1]
            _UserName = _UserName.split(".")[0]
            await client.send_message(message.channel,_UserName+":"+_TextFileR.readline())
            _TextFileR.close

    if message.content.startswith("-Play"):
        _Specified_Channel = message.content.split(" ")[1]
        _Channels = message.channel.server.channels
        for c in _Channels:
            if (client.user in c.voice_members) and (c.name != _Specified_Channel) and (c.type == discord.ChannelType.voice):
                voice = client.voice_client_in(message.server)
                await voice.disconnect()
        for c in _Channels:
            if c.name == _Specified_Channel and c.type == discord.ChannelType.voice:
                if client.user in c.voice_members:
                    voice = client.voice_client_in(message.server)
                    await voice.disconnect()
                voice = await client.join_voice_channel(c)
                player = await voice.create_ytdl_player(message.content.split(" ")[2])
                player.start()

    if message.content.startswith("_Play"):
        _Channels = message.channel.server.channels
        for c in _Channels:
            if client.user in c.voice_members and not message.author in c.voice_members:
                voice = client.voice_client_in(message.server)
                await voice.disconnect()
        for c in _Channels:
            if message.author in c.voice_members:
                if client.user in c.voice_members:
                    voice = client.voice_client_in(message.server)
                    await voice.disconnect()
                voice = await client.join_voice_channel(c)
                player = await voice.create_ytdl_player(message.content.split(" ")[1])
                player.start()
    if message.content.startswith("vc"):
        _vcword = message.content.split(" ")[1]
        if _vcword == "イキスギィ":
            _URL = "https://www.youtube.com/watch?v=XK6QWxOlQjY"
        _Channels = message.channel.server.channels
        for c in _Channels:
            if client.user in c.voice_members and not message.author in c.voice_members:
                voice = client.voice_client_in(message.server)
                await voice.disconnect()
        for c in _Channels:
            if message.author in c.voice_members:
                if client.user in c.voice_members:
                    voice = client.voice_client_in(message.server)
                else:
                    voice = await client.join_voice_channel(c)
                player = await voice.create_ytdl_player(_URL)
                player.start()
    if message.content.startswith("leave"):
        voice = client.voice_client_in(message.server)
        await voice.disconnect()

@client.event
async def on_member_update(before,after):
    if(before.game!=after.game):
        if(after.game==None):
            #await client.send_message(client.get_channel('457486096155148291'),after.name+'is not playing game')
            if(after.name=='かなめ　しおん'):
                await client.send_message(client.get_channel('460052349579165696'),after.name+'is not playing game')
        else:
            #await client.send_message(client.get_channel('457486096155148291'),after.name+'isPlaying'+after.game.name)
            if(after.name=='かなめ　しおん'):
                await client.send_message(client.get_channel('460052349579165696'),after.name+'isPlaying'+after.game.name)

        
    sleep(10)

client.run("NDU2MDYxOTY3MDQ0NDQ0MTkx.DsxL1w.itOm9nFRU5q5tdwhHH8biJduIYA")