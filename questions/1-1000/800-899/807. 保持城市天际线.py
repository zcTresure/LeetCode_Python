# -*- coding: utf-8 -*-
# File:      807. 保持城市天际线.py
# DATA:      2021/12/13
# Software:  PyCharm
__author__ = 'zcFang'

from typing import List


class Solution:
    # 贪心
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        n = len(grid)
        rows_max = [0] * n
        cols_max = [0] * n
        for i in range(n):
            for j in range(n):
                rows_max[i] = max(rows_max[i], grid[i][j])
                cols_max[j] = max(cols_max[j], grid[i][j])

        ans = 0
        for i in range(n):
            for j in range(n):
                ans += min(rows_max[i], cols_max[j]) - grid[i][j]

        return ans


grid = [[3, 0, 8, 4], [2, 4, 5, 7], [9, 2, 6, 3], [0, 3, 1, 0]]
print(Solution().maxIncreaseKeepingSkyline(grid))
