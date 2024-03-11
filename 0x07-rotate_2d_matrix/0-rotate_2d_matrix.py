#!/usr/bin/python3
"""
Define rotate_2d_matrix function.
"""


def rotate_2d_matrix(matrix):
    """
    Rotate an array by 90 degrees.
    """
    for i in range(len(matrix)):
        matrix[i].reverse()

    for row in range(len(matrix)):
        for col in range(row, len(matrix)):
            matrix[row][col], matrix[col][row] = \
                matrix[col][row], matrix[row][col]

    for i in range(len(matrix)):
        matrix[i].reverse()

    matrix.reverse()
