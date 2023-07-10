#!/usr/bin/python3
"""Defines a Rectangle child class Square."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """square class inherited rectangle"""

    def __init__(self, size):
        """new square object"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
