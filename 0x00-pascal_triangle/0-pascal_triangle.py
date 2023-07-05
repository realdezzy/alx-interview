#!/usr/bin/python3
"""
Pascal Triangle

"""


def pascal_triangle(n):
    """ Simple Pascal Triangle

    Args:
        n (int): number of rows

    Returns:
        list: a list of lists of (n) rows
    """
    if n <= 0:
        return []

    result = [[1]]

    for i in range(n - 1):
        temp = [0] + result[-1] + [0]
        new_row = []
        for j in range(len(result[-1]) + 1):
            new_row.append(temp[j] + temp[j + 1])
        result.append(new_row)
    return result
