#!/usr/bin/python3
"""Student Class JSON Function"""


class Student:
    """student class using JSON format"""

    def __init__(self, first_name, last_name, age):
        """Initialize new Student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """dictionary representation of Student Attrib"""
        if (type(attrs) == list and
                all(type(elemt) == str for elemt in attrs)):
            return {z: getattr(self, z) for z in attrs if hasattr(self, z)}
        return self.__dict__

    def reload_from_json(self, json):
        """Replaces Student attribute"""
        for z, v in json.items():
            setattr(self, z, v)
