## Requirements and Instructions
Specifies all requirements to run the discord bot

Prerequisites

* [Python](https://www.python.org)
* [Docker](https://www.docker.com/)

Upgrade pip:
```
python -m pip install --upgrade pip;
```
To clone the project from the repository:
```
git clone git@github.com:vamsitadikonda/chat-defender-bot.git
```

Build a Docker Image 
```
docker build -t discord-bot .
```

You can run the bot by running the docker Image
```
docker run -d discord-bot
```
