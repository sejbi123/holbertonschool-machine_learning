#!/usr/bin/env python3
"""Defines a function to calculate the shape of a matrix."""


def matrix_shape(matrix):
    """Calculates the shape of a matrix."""
    shape = []

    while type(matrix) is list:
        shape.append(len(matrix))
        matrix = matrix[0]

    return shape
