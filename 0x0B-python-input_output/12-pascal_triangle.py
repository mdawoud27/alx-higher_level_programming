#!/usr/bin/python3
"""Module doc string"""


def pascal_triangle(n):
    """Function that returns a list of lists of integers
    representing the Pascal’s triangle of n"""
    pascal_triangle = []
    if n <= 0:
        return pascal_triangle
    for i in range(n):
        row = []
        for j in range(i + 1):
            if j == 0 or j == i:
                row.append(1)
            else:
                prev_row = pascal_triangle[i - 1]
                value = prev_row[j - 1] + prev_row[j]
                row.append(value)
        pascal_triangle.append(row)
    return pascal_triangle
