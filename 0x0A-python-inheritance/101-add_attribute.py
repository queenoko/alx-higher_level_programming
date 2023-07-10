#!/usr/bin/python3
"""function that adds attributes to an objects"""


def add_attribute(obj, attribu, value):
    """Adds new attribute to object class"""
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, attribu, value)
