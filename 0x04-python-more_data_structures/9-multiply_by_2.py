#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    dict = {}
    for element in a_dictionary:
        dict[element] = a_dictionary[element] * 2

    return dict
