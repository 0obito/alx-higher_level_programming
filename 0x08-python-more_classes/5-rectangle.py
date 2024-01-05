#!/usr/bin/python3
"""Defines a class Rectangle"""


class Rectangle:
    """
       Class that defines properties of a rectangle.
    """
    def __init__(self, width=0, height=0):
        """
           Instantiation with optional width and height.
        """
        self.height = height
        self.width = width

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

    def area(self):
        """
        Returns the rectangle's area.
        """
        return self.__height * self.__width

    def perimeter(self):
        """
        Returns the rectangle's perimeter.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return (self.__height + self.__width) * 2

    def __str__(self):
        """
        Returns a string representation of the rectangle using '#'.
        """
        if self.__width == 0 or self.__height == 0:
            return ""

        rectangle_str = ""
        for _ in range(self.__height):
            rectangle_str += '#' * self.__width + '\n'

        return rectangle_str[:-1]

    def __repr__(self):
        """
        Returns a string representation of the rectangle.
        """
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """
        Print the message Bye rectangle... when an instance is deleted
        """
        print("Bye rectangle...")
