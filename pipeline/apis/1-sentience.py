#!/usr/bin/env python3
"""Find the home planets of all sentient species."""

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


def sentientPlanets():
    """Return the home planets of all sentient species."""
    species_url = "https://swapi-api.hbtn.io/api/species/"
    species_list = fetch_all(species_url)

    planets = []
    planet_cache = {}

    for species in species_list:
        classification = species.get("classification") or ""
        designation = species.get("designation") or ""

        if (
            "sentient" in classification.lower()
            or "sentient" in designation.lower()
        ):
            homeworld = species.get("homeworld")

            if not homeworld:
                planet_name = "unknown"
            else:
                if homeworld not in planet_cache:
                    response = requests.get(homeworld, timeout=10)
                    response.raise_for_status()
                    planet_cache[homeworld] = response.json().get(
                        "name", "unknown"
                    )

                planet_name = planet_cache[homeworld]

            if planet_name not in planets:
                planets.append(planet_name)

    return planets
