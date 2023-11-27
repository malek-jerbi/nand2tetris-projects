// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Mult.asm

// Multiplies R0 and R1 and stores the result in R2.
// Assumes that R0 >= 0, R1 >= 0, and R0 * R1 < 32768.
// (R0, R1, R2 refer to RAM[0], RAM[1], and RAM[2], respectively.)

//// Replace this comment with your code.
    

    @R0
    D=M
    @zero
    D;JEQ

    @first
    M=D

    @R1
    D=M

    @zero
    D;JEQ

    @temp
    M=D
    
(loop)    
    @end
    D-1;JEQ

    @first
    D=M
    @R0
    M=M+D
    
    @temp
    D=M
    D=D-1
    M=D

    @loop
    0;JMP
    
(end)
    @R0
    D=M
    @R2
    M=D

(exit)
    @exit
    0;JMP

(zero)
    @R2
    M=0

(secondexit)
    @secondexit
    0;JMP
