#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if my_list is not None:
        lists = reversed(my_list)
        for i in lists:
            print("{:d}".format(i), end="\n")
