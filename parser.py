from instructions import *

def parse(tokens : list):
    for token in tokens:
        if token[0] in instructions:
            data = instructions[tokens[0]]
            type = data[0][0]
            pattern = data[1:]
            if not check_pattern(pattern, token):
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
                raise Exception("Assembler error! Invalid instruction type!")
        else:
            raise Exception("Error! Invalid instruction " + tokens[0])

def  

symbolic_registers = [
    's',
    'd',
    't'
]

def is_register(token : str):
    
def check_pattern(pattern : list, instruction : list):
    if len(pattern) != len(instruction[1:]):
        return False
    for operand in zip(pattern, instruction[1:]):
        correct = operand[0]
        given   = operand[1]
        if correct in symbolic_registers:
            return is_register(given)
        elif 