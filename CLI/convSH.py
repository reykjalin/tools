#!/usr/bin/python
import sys, subprocess, os, re

if len(sys.argv) < 3:
    print('Incorrect usage')
    exit(1)

if not os.path.isfile(sys.argv[1]):
    print('File does not exist')
    exit(1)

od = subprocess.check_output(['/usr/bin/objdump', '-d', sys.argv[1]])

od = od.split('\n')

code = []
rx = re.compile(r'^ ([0-9|a-z]+):(.*)')
for line in od:
    res = rx.match(line)
    if not res is None:
        code.append(res.group(0).split('\t')[1].strip())

shellcode = ' '.join(code)
shellcode = shellcode.replace(' ', '\\x')
shellcode = '\\x' + shellcode


with open(sys.argv[2], 'w') as codeFile:
    codeFile.write('#include <stdio.h>\n\n')
    codeFile.write('char code[] = "' + shellcode + '";\n\n')
    codeFile.write('int main() {\n')
    codeFile.write('    int (*func)();\n')
    codeFile.write('    func = (int (*)()) code;\n')
    codeFile.write('    (int)(*func)();\n')
    codeFile.write('    return 0;\n')
    codeFile.write('}\n')
