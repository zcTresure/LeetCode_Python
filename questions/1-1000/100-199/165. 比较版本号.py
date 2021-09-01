# -*- coding: utf-8 -*-
# File:      165. 比较版本号.py
# DATA:      2021/9/1
# Software:  PyCharm
__author__ = 'zcFang'

from itertools import zip_longest


class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        for v1, v2 in zip_longest(version1.split('.'), version2.split('.'), fillvalue=0):
            print(v1, v2)
            x, y = int(v1), int(v2)
            if x != y:
                return 1 if x > y else -1
        return 0


version1 = "1.01"
version2 = "1.001.0"
print(Solution().compareVersion(version1, version2))
