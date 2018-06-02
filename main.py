from sys import argv
from lexer import tokenize
from parser import parse
from util import bin_to_hex


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
                
                for token in tokens:
                    print(token)
                
                try:
                    for token in tokens:
                        print(parse(token) + " " + bin_to_hex(parse(token), 8))
                except Exception as exc:
                    print(exc)
        except:
            print("Error! Failed to open " + filename + "!")
            exit(1)

main()
