#!/usr/bin/env python3
"""Get a GitHub user's location using the GitHub API."""

import sys
import math
import time
import requests


def main():
    """Print the location of a GitHub user."""
    url = sys.argv[1]
    response = requests.get(url, timeout=10)

    if response.status_code == 404:
        print("Not found")
    elif response.status_code == 403:
        reset_time = int(response.headers.get("X-Ratelimit-Reset", 0))
        minutes = math.ceil((reset_time - time.time()) / 60)
        print(f"Reset in {max(0, minutes)} min")
    elif response.status_code == 200:
        data = response.json()
        print(data.get("location") or "None")


if __name__ == "__main__":
    main()
    