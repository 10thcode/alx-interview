#!/usr/bin/python3
"""
Defines island_perimeter function
"""


def island_perimeter(grid):
    """
    Gets the perimeter of the island described in grid
    """
    if grid is None or grid == [] or len(grid) == 0 or len(grid[0]) == 0:
        return 0

    result = 0

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 1:
                if i == 0 or grid[i-1][j] == 0:
                    result += 1

                if i == len(grid) - 1 or grid[i+1][j] == 0:
                    result += 1

                if j == 0 or grid[i][j-1] == 0:
                    result += 1

                if j == len(grid[i]) - 1 or grid[i][j+1] == 0:
                    result += 1

    return result
