#!/usr/bin/python3
"""0-read_file.py module"""


def read_file(filename=""):
    """read_file(filename="") function"""
    with open(filename, 'r', encoding="UTF8") as f:
        for line in f:
            print(line, end="")
