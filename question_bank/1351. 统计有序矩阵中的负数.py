import numpy as np


def countNegatives(self, grid: list) -> int:
    return int((np.array(grid) < 0).sum())


grid = [[4, 3, 2, -1], [3, 2, 1, -1], [1, 1, -1, -2], [-1, -1, -2, -3]]
print(countNegatives(1, grid))
