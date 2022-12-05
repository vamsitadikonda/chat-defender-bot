#!/usr/bin/python
import os
import time

import mysql.connector


class DbConnector:
    """
    An object used to connect to a database and perform necessary functions like creating tables, reading and writing
    to the database.
    """

    def __init__(self):
        self.connector = None

    def connect(self):
        """
        Function to open a database connection
        :return:
        """
        retry_count = 10
        while retry_count > 0 and self.connector is None:
            try:
                self.connector = mysql.connector.connect(
                    host=os.getenv("DB_HOST"),
                    port=int(os.getenv("DB_PORT")),
                    user=os.getenv("DB_USER"),
                    password=os.getenv("DB_PASSWORD"),
                )

            except Exception as error:
                print(
                    "Failed to connect to the database: {} retry count:{}".format(
                        error, retry_count
                    )
                )
            finally:
                time.sleep(10)
                retry_count -= 1

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
            cursor.execute(
                "CREATE TABLE discorddb.pwords (server_name NVARCHAR(255), word NVARCHAR(255))"
            )
            cursor.execute(
                "CREATE TABLE discorddb.user_activity (user_id NVARCHAR(255), server_name NVARCHAR(255), offense_count INT DEFAULT 0, "
                "apology_count INT DEFAULT 0, is_banned TINYINT DEFAULT 0)"
            )
            print("Created tables for the database")
            self.connector.commit()
            print("Commited the db changes")

            print("Inserted records in the database")
            self.connector.commit()

        except Exception as error:
            print("Failed to get record from MySQL table: {}".format(error))
        finally:
            cursor.close()
            return True

    def executequery(self, query, cond):
        """
        Function to get data from query in the database
        :return:
        """
        data = None
        try:
            cursor = self.connector.cursor()
            cursor.execute(query, cond)
            data = cursor.fetchall()
        except Exception as error:
            print("Failed to get record from MySQL table: {}".format(error))
        finally:
            cursor.close()
            return data

    def close(self):
        """
        Disconnect from database server
        """
        try:
            if self.connector.is_connected():
                self.connector.close()
        except Exception as error:
            print("Failed to connect to the database: {}".format(error))
        return True
