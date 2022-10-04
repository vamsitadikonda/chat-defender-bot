import discord


class DefenderBot:
    """
    Discord Bot Object used to listen to chats.
    """

    def __init__(self, token):
        self._token = token
        self.intents = None
        self.client = None

    def parseMessage(message):
