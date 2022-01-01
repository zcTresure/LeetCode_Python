# -*- coding: utf-8 -*-
# File:      1091. 二进制矩阵中的最短路径.py
# DATA:      2021/12/29
# Software:  PyCharm
__author__ = 'zcFang'

import collections
from typing import List


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        l = len(grid)
        if grid[0][0] != 0 or grid[l - 1][l - 1] != 0:  # 处理特殊情况
            return -1
        if l == 1:
            return 1

        visited = set((0, 0))  # 存放已遍历的位置的集合
        Q = collections.deque([(0, 0)])  # 存放接下来一轮的地址
        Q2 = collections.deque([])  # 在一轮中暂存所有的位置
        ans = 0

        while Q:
            ans += 1
            while Q:  # 首先把此轮中Q内所有点的周围遍历过去，为了方便记录ans，每次都遍历完后，才把新的点重新加入
                i, j = Q.popleft()
                if i == l - 1 and j == l - 1:  # 发现已经找到终点，那就可以直接返回了
                    return ans
                for (x, y) in [(i - 1, j), (i + 1, j), (i, j + 1), (i, j - 1), (i + 1, j + 1), (i + 1, j - 1),
                               (i - 1, j + 1), (i - 1, j - 1)]:
                    if (x, y) not in visited and l > x >= 0 and l > y >= 0:
                        if grid[x][y] == 0:
                            visited.add((x, y))
                            Q2.append((x, y))
            while Q2:  # 把Q2中的下一轮需要遍历的点加回到Q中
                Q.append(Q2.popleft())
        return -1  # 遍历完了还没到达终点，说明根本无法过来


grid = [[0, 1], [1, 0]]
print(Solution().shortestPathBinaryMatrix(grid))
