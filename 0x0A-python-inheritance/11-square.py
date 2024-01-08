#!/usr/bin/python3
"""Module for 11-square"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A class that inherits from Rectange class"""
    def __init__(self, size):
        """Instantiation with size"""
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """str magic method"""
        return f"[Square] {self.__size}/{self.__size}"
