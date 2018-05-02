import sys
import parser
import code
import symbol

name = sys.argv[1][:-4]
name = name + ".hack"
print name
f = open(sys.argv[1],"r")
contents = f.readlines()
f.closed
p = parser.Parser()
trimmed_instructions = p.read_in(contents)
s = symbol.Symbol()
symbols_replaced = s.replace_symbols(trimmed_instructions)
c  = code.Code();
output = c.convert_to_binary(symbols_replaced)
with open(name, 'w') as the_file:
    the_file.write(str(output))


