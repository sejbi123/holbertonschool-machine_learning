#!/usr/bin/env python3
"""Exponential distribution"""


class Exponential:
    """Exponential distribution: the waiting time until the next event"""

    def __init__(self, data=None, lambtha=1.):
        """Sets lambtha, estimated from data if given"""
        if data is None:
            if lambtha <= 0:
                raise ValueError("lambtha must be a positive value")
            self.lambtha = lambtha
        else:
            if not isinstance(data, list):
                raise TypeError("data must be a list")
            if len(data) < 2:
                raise ValueError("data must contain multiple values")

            self.lambtha = len(data) / sum(data)
            self.data = data

    def pdf(self, x):
        """PDF at time x: lambtha * e^(-lambtha * x)"""

        if x < 0:
            return 0

        e = 2.7182818285

        return self.lambtha * e ** (-self.lambtha * x)

    def cdf(self, x):
        """CDF at time x: 1 - e^(-lambtha * x), the chance of waiting x or
        less"""

        if x < 0:
            return 0

        e = 2.7182818285

        return 1 - e ** (-self.lambtha * x)
    