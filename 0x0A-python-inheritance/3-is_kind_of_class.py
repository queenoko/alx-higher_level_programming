#!/usr/bin/python3
"""checks if object is an inherited or instance of a class"""


def is_kind_of_class(obj, a_class):
    """returns
     if the object is an instance of, or if the object is an
     instance of a class that inherited from, the specified class
     else return false
    """
    return (isinstance(obj, a_class))
