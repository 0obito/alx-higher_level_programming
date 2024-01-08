#!/usr/bin/python3
"""1-my_list.py - Module for the MyList class"""

class MyList(list):
    """
    MyList - A custom list class that inherits the built-in list class.
    """
    def print_sorted(self):
        """
        print_sorted(self) - Print the sorted elements of the list.
        """
        print(sorted(self))
