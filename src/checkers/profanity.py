from src.checkers import Checker
import src.utils.db


class ProfanityChecker(Checker):
    def __init__(self):
        self.words = ["fuck", "ass", "stupid"]
        self.conn = src.utils.db.DbConnector()
        self.conn.connect()
        self.conn.create_tables()

    def check_word(self, word: str):
        return bool(word in self.words)

    def check_message(self, message: str):
        """
        Function to check if a message has profane words
        :param message: Message String
        :return: Boolean
        """
        for word in message.split():
            if self.check_word(word):
                return True
        return False

    def report_word(self, word):
        """
        function to add profane words.
        :return: True once added else False
        """
        try:
            self.words.append(word)
            return True
        except Exception:
            print("Couldn't add word: {}".format(word))
        return False
