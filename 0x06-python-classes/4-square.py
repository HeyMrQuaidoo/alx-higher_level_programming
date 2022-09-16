#!/usr/bin/python3
""" this python module defines a square """


class Square:
    """ class that defines a square """

    def __init__(self, size=0):
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            """ if everything is fine ..."""
            self.__size = size

    def area(self):
        """calculates the area of a square"""
        return self.__size ** 2

    @property
    def size(self):
        """defines a private attribute - size"""
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
