# -*- coding: utf-8 -*-
# File:    1219. 黄金矿工.py
# Date:    2022/2/14
# Software: Pycharm
__author__ = 'zcFang'

from typing import List


class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        ans = 0

        def backtrack(x: int, y: int, gold: int) -> None:
            gold += grid[x][y]
            nonlocal ans
            ans = max(ans, gold)
            rec = grid[x][y]
            grid[x][y] = 0
            for nx, ny in ((x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)):
                if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] > 0:
                    backtrack(nx, ny, gold)
            grid[x][y] = rec

        for i in range(m):
            for j in range(n):
                if grid[i][j] != 0:
                    backtrack(i, j,0)

        return ans


print(Solution().getMaximumGold(grid=[[0, 6, 0], [5, 8, 7], [0, 9, 0]]))
