#!/usr/bin/env python3
"""Set Timestamp as the DataFrame index."""


def index(df):
    """Set the Timestamp column as the index and return the DataFrame."""
    return df.set_index("Timestamp")
