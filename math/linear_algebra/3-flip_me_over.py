#!/usr/bin/env python3
"""Defines a function to transpose a matrix."""


def matrix_transpose(matrix):
    """Returns the transpose of a 2D matrix."""
    transpose = []

    for j in range(len(matrix[0])):
        new_row = []
        for i in range(len(matrix)):
            new_row.append(matrix[i][j])
        transpose.append(new_row)

    return transpose
