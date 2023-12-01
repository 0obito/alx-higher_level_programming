#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    rev = []
    for i in my_list:
        rev.append(i)
    rev.reverse()

    for element in rev:
        print("{}".format(element))
