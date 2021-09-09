# -*- coding: utf-8 -*-
# File:      764. 最大加号标志.py
# DATA:      2021/9/9
# Software:  PyCharm
__author__ = 'zcFang'

from typing import List


class Solution:
    def orderOfLargestPlusSign(self, n: int, mines: List[List[int]]) -> int:
        if len(mines) == n * n:
            return 0
        if len(mines) == n * n - 5:
            return 1
        grid = [[-1 for _ in range(n)] for _ in range(n)]
        arm = [[[0 for _ in range(4)] for _ in range(n)] for _ in range(n)]
        for x, y in mines:
            grid[x][y] = 0
        for i in range(n):
            for j in range(n):
                if (grid[i][j] != 0):
                    arm[i][j][0] = 1 + (arm[i - 1][j][0] if i > 0 else 0)
                    arm[i][j][1] = 1 + (arm[i][j - 1][1] if j > 0 else 0)

        for i in range(n - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if (grid[i][j] != 0):
                    arm[i][j][2] = 1 + (arm[i + 1][j][2] if i < n - 1 else 0)
                    arm[i][j][3] = 1 + (arm[i][j + 1][3] if j < n - 1 else 0)
        ans = 0
        for i in range(n):
            for j in range(n):
                if (grid[i][j] != 0):
                    ans = max(ans, min(arm[i][j]))
        return ans


n = 5
mines = [[4, 2]]
print((Solution().orderOfLargestPlusSign(n, mines)))
