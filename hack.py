from parser import Parser
import string


class HackCaesar(Parser):
    def __init__(self, task='default_1', path='default_2', cyp_type='ca', key='default_4'):
        super().__init__()
        self._task = task
        self._path = path
        self._cyp_type = cyp_type
        self._key = key
        self._typicaldistr = ('e', 't', 'i', 'o', 'n', 's', 'r', 'h', 'l', 'd', 'c', 'u', 'm', 'f', 'p', 'g', 'w', 'y', 'b'
                              'v', 'k', 'x', 'j', 'q', 'z',
                              '!', '"', '#', '$', '%', '&', '\'', '(', ')', '*', '+', ',', '-', '.', '/',
                              '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
                              ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '.', '~')


        tmp = [0] * 127
        with open(path, encoding='utf-8') as file:
            text = file.read().lower()
            for symb in text:
                if 33 <= ord(symb) <= 125:
                    tmp[ord(symb)] += 1

        tmp_dict = dict()
        for i in range(33, 126):
            if chr(i).lower() == chr(i):
                tmp_dict[chr(i)] = tmp[i]

        self._freq = {k: v for k, v in sorted(tmp_dict.items(), key=lambda v: v[1], reverse=True)}
        self._func = {k: v for k, v in zip(self.freq.keys(), self._typicaldistr)}

    @property
    def freq(self):
        return self._freq

    def hack(self):
        file = open('hacked.txt', 'w')
        source = open(self._path, 'r')
        text = source.read().lower()
        for symb in text:
            if 33 <= ord(symb) <= 125:
                file.write(self._func[symb])
        source.close()
        file.close()
