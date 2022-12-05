#!/usr/bin/python3
"""this module prints a square"""


def print_square(size):
    """this function prints a square with size, <size>
    tests:
    >>> print_square(1)
    #
    >>> print_square(3)
    ###
    ###
    >>> print_square(0)


    """
    if type(size) != int:
        raise TypeError("size must be an integer")
    elif size < 0 and type(size) is float:
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    for i in range(1, size + 1):
        for j in range(size):
            print("#", end="")
        print()
