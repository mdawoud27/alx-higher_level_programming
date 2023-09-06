#!/usr/bin/python3
"""Module doc string."""


def text_indentation(text):
    """Text indentation.

    Args:
        text (str): Text
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    new_line = False
    for char in text:
        if char == ':' or char == '?' or char == '.':
            print(char, end='')
            print('\n')
            new_line = True
        elif char == ' ' and new_line:
            continue
        else:
            print(char, end='')
            new_line = False
