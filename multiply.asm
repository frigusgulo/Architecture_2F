// Program in HACK assembly language that takes the input of
// Ram[0] and multiplies by Ram[1]

@R0
D=M
@x
M=D
@R1
D=M
@y
M=D

(LOOP)
@y
D=M
@END
D;JEQ

@x
M=M+M
@y
M=M-1
@LOOP
0;JMP

(END)
@END
0;JMP