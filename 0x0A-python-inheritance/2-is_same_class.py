#!/usr/bin/python3
"""Inheritance module"""


def is_same_class(obj, a_class):
    """tells whether argA is same class of argB"""
    return True if isinstance(obj, a_class) and type(obj) == a_class else False
