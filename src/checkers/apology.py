#!/usr/bin/python
from . import Checker
import src.utils.db
from textblob import TextBlob
import operator


class ApologyChecker(Checker):
    def __init__(self):
        self.conn = src.utils.db.DbConnector()
        self.conn.connect()

    def check_message(self, message):
        """
        Just checks for Sorry message
        :param message: message string
        :return:True or False
        """

        score = TextBlob(message).sentiment.polarity  # classifying the text
        print(score)

        sentiment = None
        if score > 0:
            sentiment = "pos"
        elif score < 0:
            sentiment = "neg"
        else:
            sentiment = "neu"

        if sentiment == "pos":
            return False
        else:  # if the sentiment is neutral or negative and we find an apology we return True
            return (
                message.find("sorry") != -1
                or message.find("my bad") != -1
                or message.find("apology") != -1
            )

    def check_user_for_warning(self, user_id, server_name):
        """
        Function to check whether a user has any outstanding warnings or not
        """

        try:
            self.add_user(user_id, server_name)
            cursor = self.conn.connector.cursor()
            sql_query = "SELECT offense_count - apology_count FROM discorddb.user_activity WHERE user_id = %s AND server_name = %s"
            cursor.execute(sql_query, (user_id, server_name))
            result = cursor.fetchone()
            out_count = result[0]
        except Exception as error:
            print("Failed to get record from MySQL table: {}".format(error))
        finally:
            cursor.close()
            if out_count > 0:
                print("Offenses more than expected. Banning User")
                self.ban_user(user_id, server_name, 1)
                return False

            self.ban_user(user_id, server_name, 0)
            return True

    def add_warning(self, user_id, server_name):
        try:
            self.add_user(user_id, server_name)
            cursor = self.conn.connector.cursor()
            sql_query = "UPDATE discorddb.user_activity SET offense_count = offense_count+1 WHERE user_id = %s AND server_name = %s"

            val = (user_id, server_name)
            cursor.execute(sql_query, val)
            self.conn.connector.commit()
        except Exception as error:
            print("Failed to get record from MySQL table: {}".format(error))
        finally:
            cursor.close()
            return True

    def add_user(self, user_id, server_name):
        """
        Function to add user onto the database. If already banned, can't add user.
        :param user_id:
        :param server_name:
        :return:
        """
        try:
            cursor = self.conn.connector.cursor()
            sql_query = "SELECT is_banned FROM discorddb.user_activity WHERE user_id = %s AND server_name = %s"
            cursor.execute(sql_query, (user_id, server_name))
            result = cursor.fetchone()
            if not result:
                print("User not present in the channel.")
                sql_query = "INSERT INTO discorddb.user_activity (user_id, server_name) VALUES (%s,%s)"
                val = (user_id, server_name)
                cursor.execute(sql_query, val)
                self.conn.connector.commit()
                print("User is added into the channel")
            else:
                if result[0] == 1:
                    print(
                        "User is banned from this server. Can't insert into the channel"
                    )

        except Exception as error:
            print("Failed to get record from MySQL table: {}".format(error))
        finally:
            cursor.close()
            return True

    def add_apology(self, user_id, server_name):
        try:
            self.add_user(user_id, server_name)
            cursor = self.conn.connector.cursor()
            sql_query = "UPDATE discorddb.user_activity SET apology_count = apology_count+1 WHERE user_id = %s AND server_name = %s"
            val = (user_id, server_name)
            cursor.execute(sql_query, val)
            sql_query = "UPDATE discorddb.user_activity SET offense_count = CASE WHEN offense_count < apology_count THEN apology_count ELSE offense_count END WHERE user_id = %s AND server_name = %s"
            cursor.execute(sql_query, val)
            self.conn.connector.commit()
        except Exception as error:
            print("Failed to get record from MySQL table: {}".format(error))
        finally:
            cursor.close()
            return True

    def ban_user(self, user_id, server_name, is_banned):
        try:
            self.add_user(user_id, server_name)
            cursor = self.conn.connector.cursor()
            sql_query = "UPDATE discorddb.user_activity SET is_banned = %s WHERE user_id = %s AND server_name = %s"
            val = (is_banned, user_id, server_name)
            cursor.execute(sql_query, val)
            self.conn.connector.commit()
        except Exception as error:
            print("Failed to get record from MySQL table: {}".format(error))
        finally:
            cursor.close()
            return True
