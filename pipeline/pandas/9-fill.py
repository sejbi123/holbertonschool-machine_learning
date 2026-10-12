#!/usr/bin/env python3
"""Fill missing values in a DataFrame."""


def fill(df):
    """Fill missing values and remove the Weighted_Price column."""
    df = df.drop(columns=["Weighted_Price"])
    df["Close"] = df["Close"].ffill()

    for col in ["High", "Low", "Open"]:
        df[col] = df[col].fillna(df["Close"])

    df[["Volume_(BTC)", "Volume_(Currency)"]] = df[
        ["Volume_(BTC)", "Volume_(Currency)"]
    ].fillna(0)

    return df
