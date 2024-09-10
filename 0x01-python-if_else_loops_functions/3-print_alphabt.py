#!/usr/bin/python3
for i in 'abcdefghijklmnopqrstuvwxyz':
    if i not in ['e', 'q']:
        print('{:c}'.format(i), end='')
