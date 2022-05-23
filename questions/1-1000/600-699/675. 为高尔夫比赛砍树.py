# -*- coding: utf-8 -*-
# File:      675. 为高尔夫比赛砍树.py
# DATA:      2022/5/23
# Software:  PyCharm
__author__ = 'zcFang'

from collections import deque
from typing import List


class Solution:
    def cutOffTree(self, forest: List[List[int]]) -> int:
        def bfs(pre_x: int, pre_y: int, cur_x: int, cur_y: int) -> int:
            m, n = len(forest), len(forest[0])
            q = deque([(0, pre_x, pre_y)])
            visited = {(pre_x, pre_y)}
            while q:
                distance, x, y = q.popleft()
                if x == cur_x and y == cur_y:
                    return distance
                for new_x, new_y in ((x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)):
                    if 0 <= new_x < m and 0 <= new_y < n and forest[new_x][new_y] and (new_x, new_y) not in visited:
                        visited.add((new_x, new_y))
                        q.append((distance + 1, new_x, new_y))
            return -1

        trees = sorted((h, i, j) for i, row in enumerate(forest) for j, h in enumerate(row) if h > 1)
        ans = pre_x = pre_y = 0
        for _, cur_x, cur_y in trees:
            distance = bfs(pre_x, pre_y, cur_x, cur_y)
            if distance < 0:
                return -1
            ans += distance
            pre_x, pre_y = cur_x, cur_y
        return ans


print(Solution().cutOffTree(forest=[[1, 2, 3], [0, 0, 4], [7, 6, 5]]))
