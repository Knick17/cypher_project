import sys


class ArgsNumError(Exception):
    def __init__(self, text):
        self.txt = text


class TaskTypeError(Exception):
    def __init__(self, text):
        self.txt = text


class Parser:
    def __init__(self):
        self._task = 'default_1'
        self._path = 'default_2'
        self._cyp_type = 'default_3'
        self._key = 'default_4'

    @property
    def task(self):
        return self._task

    @property
    def path(self):
        return self._path

    @property
    def cyp_type(self):
        return self._cyp_type

    @property
    def key(self):
        return self._key

    @task.setter
    def task(self, a):
        if a not in {'e', 'd', 'h'}:
            raise TaskTypeError('wrong command type')
        self._task = a

    @path.setter
    def path(self, a):
        try:
            open(a, 'r')
        except FileNotFoundError:
            raise FileNotFoundError
        self._path = a

    @cyp_type.setter
    def cyp_type(self, a):
        if a not in {'Ca', 'Vi', 'Ve'}:
            raise TaskTypeError('wrong cypher type')
        self._cyp_type = a

    @key.setter
    def key(self, a):
        if not a.isdigit():
            raise TaskTypeError('wrong key type')
        self._key = a


cyp_type = 'default_3'
key = 'default_4'

inpt = Parser()


try:
    if len(sys.argv) == 1:
        raise ArgsNumError('0 args, at least 2 needed')
    elif len(sys.argv) == 2:
        raise ArgsNumError('1 arg, at least 2 needed')
    inpt.task = sys.argv[1]
    open(sys.argv[2], 'r')
    inpt.path = sys.argv[2]
    if (inpt.task == 'e' or inpt.task == 'd') and len(sys.argv) < 5:
        raise ArgsNumError('2 or 3 args, at least 4 needed')
    inpt.cyp_type = sys.argv[3]
    inpt.key = sys.argv[4]
except ArgsNumError as mr:
    print(mr)
except TaskTypeError as mr:
    print(mr)
except FileNotFoundError:
    print('wrong path')
else:
    print(inpt.task, inpt.path, inpt.cyp_type, inpt.key)
