// Program in HACK assembly language that takes the input of
// Ram[0] and multiplies by Ram[1]

@R0
D=M
@x
M+D
@R1
D = M -1
@y
M = D
@z
M = 0

(LOOP)
@z
D = M
@y
D = D - M
@END
D;JGT

@x
M = M + M
@z
M = M +1
@LOOP
0;JMP

(END)
@END
0;JMP