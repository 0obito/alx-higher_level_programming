#!/usr/bin/python3
def uniq_add(my_list=[]):
    i = 0
    uniqList = set(my_list)
    for element in uniqList:
        i += element

    return i
