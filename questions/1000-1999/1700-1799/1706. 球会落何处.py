# -*- coding: utf-8 -*-
# File:      1706. 球会落何处.py
# DATA:      2022/2/24
# Software:  PyCharm
__author__ = 'zcFang'

from typing import List


class Solution:
    # 模拟
    def findBall(self, grid: List[List[int]]) -> List[int]:
        n = len(grid[0])
        ans = [-1] * n
        for j in range(n):
            col = j
            for row in grid:
                dir = row[col]
                col += dir
                if col < 0 or col == n or row[col] != dir:
                    break
            else:
                ans[j] = col
        return ans

grid = [[1, 1, 1, -1, -1],
        [1, 1, 1, -1, -1],
        [-1, -1, -1, 1, 1],
        [1, 1, 1, 1, -1],
        [-1, -1, -1, -1, -1]]
print(Solution().findBall(grid))
