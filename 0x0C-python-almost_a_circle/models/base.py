#!/usr/bin/python3
"""Base class"""


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
