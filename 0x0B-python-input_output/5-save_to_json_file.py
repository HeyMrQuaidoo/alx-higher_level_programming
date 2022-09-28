#!/usr/bin/python3
"""Module for file input/output"""

import json


def save_to_json_file(my_obj, filename):
    """returns the JSON representation of a string"""
    with open(filename, 'w') as p:
        return json.dump(my_obj, p)
