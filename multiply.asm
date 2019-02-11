// Program in HACK assembly language that takes the input of
// Ram[0] and multiplies by Ram[1]


@x
M=0
@R1
D=M
@y
M=D
@R3
M=0

(LOOP)
@y
D=M
@END
D;JEQ

@R0
D = M
@R2
M = M + D

@y
M=M-1
@LOOP
0;JMP

(END)
@END
0;JMP
