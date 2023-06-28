#!/usr/bin/python3
# 103-magic_class.py
"""Magic Class docstring"""
import math


class MagicClass:
    """setting up magic class"""

    def __init__(self, radius=0):
        """Initializing Area"""
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be an number')
        self.__radius = radius

    def area(self):
        """radius area docstring"""
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """circumfrence docstring"""
        return 2 * math.pi * self.__radius
