#!/usr/bin/python3
"""Inheritance module"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Square inherits features of Rectangle """

    def __init__(self, size):
        """this is called on new instances"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(self.__size, self.__size)

    def __str__(self):
        """prints a string of how the area is calculated"""
        return "[Square] {}/{}".format(self.__size, self.__size)

    def area(self):
        """calculates the area of a square"""
        return self.__size ** 2
