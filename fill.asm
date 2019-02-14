// Colton Gerth, Franklyn Dunbar, Justin Bancal
// Assignment for Architecture, U of Montana
// Feb 13 2019

@SCREEN
D=A
@Addres
M = D
@KBD
D= A-D
@n
M = D


(LOOP)      //----Rom loop
@i
M=0
@SCREEN
D=A
@Addres
M = D

@KBD
D = M

  @WHITE    //-----White keyboard !press
  D;JEQ


  @BLACK        //-----Black keyboard press
  D;JNE

  (WHITE)     //Write white
  @Addres
  A=M
  M=0
  A = D + 1
  @Addres
  M=M+1
  @i
  M=M+1
  D=M
  
  @n
  D=M-D     // when i = n D will be 0
  @WHITE
  D;JGT
  @LOOP
  0;JEQ
  
(BLACK)     //Write BlBlack 
  
 
  @Addres
  A=M
  M=-1
  A = D + 1
  @Addres
  M=M+1
  @i
  M=M+1
  D=M
  @n
  D=M-D   // when i = n D will be 0
  @BLACK  
  D;JGT
  @LOOP
  0;JEQ