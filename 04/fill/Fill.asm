// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Fill.asm

// Runs an infinite loop that listens to the keyboard input.
// When a key is pressed (any key), the program blackens the screen
// by writing 'black' in every pixel;
// the screen should remain fully black as long as the key is pressed. 
// When no key is pressed, the program clears the screen by writing
// 'white' in every pixel;
// the screen should remain fully clear as long as no key is pressed.


@color    // declare color variable
M=0      // by default is white

(LOOP)

  @SCREEN
  D=A
  @address
  M=D     

  @KBD  
  D=M
  @BLACK
  D;JGT   
  
  @color
  M=0    
  @CHANGE_COLOR
  0;JMP    
  
  (BLACK)
    @color
    M=-1    

  (CHANGE_COLOR)
    @color
    D=M
    @address
    A=M         
    M=D       
    
    @address
    M=M+1
    D=M
        
    @24576
    D=D-A
    @CHANGE_COLOR
    D;JLT

@LOOP
0;JMP 