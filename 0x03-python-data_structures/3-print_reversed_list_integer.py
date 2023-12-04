#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
  #  rev = []
 #   for i in my_list:
#        rev.append(i)
    my_list.reverse()

    for element in my_list:
        print("{:d}".format(element))
