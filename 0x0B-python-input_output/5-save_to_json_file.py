#!/usr/bin/python3
"""Module doc string"""
import json


def save_to_json_file(my_obj, filename):
    """Function that writes an Object to a text file, using a JSON representation."""
    with open(filename, 'w') as fn:
        json.dump(my_obj, fn)
