#!/usr/bin/python3
# 3-square.py
"""Module that defines area of square"""


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

    def area(self):
        """Calculate area of square
        Returns size of square
        """

        return (self.__size ** 2)
