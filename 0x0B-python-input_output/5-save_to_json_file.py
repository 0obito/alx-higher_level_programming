#!/usr/bin/python3
"""5-save_to_json_file module"""
import json


def save_to_json_file(my_obj, filename):
    """save_to_json_file(my_obj, filename) function"""
    with open(filename, 'w') as file:
        json.dump(my_obj, file)
