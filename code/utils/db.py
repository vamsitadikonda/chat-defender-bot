import mysql.connector


class DbConnector:
    def __init__(self):
        self.host = "localhost"
        self.user = "root"
        self.password = "pass"
        self.DB = "DISCORD"
        self.connector = None

        ##TODO Connect to database, insertData() and close connection

    def connect(self):
        """
        Function to Open database connection
        :return:
        """
        try:
            self.connector = mysql.connector.connect(host=self.host, port=self.port, user=self.user,
                                                     password=self.password, database=self.DB)
        except Exception as error:
            print("Failed to connect to the database: {}".format(error))
        finally:
            if self.connection.is_connected():
                self.close()

    def insertData(self):
        """
        Function to create and insert tables in the database
        :return:
        """
        try:
            cursor = self.connector.cursor()

            # Create tables and insert data(if any)

            self.connector.commit()
        except Exception as error:
            print("Failed to get record from MySQL table: {}".format(error))
        finally:
            if self.connection.is_connected():
                cursor.close()
                self.close()
            return True

    def executequery(self, query, cond):
        """
        Function to get data from query in the Database
        :return:
        """
        try:
            data = None
            cursor = self.connector.cursor()
            cursor.execute(query, cond)
            data = cursor.fetchall()
        except Exception as error:
            print("Failed to get record from MySQL table: {}".format(error))
        finally:
            if self.connection.is_connected():
                cursor.close()
                self.close()
            return data

    def read(self):
        """
        Function to read version of the Database
        :return:
        """
        try:
            cursor = self.connector.cursor()
            # execute SQL query using execute() method.
            cursor.execute("SELECT VERSION()")
            # Fetch a single row using fetchone() method.
            data = cursor.fetchone()
            print("Database version : %s " % data)
        except Exception as error:
            print("Failed to read data from MySQL table: {}".format(error))
        finally:
            if self.connection.is_connected():
                cursor.close()
                self.close()

    def close(self):
        """
            disconnect from server
        """
        try:
            if self.connection.is_connected():
                self.close()
        except Exception as error:
            print("Failed to connect to the database: {}".format(error))
        return True
