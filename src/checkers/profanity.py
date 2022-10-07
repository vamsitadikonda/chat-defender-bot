from src.checkers import Checker
import src.utils.db


class ProfanityChecker(Checker):
    def __init__(self):
        self.words = []
        self.conn = src.utils.db.DbConnector()
        self.conn.connect()
        self.conn.create_tables()
        self.report_word("discord", "EFF U")

    def add_words(self):
        try:
            cursor = self.conn.connector.cursor()
            sql_query = "SELECT word FROM discorddb.pwords"
            cursor.execute(sql_query)
            result = cursor.fetchall()
            for record in result:
                word = record[0]
                if word not in self.words:
                    self.words.append(word)

        except Exception as error:
            print("Failed to get record from MySQL table: {}".format(error))
        finally:
            cursor.close()

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
