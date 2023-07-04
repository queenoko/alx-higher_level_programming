#!/usr/bin/python3
"""Class that defines an object rectangle"""


class Rectangle:
    """rectangle class"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initializes rectangle

        Arg:
        width: width of a rectangle
        height: Height of rectangle
        Raises:
        TypeError: If size is not integer
        ValueError: If size is < 0
        """

        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """retrives the attributes of width"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets the attributes of width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """retrives the attributes of height"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets the attributes of height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns and prints the area of a rectangle"""
        return (self.__width * self.__height)

    def perimeter(self):
        """Returns and prints the perimeter of a rectangle"""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self) -> str:
        """represents a diagram of object rectangle"""
        if self.__width == 0 or self.__height == 0:
            return ("")
        rectangle_shape = ""
        for col in range(self.__height):
            for row in range(self.__width):
                try:
                    rectangle_shape += str(self.print_symbol)
                except Exception:
                    rectangle_shape += type(self.print_symbol)
            if col < self.__height - 1:
                rectangle_shape += "\n"
        return (rectangle_shape)

    def __repr__(self):
        """returns and prints rectangle representation"""
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        """returns and prints msg for deleted object"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """static method that returns the biggest rectangle based on area"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2
