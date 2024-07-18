import discord
import Responses
from discord import app_commands
from discord.ext import commands
import random
import numpy as np
total = 0
async def send_message(message,user_message, is_private):
    try:
        response = Responses.handle_response(user_message)#response is in responses.py on the function of handle_respon se
        await message.author.send(user_message) if is_private == True else await message.channel.send(response)# send to user if isprivate= true, else send to sever
    except Exception as e:   #message place to author(dm) send
        print(e)



#function to run bot on main
def run_discord_bot():
    #token and bot setup
    TOKEN = 'MTA2ODg4ODA2MjY2ODU4NzA2MQ.G1MtFY.jHaFBOR8yVhZtfX6CZ42AFDeLoncvf6bgvpcLw'
    intents = discord.Intents.default()
    intents.message_content = True
    bot = commands.Bot(command_prefix="!", intents= discord.Intents.all())#slash command
    # client = discord.Client(intents=intents)
    @bot.event
    async def on_ready():
        print(f'{bot.user} is now running')
        try:
            synced = await bot.tree.sync()
            print(f"synced {len(synced)} command(s)")
        except Exception as e:
            print("error")



    #on when there is change in client(the meaning of client.event). variable message is the messages in discord
    @bot.event
    async def on_message(message):
        if message.author == bot.user:
            return 
        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)

        print(f"{username} said: '{user_message}' ({channel})")#checking if code is working

    #slash command
    @bot.tree.command(name="hello",description="says hello")
    async def hello(interaction: discord.Interaction):
        await interaction.response.send_message(f"hey{interaction.user.mention}! this is a slash command")

    @bot.tree.command(name="cube", description="randomness")
    @app_commands.describe(maxim = "maximum")
    async def cube(interaction: discord.Interaction, maxim: int):
        x = str(random.randint(1,maxim))
        await interaction.response.send_message(f"{interaction.user.name} rolled a {x}! ")

    @bot.tree.command(name="add", description=" adds two integers")
    @app_commands.describe(number1 = "first number", number2 = "second number")
    async def add(interaction: discord.Integration, number1: int, number2: int):
        await interaction.response.send_message(number1 + number2)

    @bot.tree.command(name="say")
    @app_commands.describe(text = "your quote")
    async def say(interaction: discord.Interaction, text: str):
         await interaction.response.send_message(f"{interaction.user.mention} said '{text}'")

    @bot.tree.command(name = "fish")
    async def say(interaction: discord.Interaction):
        itemchoice = ["cat","fish","magnet","nothing"]
        secure_random = random.SystemRandom()
        item = secure_random.choice(itemchoice)
        print (item)
        match item:
            case "cat":
                amount = 200
            case "fish":
                amount = 40
            case "magnet":
                amount = 90
            case "nothing":
                amount = 0
        await interaction.response.send_message(f"you fished up a {item}, worth {amount}")
        global total
        total = interaction.user.total+amount

    
    @bot.tree.command(name = "balance")
    async def balance(interaction: discord.Interaction):
        await interaction.response.send_message(f"your balance is {total}") 


    


    bot.run(TOKEN)