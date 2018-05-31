from instructions import *

def parse(tokens : list):
    for token in tokens:
        if token[0] in instructions:
            data = instructions[tokens[0]]
            type = data[0][0]
            pattern = data[1:]
            if not does_match_pattern(pattern, token):
                raise Exception("Error! Invalid instruction operands! " + token[0]
                                + ": expected " + ', '.join(pattern) + ", given "
                                + ', '.join(token[1:]))
            if type == 'R':
                opcode = '0' * 6
                funct  = data[0][1]
            elif type == 'I':
                opcode = data[0][1]
                funct  = '0' * 6
            else:
                raise Exception("Assembler error! Invalid instruction type: " + type)
        else:
            raise Exception("Error! Invalid instruction " + tokens[0])

internal_symbolic_registers = [
    's',
    'd',
    't'
]

def is_decimal(number : str) -> bool:
    
    
def is_hexadecimal(number : str) -> bool:
    

def match_number(pattern : str, number : str) -> bool:
    type = pattern[0]
    size = int(pattern[1:], 10)
    max_size = 2**size - 1
    if pattern[0] == 'i':
        # TODO: map parse_number to token list before checking pattern
    else:
        raise Exception("Assembler error! Invalid constant type: " + pattern[0])

def is_register(token : str) -> bool:
    
    
def does_match_pattern(pattern : list, instruction : list) -> bool:
    if len(pattern) != len(instruction[1:]):
        return False
    for operand in zip(pattern, instruction[1:]):
        correct = operand[0]
        given   = operand[1]
        # Operand can be either a register or a numeric constant
        if correct in internal_symbolic_registers:
            return is_register(given)
        else:
            return match_number(correct, given)