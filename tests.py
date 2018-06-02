from parser import try_translate_symbolic_register

def reg_test():
    regs = ['$zero', '$at', '$v0', '$v1',
            '$a0', '$a1', '$a3', '$t0', '$t1',
            '$t7', '$t8', '$t9', '$s0', '$s1' ,'$s7',
            '$k0', '$k1', '$gp', '$sp', '$fp', '$ra']
    for reg in regs:
        print(reg + " -> " + try_translate_symbolic_register(reg))
