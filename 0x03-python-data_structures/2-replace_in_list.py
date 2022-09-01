#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    ind = len(my_list) - 1
    if idx > ind or idx < 0:
        return my_list
    my_list[idx] = element
    return my_list
