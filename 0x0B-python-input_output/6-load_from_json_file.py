#!/usr/bin/python3
"""6-load_from_json_file module"""
import json


def load_from_json_file(filename):
    """load_from_json_file(filename) function"""
    with open(filename, 'r') as file:
        data = json.load(file)
        return data
