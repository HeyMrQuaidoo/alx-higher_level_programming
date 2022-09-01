#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    max_num = -1
    max_key = None
    for key in a_dictionary.keys():
        if a_dictionary[key] > max_num:
            max_num = a_dictionary[key]
            max_key = key
    return max_key
