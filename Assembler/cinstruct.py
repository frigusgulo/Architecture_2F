"""
Hack Assembler.
Written for CS 300 "Computer Architecture"
Written by Franklyn Dunbar, Wit Sampson,
and Justin Bancale

HOW TO USE:

from terminal:

python cinstruct.py "Filename.asm" 
"""

#!/usr/bin/env python3
import sys
import re


dest = {
  "null": "000",
  "M": "001",
  "D": "010",
  "MD": "011",
  "A": "100",
  "AM": "101",
  "AD": "110",
  "AMD": "111"
}

jump = {
  "null": "000",
  "JGT": "001",
  "JEQ": "010",
  "JGE": "011",
  "JLT": "100",
  "JNE": "101",
  "JLE": "110",
  "JMP": "111"
}

comp_nota = {
  "0": "101010",
  "1": "111111",
  "-1": "111010",
  "D": "001100",
  "A": "110000",
  "!D": "001101",
  "!A": "110001",
  "-D": "001111",
  "-A": "110011",
  "D+1": "011111",
  "A+1": "110111",
  "D-1": "001110",
  "A-1": "110010",
  "D+A": "000010",
  "A+D": "000010",
  "D-A": "010011",
  "A-D": "000111",
  "D&A": "000000",
  "A&D": "000000",
  "D|A": "010101",
  "A|D": "010101"

}

comp_a = {
  "M": "110000",
  "!M": "110001",
  "-M": "110011",
  "M+1": "110111",
  "M-1": "110010",
  "D+M": "000010",
  "M+D": "000010",
  "D-M": "010011",
  "M-D": "000111",
  "D&M": "000000",
  "M&D": "000000",
  "D|M": "010101",
  "M|D": "010101"
}

def_add = {
  "SP": "0",
  "LCL": "1",
  "ARG": "2",
  "THIS": "3",
  "THAT": "4",
  "R0": "0",
  "R1": "1",
  "R2": "2",
  "R3": "3",
  "R4": "4",
  "R5": "5",
  "R6": "6",
  "R7": "7",
  "R8": "8",
  "R9": "9",
  "R10": "10",
  "R11": "11",
  "R12": "12",
  "R13": "13",
  "R14": "14",
  "R15": "15",
  "SCREEN": "16384",
  "KBD": "24567"
}

class Assembler(object):
  prognextadd = 0
  memnextadd = 16
  code_addr = {}
  newvars = {}
  assemblycode = []

  def __init__(self, object):
    for line in open(object, 'r'):
      if line.strip():
      	if not line.startswith("//"):
          lineboi1 = line.replace(" ", "").replace("\n","")
          self.assemblycode.append(lineboi1)
    
  def assemble(self):
    output = open("output.txt", "w") 
    for line in self.assemblycode: 
      if not line.startswith("//"):
        if not line.isspace():
          splitboi = line.split("//")[0]
          self.gen_code_line_addr(splitboi)
          self.gen_code(splitboi,output)
    output.close()
 
  @classmethod
  def gen_code_line_addr(self,line):
    global code_addr
    global prognextadd
    lineboi = re.split('(\(|\)|=|;|@)', line)
    
    if lineboi[1] == '(':
      if lineboi[2].isdigit():
        return
    if lineboi[2] not in self.code_addr:
      self.code_addr[lineboi[2]] = self.prognextadd

    self.prognextadd += 1
  
 
    
  @classmethod
  def gen_code(self,line,output):
    global memnextadd
    global code_addr 
    lineboi = re.split('(\(|\)|=|;|@)', line)
    if lineboi[1] == '(':
      return
    if lineboi[1] == '=':
      if lineboi[2] in comp_a:
        a = '1'
        output.write('111' + a + comp_a[lineboi[2]] + dest[lineboi[0]] + '000')
      else :
        a = '0'
        output.write('111' + a + comp_nota[lineboi[2]] + dest[lineboi[0]] + '000')
      output.write('\n')
      return
    if lineboi[1] == ';':
        if lineboi[1] in comp_a:
          output.write('111' + '0' + comp_a[lineboi[0]] + '000' + jump[lineboi[2]])
        else:
          output.write('111' + '0' + comp_nota[lineboi[0]] + '000' + jump[lineboi[2]])
        output.write('\n')
        return
    if lineboi[1] == '@':
      if lineboi[2].isdigit():
        output.write('0' + format(int(lineboi[2]), '015b'))
        output.write('\n')
        return
      if lineboi[2] in self.code_addr:
        output.write('0' + format(self.code_addr[lineboi[2]], '015b'))
        output.write('\n')
        return
      if lineboi[2] in def_add:
        output.write('0' + format(def_add[lineboi[2]], '015b'))
        output.write('\n')
        return
      if lineboi[2] in self.newvars:
        output.write('0' + format(newvars[lineboi[2]], '015b'))
        output.write('\n')
        return
      self.newvars[lineboi[2]] = self.memnextadd
      output.write('0' + format(self.memnextadd, '015b'))
      output.write('\n')
      self.memnextadd += 1
      return 
    else :
      return

if __name__ == "__main__":
  assembler = Assembler(sys.argv[1])
  assembler.assemble()# run our code