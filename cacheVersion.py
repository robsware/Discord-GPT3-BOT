import os
import random
from ask11 import ask
import time
import discord
from threading import Timer
#from dotenv import load_dotenv

#load_dotenv()
TOKEN = ''
GUILD = ''

client = discord.Client()



@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')

    #print(f'{client.user.} has connected to Discord!')

cacheText = ""
t = 7200


def emptyCache():
    global cacheText
    cacheText = ""

def newTimer():
    global t
    t = Timer(7200.0, emptyCache)
newTimer()


@client.event
async def on_message(message):
    global cacheText

    if message.author == client.user:
        return


    if message.content.startswith("<@!789793159974092821> ") or message.content.startswith("<@789793159974092821> "):
        response = ask(cacheText + message.content.split(" ", 1)[1])

        t.cancel()
        newTimer()
        t.start()
        print ("Timer restarted")

        cacheText = cacheText + "User: " + message.content.split(" ", 1)[1] +  "\n11: " + response + "\n"


        if ("11:") in response:
            responseLength = response.split("11:")
            for thing in responseLength:
                await message.channel.send(thing)
        else:
            await message.channel.send(response)

    else:
        print(message.content)


@client.event
async def on_error(event, *args, **kwargs):
    with open('err.log', 'a') as f:
        if event == 'on_message':
            f.write(f'Unhandled message: {args[0]}\n')
        else:
            raise discord.DiscordException






client.run(TOKEN)


