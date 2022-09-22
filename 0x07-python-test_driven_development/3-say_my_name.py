#!/usr/bin/python3
"""this module prints a name"""


def say_my_name(first_name, last_name=""):
    """
    this function prints the name of a person
    :param first_name: (str)
    :param last_name: (str)
    :return: none

    tests:
    >>> say_my_name("John", "Smith")
    My name is John Smith
    >>> say_my_name("Walter", "White")
    My name is Walter White
    >>> say_my_name("Bob")
    My name is Bob
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print(f"My name is {first_name} {last_name}")
