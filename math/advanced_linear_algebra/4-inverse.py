#!/usr/bin/env python3
"""Module for calculating the inverse of a matrix."""
determinant = __import__('0-determinant').determinant
adjugate = __import__('3-adjugate').adjugate


def inverse(matrix):
    """Calculates the inverse of a matrix.

    Args:
        matrix: list of lists whose inverse should be calculated

    Returns:
        The inverse of matrix, or None if matrix is singular

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

    det = determinant(matrix)

    if det == 0:
        return None

    adj = adjugate(matrix)

    inverse_mat = [
        [adj[i][j] / det for j in range(n)]
        for i in range(n)
    ]

    return inverse_mat
