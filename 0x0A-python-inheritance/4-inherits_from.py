#!/usr/bin/python3
"""Module for inherits_from.py"""


def inherits_from(obj, a_class):
    """Function that checks if an object is an instance of a sub-class
       of the given class.
    """
    return issubclass(type(obj), a_class) and type(obj) != a_class
