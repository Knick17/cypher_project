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
        if self.cyp_type == 'Ca' and not a.isdigit():
            raise TaskTypeError('wrong key type')
        self._key = a


class Caesar(Parser):
    def __init__(self, task='default_1', path='default_2', cyp_type='Ca', key='default_4'):
        super().__init__()
        self._alphabet = dict()
        self._task = task
        self._path = path
        self._cyp_type = cyp_type
        self._key = key

    @property
    def alphabet(self):
        return self._alphabet

    def decrypt_alphabet(self):
        if self._cyp_type == 'Ca':
            for k in range(33, 126):
                if k - int(self._key) < 0:
                    self._alphabet.update({chr(k): chr((k - int(self._key)) + 126)})
                else:
                    self._alphabet.update({chr(k): chr(k - int(self._key))})

    def encrypt_alphabet(self):
        if self._cyp_type == 'Ca':
            for k in range(33, 126):
                if k + int(self._key) > 125:
                    self._alphabet.update({chr(k): chr((k + int(self._key)) % 126 + 33)})
                else:
                    self._alphabet.update({chr(k): chr(k + int(self._key))})


class Vigenere(Parser):
    def __init__(self, task='default_1', path='default_2', cyp_type='Vi', key='default_4'):
        super().__init__()
        self._task = task
        self._path = path
        self._cyp_type = cyp_type
        self._key = key
        self._edited_key = ''
        f = open(self.path, 'r')
        ln = len(f.read().replace(' ', ''))
        for i in range(ln):
            self._edited_key += self._key[i % len(self._key)]
        f.close()

    def encrypt_message(self):
        f = open(self._path, 'r')
        w = open('output.txt', 'w')
        cnt = 0
        for sym in f.read():
            if ord(sym) > 125 or ord(sym) < 33:
                w.write(sym)
            else:
                new_idx = ((ord(sym) - 33) + ord(self._edited_key[cnt]) - 33) % 93 + 33
                w.write(chr(new_idx))
                cnt += 1
        f.close()
        w.close()
        return w


inpt = Parser()

try:
    if len(sys.argv) == 1:
        raise ArgsNumError('0 args, at least 2 needed')
    elif len(sys.argv) == 2:
        raise ArgsNumError('1 arg, at least 2 needed')
    inpt.task = sys.argv[1]
    tmp = open(sys.argv[2], 'r')
    tmp.close()
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
    encr = Vigenere(inpt.task, inpt.path, inpt.cyp_type, inpt.key)
    encr.encrypt_message()
    print(inpt.task, inpt.path, inpt.cyp_type, inpt.key)
