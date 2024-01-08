#!/usr/bin/python3
"""
Module: add_integer.
This module performs a mathematical
  addition operation on 2 integers.
"""
def add_integer(a, b=98):
    """
    Function: add_integer.
    Parameters:
    - a (int or float): The first number to be added.
    - b (int or float): The second number to be added.
    Returns: The sum of a and b.
    """
    if type(a) is not int or type(b) is not int:
        if type(a) is not float:
            raise TypeError("a must be an integer")
        if type(b) is not float:
            raise TypeError("b must be an integer")

    return int(a) + int(b)
