from instructions import *
from encoder import encode


# Parses a single line of assembly program.
def parse(tokens: list):
    if tokens[0] in instructions:
        data = instructions[tokens[0]]
        type = data[0][0]
        pattern = data[1:]

        # Parsing integer literals
        tokens = list(map(try_parse_number, tokens))

        # Removing symbolic register names
        tokens = list(map(try_translate_symbolic_register, tokens))

        if not does_match_pattern(pattern, tokens):
            raise Exception("Error! Invalid instruction operands! " + tokens[0]
                            + ": expected " + ', '.join(pattern) + ", given "
                            + ', '.join(tokens[1:]))

        return encode(data, tokens, type)

    else:
        raise Exception("Error! Invalid instruction " + tokens[0])


def try_parse_number(number: str):
    try:
        return parse_integer(number)
    except:
        return number


def parse_integer(number: str) -> int:
    if is_decimal(number):
        return int(number, 10)
    elif is_hexadecimal(number):
        return int(number, 16)
    else:
        raise Exception("Error! Invalid integer literal " + number)


def is_decimal(number: str) -> bool:
    try:
        int(number, 10)
        return True
    except:
        return False


def is_hexadecimal(number: str) -> bool:
    if number[:2] != '0x':
        return False
    try:
        int(number, 16)
        return True
    except:
        return False


def does_number_match(pattern: str, number) -> bool:
    type = pattern[0]
    # Extracting the desired size of the constant
    size = int(pattern[1:], 10)

    # Finding the max and min number that can be represented with given number of bits.
    # This only works with signed integers for now:
    max_size = 2 ** size - 1
    min_size = -(2 ** size)

    if pattern[0] == 'i':
        if isinstance(number, int) and max_size >= number >= min_size:
            return True
        else:
            return False
    else:
        raise Exception("Assembler error! Invalid constant type: " + pattern[0])


internal_symbolic_registers = ['s', 'd', 't']


def try_translate_symbolic_register(register):
    if isinstance(register, str) and register[0] == '$':
        if is_decimal(register[1:]) and 0 <= int(register[1:]) < 32:
            return register
        else:
            if register[1:] == "zero":
                return "$0"
            elif register[1:] == "at":
                return "$1"
            elif register[1:] == "gp":
                return "$28"
            elif register[1:] == "sp":
                return "$29"
            elif register[1:] == "fp":
                return "$30"
            elif register[1:] == "ra":
                return "$31"
            elif is_decimal(register[2:]):
                index = int(register[2:])
                name  = register[1]
                if name == 'v' and 0 <= index <= 1:
                    return "$" + str(2 + index)
                if name == 'a' and 0 <= index <= 3:
                    return "$" + str(4 + index)
                if name == 't' and 0 <= index <= 9:
                    if index <= 7:
                        return '$' + str(8 + index)
                    else:
                        return '$' + str(24-8 + index)
                if name == 's' and 0 <= index <= 7:
                    return '$' + str(16 + index)
                if name == 'k' and 0 <= index <= 1:
                    return '$' + str(26 + index)
                else:
                    return register
            else:
                return register
    else:
        return register


def is_register(token: str) -> bool:
    if len(token) < 2 or token[0] != '$':
        return False
    elif 0 <= int(token[1:]) < 32:
        return True
    return False


def does_match_pattern(pattern: list, instruction: list) -> bool:
    if len(pattern) != len(instruction[1:]):
        return False
    for operand in zip(pattern, instruction[1:]):
        correct = operand[0]
        given = operand[1]
        # Operand can be either a register or a numeric constant
        if correct in internal_symbolic_registers:
            return is_register(given)
        else:
            return does_number_match(correct, given)
