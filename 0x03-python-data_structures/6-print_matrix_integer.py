#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for element in matrix:
        i = 0
        for sub in element:
            print("{:d}".format(sub), end='')
            if i < (len(element) - 1):
                print(" ", end='')
                i += 1
        print("")
