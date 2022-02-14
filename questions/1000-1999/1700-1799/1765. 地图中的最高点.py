# -*- coding: utf-8 -*-
# File:    1765. 地图中的最高点.py
# Date:    2022/2/14
# Software: Pycharm
__author__ = 'zcFang'

from collections import deque
from typing import List


class Solution:
    # 多元广度优先搜索
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        m, n = len(isWater), len(isWater[0])
        ans = [[water - 1 for water in row] for row in isWater]
        # 将所有水源入队
        q = deque((i, j) for i, row in enumerate(isWater) for j, water in enumerate(row) if water)
        while q:
            i, j = q.popleft()
            for x, y in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
                if 0 <= x < m and 0 <= y < n and ans[x][y] == -1:
                    ans[x][y] = ans[i][j] + 1
                    q.append((x, y))
        return ans


print(Solution().highestPeak(isWater=[[0, 1], [0, 0]]))
