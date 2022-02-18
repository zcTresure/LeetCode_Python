# -*- coding: utf-8 -*-
# File:    1791. 找出星型图的中心节点.py
# Date:    2022/2/18
# Software: Pycharm
__author__ = 'zcFang'

from typing import List


class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        n = len(edges) + 1
        degrees = [0] * (n + 1)
        for x, y in edges:
            degrees[x] += 1
            degrees[y] += 1
        for i, d in enumerate(degrees):
            if d == n - 1:
                return i


print(Solution().findCenter(edges=[[1, 2], [2, 3], [4, 2]]))
