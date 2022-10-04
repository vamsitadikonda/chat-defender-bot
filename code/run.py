import os
import discord
from dotenv import load_dotenv
from checkers.profanity import ProfanityChecker
from checkers.apology import ApologyChecker
from utils.msg import clean_message, get_msg_template

load_dotenv("bot.env")
token = os.getenv("token")
intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f"{client.user} has connected to Discord!")


@client.event
async def on_message(message):
    """
    :param message: The context of the message sent on Discord
    :return: None
    """
    print(f'Message from {message.author}: {message.content}')
    # check if message is by Bot
    author = message.author
    aid = message.author.id
    if author == client.user:
        return
    msg_content = clean_message(str(message.content))
    if msg_content.find('hello') != -1:
        await message.channel.send("Hi there!")
    # check for profanity
    if pc.check_message(msg_content):
        await message.delete()
        # checking if the user has a first time offense
        warning = ac.check_user(aid, "profane")
        await message.channel.send(get_msg_template(aid, "profane", warning))


ac = ApologyChecker()
pc = ProfanityChecker()
client.run(token)
