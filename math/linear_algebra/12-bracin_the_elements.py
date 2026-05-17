#!/usr/bin/env python3
"""This module performs element-wise operations on two numpy ndarrays"""


def np_elementwise(mat1, mat2):
    """Returns a tuple of element-wise sum, difference, product, quotient"""
    return (mat1 + mat2, mat1 - mat2, mat1 * mat2, mat1 / mat2)
