#!/bin/usr/python3
"""pascal_trinagle"""


def pascal_triangle(n):
    """Gets pascal triangle"""
    if n <= 0:
        return []

    tri = [[1]]
    i = 1

    while i < n:
        arr = [1]
        j = i - 1

        for k in range(j):
            arr.append(tri[j][k] + tri[j][k+1])

        tri.append([*arr, 1])
        i += 1

    return tri
