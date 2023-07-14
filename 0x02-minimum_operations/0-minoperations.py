#!/usr/bin/python3
""" Minimum Operations"""


def minOperations(n):
    counter = 0
    copychar = 1
    charH = 1

    if n < 1:
        return 0

    while charH < n:
        if ((n % charH) == 0):
            copychar = charH
            counter += 1
        charH += copychar
        counter += 1

    return counter

