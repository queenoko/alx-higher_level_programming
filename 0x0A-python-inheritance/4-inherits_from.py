#!/usr/bin/python3
"""checks if object is an instance of a class
is inherited directly or indirectly
"""


def inherits_from(obj, a_class):
    """Returns true if object is an instance of a
    class is inherited directly or indirectly, else false
    """
    return (issubclass(type(obj), a_class) and type(obj) != a_class)
