#!/usr/bin/env python3
"""Convert the last 10 rows of High and Close to a NumPy array."""

import numpy as np


def array(df):
    """Create a NumPy array from the High and Close columns."""
    return df[['High', 'Close']].tail(10).to_numpy()
