from . import Checker
import os
import pickle


class BullyChecker(Checker):
    def __init__(self):
        self.use_gpu = bool(os.getenv("USE_GPU", False))
        self.model = None
        self.load_model()

    def load_model(self):
        filename = './data/toxic_model.sav'
        self.model = pickle.load(open(filename, 'rb'))

    def check_message(self, msg: str):
        """
        Function to check if a message has profane words
        :param msg: Message String
        :return: Boolean
        """
        pre_process_msg = self.pre_process(msg)
        return self.model.predict(pre_process_msg)
