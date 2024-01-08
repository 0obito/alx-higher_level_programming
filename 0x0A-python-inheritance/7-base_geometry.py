#!/usr/bin/python3
"""Module for 7-base_geometry.py"""


class BaseGeometry:
    """an empty class BaseGeometry"""
    def area(self):
        """Public instance method that raises an exception"""
        raise Exception("area() is not implemented")
    def integer_validator(self, name, value):
        """Public instance method that validates value"""
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
