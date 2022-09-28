#!/usr/bin/python3
"""Input/output module"""


def write_file(filename="", text=""):
    """writes to a txt file"""
    with open(filename, "w", encoding='utf-8') as file:
        file.write(text)
    return len(text)
