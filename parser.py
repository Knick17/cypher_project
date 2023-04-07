from errors import TaskTypeError


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
        if a.lower() not in {'e', 'd', 'h'}:
            raise TaskTypeError('wrong command type')
        self._task = a.lower()

    @path.setter
    def path(self, a):
        try:
            open(a, 'r')
        except FileNotFoundError:
            raise FileNotFoundError
        self._path = a

    @cyp_type.setter
    def cyp_type(self, a):
        if a.lower() not in {'ca', 'vi', 've'}:
            raise TaskTypeError('wrong cypher type')
        self._cyp_type = a.lower()

    @key.setter
    def key(self, a):
        if self.cyp_type.lower() == 'ca' and not a.isdigit():
            raise TaskTypeError('wrong key type')
        self._key = a
