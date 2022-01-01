# -*- coding: utf-8 -*-
# File:      2022. 将一维数组转变成二维数组.py
# DATA:      2022/1/1
# Software:  PyCharm
__author__ = 'zcFang'

from typing import List


class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        return [original[i: i + n] for i in range(0, len(original), n)] if len(original) == m * n else []


original = [1, 2, 3, 4]
m, n = 4, 1
print(Solution().construct2DArray(original, m, n))
