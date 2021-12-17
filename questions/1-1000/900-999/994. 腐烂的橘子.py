# -*- coding: utf-8 -*-
# File:      994. 腐烂的橘子.py
# DATA:      2021/12/16
# Software:  PyCharm
__author__ = 'zcFang'

from collections import deque
from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        drics = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        ans, count = 0, 0
        queue = deque()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    count += 1
                elif grid[i][j] == 2:
                    queue.append((i, j))

        while count > 0 and queue:
            ans += 1
            cur_round = len(queue)
            for c in range(cur_round):
                i, j = queue.popleft()
                for x, y in drics:
                    nx, ny = i + x, j + y
                    if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == 1:
                        queue.append((nx, ny))
                        grid[nx][ny] = 2
                        count -= 1
        if count > 0:
            return -1
        return ans


# grid = [[2, 1, 1], [1, 1, 0], [0, 1, 1]]
grid = [[2, 1, 1], [0, 1, 1], [1, 0, 1]]
print(Solution().orangesRotting(grid))
