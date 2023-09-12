#!/usr/bin/python3
"""Module doc string"""
import json


def load_from_json_file(filename):
    """Function that creates an Object from a “JSON file”."""
    with open(filename) as fn:
        return json.load(fn)
