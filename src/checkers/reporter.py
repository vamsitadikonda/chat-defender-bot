#!/usr/bin/python
from . import Checker


class ReportChecker(Checker):
    def check_message(self, msg:str):
        return msg.startswith('!report')

    def parse_message(self, msg):
        return msg.split(" ")[1], msg.split(" ")[2]

