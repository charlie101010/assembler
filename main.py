import sys
import parser
import code

f = open(sys.argv[1],"r")
contents = f.readlines()
p = parser.Parser()
trimmed_instructions = p.read_in(contents)
c  = code.Code();
output = c.convert_to_binary(trimmed_instructions)
print output

