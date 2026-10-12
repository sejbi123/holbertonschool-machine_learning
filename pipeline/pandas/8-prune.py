#!/usr/bin/env python3
"""Remove rows where Close contains NaN values."""


def prune(df):
    """Remove rows with NaN values in the Close column."""
    return df.dropna(subset=["Close"])
