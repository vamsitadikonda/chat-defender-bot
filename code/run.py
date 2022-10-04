import os
import discord
from dotenv import load_dotenv
from getpass import getpass
import mysql.connector

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
    print(f'Message from {message.author}: {message.content}')
    print("message received! :{}".format(message.channel))
    if message.author == client.user:
        return

    if message.content.find('hello')!=-1:
        await message.channel.send("Hi there!")
        connectSql()


def connectSql():
    mydb = mysql.connector.connect(
        host="mysql_db",
        port="3306",
        user="root",
        password="pass"
    )

    mycursor = mydb.cursor()
    print("creating data base")
    mycursor.execute("CREATE DATABASE test4")
client.run(token)
