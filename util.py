def bin_to_hex(bin : str, length : int) -> str:
    hexadecimal = hex(int(bin, 2))[2:]
    extension = (length - len(hexadecimal)) * '0'
    return (extension + hexadecimal).upper()


def fix_bin_length(binary : str, length : int) -> str:
    if len(binary) != length:
        zero_count = length - len(binary)
        if zero_count < 0:
            raise Exception("Assembler error! Invalid binary number length " + binary)
        return zero_count * '0' + binary
    else:
        return binary


def dec_to_bin(num : int, length : int) -> str:
    if num >= 0:
        return fix_bin_length(str(bin(num))[2:], length)
    else:
        positive = str(bin(-num))[2:]
        negated = '1' * (length - len(positive))
        for c in positive:
            negated += '1' if c == '0' else '0'
        num = int(negated, 2) + 1
        return str(bin(num))[2:]


def dec_int_to_hex(dec : int, length : int) -> str:
    return bin_to_hex(dec_to_bin(dec, 4 * length), length)

def hex_to_little_endian(num : str) -> str:
    little_endian = ''
    if len(num) % 2 != 0:
        num = '0' + num
    for byte in zip(list(num)[0::2], list(num)[1::2]):
        little_endian = byte[0] + byte[1] + little_endian
    return little_endian