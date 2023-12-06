#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    i = 0
    newMatrix = []
    line = []
    for element in matrix:
        for sub in element:
            line.append(sub ** 2)
        newMatrix.append(line)
        line = []
    return newMatrix
