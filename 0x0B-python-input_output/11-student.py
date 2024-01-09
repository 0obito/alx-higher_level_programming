#!/usr/bin/python3
"""student module"""


class Student():
    """Student class"""
    def __init__(self, first_name, last_name, age):
        """Instantiation"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Public method that retrieves a dictionary representation"""
        if attrs is None:
            return self.__dict__
        else:
            return {key: value for key,
                    value in self.__dict__.items() if key in attrs}

    def reload_from_json(self, json):
        """Replaces all attributes of the Student instance"""
        for key, value in json.items():
            setattr(self, key, value)
