#!/usr/bin/python
"""
Checkers Module:
This module contains all the checks that can be done after parsing a message.
The module contains multiple classes each targeting an individual function.
The classes are organized based on the broad area they are responsible for.
The main functions are Bully, Apology and Profanity with scope to add more.
"""


class Checker:
    """
    An Abstract Class for all Checker Classes. It is inherited by all the Checker objects
    """

    def check_message(self, msg: str):
        """
        Function to parse the message and check for a trait in the message.
        :param msg:
        :return:
        """
        NotImplementedError
