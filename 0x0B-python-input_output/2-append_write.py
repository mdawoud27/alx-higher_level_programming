#!/usr/bin/python3
"""Module doc string"""


def append_write(filename="", text=""):
    """Function that appends a string at the end of a text file."""
    with open(filename, 'a') as fn:
        return fn.write(text)
