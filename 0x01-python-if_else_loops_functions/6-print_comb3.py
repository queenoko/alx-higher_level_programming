#!/usr/bin/python3
for g in range(0, 10):
    for k in range(g + 1, 10):
        if g == 8 and k == 9:
            print('89')
        else:
            print('{}{}, '.format(g, k), end='')
