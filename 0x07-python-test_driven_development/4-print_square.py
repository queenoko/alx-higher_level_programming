#!/usr/bin/python3
"""
Function module that prints a square
"""


def print_square(size):
    """The function that prints a square with # character

    Arg:
    size (int): This represents the length of the square

    Raises:
    TypeError: Size is not an integer
    TypeError: Size is a float and less than zero
    ValueError: Size is less than zero

    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    elif isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    for y in range(0, size):
        for z in range(size):
            print("#", end="")
        print("")
