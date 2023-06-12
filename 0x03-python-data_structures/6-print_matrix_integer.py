#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for r in matrix:
        for c in range(len(r)):
            if c == len(r) -1:
                print("{:d}".format(r[c]), end='')
            else:
                print("{:d}".format(r[c]), end=' ')
        print()
