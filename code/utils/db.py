import pymysql


class DbConnector:
    def __init__(self):
        self.host = "localhost"
        self.user = "testuser"
        self.password = "test123"
        self.DB = "TESTDB"
        self.connector = None

    def connect(self):
        """
        Function to Open database connection
        :return:
        """
        self.connector = pymysql.connect(self.host, self.user, self.password, self.DB)

    def read(self,):
        cursor = self.connector.cursor()
        # execute SQL query using execute() method.
        cursor.execute("SELECT VERSION()")
        # Fetch a single row using fetchone() method.
        data = cursor.fetchone()
        print("Database version : %s " % data)

    def close(self):
        """
            disconnect from server
        """
        return self.connector.close()