class ValidatorException(Exception):
    def __init__(self, message_list = "Validation error: "):
        self._message_list = message_list

    def get_messsage(self):
        return self._message_list

    def __str__(self):
        result = ""
        for message in self.get_messsage():
            result += message
            result += "\n"
        return result
    