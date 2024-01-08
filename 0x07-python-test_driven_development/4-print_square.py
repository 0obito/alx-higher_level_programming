#!/usr/bin/python3
"""
Module: 4-print_square.
Prints a square with the character #.
"""
def print_square(size):
    """
    Function: print_square(size).
    Parameters:
      - size: size length of the square.
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print("")
