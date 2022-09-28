#!/usr/bin/python3
"""Module for file input/output"""

import json


def from_json_string(my_str):
    """returns the JSON representation of a string"""
    return json.loads(my_str)
