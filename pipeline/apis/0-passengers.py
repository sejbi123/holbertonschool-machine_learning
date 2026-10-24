#!/usr/bin/env python3
"""Find starships that can carry a specified number of passengers."""

import requests


def fetch_all(url):
    """Fetch all API results by following pagination links."""
    results = []

    while url:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()

        results.extend(data["results"])
        url = data.get("next")

    return results


def parse_passengers(raw):
    """Convert a passenger capacity string to an integer if possible."""
    if raw is None:
        return None

    cleaned = raw.replace(",", "").strip().lower()

    if cleaned in ("n/a", "unknown", ""):
        return None

    if "-" in cleaned:
        cleaned = cleaned.split("-")[0]

    if cleaned.isdigit():
        return int(cleaned)

    return None


def availableShips(passengerCount):
    """Return names of ships that can carry at least passengerCount."""
    url = "https://swapi-api.hbtn.io/api/starships/"
    ships = []

    for ship in fetch_all(url):
        capacity = parse_passengers(ship.get("passengers"))

        if capacity is not None and capacity >= passengerCount:
            ships.append(ship["name"])

    return ships
