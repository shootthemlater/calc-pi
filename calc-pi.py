#!/usr/bin/env python
"""Computation of pi.

This script computes an approximation of pi using
the following recurrence relation:

2[A(2n)/n]^2=[2A(n)/n]^2/[1+sqrt[1-[2A(n)/n]^2]]
"""
__author__ = "Jess Pizzol"

from math import sqrt, pi

N = 25  # number of steps
s = 1   # index counter
An = [2]    # term values
En = [abs(pi - An[0])]  # error values
n = 4   # initial term number is 4

for i in range(2, N):
    val = n * sqrt(((((2*An[s-1])/n)**2) /
                    (1+sqrt(1-((2*An[s-1])/n)**2)))/2)
    An.append(val)  # add new term to list
    En.append(abs(pi - An[s]))  # add new error to list
    s += 1  # increment index counter
    n *= 2  # term number doubles each step

print(En)
print(An)
