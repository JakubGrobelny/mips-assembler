Simplified MIPS assembler v0.0.0.1
Jakub Grobelny, 2018

Usage:

    python3 mipsasm.py «filename» «flags ...»

    Available flags:

        -l – displays encoded instructions using little-endian
            (big-endian by default)
        -s – displays simplified output, without addresses, 
            instructions and operands

    Output is printed using following format:

        «section»
        «address»  «encoded instruction»  «instruction»

Available instructions:

    lui, addi, addiu, slti, sltiu, andi, ori, xori, sll, srl, 
    sra, sllv, srlv, srav, mfhi, mthi, mflo, mtlo, mult, multu, 
    div, divu, add, addu, sub, subu, and, or, xor, nor, slt, sltu

Available operands:

    - registers $0...$31
    - registers $zero, $at, $v0...$v1, $a0...$a3, $t0...$t9, 
                       $s0...$s7, $k0...$k1, $gp, $sp, $fp, $ra
    - decimal integers
    - hexadecimal integers (starting with '0x')

Testing:

    The 'tests' folder contains input files ('.in' extension) and corresponding
    output files ('.out' extension).
    Contents of output files should be equal to the output of the program
    run with '-s' flag.
    Output files have been generated using MARS and following websites:
        https://www.eg.bucknell.edu/~csci320/mips_web/
        http://www.kurtm.net/mipsasm/index.cgi

    'test-all.in' contains every instruction supported by the assembler.
    'test0.in' and 'test1.in' contain tests of every register supported
    by the assembler ($0...$31 and conventional names respectively).
    'test-error.in' contains invalid assembly code that
    should cause the assembler to display proper errors.