"""
Dictionary for an assembler for hack.

"""

dest = {"null": "000", "M": "001", "D": "010", "MD": "011","A":"100","AM":"101","AD":"110","AMD":"111" }

jump = {"null":"000","JGT":"001","JEQ":"010","JGE":"011","JLT":"100","JNE":"101","JLE":"110","JMP":"111"}

comp_nota = {"0":"101010","1":"111111","-1":"111010","D":"001100","A":"110000","!D":"001101","!A":"110001","-D":"001111","-A":"110011",
"D+1":"011111","A+1":"110111","D-1":"001110","A-1":"110010","D+A":"000010","D-A":"010011","A-D":"000111","D&A":"000000","D|A":"010101" }

comp_a = {"M":"110000","!M":"110001","-M":"110011","M+1":"110111","M-1":"110010","D+M":"000010","D-M":"010011","M-D":"000111","D&M":"000000",
"D|M":"010101"}

def_add = {"SP":"0","LCL":"1","ARG":"2","THIS":"3","THAT":"4","R0":"0","R1":"1","R2":"2","R3":"3","R4":"4","R5":"5","R6":"6",
"R7":"7","R8":"8","R9":"9","R10":"10","R11":"11","R12":"12","R13":"13","R14":"14","R15":"15","SCREEN":"16384","KBD":"24567"}


class Assembler(object):
	prognextadd = 0
	memnextadd = 16
	code_addr = {}
	newvars = {}
	assemblycode = []

	def _init_(self,file):
		for line in open(file, 'r'):
            if not line.strip():
            self.assemblycode.append(line.replace(" ",""))

    def assemble(self):
    	for line in self.assemblycode:
    		if not line.startswith("//")
    			gen_code_line_addr(line.split("//")[0])
    			gen_code(line.split("//")[0])



    def gen_code_line_addr(line):
    	global code_addr
    	global prognextadd

    	newline = re.split('(\(|\)|=|;|@)', line)
    	if newline[1] == '('
    		if newline[2].isdigit():
    			return
    		if newline[2] not in code_addr
    			code_addr[newline[2]] = prognextadd

    	prognextadd += 1

   	def gen_code(line):
   
    global memnextadd
   	global code_addr

    newline = re.split('(\(|\)|=|;|@)', line)
    if newline[1] == '(':
        return
    if newline[1] == '=':
        if newline[2] in comp_a :
        	a = '1'
        	print('111' + a + comp_a[newline[2]] + dest[newline[0]] + '000')
        else :
        	a = '0'
        	print('111' + a + comp_nota[newline[2]] + dest[newline[0]] + '000')
        return
    if newline[1] == ';':
        print('111' + '0' + comp_a[newline[0]] + '000' + jump[newline[2]])
        return
    if newline[1] == '@':
        if newline[2].isdigit():
            print('0' + format(int(newline[2]), '015b'))
            return
        if newline[2] in code_addr:
            print('0' + format(code_addr[newline[2]], '015b'))
            return
        if newline[2] in def_add:
            print('0' + format(def_add[newline[2]], '015b'))
            return
        if newline[2] in newvars:
            print('0' + format(newvars[newline[2]], '015b'))
            return
        newvars[newline[2]] = memnextadd
        print('0' + format(memnextadd, '015b'))
        memnextadd += 1
        return
    else:
        return    

if __name__ == "__main__":
    assembler = Assembler(sys.argv[1])
    assembler.assemble() # run our code