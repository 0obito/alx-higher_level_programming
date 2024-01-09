#!/usr/bin/python3
"""1-write_file.py module"""


def write_file(filename="", text=""):
    """write_file(filename="", text="") function"""
    with open(filename, 'w', encoding="UTF8") as file:
        return file.write(text)
