#!/usr/bin/python3
"""base module"""
import json


class Base:
    """Base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialization of Base class"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Static method: returns the JSON string
        representation of list_dictionaries
        """
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Class method: saves instances to a file in JSON format"""
        dict_list = []
        if list_objs is None:
            list_objs = []
        for obj in list_objs:
            dict_list.append(obj.to_dictionary())

        with open("{}.json".format(cls.__name__), 'w') as file:
            text = cls.to_json_string(dict_list)
            return file.write(text)
