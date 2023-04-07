from parser import Parser


class Caesar(Parser):
    def __init__(self, task='default_1', path='default_2', cyp_type='ca', key='default_4'):
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
        if self._cyp_type.lower() == 'ca':
            for k in range(33, 126):
                if k - int(self._key) < 0:
                    self._alphabet.update({chr(k): chr((k - int(self._key)) + 126)})
                else:
                    self._alphabet.update({chr(k): chr(k - int(self._key))})

    def encrypt_alphabet(self):
        if self._cyp_type.lower() == 'ca':
            for k in range(33, 126):
                if k + int(self._key) > 125:
                    self._alphabet.update({chr(k): chr((k + int(self._key)) % 126 + 33)})
                else:
                    self._alphabet.update({chr(k): chr(k + int(self._key))})

    def encrypt_message(self):
        f = open(self._path, 'r')
        w = open('output_ca_en.txt', 'w')
        self.encrypt_alphabet()
        for sym in f.read():
            if ord(sym) > 125 or ord(sym) < 33:
                w.write(sym)
            else:
                w.write(self._alphabet[sym])
        f.close()
        w.close()
        return w

    def decrypt_message(self):
        f = open(self._path, 'r')
        w = open('output_ca_de.txt', 'w')
        self.decrypt_alphabet()
        for sym in f.read():
            if ord(sym) > 125 or ord(sym) < 33:
                w.write(sym)
            else:
                w.write(self._alphabet[sym])
        f.close()
        w.close()
        return w


class Vigenere(Parser):
    def __init__(self, task='default_1', path='default_2', cyp_type='Vi', key='default_4'):
        super().__init__()
        self._task = task
        self._path = path
        self._cyp_type = cyp_type
        self._key = key
        self._edited_key = ''
        f = open(self.path, 'r')
        fin_len = len(f.read().replace(' ', ''))
        bas_len = len(self._key)
        self._edited_key = self._key * (fin_len // bas_len)
        for i in range(fin_len % bas_len):
            self._edited_key += self._key[i]
        f.close()

    def encrypt_message(self):
        f = open(self._path, 'r')
        w = open('output_vi_en.txt', 'w')
        cnt = 0
        for sym in f.read():
            if ord(sym) > 125 or ord(sym) < 33:
                w.write(sym)
            else:
                new_idx = (ord(sym) - 33 + ord(self._edited_key[cnt]) - 33) % 93 + 33
                w.write(chr(new_idx))
                cnt += 1
        f.close()
        w.close()
        return w

    def decrypt_message(self):
        f = open(self._path, 'r')
        w = open('output_vi_de.txt', 'w')
        cnt = 0
        for sym in f.read():
            if ord(sym) > 125 or ord(sym) < 33:
                w.write(sym)
            else:
                new_idx = ((ord(sym) - 33) - (ord(self._edited_key[cnt]) - 33)) % 93 + 33
                w.write(chr(new_idx))
                cnt += 1
        f.close()
        w.close()
        return w


class Vernam(Parser):
    def __init__(self, task='default_1', path='default_2', cyp_type='Vi', key='default_4'):
        super().__init__()
        self._task = task
        self._path = path
        self._cyp_type = cyp_type
        self._key = key
        self._edited_key = ''
        f = open(self.path, 'r')
        fin_len = len(f.read().replace(' ', ''))
        bas_len = len(self._key)
        self._edited_key = self._key * (fin_len // bas_len)
        for i in range(fin_len % bas_len):
            self._edited_key += self._key[i]
        f.close()

    def encrypt_message(self):
        f = open(self._path, 'r')
        w = open('output_ve_en.txt', 'w')
        cnt = 0
        for sym in f.read():
            if ord(sym) > 125 or ord(sym) < 33:
                w.write(sym)
            else:
                new_idx = ((ord(sym) - 33) + (ord(self._edited_key[cnt]) - 33)) % 93 + 33
                w.write(chr(new_idx))
                cnt += 1
        f.close()
        w.close()
        return w

    def decrypt_message(self):
        f = open(self._path, 'r')
        w = open('output_ve_de.txt', 'w')
        cnt = 0
        for sym in f.read():
            if ord(sym) > 125 or ord(sym) < 33:
                w.write(sym)
            else:
                new_idx = ((ord(sym) - 33) - (ord(self._edited_key[cnt]) - 33)) % 93 + 33
                w.write(chr(new_idx))
                cnt += 1
        f.close()
        w.close()
        return w
