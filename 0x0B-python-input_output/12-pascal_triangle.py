#!/usr/bin/python3
"""function of Pascal's Triangle"""


def pascal_triangle(n):
    """Pascal's Triangle of size n"""
    if n <= 0:
        return []

    pas_triangle = [[1]]
    while len(pas_triangle) != n:
        tri = pas_triangle[-1]
        temp = [1]
        for z in range(len(tri) - 1):
            temp.append(tri[i] + tri[i + 1])
        temp.append(1)
        pas_triangle.append(temp)
    return pas_triangle
