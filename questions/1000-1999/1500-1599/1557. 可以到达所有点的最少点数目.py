# -*- coding: utf-8 -*-
# File:    1557. 可以到达所有点的最少点数目.py
# Date:    2022/1/9
# Software: Pycharm
__author__ = 'zcFang'

from typing import List


class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        endSet = set(y for x, y in edges)
        ans = [i for i in range(n) if i not in endSet]
        return ans


n = 6
edges = [[0, 1], [0, 2], [2, 5], [3, 4], [4, 2]]
print(Solution().findSmallestSetOfVertices(n, edges))
