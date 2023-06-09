#!/usr/bin/python3
"""Class that defines an object rectangle"""


class Rectangle:
    """rectangle class"""

    def __init__(self, width=0, height=0):
        """Initializes rectangle

        Arg:
        width: width of a rectangle
        height: Height of rectangle
        Raises:
        TypeError: If size is not integer
        ValueError: If size is < 0
        """

        self.width = width
        self.height = height

    @property
    def width(self):
        """retrives the attributes of width"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets the attributes of width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """retrives the attributes of height"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets the attributes of height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
