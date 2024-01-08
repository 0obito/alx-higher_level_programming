#!/usr/bin/python3
"""Module for 10-square"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A class that inherits from Rectange class"""
    def __init__(self, size):
        """Instantiation with size"""
        self.__size = size
        super().__init__(size, size)
        self.integer_validator("size", self.__size)

    def area(self):
        """area method implementation"""
        return super().area()
