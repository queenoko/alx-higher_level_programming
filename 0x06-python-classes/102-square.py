#!/usr/bin/python3
# 102-square.py
"""Square Module"""


class Square:
    """defines Square"""

    def __init__(self, size=0):
        """Create square
        Arg:
        Size: length of side of square
        """
        self.__size = size

    @property
    def size(self):
        """The property of size as lenght of size of square
        Raises:
        TypeError: if Size != int
        ValueErroe: if size < 0
        """
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        """Gets area of square
        Returns the squared size
        """
        return self.__size * self.__size

    def __le__(self, other):
        return self.area() <= other.area()

    def __lt__(self, other):
        return self.area() < other.area()

    def __ge__(self, other):
        return self.area() >= other.area()

    def __ne__(self, other):
        return self.area() != other.area()

    def __gt__(self, other):
        return self.area() > other.area()

    def __eq__(self, other):
        return self.area() == other.area()
