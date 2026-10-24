#!/usr/bin/env python3
"""Get a GitHub user's location using the GitHub API."""

import sys
from datetime import datetime
import requests


def main():
    """Print the location of a GitHub user."""
    url = sys.argv[1]

    response = requests.get(url, timeout=10)

    if response.status_code == 404:
        print("Not found")
    elif response.status_code == 403:
        reset_time = int(response.headers.get("X-Ratelimit-Reset", 0))
        current_time = datetime.now().timestamp()
        minutes = max(0, int((reset_time - current_time) / 60))
        print(f"Reset in {minutes} min")
    elif response.status_code == 200:
        data = response.json()
        print(data.get("location") or "None")


if __name__ == "__main__":
    main()
    