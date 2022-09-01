#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    if a_dictionary is None:
        return
    return dict(map(lambda x: (x[0], x[1] * 2), a_dictionary.items()))
