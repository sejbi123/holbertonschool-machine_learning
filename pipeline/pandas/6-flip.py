#!/usr/bin/env python3
"""Sort a DataFrame in reverse chronological order and transpose it."""


def flip_switch(df):
    """Sort the DataFrame in descending order and transpose it."""
    df = df.sort_values(by="Timestamp", ascending=False)
    return df.transpose()
