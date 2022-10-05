from code.checkers import Checker


class BullyChecker(Checker):
    def __init__(self):
        self.model = None

    def pre_process(self, msg):
        # ToDo Add preprocessing
        return msg

    def check_message(self, msg: str):
        """
        Function to check if a message has profane words
        :param msg: Message String
        :return: Boolean
        """
        pre_process_msg = self.pre_process(msg)
        return self.model.predict(pre_process_msg)
