from parser import Parser

FREQ = ('e', 't', 'i', 'o', 'n', 's', 'r', 'h', 'l', 'd', 'c', 'u', 'm', 'f', 'p', 'g', 'w', 'y', 'b'
                                                                                                  'v', 'k', 'x', 'j',
        'q', 'z',
        '!', '"', '#', '$', '%', '&', '\'', '(', ')', '*', '+', ',', '-', '.', '/',
        '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
        ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '.', '~')


class HackCaesar(Parser):
    def __init__(self, pars, readsaver):
        super().__init__(readsaver)
        self._input_path = readsaver.input_path
        self._output_path = readsaver.output_path
        self._input_text = readsaver.input_text
        self._input_file = readsaver.input_file
        self._output_file = readsaver.input_file

        self._task = pars.task
        self._cyp_type = pars.cyp_type
        self._key = pars.key

        self._typicaldistr = FREQ
        self._freq = dict()
        self._func = dict()

    def make_freq(self):
        self.Open()
        self.Read()
        text = self.input_text.lower()
        tmp = [0] * 127

        for symb in text:
            if 33 <= ord(symb) <= 125:
                tmp[ord(symb)] += 1

        tmp_dict = dict()
        for i in range(33, 126):
            if chr(i).lower() == chr(i):
                tmp_dict[chr(i)] = tmp[i]

        self._freq = {k: v for k, v in sorted(tmp_dict.items(), key=lambda v: v[1], reverse=True)}
        self.Close()

    def make_func(self):
        self._func = {k: v for k, v in zip(self.freq.keys(), self._typicaldistr)}


    @property
    def freq(self):
        return self._freq

    def hack(self):
        self.make_freq()
        self.make_func()
        self.Open()
        self.Read()
        text = self.input_text.lower()
        for symb in text:
            if 33 <= ord(symb) <= 125:
                self.Write(self._func[symb])
        self.Close()
