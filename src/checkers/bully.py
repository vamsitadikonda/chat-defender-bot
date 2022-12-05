#!/usr/bin/python
from . import Checker
import os
import pickle
from . import Checker


class BullyChecker(Checker):
    def __init__(self):
        self.use_gpu = bool(os.getenv("USE_GPU", False))
        # model threshold
        print(f"The use gpu flag is: {self.use_gpu}")
        self.sensitivity_threshold = 0.8
        self.model = None
        self.load_model()

    def load_model(self):
        """
        Function to load pickle file for ML model
        """
        filename = "./data/toxic_model.sav"
        self.model = pickle.load(open(filename, "rb"))

    def check_message(self, msg: str):
        """
        Function to check if a message has profane words
        :param msg: Message String
        :return: Boolean
        """
        predicts_dict = self.model.predict(msg)

        """
        Function to add profane words to a list and return the same
        """

        def getThreats(d):
            ret = []
            for x in sorted([(predicts_dict[k], k) for k in predicts_dict]):
                if x[0] >= self.sensitivity_threshold:
                    ret.append(x[1])
            return ret

        return getThreats(predicts_dict)
