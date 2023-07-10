#!/usr/bin/python3
"""Defines Rectangle class which inherits from BaseGeometry parent class."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """represents a rectangle class using parent class BaseGeometry"""

    def __init__(self, width, height):
        """Intialize a new rectangle object"""

        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """returns and prints area of rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """returns the print() and str() representation of Rectangle"""
        string_rep = "[" + str(self.__class__.__name__) + "] "
        string_rep += str(self.__width) + "/" + str(self.__height)
        return string_rep
