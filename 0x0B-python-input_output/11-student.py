#!/usr/bin/python3
"""Module doc string"""


class Student:
    """Student class doc string"""
    def __init__(self, first_name, last_name, age):
        """Instantiation function."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Function that retrieves a dictionary representation."""
        if attrs is None:
            return self.__dict__
        else:
            filtered_attrs = {}
            for attr in attrs:
                if hasattr(self, attr):
                    filtered_attrs[attr] = getattr(self, attr)
            return filtered_attrs

    def reload_from_json(self, json):
        """Function that replaces all attributes of the Student instance."""
        for key, value in json.items():
            setattr(self, key, value)
