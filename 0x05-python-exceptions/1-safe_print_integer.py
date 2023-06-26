#!/usr/bin/python3

def safe_print_integer(value):

    """prints integer with "{:d}".format().

    Arg:
    value (int): Integer to print

    Return:
    If TypeError or ValueError occurs return false, else true
    """

    try:
        print("{:d}".format(value))
        return (True)
    except (TypeError, ValueError):
        return (False)
