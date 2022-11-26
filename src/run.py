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
    author_id = message.author.id
    channel_name = message.channel.id
    if author == client.user:
        return
    # Step 1: Pre-process message
    print(f"The message is: {message.content}, The channel is: {channel_name}, The Author Info: {author}-{author_id}")
    msg_content = clean_message(str(message.content))
    if msg_content.find('hello') != -1:
        await message.reply("Hey <@{0}> how's it going?".format(author_id))
    if msg_content.find('help') != -1:
        await message.reply(get_help_message())
    
     # Step 2: Reporting a Profane Word
    if rc.check_message(msg_content):
        report_type, report_token = rc.parse_message(msg_content)
        if report_type == "word":
            if pc.add_words(channel_name, report_token):
                await message.reply("{0} has been added as a toxic word".format(report_token))
    # Step 3: Check for profanity
    elif pc.check_message(channel_name, msg_content):
        # Step2.1 : Checking if the user has a first time offense
        warning = ac.check_user_for_warning(author_id, channel_name)
        await message.channel.send(get_msg_template(author_id, "profanity", warning))
        # Step2.2: Banning user if not a first-time offense
        ac.add_warning(author_id, channel_name)
        if not warning:
            await message.author.ban()

    # Step 4: Check for Bully & Toxic Traits
    traits = bc.check_message(msg_content)
    print("The traits are", traits)
    if len(traits) > 0:
        # Step3.1 : Checking if the user has a first time offense
        warning = ac.check_user_for_warning(author_id, channel_name)
        await message.channel.send(get_msg_template(author_id, traits, warning))
        # Step3.2: Banning user if not a first-time offense
        ac.add_warning(author_id, channel_name)
        if not warning:
            await message.author.ban()

    # Step 5: Check for Apology only when there is no profanity usage or bulling found 
    elif ac.check_message(msg_content):
        if ac.add_apology(author_id, channel_name):
            await message.reply("Hey <@{0}>, your apology is accepted by the bot".format(author_id))

   

if __name__ == "__main__":
    load_dotenv("bot.env")
    token = os.getenv("token")
    bc = BullyChecker()
    ac = ApologyChecker()
    pc = src.checkers.profanity.ProfanityChecker()
    rc = ReportChecker()
    client.run(token)
