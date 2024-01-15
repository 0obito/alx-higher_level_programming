#!/usr/bin/python3
"""base module"""
import json
import csv


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

    @staticmethod
    def from_json_string(json_string):
        """Static method: returns the list of the JSON string representation"""
        if json_string is None or not json_string:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Class method: returns an instance with all attributes already set"""
        dummy_instance = cls(1, 2)
        dummy_instance.update(**dictionary)
        return dummy_instance

    @classmethod
    def load_from_file(cls):
        """Class method: returns a list of instances"""
        instances_list = []
        try:
            with open(f"{cls.__name__}.json", 'r') as file:
                json_string = file.read()
                dicts = cls.from_json_string(json_string)
                for dictionary in dicts:
                    instances_list.append(cls.create(**dictionary))
                return instances_list
        except FileNotFoundError:
            return instances_list

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Class method: saves instances to a file in CSV format"""
        if list_objs is None:
            list_objs = []

        dicts_list = [obj.to_dictionary() for obj in list_objs]

        with open(f"{cls.__name__}.csv", 'w', newline='') as csvfile:
            csv_writer = csv.writer(csvfile)
            csv_writer.writerows(dicts_list)

    @classmethod
    def load_from_file_csv(cls):
        """Class method: loads instances from a CSV format file"""
        instances_list = []
        try:
            with open(f"{cls.__name__}.csv", 'r', newline='') as csvfile:
                csv_reader = csv.reader(csvfile)
                headers = next(csv_reader)
                for row in csv_reader:
                    data_dict = {header: int(value) for header, value in zip(headers, row)}
                    instance = cls.create(**data_dict)
                    instances_list.append(instance)
        except FileNotFoundError:
            pass

        return instances_list
