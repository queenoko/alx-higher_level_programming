#!/usr/bin/python3
for g in range(ord('z'), ord('a') - 1, -1):
    if g % 2 == 0:
        differ = 0
    else:
        differ = 32
    print('{}'.format(chr(g - differ)), end='')
