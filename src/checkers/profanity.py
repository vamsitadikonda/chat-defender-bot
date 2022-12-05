#!/usr/bin/python
from src.checkers import Checker
import src.utils.db
import src.utils.redis
from src.checkers import Checker


class ProfanityChecker(Checker):
    def __init__(self):
        self.words = {}
        self.conn = src.utils.db.DbConnector()
        self.query = "SELECT word FROM discorddb.pwords".encode("utf-8")
        self.redis = src.utils.redis.Redis()
        self.conn.connect()
        self.conn.create_tables()

    def add_words(self, server, word):
        """
        Add all the words inserted into the hate words list
        :return:
        """
        try:
            if not self.redis.check_key(self.query):
                data = self.fetch_words(server)
                self.redis.add_entry(self.query, data)

            if not self.redis.check_word(
                self.query, word
            ):  # check if word not present in cache
                cursor = self.conn.connector.cursor()
                sql_query = "INSERT INTO discorddb.pwords (server_name, word) VALUES (%s,%s)"  # adding a new entry in db
                val = (server, word)
                cursor.execute(sql_query, val)
                self.conn.connector.commit()
                self.redis.add_word(
                    self.query, word
                )  # add the new word in the value set

        except Exception as error:
            print(
                "Failed to insert record in MySQL table / Redis Cache: {}".format(error)
            )
        finally:
            cursor.close()
            return True

    def fetch_words(self, server):
        """
        Fetch all words in the table and return
        :return: Set
        """
        try:
            cursor = self.conn.connector.cursor()
            sql_query = "SELECT word FROM discorddb.pwords WHERE server_name = %s"
            cursor.execute(sql_query, (server,))
            result = cursor.fetchall()
            print(f"The query result is: {result}")
        except Exception as error:
            print("Failed to fetch records from the db: {}".format(error))
        finally:
            cursor.close()
            return set(result)

    def check_word(self, word: str):
        """
        Checks and returns True if the word is in the hate words list. Else returns False
        :param word:
        :return:
        """
        return self.redis.check_word(self.query, word)

        # if server in self.words:
        #     return bool(word in self.words[server])
        # return False

    def check_message(self, server, message: str):
        """
        Function to check if a message has profane words
        :param message: Message String
        :return: Boolean
        """
        if not self.redis.check_key(self.query):
            data = self.fetch_words(server)
            print(f"The Cache has expired adding {data} into cache with a TTL")
            self.redis.add_entry(self.query, data)

        for word in message.split():
            if self.check_word(word):
                return True
        return False
