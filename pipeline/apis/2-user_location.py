#!/usr/bin/env python3
"""Get a user's location from the GitHub API."""

import sys
import math
import time
import requests


def main():
    """Print a user's location or the API rate limit reset time."""
    url = sys.argv[1]
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        print(data.get("location") or "None")
    elif response.status_code == 404:
        print("Not found")
    elif response.status_code == 403:
        reset_time = int(response.headers["X-Ratelimit-Reset"])
        minutes = math.ceil((reset_time - time.time()) / 60)
        print("Reset in {} min".format(max(0, minutes)))


if __name__ == "__main__":
    main()
    