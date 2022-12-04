#!/usr/bin/python
class MockCursor:
    def execute(self, query, cond=""):
        print("mock execute query:{} cond={}".format(query, cond))
        return query

    def close(self):
        print("Calling Mock cursor close")
        return True

    def fetchall(self):
        return ["fetch1", "fetch2"]

    def fetchone(self):
        return "fetch1"


class MockConnector:
    def __init__(self):
        self.cursor_obj = MockCursor()
        print("Creating Mock Connector")

    def cursor(self):
        return self.cursor_obj

    def commit(self):
        """mock commit function"""
        return True

    def is_connected(self):
        return True

    def close(self):
        print("Closing Mock Connector")
        return True
