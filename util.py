def bin_to_hex(bin : str, length : int) -> str:
    hexadecimal = hex(int(bin, 2))[2:]
    extension = (length - len(hexadecimal)) * '0'
    return (extension + hexadecimal).upper()