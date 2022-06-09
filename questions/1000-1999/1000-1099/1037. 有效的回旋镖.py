# -*- coding: utf-8 -*-
# File:      1037. 有效的回旋镖.py
# DATA:      2022/6/8
# Software:  PyCharm
from typing import List


class Solution:
    def isBoomerang(self, points: List[List[int]]) -> bool:
        v1 = (points[1][0] - points[0][0], points[1][1] - points[0][1])
        v2 = (points[2][0] - points[1][0], points[2][1] - points[1][1])
        return v1[0] * v2[1] - v1[1] * v2[0] != 0


print(Solution().isBoomerang(points=[[1, 1], [2, 3], [3, 2]]))
print(Solution().isBoomerang(points=[[1, 1], [2, 2], [3, 3]]))
