#!/usr/bin/python3
for x in range(10):
    for y in range(x + 1, 10):
        if x == 8 and y == 9:
            print('98')
        else:
            print('{}{}, '.format(x, y), end='')
