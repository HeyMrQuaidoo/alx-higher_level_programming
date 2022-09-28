#!/usr/bin/python3
"""this module inserts a new attribute"""


def add_attribute(cls, name, value):
    """adds attribute to the dict"""
    if hasattr(cls, "__dict__"):
        cls.__setattr__(name, value)
    else:
        raise TypeError("can't add new attribute")
