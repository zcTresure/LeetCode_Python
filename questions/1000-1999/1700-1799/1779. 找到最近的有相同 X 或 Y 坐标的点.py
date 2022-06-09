# -*- coding: utf-8 -*-
# File:      1779. 找到最近的有相同 X 或 Y 坐标的点.py
# DATA:      2022/6/9
# Software:  PyCharm
from typing import List


class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        points = [(i, j, k) for k, (i, j) in enumerate(points) if i == x or y == j]
        if not points:
            return -1
        ans = index = float('inf')
        for (i, j, k) in points:
            distance = abs(x - i) + abs(y - j)
            if ans > distance:
                index = min(index, k) if ans == distance else k
                ans = distance
        return index


print(Solution().nearestValidPoint(x=3, y=4, points=[[1, 2], [3, 1], [2, 4], [2, 3], [4, 4]]))
print(Solution().nearestValidPoint(x=3, y=4, points=[[3, 4]]))
print(Solution().nearestValidPoint(x=2, y=3, points=[[3, 4]]))
