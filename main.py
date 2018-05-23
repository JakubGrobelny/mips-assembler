from sys import argv
from lexer import tokenize


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
        except:
            print("Error! Failed to open " + filename + "!")
            exit(1)
    
    tokens = tokenize(lines)

main()
