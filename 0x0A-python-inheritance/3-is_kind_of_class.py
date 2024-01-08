#!/usr/bin/python3
"""Module for is_kind_of_class.py"""


def is_kind_of_class(obj, a_class):
    """Function that checks if an object is an instance of a class,
       or one of its sub-classes.
    """
    return isinstance(obj, a_class)
