# -*- coding: utf-8 -*-
# File:      62. 不同路径 II.py
# DATA:      2022/1/3
# Software:  PyCharm
__author__ = 'zcFang'

from math import comb


class Solution:
    # 动态规划
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[1] * n] + [[1] + [0] * (n - 1) for _ in range(m - 1)]
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[m - 1][n - 1]

    # 组合数学
    def uniquePaths(self, m: int, n: int) -> int:
        return comb(m + n - 2, n - 1)


m, n = 3, 7
print(Solution().uniquePaths(m, n))
