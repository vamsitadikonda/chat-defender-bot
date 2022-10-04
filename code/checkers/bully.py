class BullyChecker:
    def __init__(self):
        self.model = None

    def preprocess(self, msg):
        #ToDo Add preprocessing
        return msg

    def checkMessage(self, msg: str):
        """
        Function to check if a message has profane words
        :param msg: Message String
        :return: Boolean
        """
        pre_process_msg = self.preprocess(msg)
        return self.model.predict(pre_process_msg)

