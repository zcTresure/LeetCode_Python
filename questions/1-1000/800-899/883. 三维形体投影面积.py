# -*- coding: utf-8 -*-
# File:      883. 三维形体投影面积.py
# DATA:      2022/4/26
# Software:  PyCharm
__author__ = 'zcFang'

from typing import List


class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        front_v, top_v, left_v = 0, 0, 0
        max_len = 0
        for row in grid:
            top_v += len(row) - row.count(0)
            max_len = max(max_len, len(row))
            front_v += max(row)
        for j in range(max_len):
            tmp = 0
            for row in grid:
                tmp = max(tmp, row[j])
            left_v += tmp
        return front_v + top_v + left_v


print(Solution().projectionArea(grid=[[1, 2], [3, 4]]))
print(Solution().projectionArea(grid=[[2]]))
print(Solution().projectionArea(grid=[[1, 0], [0, 2]]))
