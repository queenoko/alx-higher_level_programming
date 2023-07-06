#!/usr/bin/python3
"""Finding the max integer in a list Module
"""


def max_integer(list=[]):
    """Function that fis and print the maximun integer in a integer list
    if list is empty return None
    """
    if len(list) == 0:
        return None
    result_list = list[0]
    z = 1
    while z < len(list):
        if list[z] > result_list:
            result_list = list[z]
        z += 1
    return result_list
