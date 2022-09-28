#!/usr/bin/python3
"""Inheritance module"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Square inherits features of Rectangle """

    def __init__(self, size):
        """ instantiation initializer """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(self.__size, self.__size)

    def area(self):
        """calculates the area of a square"""
        return self.__size ** 2
