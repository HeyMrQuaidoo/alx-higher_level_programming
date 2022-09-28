#!/usr/bin/python3
"""Inheritance module"""


class BaseGeometry:
    """Base geometry class"""
    def area(self):
        """just raises exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates @value"""
        if type(name) == str:
            if type(value) != int:
                raise TypeError("{} must be an integer".format(name))
            if value <= 0:
                raise ValueError("{} must be greater than 0".format(name))
