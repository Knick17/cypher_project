import sys
from parser import Parser, ReadSaver
from errors import ArgsNumError, TaskTypeError
from scramblers import Caesar, Vigenere, Vernam
from hack import HackCaesar

task = ''
path = ''
outpath = ''
cyp_type = ''
key = ''

try:
    if len(sys.argv) == 1:
        raise ArgsNumError('0 args, at least 2 needed')
    elif len(sys.argv) == 2:
        raise ArgsNumError('1 arg, at least 2 needed')
    elif len(sys.argv) >= 3:
        task = sys.argv[1]
        path = sys.argv[2]

    rs = ReadSaver()
    rs.input_path = path

    if task == 'h':
        outpath = 'hacked.txt'
    elif (task == 'e' or task == 'd') and len(sys.argv) < 5:
        raise ArgsNumError('2 or 3 args, at least 4 needed')
    elif task == 'e' or task == 'd':
        cyp_type = sys.argv[3]
        key = sys.argv[4]

    if task == 'h':
        outpath = 'hacked.txt'
    if task == 'e' and cyp_type == 'ca':
        outpath = 'output_caesar_encrypted.txt'
    elif task == 'd' and cyp_type == 'ca':
        outpath = 'output_caesar_decrypted.txt'
    elif task == 'e' and cyp_type == 'vi':
        outpath = 'output_vigenere_encrypted.txt'
    elif task == 'd' and cyp_type == 'vi':
        outpath = 'output_vigenere_decrypted.txt'
    elif task == 'e' and cyp_type == 've':
        outpath = 'output_vernam_encrypted.txt'
    elif task == 'd' and cyp_type == 've':
        outpath = 'output_vernam_decrypted.txt'

    rs.output_path = outpath

    inpt = Parser(rs)

    inpt.task = task
    inpt.cyp_type = cyp_type
    inpt.key = key

except ArgsNumError as mr:
    print(mr)
except TaskTypeError as mr:
    print(mr)
except FileNotFoundError:
    print('wrong path')
else:
    if inpt.cyp_type == 'ca' and inpt.task == 'd':
        encr = Caesar(inpt, rs)
        encr.decrypt_message()
    elif inpt.cyp_type == 'ca' and inpt.task == 'e':
        encr = Caesar(inpt, rs)
        encr.encrypt_message()
        print(encr.alphabet)
    elif inpt.cyp_type == 'vi' and inpt.task == 'd':
        encr = Vigenere(inpt, rs)
        encr.decrypt_message()
    elif inpt.cyp_type == 'vi' and inpt.task == 'e':
        encr = Vigenere(inpt, rs)
        encr.encrypt_message()
    elif inpt.cyp_type == 've' and inpt.task == 'd':
        encr = Vernam(inpt, rs)
        encr.decrypt_message()
    elif inpt.cyp_type == 've' and inpt.task == 'e':
        encr = Vernam(inpt, rs)
        encr.encrypt_message()
    elif inpt.task == 'h':
        t = HackCaesar(inpt, rs)
        t.hack()
