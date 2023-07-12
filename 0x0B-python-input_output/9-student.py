#!/usr/bin/python3
"""Function Student class using JSON format"""


class Student:
    """Student class, using JSON format"""

    def __init__(self, first_name, last_name, age):
        """Initialize Student class"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Studen Dictionary"""
        return self.__dict__
