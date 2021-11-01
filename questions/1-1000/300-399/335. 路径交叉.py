# -*- coding: utf-8 -*-
# File:      335. 路径交叉.py
# DATA:      2021/10/29
# Software:  PyCharm
__author__ = 'zcFang'

from typing import List


class Solution:
    def isSelfCrossing(self, distance: List[int]) -> bool:
        for i in range(3, len(distance)):
            if distance[i] >= distance[i - 2] and distance[i - 1] <= distance[i - 3]:
                return True
            if i == 4 and distance[3] == distance[1] and distance[4] >= distance[2] - distance[0]:
                return True
            if i >= 5 and (distance[i - 3] - distance[i - 5] <= distance[i - 1] <= distance[i - 3]
                           and distance[i] >= distance[i - 2] - distance[i - 4]
                           and distance[i - 2] > distance[i - 4]):
                return True
        return False

    def isSelfCrossing(self, distance: List[int]) -> bool:
        n = len(distance)
        i = 0
        while i < n and (i < 2 or distance[i] > distance[i - 2]):
            i += 1
        if i == n: return False

        if ((i == 3 and distance[i] == distance[i - 2])
                or (i >= 4 and distance[i] >= distance[i - 2] - distance[i - 4])):
            distance[i - 1] -= distance[i - 3]
        i += 1

        # 处理第 2 种情况
        while i < n and distance[i] < distance[i - 2]:
            i += 1

        return i != n


distance = [2, 1, 3, 1]
print(Solution().isSelfCrossing(distance))
