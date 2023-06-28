#!/usr/bin/python3
# 5-square.py
"""Module that defines a square"""


class Square:
    """Square class"""

    def __init__(self, size=0):
        """ Initialize the square class
        Arg:
        Size: this is size of the square defined
        Raises:
        TypeError: size is not integer
        ValueError: size is less than 0
        """

        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')

        self.__size = size

    @property
    def size(self):
        """Retrive size of square"""

        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        """
        area of square
        returns square size
        """

        return (self.__size ** 2)

    def my_print(self):
        """print square in # shape"""

        if self.__size == 0:
            print()

        for i in range(self.__size):
            print('#' * self.__size)
