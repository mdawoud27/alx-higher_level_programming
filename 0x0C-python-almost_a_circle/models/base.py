#!/usr/bin/python3
"""Base class"""
import json


class Base:
    """Base class doc string"""
    __nb_objects = 0
    def __init__(self, id=None):
        """Class constractor.

        Args:
            id (int): """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Function that returns the JSON string representation of list_dictionaries"""
        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Function that writes the JSON string representation of list_objs to a file"""
        file_name = cls.__name__ + '.json'
        with open(file_name, 'w') as fn:
            if list_objs is None:
                fn.write('[]')
            else:
                obj_dicts = [obj.to_dictionary() for obj in list_objs]
                fn.write(Base.to_json_string(obj_dicts))

    def from_json_string(json_string):
        """Function that returns the list of the JSON string representation json_string

        Args:
            json_string (str): string representing a list of dictionaries.
        """
        if json_string is None or json_string == []:
            return []
        return json.loads(json_string)


