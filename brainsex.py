#!/usr/bin/env python
from sys import stdout, stdin, argv

valid = ('.', ',', '[', ']', '<', '>', '+', '-')
code = filter(lambda c: c in valid, open(argv[1]).read())
loop_stack, loop_map = [], {}
for pos, i in enumerate(code):
    if i == '[': loop_stack.append(pos)
    if i == ']':
        entrance = loop_stack.pop()
        loop_map[entrance], loop_map[pos] = pos, entrance
data = bytearray(30000)
data_view = memoryview(data)
ip = dp = 0
while ip < len(code) and ip >= 0 and dp >= 0 and dp < 30000:
    if code[ip] is '>':
        dp += 1
    elif code[ip] is '<':
        dp -= 1
    elif code[ip] is '+':
        data[dp] += 1
    elif code[ip] is '-':
        data[dp] -= 1
    elif code[ip] is '.':
        stdout.write(data_view[dp])
    elif code[ip] is ',':
        data_view[dp] = stdin.read(1)
    elif code[ip] is '[':
        if not data[dp]:
            ip = loop_map[ip]
    elif code[ip] is ']':
        if data[dp]:
            ip = loop_map[ip]
    ip += 1

