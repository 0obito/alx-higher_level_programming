#!/usr/bin/python3
"""Defines a class Square"""


class Square:
    """Class that defines properties of square.

    Attributes:
        __size (int): The size of one side of the square.
        __position (tuple): The position of the square.

    """
    def __init__(self, size=0, position=(0, 0)):
        """Initialize a square with a specified size and position.

        Args:
            size (int): The size of one side of the square.
            position (tuple, optional): The position of the square.

        Raises:
            TypeError: If size is not an integer or
                if position is not a tuple of two positive integers.
            ValueError: If size is less than 0 or
                if position contains non-positive integers.
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        elif (
              type(position) is not tuple or
              len(position) != 2 or
              type(position[0]) is not int or
              type(position[1]) is not int or
              position[0] < 0 or
              position[1] < 0
        ):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__size = size
            self.__position = position

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
        if self.__size == 0:
            print("")
        else:
            for k in range(self.__position[1]):
                print("")
            for x in range(self.__size):
                for y in range(self.__position[0]):
                    print(" ", end="")
                for z in range(self.__size):
                    print("#", end="")
                print("")

    @property
    def position(self):
        """Retrieve the position of the square."""
        return self.__position

    @position.setter
    def position(self, value):
        """Set the position of the square.

        Args:
            value (tuple): The position of the square.

        Raises:
            TypeError: If value is not a tuple of two positive integers.
            ValueError: If value contains non-positive integers.

        """
        if (
            type(value) is not tuple or
            len(value) != 2 or
            type(value[0]) is not int or
            type(value[1]) is not int or
            value[0] < 0 or
            value[1] < 0
        ):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value
