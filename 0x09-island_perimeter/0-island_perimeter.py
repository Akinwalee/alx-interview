#!/usr/bin/python3
"""
Finding the Perimeter of an island in a grid
"""


def island_perimeter(grid):
    """
    FInd the perimeter of an island with no lakes
    """
    perimeter = 0
    n = len(grid)
    for i in range(n):
        w = len(grid[i])
        for j in range(w):
            if grid[i][j] == 1:
                perimeter += 1 if i == 0 or grid[i - 1][j] == 0 else 0
                perimeter += 1 if i == n - 1 or grid[i + 1][j] == 0 else 0
                perimeter += 1 if j == 0 or grid[i][j - 1] == 0 else 0
                perimeter += 1 if j == w - 1 or grid[i][j + 1] == 0 else 0

    return perimeter
