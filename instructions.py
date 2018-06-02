instructions = {
    "add"   : [['R', '100000'], 'd', 's', 't'],
    "addi"  : [['I', '001000'], 't', 's', 'i16'],
    "addiu" : [['I', '001001'], 't', 's', 'i16'],
    "addu"  : [['R', '100001'], 'd', 's', 't'],
    "and"   : [['R', '100100'], 'd', 's', 't'],
    "andi"  : [['I', '001100'], 't', 's', 'i16'],
    "lui"   : [['I', '001111'], 't', 'i16'],
    "slti"  : [['I', '001010'], 't', 's', 'i16'],
    "sltiu" : [['I', '001011'], 't', 's', 'i16'],
    "ori"   : [['I', '001101'], 't', 's', 'i16'],
    "xori"  : [['I', '001110'], 't', 's', 'i16'],
    "sll"   : [['R', '000000'], 'd', 't', 'i5'],
    "srl"   : [['R', '000010'], 'd', 't', 'i5'],
    "sra"   : [['R', '000011'], 'd', 't', 'i5'],
    "sllv"  : [['R', '000100'], 'd', 't', 's'],
    "srlv"  : [['R', '000110'], 'd', 't', 's'],
    "srav"  : [['R', '000111'], 'd', 't' ,'s'],
    "mfhi"  : [['R', '010000'], 'd'],
    "mthi"  : [['R', '010001'], 's'],
    "mflo"  : [['R', '010010'], 'd'],
    "mtlo"  : [['R', '010011'], 's'],
    "mult"  : [['R', '011000'], 's', 't'],
    "multu" : [['R', '011001'], 's', 't'],
    "div"   : [['R', '011010'], 's', 't'],
    "divu"  : [['R', '011011'], 's', 't'],
    "sub"   : [['R', '100010'], 'd', 's', 't'],
    "subu"  : [['R', '100011'], 'd', 's', 't'],
    "or"    : [['R', '100101'], 'd', 's', 't'],
    "xor"   : [['R', '100110'], 'd', 's', 't'],
    "nor"   : [['R', '100111'], 'd', 's', 't'],
    "slt"   : [['R', '101010'], 'd', 's', 't'],
    "sltu"  : [['R', '101011'], 'd', 's', 't']
}

# used for printing
INSTRUCTION_MAX_LEN = len(max(instructions.keys(), key = len))