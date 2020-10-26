import os
import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

@client.event
async def on_ready():
    print('Copy and paste this in your browser to authorize bot https://discordapp.com/oauth2/authorize?client_id={}&scope=bot&permissions=0'.format(os.environ['CLIENTID']))
    print('------')
    print(f'{client.user.name} has connected to Discord!')

@client.event
async def on_message(message):
  if message.author == client.user:
    return
  
  msg = message.content
  lowercase = msg.lower()
  
  # Commands 
  if "!commands" in message.content.lower():
    embedVar = discord.Embed(title="Commands", description="The list of commands for the big shaq discord bot.", color=10181046)
    embedVar.add_field(name="!quick_maths(operator)", value="Does quick maths.", inline=False)
    embedVar.add_field(name="wagwan", value="Reponds with a greeting.", inline=False)
    embedVar.add_field(name="square up", value="Starts talking trash.", inline=False)
    embedVar.add_field(name="wagwan", value="Reponds with a greeting.", inline=False)
    embedVar.add_field(name="where are you?", value="Reveals big shaq's location.", inline=False)
    embedVar.add_field(name="what are you eating?", value="Tells you what big shaq is eating.", inline=False)
    await message.channel.send(embed=embedVar)

  if "wagwan" in lowercase:
    await message.channel.send("Yes yes my g")

  if "square up" in lowercase:
    await message.channel.send("I'll smoke you fam")
  
  if "where" in lowercase:
    await message.channel.send("Miami bruv")

  if "what are you eating" in lowercase:
    await message.channel.send("Rice krispies")

  if  "!quick_maths(+):" in message.content.lower():
    msg = message.content
    msg = msg.replace("!quick_maths:", " ")
    msg = msg.replace("+"," ")
    numbers = [int(word) for word in msg.split() if word.isdigit()]
    num = numbers[0] + numbers[1]
    await message.channel.send(num)
  
  if  "!quick_maths(-):" in message.content.lower():
    msg = message.content
    msg = msg.replace("!quick_maths:", " ")
    msg = msg.replace("-"," ")
    numbers = [int(word) for word in msg.split() if word.isdigit()]
    num = numbers[0] - numbers[1]
    await message.channel.send(num)
  
  if  "!quick_maths(/):" in message.content.lower():
    msg = message.content
    msg = msg.replace("!quick_maths:", " ")
    msg = msg.replace("/"," ")
    numbers = [int(word) for word in msg.split() if word.isdigit()]
    num = numbers[0] / numbers[1]
    await message.channel.send(num)
  
  if  "!quick_maths(*):" in message.content.lower():
    msg = message.content
    msg = msg.replace("!quick_maths:", " ")
    msg = msg.replace("*"," ")
    numbers = [int(word) for word in msg.split() if word.isdigit()]
    num = numbers[0] * numbers[1]
    await message.channel.send(num)

client.run(TOKEN)
