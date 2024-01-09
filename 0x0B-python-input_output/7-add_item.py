#!/usr/bin/python3
"""7-add_item module"""
import sys


if __name__ == "__main__":
    save = __import__('5-save_to_json_file').save_to_json_file
    load = __import__('6-load_from_json_file').load_from_json_file

    try:
        mylist = load("add_item.json")
    except FileNotFoundError:
        mylist = []

    mylist.extend(sys.argv[1:])

    save(mylist, "add_item.json")
