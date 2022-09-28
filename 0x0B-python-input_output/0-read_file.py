#!/usr/bin/python3
"""Input/output module"""


def read_file(filename=""):
    """reads a txt file and prints it to stdout"""
    with open(filename, "r") as file:
        print(file.read(), end="")
