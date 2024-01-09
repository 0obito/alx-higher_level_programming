#!/usr/bin/python3
"""7-add_item module"""
import sys
import json
save = __import__('5-save_to_json_file').save_to_json_file
load = __import__('6-load_from_json_file').load_from_json_file


try:
    mylist = load('add_item.json')
except (FileNotFoundError, json.JSONDecodeError):
    mylist = []

for item in sys.argv[1:]:
    mylist.append(item)

save(mylist, 'add_item.json')
