#!/usr/bin/env python3
"""Compute descriptive statistics for a DataFrame."""


def analyze(df):
    """Return descriptive statistics excluding the Timestamp column."""
    return df.drop(columns=["Timestamp"]).describe()
