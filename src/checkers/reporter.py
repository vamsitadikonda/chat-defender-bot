from . import Checker


class ReportChecker(Checker):
    def check_message(self, msg:str):
        return msg.startswith('!report')

    def parse_message(self, msg):
        return msg.split(" ")[1], msg.split(" ")[2]

    def report_word(self, server, word):
        """
        function to add profane words for the respective discord server.
        :return: True once added else False
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
        except Exception as error:
            print("Failed to insert record from MySQL table: {}".format(error))
        finally:
            cursor.close()
            return True
