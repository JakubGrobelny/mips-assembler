REG_BITS = 5
EMPTY_REG = '0' * REG_BITS

# Note: all inputs have been verified before running this function.
def encode(pattern : list, instruction : list, type : str):
    if type == 'R':
        opcode = '0' * 6 # opcode of every R instruction is 000000
        registers = {
            's' : EMPTY_REG,
            't' : EMPTY_REG,
            'd' : EMPTY_REG
        }
        shamt  = '0' * 5
        funct  = pattern[0][1]
        
        for op in zip(pattern[1:], instruction[1:]):
            if op[0] in registers:
                registers[op[0]] = encode_register(op[1])
            # Else operand is a number (shamt)
            else:
                shamt = fix_bin_length(dec_to_bin(op[1]), 5)
        
        encoded_registers = ''
        for reg in registers.keys():
            encoded_registers += registers[reg]
        
        result = opcode + encoded_registers + shamt + funct
        return result
    
    if type == 'I':
        opcode = pattern[0][1]
        registers = {
            's' : EMPTY_REG,
            't' : EMPTY_REG
        }
        immediate = 16 * '0'
        
        for op in zip(pattern[1:], instruction[1:]):
            if op[0] in registers:
                registers[op[0]] = encode_register(op[1])
            # Else operand is a number (immediate)
            else:
                immediate = dec_to_bin(op[1], 16)
        
        encoded_registers = ''
        for reg in registers.keys():
            encoded_registers += registers[reg]
            
        result = opcode + encoded_registers + immediate
        return result
        
    else:
        raise Exception("Assembler error! Invalid instruction type: " + type)


def fix_bin_length(binary : str, length : int) -> str:
    if len(binary) != length:
        zero_count = length - len(binary)
        if zero_count < 0:
            raise Exception("Assembler error! Invalid binary number length " + binary)
        return zero_count * '0' + binary
    else:
        return binary


def dec_to_bin(num : int, length : int) -> str:
    if num > 0:
        return fix_bin_length(str(bin(num))[2:], length)
    else:
        positive = str(bin(-num))[2:]
        negated = '1' * (length - len(positive))
        for c in positive:
            negated += '1' if c == '0' else '0'
        num = int(negated, 2) + 1
        return str(bin(num))[2:]


def encode_register(reg : str) -> str:
    num = int(reg[1:], 10)
    return fix_bin_length(str(bin(num))[2:], REG_BITS) 