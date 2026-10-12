#!/usr/bin/env python3
"""Slice selected columns of a DataFrame."""


def slice(df):
    """Select four columns and return every 60th row."""
    return df[["High", "Low", "Close", "Volume_(BTC)"]].iloc[::60]
