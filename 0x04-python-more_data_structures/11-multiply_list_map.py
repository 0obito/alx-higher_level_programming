#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):
    Result = list(map(lambda element: element*number, my_list))
    return Result