#!/usr/bin/python3
def search_replace(my_list, search, replace):
    if my_list is not None:
        res = my_list[:]
        for i in range(len(res)):
            if res[i] == search:
                res[i] = replace
    return res
