# -*- coding: utf-8 -*-
# File:      699. 掉落的方块.py
# DATA:      2022/5/26
# Software:  PyCharm
__author__ = 'zcFang'

from typing import List


class Solution:
    def fallingSquares(self, positions: List[List[int]]) -> List[int]:
        n = len(positions)
        heights = [0] * n
        for i, (left1, side1) in enumerate(positions):
            right1 = left1 + side1 - 1
            heights[i] = side1
            for j in range(i):
                left2, right2 = positions[j][0], positions[j][0] + positions[j][1] - 1
                if right1 >= left2 and right2 >= left1:
                    heights[i] = max(heights[i], heights[j] + side1)
        for i in range(1, n):
            heights[i] = max(heights[i], heights[i - 1])
        return heights


print(Solution().fallingSquares(positions=[[1, 2], [2, 3], [6, 1]]))
