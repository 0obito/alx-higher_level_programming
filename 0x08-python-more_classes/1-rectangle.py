#!/usr/bin/python3
"""Defines a class Rectangle"""


class Rectangle:
    """
       Class that defines
       properties of a rectangle.
    """
    def __init__(self, width=0, height=0):
        """
           Instantiation with
           optional width and height
        """
        self.__height = height
        self.__width = width

    @property
    def width(self):
        """
        Getter method for width.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter method for width.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """
        Getter method for height.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter method for height.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
