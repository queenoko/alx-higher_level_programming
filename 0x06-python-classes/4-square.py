#!/usr/bin/python3
# 4-square.py
"""Module that defines square"""


class Square:
    """Class that represent a square"""

    def __init__(self, size=0):
        """initialize square class
        Arg:
        size: size of squre defined
        Raises:
        TypeError: size is not an integer
        ValueError: size is less than 0
        """

        if not isinstance(size, int):
            raise TypeError('size must be integer')
        if size < 0:
            raise ValueError('size must be >= 0')

        self.__size = size

    @property
    def size(self):
        """retrive square size"""

        return self.__size

    @size.setter
    def size(size, value):
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        """
        Cal area of square
        Return square size
        """

        return (self.__size ** 2)
