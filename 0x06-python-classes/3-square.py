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
        return self.__size ** 2
