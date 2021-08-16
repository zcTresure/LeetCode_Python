# -*- coding: utf-8 -*-
# File:      526. 优美的排列.py
# DATA:      2021/8/16
# Software:  PyCharm
__author__ = 'zcFang'

from collections import defaultdict


class Solution:
    @classmethod
    def countArrangement(self, n: int) -> int:
        match = defaultdict(list)
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if i % j == 0 or j % i == 0:
                    match[i].append(j)
        res = 0
        vis = set()

        def backtrack(index: int) -> None:
            if index == n + 1:
                nonlocal res
                res += 1
                return
            for x in match[index]:
                if x not in vis:
                    vis.add(x)
                    backtrack(index+1)
                    vis.discard(x)

        backtrack(1)
        return res


print(Solution.countArrangement(10))
