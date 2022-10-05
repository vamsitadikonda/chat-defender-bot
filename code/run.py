import os
import discord
from dotenv import load_dotenv
from checkers.profanity import ProfanityChecker
from checkers.apology import ApologyChecker
from checkers.reporter import ReportChecker
from utils.msg import clean_message, get_msg_template, get_help_message

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
    # Step 0: check if message is by Bot
    author = message.author
    aid = message.author.id
    if author == client.user:
        return
    # Step 1: Pre-process message
    msg_content = clean_message(str(message.content))
    if msg_content.find('hello') != -1:
        await message.channel.send("Hi there!")
    if msg_content.find('help') != -1:
        await message.channel.send(get_help_message())
    # Step 2: Check for profanity
    if pc.check_message(msg_content):
        await message.delete()
        # Step2.1 : Checking if the user has a first time offense
        warning = ac.check_user(aid, "profane")
        await message.channel.send(get_msg_template(aid, "profane", warning))
        # Step2.2: Banning user if not a first-time offense
        # ToDo: Writing Ban logic
    # Step 3: Check for Bully & Toxic Traits
    # ToDo: Write Bully check
    # Step 4: Check for Apology
    if ac.check_message(msg_content):
        ac.add_apology(aid)
    # Step 5: Reporting a Profane Word
    if rc.check_message(msg_content):
        report_type,report_token = rc.parse_message()
        if report_type == "word":
            rc.report_word()


ac = ApologyChecker()
pc = ProfanityChecker()
rc = ReportChecker()
client.run(token)
