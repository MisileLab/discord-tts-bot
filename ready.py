import discord
import json
from discord.ext import commands
import time

Client = commands.Bot(command_prefix='/')
f = open('config.json', 'r', encoding='UTF8')
jsonString = json.load(f)
TOKEN = jsonString['token']
message = jsonString['message']
list1 = message.split(',')
f.close()

@Client.command()
async def start(ctx):
    count1 = 0
    for i in list1:
        await ctx.send(list1[count1], tts=True)
        count1 = count1 + 1
        print(count1)
        time.sleep(5)

Client.run(TOKEN)
