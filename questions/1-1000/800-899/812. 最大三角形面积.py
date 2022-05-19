# -*- coding: utf-8 -*-
# File:      812. 最大三角形面积.py
# DATA:      2022/5/16
# Software:  PyCharm
__author__ = 'zcFang'

from itertools import combinations
from typing import List


class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        def triangleArea(x1: int, y1: int, x2: int, y2: int, x3: int, y3: int) -> float:
            return abs(x1 * y2 + x2 * y3 + x3 * y1 - x1 * y3 - x2 * y1 - x3 * y2) / 2

        return max(triangleArea(x1, y1, x2, y2, x3, y3) for (x1, y1), (x2, y2), (x3, y3) in combinations(points, 3))


points = [[0, 0], [0, 1], [1, 0], [0, 2], [2, 0]]
print(Solution().largestTriangleArea(points))
