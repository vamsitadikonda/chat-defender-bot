from . import Checker
from ..utils.db import DbConnector


class ApologyChecker(Checker):
    def __init__(self):
        self.connector = DbConnector()

    def check_user(self, user_id, warning_type):
        """
        Function to check whether a user has any outstanding warnings
        :param user_id:
        :param warning_type:
        :return:
        """
        return True

    def add_warning(self, user_id, warning_type):
        pass

    def add_user(self, user_id):
        pass

    def add_apology(self,user_id):
        pass