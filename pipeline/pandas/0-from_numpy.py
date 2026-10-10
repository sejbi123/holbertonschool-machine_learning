#!/usr/bin/env python3
"""Create a pandas DataFrame from a numpy array."""

import pandas as pd


def from_numpy(array):
    """Create a DataFrame with alphabetical column labels."""
    columns = [chr(ord('A') + i) for i in range(array.shape[1])]
    return pd.DataFrame(array, columns=columns)
