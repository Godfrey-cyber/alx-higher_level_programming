#!/usr/bin/python3
for i in 'abcdefghijklmnopqrstuvwxyz':
    if chr(i) != 'e' and chr(i) != 'q':
        print('{:c}'.format(i), end='')
