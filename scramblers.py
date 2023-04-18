from parser import Parser


class Caesar(Parser):
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

        self._alphabet = dict()

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
        self.encrypt_alphabet()
        self.Open()
        self.Read()
        for sym in self._input_text:
            if ord(sym) > 125 or ord(sym) < 33:
                self.Write(sym)
            else:
                self.Write(self._alphabet[sym])
        self.Close()

    def decrypt_message(self):
        self.decrypt_alphabet()
        self.Open()
        self.Read()
        for sym in self.input_text:
            if ord(sym) > 125 or ord(sym) < 33:
                self.Write(sym)
            else:
                self.Write(self._alphabet[sym])
        self.Close()


class Vigenere(Parser):
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

        self._edited_key = ''

    def make_edited_key(self):
        self.Open()
        self.Read()
        fin_len = len(self.input_text.replace(' ', ''))
        bas_len = len(self._key)
        self._edited_key = self._key * (fin_len // bas_len)
        for i in range(fin_len % bas_len):
            self._edited_key += self._key[i]
        self.Close()

    def encrypt_message(self):
        self.make_edited_key()
        self.Open()
        self.Read()
        cnt = 0
        for sym in self.input_text:
            if ord(sym) > 125 or ord(sym) < 33:
                self.Write(sym)
            else:
                new_idx = (ord(sym) - 33 + ord(self._edited_key[cnt]) - 33) % 93 + 33
                self.Write(chr(new_idx))
                cnt += 1
        self.Close()

    def decrypt_message(self):
        self.make_edited_key()
        self.Open()
        self.Read()
        cnt = 0
        for sym in self.input_text:
            if ord(sym) > 125 or ord(sym) < 33:
                self.Write(sym)
            else:
                new_idx = ((ord(sym) - 33) - (ord(self._edited_key[cnt]) - 33)) % 93 + 33
                self.Write(chr(new_idx))
                cnt += 1
        self.Close()


class Vernam(Parser):
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

        self._edited_key = ''

    def make_edited_key(self):
        self.Open()
        self.Read()
        fin_len = len(self.input_text.replace(' ', ''))
        bas_len = len(self._key)
        self._edited_key = self._key * (fin_len // bas_len)
        for i in range(fin_len % bas_len):
            self._edited_key += self._key[i]
        self.Close()

    def encrypt_message(self):
        self.make_edited_key()
        self.Open()
        self.Read()
        cnt = 0
        for sym in self.input_text:
            if ord(sym) > 125 or ord(sym) < 33:
                self.Write(sym)
            else:
                new_idx = ((ord(sym) - 33) + (ord(self._edited_key[cnt]) - 33)) % 93 + 33
                self.Write(chr(new_idx))
                cnt += 1
        self.Close()

    def decrypt_message(self):
        self.make_edited_key()
        self.Open()
        self.Read()
        cnt = 0
        for sym in self.input_text:
            if ord(sym) > 125 or ord(sym) < 33:
                self.Write(sym)
            else:
                new_idx = ((ord(sym) - 33) - (ord(self._edited_key[cnt]) - 33)) % 93 + 33
                self.Write(chr(new_idx))
                cnt += 1
        self.Close()
