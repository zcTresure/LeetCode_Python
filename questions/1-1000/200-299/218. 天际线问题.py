# -*- coding: utf-8 -*-
# File:      218. 天际线问题.py
# DATA:      2021/7/14
# Software:  PyCharm
__author__ = 'zcFang'

import heapq
from typing import List


class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        points = list()
        for left, high, right in buildings:
            points.append([left, -high, right])
            points.append([right, 0, 0])
        points.sort()
        res = [[0, 0]]
        height = [[0, float('inf')]]
        heapq.heapify(height)
        for left, high, right in points:
            while left >= height[0][1]:
                heapq.heappop(height)
            if high < 0:
                heapq.heappush(height, [high, right])
            if res[-1][1] != -height[0][0]:
                res.append([left, -height[0][0]])
        return res[1:]


buildings = [[2, 9, 10], [3, 7, 15], [5, 12, 12], [15, 20, 10], [19, 24, 8]]
print(Solution().getSkyline(buildings))
# [[2,10],[3,15],[7,12],[12,0],[15,10],[20,8],[24,0]]
