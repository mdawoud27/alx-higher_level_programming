#!/usr/bin/python3
"""Module doc string"""


class Student:
    """Student class doc string"""
    def __init__(self, first_name, last_name, age):
        """Instantiation function."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Function that retrieves a dictionary representation."""
        return self.__dict__
