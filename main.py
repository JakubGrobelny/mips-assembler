from sys import argv
from lexer import tokenize
from parser import parse
from util import *
from instructions import INSTRUCTION_MAX_LEN


flag_values = {
    'l' : False, # little-endian
}

def parse_flags(flags : list):
    for flag in flags:
        if len(flag) != 2 or flag[0] != '-' or flag[1:] not in flag_values.keys():
            print("Error! Invalid flag " + flag)
            exit(1)
        flag_values[flag[1:]] = True


def main():
    # Input verification.
    if len(argv) < 2:    
        print("Error! Filename not specified!")
        exit(1)
    else:
        filename = argv[1]
        parse_flags(argv[2:])
        try:
            with open(filename, 'r') as file:
                lines = file.read().splitlines()
                tokens = tokenize(lines)
                try:
                    address = 0
                    print(".text")
                    for token in tokens:
                        operand_offset = INSTRUCTION_MAX_LEN - len(token[0])
                        operand_offset = ' ' * operand_offset
                        encoded = bin_to_hex(parse(token), 8)

                        if flag_values['l']:
                            encoded = hex_to_little_endian(encoded)

                        print(dec_int_to_hex(address, 8) 
                              + "    "
                              + encoded
                              + "    "
                              + token[0]
                              + "    " + operand_offset
                              + ','.join(token[1:]))
                        address += 4

                except Exception as exc:
                    print(exc)
        except:
            print("Error! Failed to open " + filename + "!")
            exit(1)

main()
