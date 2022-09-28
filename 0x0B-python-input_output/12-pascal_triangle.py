#!/usr/bin/python3
"""Pascals triangle module"""


def pascal_triangle(n):
    """returns pascal's triangle"""
    if n <= 0:
        return list()

    tr = []
    for line in range(0, n):
        # Every line has number of
        # integers equal to line
        # number
        tmp = []
        for i in range(0, line + 1):
            tmp.append(magic(line, i))
        tr.append(tmp)
    return tr


def magic(n, k):
    """magic function"""
    res = 1
    if k > n - k:
        k = n - k
    for i in range(0, k):
        res = res * (n - i)
        res = res // (i + 1)
    return res
