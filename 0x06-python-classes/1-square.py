#!/usr/bin/python3
"""Defines a class Square"""


class Square:
    """Class that defines properties of square.

    Attributes:
        __size (int): The size of one side of the square.

    """
    def __init__(self, sizee):
        """Initialize a square with a specified size.

        Args:
            sizee (int): The size of one side of the square.

        """
        self.__size = sizee
