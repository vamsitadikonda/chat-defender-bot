#!/usr/bin/python
from . import Checker


class ReportChecker(Checker):
    def check_message(self, msg: str):
        """
        Function to check if a message starts with report
        :param msg: Message String
        :return: Boolean
        """
        return msg.startswith("!report")

    # parsing the message
    def parse_message(self, msg):
        """
        Function to split the message into two parts
        :param msg: Message String
        :return: string
        """
        return msg.split(" ")[1], msg.split(" ")[2]
