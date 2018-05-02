

class Parser(object):

	def __init__(self):
		self.name = "parser"

	def read_in(self, code):
		contents_trimmed = [];
		for line in code:
			line = line.partition('//')[0]
	        	line = line.rstrip()
	        	line = line.replace(" ", "")
	        	if len(line) != 0:
	        		contents_trimmed.append(line)
	    	return contents_trimmed

	