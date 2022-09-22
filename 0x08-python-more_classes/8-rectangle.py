#!/usr/bin/python3
"""This module prints a rectangle"""


class Rectangle:
    """defines a rectangle"""
    __number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """ initializes the 'width' and 'height' attributes """

        self.__height = height
        self.__width = width
        Rectangle.__number_of_instances += 1

    def area(self):
        """a regular method that Calculates the area of a rectangle"""

        return self.__width * self.__height

    def perimeter(self):
        """calculates the perimeter of a rectangle"""

        if self.__width == 0 or self.__height == 0:
            return 0
        return (2 * self.__width) + (2 * self.__height)

    @property
    def height(self):
        """Height getter function"""

        return self.__height

    @height.setter
    def height(self, value):
        """Height setter function"""

        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    @property
    def width(self):
        """retrieves the value of width"""

        return self.__width

    @width.setter
    def width(self, value):
        """sets value to the width"""

        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError('rect_1 must be an instance of Rectangle')
        if not isinstance(rect_2, Rectangle):
            raise TypeError('rect_2 must be an instance of Rectangle')

        r1 = rect_1.width * rect_1.height
        r2 = rect_2.width * rect_2.height
        return rect_1 if r1 > r2 or r1 == r2 else rect_2

    @classmethod
    def square(cls, size=0):
        """creates new instance with height and width == size"""
        return cls(size, size)

    def __str__(self):
        if self.__width != 0 and self.__height != 0:
            sym = '#' * self.__width
            return '\n'.join(sym for _ in range(self.__height))

    def __repr__(self):    # not for that task
        if self.width != 0 and self.height != 0:
            return f"Rectangle({self.width}, {self.height})"
        else:
            return ""

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.__number_of_instances -= 1
