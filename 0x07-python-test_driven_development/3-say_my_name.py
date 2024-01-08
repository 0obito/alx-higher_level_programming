#!/usr/bin/python3
"""
Module: 3-say_my_name.
This module prints someone's full name.
"""
def say_my_name(first_name, last_name=""):
    """
    Function: say_my_name(first_name, last_name="").
    Parameters:
    - first_name (string): The person's first name.
    - last_name (string): The person's last name.
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print(f"My name is {first_name} {last_name}")
