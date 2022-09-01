#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list is None or len(my_list) < 1:
        return 0
    num = 0
    weights = 0
    for i in my_list:
        num += i[1]
        weights += i[0] * i[1]
    return weights / num
