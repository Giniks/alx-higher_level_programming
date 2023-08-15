#!/usr/bin/python3
"""Defines a function called pascal triangle"""


def pascal_triangle(n):
    """This function represents pascal triangle
    Returns a list of lists of integers.
    Representing the Pascal’s triangle of n.
    """
    if n <= 0:
        return []

    triangles = [[1]]
    while len(triangles) != n:
        tri = triangles[-1]
        tmp = [1]
        for i in range(len(tri) - 1):
            tmp.append(tri[i] + tri[i + 1])
        tmp.append(1)
        triangles.append(tmp)
    return triangles
