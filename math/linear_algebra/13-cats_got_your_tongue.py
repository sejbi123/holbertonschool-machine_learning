#!/usr/bin/env python3
"""Defines a function to concatenate NumPy arrays."""

import numpy as np


def np_cat(mat1, mat2, axis=0):
    """Concatenates two NumPy arrays along a specified axis."""
    return np.concatenate((mat1, mat2), axis=axis)
