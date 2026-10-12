#!/usr/bin/env python3
"""Select data from a DataFrame and convert it to a NumPy array."""


def array(df):
    """Return the last 10 rows of the High and Close columns."""
    return df[['High', 'Close']].tail(10).to_numpy()
