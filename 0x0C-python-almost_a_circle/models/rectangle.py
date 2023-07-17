#!/usr/bin/python3
"""This is rectangle class"""

from models.base import Base


class Rectangle(Base):
    """Represents a rectangle """

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes attributes of the object"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    # List of getter functions
    @property
    def width(self):
        """Gets value for width"""
        return self.__width

    @property
    def height(self):
        """Gets value for height"""
        return self.__height

    @property
    def x(self):
        """Gets value for x"""
        return self.__x

    @property
    def y(self):
        """Gets value for y"""
        return self.__y

    # List of setter functions
    @width.setter
    def width(self, value):
        """Sets value for width"""
        if (type(value) is not int):
            raise TypeError("width must be an integer")

        if value <= 0:
            raise ValueError("width must be > 0")

        self.__width = value

    @height.setter
    def height(self, value):
        """Sets value for height"""
        if (type(value) is not int):
            raise TypeError("height must be an integer")

        if value <= 0:
            raise ValueError("height must be > 0")

        self.__height = value

    @x.setter
    def x(self, value):
        """Sets value for x"""
        if (type(value) is not int):
            raise TypeError("x must be an integer")

        if value < 0:
            raise ValueError("x must be >= 0")

        self.__x = value

    @y.setter
    def y(self, value):
        """Sets value for y"""
        if (type(value) is not int):
            raise TypeError("y must be an integer")

        if value < 0:
            raise ValueError("y must be >= 0")

        self.__y = value

    def area(self):
        """Defines area of rectangle"""
        return (self.__height * self.__width)

    def display(self):
        """Displays the rectangle using # """
        for y in range(self.y):
            print("")
        for row in range(self.__height):
            for x in range(self.x):
                print(" ", end="")
            for column in range(self.__width):
                print("#", end="")
            print()

    def __str__(self):
        """Defines a format for the string representation of the class"""
        return f"[Rectangle] ({self.id}) {self.__x}/{self.__y} - \
{self.__width}/{self.__height}"

    def update(self, *args, **kwargs):
        """Assigns argument to each attribute"""

        if args and len(args) != 0:
            attri = 0
            for arg in args:
                if attri == 0:
                    if arg is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = arg
                elif attri == 1:
                    self.width = arg
                elif attri == 2:
                    self.height = arg
                elif attri == 3:
                    self.x = arg
                elif attri == 4:
                    self.y = arg
                attri += 1

        elif kwargs and len(kwargs) != 0:
            for m, n in kwargs.items():
                if m == "id":
                    if n is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = m
                elif m == "width":
                    self.width = n
                elif m == "height":
                    self.height = n
                elif m == "x":
                    self.x = n
                elif m == "y":
                    self.y = n

    def to_dictionary(self):
        """Returns the dictionary representation of a Rectangle"""

        obj_dictionary = {'id': self.id, 'width': self.__width,
                          'height': self.__height, 'x': self.__x,
                          'y': self.__y}

        return obj_dictionary
