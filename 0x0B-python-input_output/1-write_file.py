#!/usr/bin/python3
"""Module doc string"""


def write_file(filename="", text=""):
    """Function that writes a string to a text file."""
    with open(filename, 'w') as fn:
        return fn.write(text)
