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
        predicts_dict = self.model.predict(msg)

        def getThreats(d):
            ret = []
            for x in sorted([(predicts_dict[k], k) for k in predicts_dict]):
                if x[0] >= 0.6:
                    ret.append(x[1])
            return ret

        return getThreats(predicts_dict)
