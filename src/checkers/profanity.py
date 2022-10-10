from src.checkers import Checker
import src.utils.db


class ProfanityChecker(Checker):
    def __init__(self):
        self.words = {}
        self.conn = src.utils.db.DbConnector()
        self.conn.connect()
        self.conn.create_tables()

    def add_words(self, server, word):
        """
        Add all the words inserted into the hate words list
        :return:
        """
        try:
            cursor = self.conn.connector.cursor()
            sql_query = "SELECT word FROM discorddb.pwords WHERE server_name = %s AND word = %s"
            cursor.execute(sql_query, (server, word))
            result = cursor.fetchone()
            if not result:
                sql_query = "INSERT INTO discorddb.pwords (server_name, word) VALUES (%s,%s)"
                val = (server, word)
                cursor.execute(sql_query, val)
                self.conn.connector.commit()
            else:
                print("The word is already reported.")

            if server not in self.words:
                self.words[server] = [word]
            else:
                if word not in self.words[server]:
                    self.words[server].append(word)
            print(self.words)
        except Exception as error:
            print("Failed to insert record from MySQL table: {}".format(error))
        finally:
            cursor.close()
            return True

    def check_word(self, server, word: str):
        """
        Checks and returns True if the word is in the hate words list. Else returns False
        :param word:
        :return:
        """
        if server in self.words:
            return bool(word in self.words[server])
        return False

    def check_message(self, server, message: str):
        """
        Function to check if a message has profane words
        :param message: Message String
        :return: Boolean
        """
        for word in message.split():
            if self.check_word(server, word):
                return True
        return False
