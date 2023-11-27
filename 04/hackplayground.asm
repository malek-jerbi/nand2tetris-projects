// Adds up two numbers
// RAM[2] = RAM[0] + RAM[1]
// Usage: put the values that you wish to add 
//              in RAM[0] and RAM[1]

    @R1
    D=M

    @temp
    M=D

(loop)    
    @end
    D-1;JEQ

    @R0
    D=M
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