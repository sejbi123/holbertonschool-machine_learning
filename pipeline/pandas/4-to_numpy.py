#!/usr/bin/env python3
"""Convert the last 10 rows of High and Close to a NumPy array."""

import numpy as np


def array(df):
    """Select the last 10 rows of High and Close and return a NumPy array."""
    return df[["High", "Close"]].tail(10).to_numpy()
