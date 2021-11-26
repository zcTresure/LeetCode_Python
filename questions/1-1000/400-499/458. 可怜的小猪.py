# -*- coding: utf-8 -*-
# File:      458. 可怜的小猪.py
# DATA:      2021/11/25
# Software:  PyCharm
__author__ = 'zcFang'

from math import ceil, log


class Solution:
    # 动态规划
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        if buckets == 1:
            return 0
        combinations = [[0] * (buckets + 1) for _ in range(buckets + 1)]
        combinations[0][0] = 1
        iterations = minutesToTest // minutesToDie
        f = [[1] * (iterations + 1)] + [[1] + [0] * iterations for _ in range(buckets - 1)]
        for i in range(1, buckets):
            combinations[i][0] = 1
            for j in range(1, i):
                combinations[i][j] = combinations[i - 1][j - 1] + combinations[i - 1][j]
            combinations[i][i] = 1
            for j in range(1, iterations + 1):
                for k in range(i + 1):
                    f[i][j] += f[k][j - 1] * combinations[i][i - k]
            if f[i][iterations] >= buckets:
                return i
        return 0

    # 香农熵
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        k = minutesToTest / minutesToDie
        return ceil(log(buckets) / log(k))


buckets = 1000
minutesToDie = 15
minutesToTest = 60
print(Solution().poorPigs(buckets, minutesToDie, minutesToTest))
