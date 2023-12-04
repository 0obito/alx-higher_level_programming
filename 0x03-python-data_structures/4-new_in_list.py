#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    copy = []
    for var in my_list:
        copy.append(var)
    if idx < 0 or idx >= len(my_list):
       return copy
    else:
        copy[idx] = element
        return copy
