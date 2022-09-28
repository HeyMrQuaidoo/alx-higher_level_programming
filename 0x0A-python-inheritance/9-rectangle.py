#!/usr/bin/python3
"""Inheritance module"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ Rectangle is a child class of BaseGeometry """

    def __init__(self, width, height):
        """ initializes values for height and width if passed validator """
        super().__init__()
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def __str__(self):
        """prints a string of how the area is calculated"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)

    def area(self):
        """returns area of rectangle"""
        return self.__width * self.__height
