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
        """Function that returns the JSON string"""
        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Function that writes the JSON string"""
        file_name = f'{cls.__name__}.json'
        with open(file_name, 'w') as fn:
            if list_objs is None:
                fn.write('[]')
            else:
                obj_dicts = [obj.to_dictionary() for obj in list_objs]
                fn.write(Base.to_json_string(obj_dicts))

    def from_json_string(json_string):
        """Function that returns the list of the JSON string

        Args:
            json_string (str): string representing a list of dictionaries.
        """
        if json_string is None or json_string == []:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Function that returns an instance with all attrs already set.

        Args:
            dictionary (dict): can be thought of as
            a double pointer to a dictionary
        """
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                new_dict = cls(1, 1)
            else:
                new_dict = cls(1)
            new_dict.update(**dictionary)
            return new_dict

    @classmethod
    def load_from_file(cls):
        """Function that returns a list of instance."""
        file_name = f"{cls.__name__}.json"
        try:
            with open(file_name) as fn:
                list_of_dicts = Base.from_json_string(fn.read())
                instances = []
                for d in list_of_dicts:
                    instances.append(cls.create(**d))
                return instances
        except Exception:
            return []
