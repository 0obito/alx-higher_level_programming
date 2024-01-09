#!/usr/bin/python3
"""2-append_write module"""


def append_write(filename="", text=""):
    """append_write(filename="", text="") function"""
    with open(filename, 'a', encoding="UTF8") as file:
        return file.write(text)
