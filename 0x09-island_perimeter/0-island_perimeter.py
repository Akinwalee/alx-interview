#!/usr/bin/python3
"""
Finding the Perimeter of an island in a grid
"""


def island_perimeter(grid):
    """
    FInd the perimeter of an island
    """
    perimeter = 0
    w = len(grid[0])
    for i in range(0, len(grid)):
        for j in range(0, w):
            if grid[i][j] == 1:
                perimeter += 1 if i == 0 or grid[i - 1][j] == 0 else 0
                perimeter += 1 if i == n - 1 or grid[i + 1][j] == 0 else 0
                perimeter += 1 if j == 0 or grid[i][j - 1] == 0 else 0
                perimeter += 1 if j == w - 1 or grid[i][j + 1] == 0 else 0

    return perimeter
