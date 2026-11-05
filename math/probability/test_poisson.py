#!/usr/bin/env python3

from poisson import Poisson

p = Poisson(data=[1, 2, 3, 4])
print("Lambda:", p.lambtha)

print("PMF P(X=2):", p.pmf(2))

print("CDF P(X<=2):", p.cdf(2))
