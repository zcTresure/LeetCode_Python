# -*- coding: utf-8 -*-
# File:      598. 范围求和 II.py
# DATA:      2021/11/7
# Software:  PyCharm
__author__ = 'zcFang'

from typing import List


class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        mina, minb = m, n
        for a, b in ops:
            mina = min(mina, a)
            minb = min(minb, b)
        return mina * minb


m = 3
n = 3
operations = [[2, 2], [3, 3]]
print(Solution().maxCount(m, n, operations))
