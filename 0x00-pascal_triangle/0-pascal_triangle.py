#!/usr/bin/python3
"""
Pascal Triangle

"""


def pascal_triangle(number_of_rows: int) -> list[list[int]]:
    """ Simple Pascal Triangle

    Args:
        number_of_rows (int): number of rows

    Returns:
        list: a list of lists of (n) rows
    """
    if number_of_rows <= 0:
        return [[]]

    result = [[1]]

    for i in range(number_of_rows - 1):
        temp = [0] + result[-1] + [0]
        new_row = []
        for j in range(len(result[-1]) + 1):
            new_row.append(temp[j] + temp[j + 1])
        result.append(new_row)
    return result
