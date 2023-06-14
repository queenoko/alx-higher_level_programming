#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    """returns a new dictionary with all values multiplied by 2"""
    return ({q: a_dictionary[q] * 2 for q in a_dictionary})
