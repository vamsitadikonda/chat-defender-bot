import sys
from pathlib import Path  # if you haven't already done so

file = Path(__file__).resolve()
parent, root = file.parent, file.parents[1]
sys.path.append(str(root))

# Additionally remove the current file's directory from sys.path
try:
    sys.path.remove(str(parent))
except ValueError:  # Already removed
    pass

import os
import discord
from dotenv import load_dotenv
import src.checkers.profanity
from src.checkers.apology import ApologyChecker
from src.checkers.reporter import ReportChecker
from src.utils.msg import clean_message, get_msg_template, get_help_message
from src.checkers.bully import BullyChecker

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
    print(f'Message from {message.author}: {message.content}: {message.channel.name}')
    # Step 0: check if message is by Bot
    author = message.author
    aid = message.author.id
    channel_name = message.channel.id
    if author == client.user:
        return
    # Step 1: Pre-process message
    msg_content = clean_message(str(message.content))
    if msg_content.find('hello') != -1:
        await message.reply("Hey <@{0}> how's it going?".format(aid))
    if msg_content.find('help') != -1:
        await message.reply(get_help_message())
    # Step 2: Check for profanity
    if pc.check_message(msg_content):
        #await message.delete()
        # Step2.1 : Checking if the user has a first time offense
        warning = ac.check_user_for_ban(aid, channel_name)
        await message.channel.send(get_msg_template(aid, "profanity", warning))
        # Step2.2: Banning user if not a first-time offense
        # ToDo: Writing Ban logic
        if not warning:
            ac.add_warning(aid, channel_name)

    # Step 3: Check for Bully & Toxic Traits
    traits = bc.check_message(msg_content)
    if len(traits) > 0:
        #await message.delete()
        # Step3.1 : Checking if the user has a first time offense
        warning = ac.check_user_for_ban(aid, channel_name)
        await message.channel.send(get_msg_template(aid, traits, warning))
        # Step3.2: Banning user if not a first-time offense
        # ToDo: Writing Ban logic
        if not warning:
            ac.add_warning(aid, channel_name)

    # Step 4: Check for Apology
    if ac.check_message(msg_content):
        ac.add_apology(aid, channel_name)

    # Step 5: Reporting a Profane Word
    if rc.check_message(msg_content):
        report_type, report_token = rc.parse_message()
        if report_type == "word":
            rc.report_word()

if __name__ == "__main__":
    load_dotenv("bot.env")
    token = os.getenv("token")
    bc = BullyChecker()
    ac = ApologyChecker()
    pc = src.checkers.profanity.ProfanityChecker()
    rc = ReportChecker()
    client.run(token)
