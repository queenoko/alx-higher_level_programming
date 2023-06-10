#!/usr/bin/python3

def no_c(my_string):
    """remove c and C from string"""
    copy = [z for z in my_string if z != 'c' and z != 'C']
    return ("".join(copy))
