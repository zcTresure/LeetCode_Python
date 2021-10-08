# -*- coding: utf-8 -*-
# File:      223. 矩形面积.py
# DATA:      2021/10/8
# Software:  PyCharm
__author__ = 'zcFang'


class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        area1 = (ax2 - ax1) * (ay2 - ay1)
        area2 = (bx2 - bx1) * (by2 - by1)
        overlapWidth = min(ax2, bx2) - max(ax1, bx1)
        overlapHeight = min(ay2, by2) - max(ay1, by1)
        overlapArea = max(overlapWidth, 0) * max(overlapHeight, 0)
        return area1 + area2 - overlapArea


ax1, ay1 = -3, 0
ax2, ay2 = 3, 4
bx1, by1 = 0, -1
bx2, by2 = 9, 2
print(Solution().computeArea(ax1, ay1, ax2, ay2, bx1, by1, bx2, by2))
