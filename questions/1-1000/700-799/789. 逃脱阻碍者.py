# -*- coding: utf-8 -*-
# File:      789. 逃脱阻碍者.py
# DATA:      2021/8/22
# Software:  PyCharm
__author__ = 'zcFang'

from typing import List


class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        source = [0, 0]
        distance = self.manhattanDistance(source, target)
        return all(self.manhattanDistance(ghost, target) > distance for ghost in ghosts)

    def manhattanDistance(self, point1: List[int], point2: List[int]) -> int:
        return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])


ghosts = [[1, 0], [0, 3]]
target = [0, 1]
# ghosts = [[5,0],[-10,-2],[0,-5],[-2,-2],[-7,1]]
# target = [7,7]
print(Solution().escapeGhosts(ghosts, target))
