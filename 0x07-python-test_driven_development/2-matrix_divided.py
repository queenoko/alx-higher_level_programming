#!/usr/bin/python3
"""
Module defines a matrix division function
"""


def matrix_divided(matrix, div):
    """Function that divides elements of matrix of a given number

    Arg:
    matrix: list of lists (matrix)- members can be of type ints or floats
    div: Number to be used to perform division (can be a float or an integer)
    Raises:
    TypeError: If the matrix contains non-numbers
    TypeError: If the matrix contains rows of different sizes
    TypeError: If div is not an int or float
    ZeroDivisionError: If div is 0
    Returns:
    New matrix that represents result of divisions
    """
    if (not isinstance(matrix, list) or matrix == [] or
            not all(isinstance(row1, list) for row1 in matrix) or
            not all((isinstance(elent, int) or isinstance(elent, float))
                    for elent in [num1 for row1 in matrix for num1 in row1])):
        raise TypeError("matrix must be a matrix (list of lists) of "
                        "integers/floats")

    if not all(len(row1) == len(matrix[0]) for row1 in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return ([list(map(lambda x: round(x / div, 2), row1)) for row1 in matrix])
