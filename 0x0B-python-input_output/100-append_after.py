#!/usr/bin/python3
"""Module doc string"""


def append_after(filename="", search_string="", new_string=""):
    """Function that inserts a line of text to a file."""
    lines = []
    with open(filename) as fn:
        lines = fn.readlines()

    with open(filename, 'w') as fn:
        for line in lines:
            fn.write(line)
            if search_string in line:
                fn.write(new_string)
