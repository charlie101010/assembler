import sys
import parser
import code

name = sys.argv[1][:-4]
name = name + ".hack"
print name
f = open(sys.argv[1],"r")
contents = f.readlines()
f.closed
p = parser.Parser()
trimmed_instructions = p.read_in(contents)
c  = code.Code();
output = c.convert_to_binary(trimmed_instructions)
with open(name, 'a') as the_file:
    the_file.write(str(output))
print output

