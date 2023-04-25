class ArgsNumError(Exception):
    def __init__(self, text):
        self.txt = text


class TaskTypeError(Exception):
    def __init__(self, text):
        self.txt = text
