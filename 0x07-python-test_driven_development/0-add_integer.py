#!/usr/bin/python3
"""
Module function that adds up 2 integers
"""


def add_integer(a, b=98):
    """Prints and return the sum of two integers or floats as integers

    Arg:
    a: first number
    b: second number

    Returns:
    The sum of the two numbers

    Raises:
    TypeError: If one of the arguments not an integer or a float
    """

    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
