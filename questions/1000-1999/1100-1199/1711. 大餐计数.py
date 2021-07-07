# -*- coding: utf-8 -*-
# File:      1711. 大餐计数.py
# DATA:      2021/7/7
# Software:  PyCharm
__author__ = 'zcFang'

from typing import List
from collections import Counter


class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        cnts = Counter(deliciousness)
        return (sum(cnts[key] * (cnts[key] - 1) if key == 2 ** (i - 1) else cnts[key] * cnts[2 ** i - key]
                    for key in cnts for i in range(22)) // 2) % (10 ** 9 + 7)

    powersOfTwo = [2 ** i for i in range(22)]
    mod = 10 ** 9 + 7

    def countPairs(self, deliciousness: List[int]) -> int:
        cnts = Counter(deliciousness)
        return (sum(cnts[key] * (cnts[key] - 1) if key == target - key else cnts[key] * cnts[target - key]
                    for key in cnts for target in self.powersOfTwo)) // 2 % self.mod


delicioisness = [1, 3, 5, 7, 9]
print(Solution().countPairs(delicioisness))
