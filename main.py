import sys
from parser import Parser
from errors import ArgsNumError, TaskTypeError
from scramblers import Caesar, Vigenere, Vernam
from hack import HackCaesar

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
    elif inpt.task == 'e' or inpt.task == 'd':
        inpt.cyp_type = sys.argv[3]
        inpt.key = sys.argv[4]
except ArgsNumError as mr:
    print(mr)
except TaskTypeError as mr:
    print(mr)
except FileNotFoundError:
    print('wrong path')
else:
    if inpt.cyp_type == 'ca':
        encr = Caesar(inpt.task, inpt.path, inpt.cyp_type, inpt.key)
    elif inpt.cyp_type == 'vi':
        encr = Vigenere(inpt.task, inpt.path, inpt.cyp_type, inpt.key)
    elif inpt.cyp_type == 've':
        encr = Vernam(inpt.task, inpt.path, inpt.cyp_type, inpt.key)

    if inpt.task == 'd':
        encr.decrypt_message()
    elif inpt.task == 'e':
        encr.encrypt_message()
    elif inpt.task == 'h':
        t = HackCaesar(inpt.task, inpt.path, inpt.cyp_type, inpt.key)
        t.hack()