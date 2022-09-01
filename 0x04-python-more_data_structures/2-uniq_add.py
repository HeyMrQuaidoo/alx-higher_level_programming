#!/usr/bin/python3
def uniq_add(my_list=[]):
    if my_list == None:
        return
    list_set = set(my_list)
    res = 0
    for n in list_set:
        res += n
    return res
