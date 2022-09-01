#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if matrix is not None:
        res = [[n * n for n in i] for i in matrix]
        return res
    else:
        return
