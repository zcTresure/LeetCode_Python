# -*- coding: utf-8 -*-
# File:    1220. 统计元音字母序列的数目.py
# Date:    2022/1/17
# Software: Pycharm
__author__ = 'zcFang'

import numpy as np


class Solution:
    def countVowelPermutation(self, n: int) -> int:
        MOD = 1000000007
        dp = [1, 1, 1, 1, 1]
        for _ in range(n - 1):
            dp = [(dp[1] + dp[2] + dp[4]) % MOD, (dp[0] + dp[2]) % MOD, (dp[1] + dp[3]) % MOD, dp[2],
                  (dp[2] + dp[3]) % MOD]
        return sum(dp) % MOD

    def countVowelPermutation(self, n: int) -> int:
        factor = np.mat([(0, 1, 0, 0, 0), (1, 0, 1, 0, 0), (1, 1, 0, 1, 1), (0, 0, 1, 0, 1), (1, 0, 0, 0, 0)],
                        np.dtype('O'))
        res = np.mat([(1, 1, 1, 1, 1)], np.dtype('O'))
        n -= 1
        while n > 0:
            if n % 2 == 1:
                res = res * factor % 1000000007
            factor = factor * factor % 1000000007
            n = n // 2
        return res.sum() % 1000000007


print(Solution().countVowelPermutation(n=5))
