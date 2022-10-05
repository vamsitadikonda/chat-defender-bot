import os
import time

import mysql.connector


class DbConnector:
    def __init__(self):
        self.connector = None

        mycursor = mydb.cursor()
        print("creating data base")
        mycursor.execute("CREATE DATABASE test4")

        # TODO Connect to database, insertData() and close connection

    def connect(self):
        """
        Function to Open database connection
        :return:
        """
        retry = 10
        while retry > 0 and self.connector is None:
            try:
                self.connector = mysql.connector.connect(
                    host=os.getenv("DB_HOST"), port=os.getenv("DB_PORT"),
                    user=os.getenv("DB_USER"), password=os.getenv("DB_PASSWORD"))

            except Exception as error:
                print("Failed to connect to the database: {}".format(error))
            finally:
                time.sleep(20)
                retry -= 1

    def create_tables(self):
        """
        Function to create and insert tables in the database
        :return:
        """
        try:
            cursor = self.connector.cursor()
            cursor.execute("CREATE DATABASE discorddb")
            print("Created database discorddb")
            # Create tables and insert data(if any)
            print("Inserted records in the database")
            self.connector.commit()
        except Exception as error:
            print("Failed to get record from MySQL table: {}".format(error))
        finally:
            cursor.close()
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
            cursor.close()
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
            cursor.close()

    def close(self):
        """
            disconnect from server
        """
        try:
            if self.connection.is_connected():
                self.connector.close()
        except Exception as error:
            print("Failed to connect to the database: {}".format(error))
        return True
