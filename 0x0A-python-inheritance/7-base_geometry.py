#!/usr/bin/python3
"""Defines BaseGeometry class"""


class BaseGeometry:
    """base geometry class"""

    def area(self):
        """not implemented method"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates value as integer
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
