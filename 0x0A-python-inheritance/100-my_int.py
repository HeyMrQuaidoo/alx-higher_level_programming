#!/usr/bin/python3
"""This module inverts comparison operators"""


class MyInt(int):
    """This class creates a personalized int"""

    def __init__(self, num):
        """initializes the class"""
        self.num = num

    def __eq__(self, other):
        """handles the == operator"""
        return self.num.__ne__(other)

    def __ne__(self, other):
        """reverts != operator"""
        return self.num.__eq__(other)
