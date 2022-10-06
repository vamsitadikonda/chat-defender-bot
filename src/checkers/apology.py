from . import Checker
import src.utils.db


class ApologyChecker(Checker):
    def __init__(self):
        self.conn = src.utils.db.DbConnector()
        self.conn.connect()


    def check_user(self, user_id, server_name):
        """
        Function to check whether a user has any outstanding warnings
        """

        try:
            out = 0
            cursor = self.conn.connector.cursor()
            sql_query = "SELECT offense_count - apology_count FROM discorddb.user_activity WHERE user_id = %s AND server_name = %s"
            cursor.execute(sql_query, (user_id, server_name))
            result = cursor.fetchone()
            out = result[0]
        except Exception as error:
            print("Failed to get record from MySQL table: {}".format(error))
        finally:
            cursor.close()
            if out > 0:
                print("Offenses more than expected. Banning User")
                self.ban_user(user_id, server_name, 1)
                return True
            print("Apologized enough. Unbanning User")
            self.ban_user(user_id, server_name, 0)
            return False

    def add_warning(self, user_id, server_name):
        try:
            cursor = self.conn.connector.cursor()
            sql_query = "UPDATE discorddb.user_activity SET offense_count = offense_count+1 WHERE user_id = %s AND server_name = %s"

            val = (user_id,server_name)
            cursor.execute(sql_query, val)
            self.conn.connector.commit()
        except Exception as error:
            print("Failed to get record from MySQL table: {}".format(error))
        finally:
            cursor.close()
            return True

    def add_user(self, user_id, server_name):
        try:
            cursor = self.conn.connector.cursor()
            sql_query = "SELECT is_banned FROM discorddb.user_activity WHERE user_id = %s AND server_name = %s"
            cursor.execute(sql_query, (user_id, server_name))
            result = cursor.fetchone()
            if not result:
                sql_query = "INSERT INTO discorddb.user_activity (user_id, server_name) VALUES (%s,%s)"
                val = (user_id, server_name)
                cursor.execute(sql_query, val)
                self.conn.connector.commit()
            else:
                if result[0] == 1:
                    print("User is banned from this server. Can't insert into the channel")
                else:
                    print("User is already present in the channel")
        except Exception as error:
            print("Failed to get record from MySQL table: {}".format(error))
        finally:
            cursor.close()
            return True

    def add_apology(self, user_id, server_name):
        try:
            cursor = self.conn.connector.cursor()
            sql_query = "UPDATE discorddb.user_activity SET apology_count = apology_count+1 WHERE user_id = %s AND server_name = %s"
            val = (user_id, server_name)
            cursor.execute(sql_query, val)
            self.conn.connector.commit()
        except Exception as error:
            print("Failed to get record from MySQL table: {}".format(error))
        finally:
            cursor.close()
            return True

    def ban_user(self, user_id, server_name, is_banned):
        try:
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
