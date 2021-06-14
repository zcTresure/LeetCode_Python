# -*- coding: utf-8 -*-
# File:     279. 完全平方数.py
# Date:     2021/6/11
# Software: PyCharm
__author__ = 'zcFang'

from math import sqrt


class Solution:
    def numSquares(self, n: int) -> int:
        dp = [0] * (n + 1)
        for i in range(1, n + 1):
            minn = float('inf')
            for j in range(1, int(sqrt(i)) + 1):
                minn = min(minn, dp[i - j * j])
            dp[i] = minn + 1
        return dp[n]


n = 12
print(Solution().numSquares(n))
