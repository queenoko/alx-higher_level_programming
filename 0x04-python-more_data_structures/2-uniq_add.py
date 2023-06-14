#!/usr/bin/python3

def uniq_add(my_list=[]):
    """ adds all unique integers in a list (only once for each integer)."""
    digit = 0
    for item in set(my_list):
        digit += item
    return digit
