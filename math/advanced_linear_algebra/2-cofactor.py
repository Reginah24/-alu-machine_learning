#!/usr/bin/env python3
"""Module for calculating the cofactor matrix of a matrix."""
minor = __import__('1-minor').minor


def cofactor(matrix):
    """Calculates the cofactor matrix of a matrix.

    Args:
        matrix: list of lists whose cofactor matrix should be calculated

    Returns:
        The cofactor matrix of matrix

    Raises:
        TypeError: if matrix is not a list of lists
        ValueError: if matrix is not square or is empty
    """
    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError("matrix must be a list of lists")

    for row in matrix:
        if not isinstance(row, list):
            raise TypeError("matrix must be a list of lists")

    if matrix == [[]] or len(matrix[0]) == 0:
        raise ValueError("matrix must be a non-empty square matrix")

    n = len(matrix)
    for row in matrix:
        if len(row) != n:
            raise ValueError("matrix must be a non-empty square matrix")

    minor_mat = minor(matrix)

    cofactor_mat = [
        [
            minor_mat[i][j] * ((-1) ** (i + j))
            for j in range(n)
        ]
        for i in range(n)
    ]

    return cofactor_mat
