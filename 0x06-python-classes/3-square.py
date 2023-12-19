#!/usr/bin/python3
"""Defines a class Square"""


class Square:
    """Class that defines properties of square.

    Attributes:
        __size (int): The size of one side of the square.

    """
    def __init__(self, sizee=0):
        """Initialize a square with a specified size.

        Args:
            sizee (int): The size of one side of the square.

        """
        if type(sizee) is not int:
            raise TypeError("size must be an integer")
        elif sizee < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = sizee
    def area(self):
        """Return the square's size

        """
        return self.__size**2
