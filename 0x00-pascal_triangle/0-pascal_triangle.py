#!/bin/usr/python3
'''
Contains a function that return interger representation
of Pascal triangle
'''


def pascal_triangle(n):
    '''
    Gets the list of list of intergers representing
    the Pascal's triangle of n

    Args:
        n [int]: a number

    Returns:
        tri [[int]]: a list of list of integer
    '''
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
