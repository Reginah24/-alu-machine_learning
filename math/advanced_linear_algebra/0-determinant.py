#!/usr/bin/env python3
"""Module for calculating the determinant of a matrix."""


def determinant(matrix):
    """Calculates the determinant of a matrix.

    Args:
        matrix: list of lists whose determinant should be calculated

    Returns:
        The determinant of matrix

    Raises:
        TypeError: if matrix is not a list of lists
        ValueError: if matrix is not square
    """
    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError("matrix must be a list of lists")

    for row in matrix:
        if not isinstance(row, list):
            raise TypeError("matrix must be a list of lists")

    # 0x0 matrix
    if matrix == [[]]:
        return 1

    n = len(matrix)
    for row in matrix:
        if len(row) != n:
            raise ValueError("matrix must be a square matrix")

    # 1x1 matrix
    if n == 1:
        return matrix[0][0]

    # 2x2 matrix
    if n == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

    # Cofactor expansion along the first row
    det = 0
    for col in range(n):
        # Build the submatrix excluding row 0 and current col
        submatrix = [
            [matrix[row][c] for c in range(n) if c != col]
            for row in range(1, n)
        ]
        sign = (-1) ** col
        det += sign * matrix[0][col] * determinant(submatrix)

    return det