#!/usr/bin/env python3
"""Poisson distribution module"""


class Poisson:
    """Represents a Poisson distribution"""

    e = 2.7182818285

    def __init__(self, data=None, lambtha=1.):
        """
        Class constructor

        data: list of the data used to estimate the distribution
        lambtha: expected number of occurrences in a given time frame
        """
        if data is None:
            if lambtha <= 0:
                raise ValueError("lambtha must be a positive value")
            self.lambtha = float(lambtha)
        else:
            if not isinstance(data, list):
                raise TypeError("data must be a list")
            if len(data) < 2:
                raise ValueError("data must contain multiple values")
            self.lambtha = float(sum(data) / len(data))

    def pmf(self, k):
        """
        Calculates the PMF for a given number of successes

        k: number of successes
        Returns the PMF value for k, or 0 if k is out of range
        """
        k = int(k)
        if k < 0:
            return 0

        factorial = 1
        for i in range(1, k + 1):
            factorial *= i

        return (Poisson.e ** (-self.lambtha)
                * self.lambtha ** k) / factorial

    def cdf(self, k):
        """
        Calculates the CDF for a given number of successes

        k: number of successes
        Returns the CDF value for k, or 0 if k is out of range
        """
        k = int(k)
        if k < 0:
            return 0

        total = 0
        for i in range(k + 1):
            total += self.pmf(i)

        return total
