#!/usr/bin/env python3
"""Sort a DataFrame by High price in descending order."""


def high(df):
    """Sort the DataFrame by High in descending order."""
    return df.sort_values(by="High", ascending=False)
