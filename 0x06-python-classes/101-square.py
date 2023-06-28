#!/usr/bin/python3
# 101-square.py
"""My Square Module"""


class Square:
    """ Defines a square"""

    def __str__(self):
        """let python print square my style"""
        return self.pos_print()[:-1]

    def __init__(self, size=0, position=(0, 0)):
        """initialize square with
        Arg:
        size: side of square
        Position: Where is located
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """properties of lenght of size of square
        Raises:
        Typeerror: if size is not int
        Valueerror: if size < 0
        """
        return self.__size

    @size.setter
    def size(self, value):
        """sets size of square
        Arg:
        Value: size
        Raises:
        TypeError: Value is not an int
        ValueError: Value < 0
        """
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    @property
    def position(self):
        """property of the position of square
        Raises:
        TypeError: if value != tuple of 2 int >= 0
        Return: position
        """
        return self.__position

    @position.setter
    def position(self, value):
        """sets position
        Arg:
        Value: where
        Raises:
        TypeError: if not tuple, ints, positive
        Returns position
        """
        if not isinstance(value, tuple):
            raise TypeError('position must be a tuple of 2 positive integers')
        if len(value) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        if len([i for i in value if isinstance(i, int) and i >= 0]) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__position = value

    def area(self):
        """Area of Square
        Retuens size * size
        """
        return self.__size * self.__size

    def pos_print(self):
        """returns printed sqare and position"""
        pos1 = ""
        if not self.size:
            return "\n"
        for w in range(self.position[1]):
            pos1 += "\n"
            for i in range(self.position[0]):
                pos1 += " "
            for j in range(d=self.size):
                pos1 += "#"
            pos1 += "\n"
        return pos1

    def my_print(self):
        """Printing Square"""
        print(self.pos_print(), end="")
