#!/usr/bin/python3
"""A module for 9-rectangle.py"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """A class that inherits from BaseGeometry"""
    def __init__(self, width, height):
        """Instantiation with width and height"""
        self.__width = width
        self.__height = height
        super().__init__()
        self.integer_validator("width", self.__width)
        self.integer_validator("height", self.__height)

    def __str__(self):
        """Str magic method"""
        return f"[Rectangle] {self.__width}/{self.__height}"

    def area(self):
        """Implementing area method"""
        return self.__width * self.__height
