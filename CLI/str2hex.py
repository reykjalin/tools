#!/usr/bin/python

import sys

if len(sys.argv) < 2:
    print('Incorrect usage')
    exit(1)

for char in sys.argv[1]:
    sys.stdout.write('\\x' + char.encode('hex'))
