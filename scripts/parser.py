from scripts.errors import TaskTypeError


class ReadSaver:
    def __init__(self):
        self._input_file = 'default_1'
        self._output_file = 'default_2'
        self._input_text = 'default_3'
        self._input_path = 'default_4'
        self._output_path = 'default_5'

    @property
    def input_path(self):
        return self._input_path

    @property
    def output_path(self):
        return self._output_path

    @property
    def input_text(self):
        return self._input_text

    @property
    def input_file(self):
        return self._input_file

    @property
    def output_file(self):
        return self._output_file

    @input_path.setter
    def input_path(self, path):
        try:
            x = open(path, 'r')
            x.close()
            self._input_path = path
        except FileNotFoundError:
            raise FileNotFoundError

    @output_path.setter
    def output_path(self, path):
        self._output_path = path

    def Open(self):
        try:
            self._input_file = open(self._input_path, 'r')
            self._output_file = open(self._output_path, 'w')
        except FileNotFoundError:
            raise FileNotFoundError

    def Read(self):
        self._input_text = self._input_file.read()

    def Write(self, sym):
        self._output_file.write(sym)

    def Close(self):
        self._output_file.close()
        self._input_file.close()


class Parser(ReadSaver):
    def __init__(self, readsaver):
        super().__init__()
        self._input_path = readsaver.input_path
        self._output_path = readsaver.output_path
        self._input_text = readsaver.input_text
        self._input_file = readsaver.input_file
        self._output_file = readsaver.input_file

        self._task = 'default_1'
        self._cyp_type = 'default_3'
        self._key = 'default_4'

    @property
    def task(self):
        return self._task

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

    @cyp_type.setter
    def cyp_type(self, a):
        if a.lower() not in {'ca', 'vi', 've'} and self.task.lower() in {'e', 'd'}:
            raise TaskTypeError('wrong cypher type')
        self._cyp_type = a.lower()

    @key.setter
    def key(self, a):
        if self.cyp_type.lower() == 'ca' and not a.isdigit():
            raise TaskTypeError('wrong key type')
        self._key = a
