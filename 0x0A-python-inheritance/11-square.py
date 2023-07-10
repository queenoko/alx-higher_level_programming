#!/usr/bin/python3
"""child class Square inherits rectangle class"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """square class inherits rectangle"""

    def __init__(self, size):
        """Initialize a new square object"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
