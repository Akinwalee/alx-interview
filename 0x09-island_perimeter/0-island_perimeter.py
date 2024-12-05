#!/usr/bin/python3
"""
Finding the Perimeter of an island in a grid
"""


def island_perimeter(grid):
    """
    FInd the perimeter of an island
    """
    perimeter = 0
    for i in range(1, len(grid) - 1):
        for j in range(1, len(grid[i]) - 1):
            if grid[i][j] == 1:
                perimeter += 1 if grid[i - 1][j] == 0 else 0
                perimeter += 1 if grid[i + 1][j] == 0 else 0
                perimeter += 1 if grid[i][j - 1] == 0 else 0
                perimeter += 1 if grid[i][j + 1] == 0 else 0

    return perimeter
