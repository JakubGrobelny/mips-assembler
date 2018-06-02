from sys import argv
from lexer import tokenize
from parser import parse
from util import *
from instructions import INSTRUCTION_MAX_LEN


def main():
    # Input verification.
    if len(argv) != 2:    
        print("Error! Filename not specified!")
        exit(1)
    else:
        filename = argv[1]
        try:
            with open(filename, 'r') as file:
                lines = file.read().splitlines()
                tokens = tokenize(lines)

                try:
                    address = 0
                    print(".text")
                    for token in tokens:
                        operand_offset = INSTRUCTION_MAX_LEN - len(token[0])
                        operand_offset = 0 if operand_offset < 0 else operand_offset
                        
                        print(dec_int_to_hex(address, 8) 
                              + "    "
                              + bin_to_hex(parse(token), 8)
                              + "    "
                              + token[0]
                              + "    " + (' ' * operand_offset)
                              + ','.join(token[1:]))
                        address += 4

                except Exception as exc:
                    print(exc)
        except:
            print("Error! Failed to open " + filename + "!")
            exit(1)

main()
