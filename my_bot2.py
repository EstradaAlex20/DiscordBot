import random
import requests


from discord import Game
from discord.ext.commands import Bot


BOT_PREFIX = '!'
TOKEN = 'put your token here'

@client.command(name='die',
                description='returns a value 0-6',
                pass_context=True)
async def six_side_die(context):
    await client.say(str(random.randint(0,6)) + context.message.author.mention)



@client.command()
async def square(num):
    sq = int(num) * int(num)
    await client.say(str(sq))


@client.event
async def on_ready():
    await client.change_presence(game=Game(name="with python"))
    print("Logged in as " + client.user.name)


@client.command()
async def bitcoin():
    url = 'https://api.coindesk.com/v1/bpi/currentprice/BTC.json'
    response = requests.get(url)
    value = response.json()['bpi']['USD']['rate']
    await client.say("Bitcoin price is: " + value)

client.run(TOKEN)
