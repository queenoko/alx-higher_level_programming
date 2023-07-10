#!/usr/bin/python3
"""Check if object is an instance of specified class"""


def is_same_class(obj, a_class):
    """Returns
    true if object is an instance of
    specified class, else false
    """
    return (type(obj) == a_class)
