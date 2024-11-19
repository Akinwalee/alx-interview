#!/usr/bin/python3
"""
Rotating a 2D matrix in-place
"""


def rotate_2d_matrix(matrix):
    """
    Rotate 2D matrix
    """
    n = len(matrix)

    for i in range(n // 2):
        """n // 2 is the number of cycles in the 2D grid"""
        for j in range(i, n - i - 1):
            temp = matrix[i][j]

            matrix[i][j] = matrix[n - j - 1][i]
            matrix[n - j - 1][i] = matrix[n - i - 1][n - j - 1]
            matrix[n - i - 1][n - j - 1] = matrix[j][n - i -1]
            matrix[j][n - i -1] = temp