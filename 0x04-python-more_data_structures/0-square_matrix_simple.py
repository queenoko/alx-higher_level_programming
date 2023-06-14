#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    """Compute the square value of integers of matrix"""
    return [list(map(lambda x: x ** 2, row)) for row in matrix]
