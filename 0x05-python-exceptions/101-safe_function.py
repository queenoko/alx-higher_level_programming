#!/usr/bin/python3

import sys


def safe_function(fct, *args):
    """Execute a function safely

    Arg:
    fct: function to execute
    args: fct argument

    Return:
    if error occurs - None
    else the result call to fct
    """

    try:
        result_fct = fct(*args)
        return (result_fct)
    except:
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
        return (None)
