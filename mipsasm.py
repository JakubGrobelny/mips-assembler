from sys import argv
from lexer import tokenize
from parser import parse
from util import *
from instructions import INSTRUCTION_MAX_LEN

flag_values = {
    'l': False,  # little-endian
    's': False
}


def parse_flags(flags: list):
    for flag in flags:
        if len(flag) != 2 or flag[0] != '-' or flag[1:] not in flag_values.keys():
            print("Error! Invalid flag " + flag)
            exit(1)
        flag_values[flag[1:]] = True


def print_instructions():
    print("Usage: python3 mipsasm.py <filename> <flags> ...")
    print("\nAvaliable flags:")
    print("    -l -- enables little-endian")
    print("    -s -- disables address, instruction and operand printing")


def main():
    # Input verification.
    if len(argv) < 2:
        print("Error! Filename not specified!")
        exit(1)
    else:
        if argv[1] == '-help':
            print_instructions()
            exit(0)
        
        filename = argv[1]
        parse_flags(argv[2:])
        
        try:
            with open(filename, 'r') as file:
                lines = file.read().splitlines()
                tokens = tokenize(lines)
                try:
                    address = 0
                    if not flag_values['s']:
                        print(".text") # section
                    
                    for token in tokens:
                        # Offset used to align operands.
                        operand_offset = INSTRUCTION_MAX_LEN - len(token[0])
                        operand_offset = ' ' * operand_offset
                        
                        # Instruction as a hexadecimal number.
                        encoded = bin_to_hex(parse(token), 8)

                        # -l flag enables little-endian
                        if flag_values['l']:
                            encoded = hex_to_little_endian(encoded)

                        if not flag_values['s']:
                            instruction_info = token[0] + " " \
                                               + operand_offset \
                                               + ','.join(token[1:])
                            print(dec_int_to_hex(address, 8)
                                  + "    " + encoded
                                  + "    " + instruction_info)
                        else:
                            print(encoded)
                        
                        address += 4

                except Exception as exc:
                    print(exc)
        except Exception as exc:
            print("Error! Failed to open " + filename + "!")
            exit(1)


main()
