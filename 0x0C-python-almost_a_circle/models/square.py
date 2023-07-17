#!/usr/bin/python3
"""This is square class"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Represents square"""
    def __init__(self, size, x=0, y=0, id=None):
        self.size = size
        self.x = x
        self.y = y
        self.id = None
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Defines format for string representation of class"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"

    @property
    def size(self):
        """Gets value of size"""
        return self.__width

    @size.setter
    def size(self, value):
        """Sets value for size"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value
        self.__height = value

    def update(self, *args, **kwargs):
        """Updates attributes of instance"""

        if args is not None and len(args) != 0:
            if len(args) >= 1:
                if type(args[0]) != int and args[0] is not None:
                    raise TypeError("id must be an integer")
                self.id = args[0]
            if len(args) > 1:
                self.size = args[1]
            if len(args) > 2:
                self.x = args[2]
            if len(args) > 3:
                self.y = args[3]
        else:
            for key1, value in kwargs.items():
                if key1 == "id":
                    if type(value) != int and value is not None:
                        raise TypeError("id must be an integer")
                    self.id = value
                if key1 == "size":
                    self.size = value
                if key1 == "x":
                    self.x = value
                if key1 == "y":
                    self.y = value

    def to_dictionary(self):
        """Returns dictionary representation of Square"""

        obj_dictionary = {'id': self.id, 'size': self.size, 'x': self.x,
                          'y': self.y}

        return obj_dictionary
