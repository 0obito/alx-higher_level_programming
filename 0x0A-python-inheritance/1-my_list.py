#!/usr/bin/python3
"""
1-my_list: inherits from list.
"""


class MyList(list):
    """
    MyList(list): a class that inherits from a list.
    Paramerters:
      - list: a list.
    """
    def print_sorted(self):
        print(sorted(self))
