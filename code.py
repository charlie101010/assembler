
class Code(object):

	def __init__(self):

		self.desttable = {
		'NO': '000',
		'M':'001',
		'D':'010',
		'MD':'011',
		'A':'100',
		'AM':'101',
		'AD':'110',
		'AMD':'111',
		}

		self.jumpy = {
		'NO':'000',
		'JGT':'001',
		'JEQ':'010',
		'JGE':'011',
		'JLT':'100',
		'JNE':'110',
		'JMP':'111',
		}

		self.ctable = {
		'0':'0101010',
		'1':'0111111',
		'-1':'0111010',
		'D':'0001100',
		'A':'0110000',
		'!D':'0001101',
		'!A':'0110001',
		'-D':'0001111',
		'-A':'0110011',
		'D+1':'0011111',
		'A+1':'0110111',
		'D-1':'0001110',
		'A-1':'0110010',
		'D+A':'0000010',
		'D-A':'0010011',
		'A-D':'0000111',
		'D&A':'0000000',
		'D|A':'0010101',
		'M':'1110000',
		'!M':'1110001',
		'-M':'1110011',
		'M+1':'1110111',
		'M-1':'1110010',
		'D+M':'1000010',
		'D-M':'1010011',
		'M-D':'1000111',
		'D&M':'1000000',
		'D|M':'1010101',
		}

		



		

	def instruction_kind(self, line):
		if line[0]=='@':
			return 'A'
		elif line[0]=='(':
			return 'E'
		else:
			return 'C'

	def dest_value(self, subelement):
		return self.desttable[subelement]

	def jumptable(self, subelement):
		return self.jumpy[subelement]

	def control_bits(self, subelement):
		return self.ctable[subelement]



	def c_instruction_parse(self, line):
		if '=' in line:
			line = line.split('=')
			dest = line[0]
			if ';' in line[1]:
				line2=line[1].split(';')
				comp=line2[0]
				jump=line2[1]
				return dest, comp, jump
			else:
				comp=line[1]
				jump='NO'
				return dest, comp, jump
		else:
			dest = 'NO'
			line = line.split(';')
			comp=line[0]
			jump=line[1]
			return dest, comp, jump




	def convert_to_binary(self, instructions):
		binary_values = []
		for line in instructions:
			kind = self.instruction_kind(line)
			if kind == 'A':
				line = int(line[1:])
				line = bin(line)[2:].zfill(16)
				binary_values.append(line)
			elif kind == 'C':
				dest, comp, jump = self.c_instruction_parse(line)
				dest = self.dest_value(dest)
				comp = self.control_bits(comp)
				jump = self.jumptable(jump)
				binary_cvalues = '111' + comp + dest + jump
				binary_values.append(binary_cvalues)
			else:
				binary_values.append("Symbol")
		return binary_values





		

