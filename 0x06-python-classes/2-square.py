#!/usr/bin/python3
# 2-square.py
"""A class square that defines a class"""


class Square:
    """A class that represents square"""

    def __init__(self, size=0):
        """Initialize square class
        Arg:
        size: represents the defined size of square
        Msg:
        TypeError: if size is not integer
        ValueError: If size is less than 0
        """

        if not isinstance(size, int):
            raise ValueError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')

        self.__size = size
