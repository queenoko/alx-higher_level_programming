#!/usr/bin/python3


import sys

def safe_print_integer_err(value):
    """prints integer with "{:d}".format(0

    If ValueError message exist, a correspoding message is printed to
    standard error

    Arg:
    value (int): the integer to print

    Return:
    If TypeError or ValurError Exist, return false else true
    """

    try:
        print("{:d}".format(value))
        return (True)
    except (TypeError, ValueError):
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
        return (False)
