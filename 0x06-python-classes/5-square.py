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

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.

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

    @property
    def size(self):
        """Retrieve the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square.

        Args:
            value (int): The size of one side of the square.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.

        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def my_print(self):
        """Print the square using #

        """
        for x in range(self.__size):
            for y in range(self.__size):
                print("#", end="")
            print("")
