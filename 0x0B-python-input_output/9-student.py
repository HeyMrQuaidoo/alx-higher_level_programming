#!/usr/bin/python3
"""Module for file input/output"""


class Student:
    """student class"""
    def __init__(self, first_name, last_name, age):
        """Initialization of the student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """return an info about student"""
        return self.__dict__
