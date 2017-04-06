# CLI Tools

### convSH.py  
Usage: `./convSH.py <binary-file> <output-c-code>.c`  
Uses objdump -d to generate shellcode, and uses that shellcode to generate a C source file that can be compiled with gcc to run the shellcode.


### str2hex.py  
Usage: `./str2hex <string>`  
Prints string in hexadecimal
