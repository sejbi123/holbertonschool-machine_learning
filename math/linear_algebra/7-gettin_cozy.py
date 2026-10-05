#!/usr/bin/env python3
"""Defines a function to concatenate two matrices."""


def cat_matrices2D(mat1, mat2, axis=0):
    """Concatenates two matrices along a specific axis."""
    if axis == 0:
        if len(mat1[0]) != len(mat2[0]):
            return None

        result = []
        for row in mat1:
            result.append(row[:])
        for row in mat2:
            result.append(row[:])

        return result

    if axis == 1:
        if len(mat1) != len(mat2):
            return None

        result = []
        for i in range(len(mat1)):
            result.append(mat1[i][:] + mat2[i][:])

        return result

    return None
