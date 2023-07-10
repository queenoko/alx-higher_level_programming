#!/usr/bin/python3
"""Inherit from parent in prev task baseGeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """defines rectangle using BaseGeometry parent class"""

    def __init__(self, width, height):
        """Intialize a new Rectangle object
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
