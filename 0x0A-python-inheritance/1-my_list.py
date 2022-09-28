#!/usr/bin/python3
"""Inheritance module"""


class MyList(list):
    """Inherits from list andp rints sorted list"""

    def print_sorted(self):
        """sorts the list in ascending order"""
        print(sorted(self))
