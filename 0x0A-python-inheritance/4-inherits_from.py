#!/usr/bin/python3
"""Inheritance module"""


def inherits_from(obj, a_class):
    """tells whether argA inherits from argB"""
    return True if isinstance(obj, a_class) and type(obj) != a_class else False
