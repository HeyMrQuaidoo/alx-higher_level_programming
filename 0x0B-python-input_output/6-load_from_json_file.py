#!/usr/bin/python3
"""Module for file input/output"""

import json


def load_from_json_file(filename):
    """returns the JSON representation of a string"""
    with open(filename, 'r') as p:
        return json.load(p)
