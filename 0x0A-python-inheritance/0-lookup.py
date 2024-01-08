#!/usr/bin/python3
"""
0-lookup:
  Returns the list of available
  attributes and methods of an object.
"""


def lookup(obj):
    """
    lookup:
      A function that returns the list of available
      attributes and methods of an object.
    parameters:
      - obj: the object to use in this function.
    return:
      available attributesand methods of obj.
    """
    return dir(obj)
