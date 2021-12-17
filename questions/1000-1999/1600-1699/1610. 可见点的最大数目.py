# -*- coding: utf-8 -*-
# File:      1610. 可见点的最大数目.py
# DATA:      2021/12/16
# Software:  PyCharm
__author__ = 'zcFang'

from bisect import bisect_right
from math import atan2, pi
from typing import List


class Solution:
    # 二分查找
    def visiblePoints(self, points: List[List[int]], angle: int, location: List[int]) -> int:
        same_cnt = 0
        polar_degrees = []
        for p in points:
            if p == location:
                same_cnt += 1
            else:
                polar_degrees.append(atan2(p[1] - location[1], p[0] - location[0]))
        polar_degrees.sort()

        n = len(polar_degrees)
        polar_degrees += [deg + 2 * pi for deg in polar_degrees]

        degree = angle * pi / 180
        maxCnt = max((bisect_right(polar_degrees, polar_degrees[i] + degree) - i for i in range(n)), default=0)
        return maxCnt + same_cnt

    # 滑动窗口
    def visiblePoints(self, points: List[List[int]], angle: int, location: List[int]) -> int:
        same_cnt = 0
        polar_degrees = []
        for p in points:
            if p == location:
                same_cnt += 1
            else:
                polar_degrees.append(atan2(p[1] - location[1], p[0] - location[0]))
        polar_degrees.sort()

        n = len(polar_degrees)
        polar_degrees += [deg + 2 * pi for deg in polar_degrees]

        maxCnt = 0
        right = 0
        degree = angle * pi / 180
        for i in range(n):
            while right < n * 2 and polar_degrees[right] <= polar_degrees[i] + degree:
                right += 1
            maxCnt = max(maxCnt, right - i)
        return same_cnt + maxCnt


points = [[2, 1], [2, 2], [3, 3]]
angle = 90
location = [1, 1]
print(Solution().visiblePoints(points, angle, location))
