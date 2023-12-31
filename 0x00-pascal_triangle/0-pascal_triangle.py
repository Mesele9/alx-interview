#!/usr/bin/python3
"""
pascal triagle
"""


def pascal_triangle(n):
    """
    Generate pascal triangle of size n.
    """
    if n <= 0:
        return []

    triangle = []

    for i in range(n):
        if (i == 0):
            triangle.append([1])
        else:
            row = []
            for j in range(i + 1):
                if (j == 0 or j == i):
                    row.append(1)
                else:
                    row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])

            triangle.append(row)

    return (triangle)
