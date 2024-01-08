#!/usr/bin/python3
"""
1-my_list: inherits from list.
"""


class MyList(list):
    """
    MyList(list): a class that inherits from a list.
    """
    def print_sorted(self):
        """Method to print the list in ascending order"""
        print(sorted(self))
