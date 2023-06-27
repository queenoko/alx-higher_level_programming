#!/usr/bin/python3
# 1-square.py
""" a class Square that defines a square where size is a private attribute"""


class Square:
    """Square Representation"""

    def __init__(self, size):
        """initialize square class
        Arg: size - defines the size of the square
        """

        self.__size = size
