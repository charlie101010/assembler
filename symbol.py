class Symbol(object):

	def __init__(self):

		self.symbol_table = {
		'RO':0,
		'R1':1,
		'R2':2,
		'R3':3,
		'R4':4,
		'R5':5,
		'R6':6,
		'R7':7,
		'R8':8,
		'R9':9,
		'R1O':10,
		'R11':11,
		'R12':12,
		'R13':13,
		'R14':14,
		'R15':15,
		'SCREEN':16384,
		'KBD':24576,
		'SP':0,
		'LCL':1,
		'ARG':2,
		'THIS':3,
		'THAT':4

		}


	def check_table(self, key):
		if key in self.symbol_table:
			return True
		else:
			return False



	def populate_table(self, instructions):
		line_count = 0
		next_available = 16
		for line in instructions:
			if line[0]=='(':
				line=line[1:-1]
				self.symbol_table[line] = line_count+1
			elif line[0]=='@':
				line = line[1:]
				line_count+=1
				if not self.check_table(line):
					self.symbol_table[line] = next_available
					next_available+=1
			else:
				line_count+=1
		print self.symbol_table


	def replace_symbols(self, instructions):
		no_symbols = []
		self.populate_table(instructions)
		for line in instructions:
			if line[0]=='@':
				isDigit = line[1].isdigit()
				if isDigit == False:
					line = line[1:]
					output = self.symbol_table[line]
					addvalue = '@' + str(output)
					no_symbols.append(addvalue)
				else:
					no_symbols.append(line)
			else:
				no_symbols.append(line)
		print no_symbols
		return no_symbols


