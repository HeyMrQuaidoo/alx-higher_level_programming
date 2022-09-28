#!/usr/bin/python3
"""Inheritance module"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Defines a rectangle"""
    def __init__(self, width, height):
        """instanciation initialiser"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = int(width)
        self.__height = int(height)
