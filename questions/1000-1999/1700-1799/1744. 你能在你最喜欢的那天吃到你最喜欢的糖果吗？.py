# -*- coding: utf-8 -*-
# File:     1744. 你能在你最喜欢的那天吃到你最喜欢的糖果吗？.py
# Date:     2021/6/1
# Software: PyCharm
__author__ = 'zcFang'

from itertools import accumulate
from typing import List


class Solution:
    def canEat(self, candiesCount: List[int], queries: List[List[int]]) -> List[bool]:
        total = list(accumulate(candiesCount))
        ans = list()
        for favoriteType, favoriteDay, dailyCap in queries:
            x1 = favoriteDay + 1
            y1 = (favoriteDay + 1) * dailyCap
            x2 = 1 if favoriteType == 0 else total[favoriteType - 1] + 1
            y2 = total[favoriteType]
            ans.append(not (x1 > y2 or y1 < x2))
        return ans


candiesCount = [7, 4, 5, 3, 8]
queries = [[0, 2, 2], [4, 2, 4], [2, 13, 1000000000]]
test = Solution()
print(test.canEat(candiesCount, queries))
