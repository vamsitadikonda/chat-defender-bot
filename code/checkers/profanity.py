class ProfanityChecker:
    def __init__(self):
        self.words = ["Fuck", "Ass", "Stupid"]

    def checkWord(self, word: str):
        return bool(word in self.words)

    def checkMessage(self, message: str):
        """
        Function to check if a message has profane words
        :param message: Message String
        :return: Boolean
        """
        for word in message.split():
            if self.checkWord(word):
                return True
        return False

    def reportWord(self, word):
        """
        function to add profane words.
        :return: True once added else False
        """
        try:
            self.words.append(word)
            return True
        except Exception:
            print("Couldnt add word: {}".format(word))
        return False