# -*- coding: utf-8 -*-
# File:      1823. 找出游戏的获胜者.py
# DATA:      2022/1/4
# Software:  PyCharm
__author__ = 'zcFang'

from collections import deque


class Solution:
    # 递归
    def findTheWinner(self, n: int, k: int) -> int:
        if n == 1: return 1
        ans = self.findTheWinner(n - 1, k) + k
        return n if ans % n == 0 else ans % n

    # 动态规划
    def findTheWinner(self, n: int, k: int) -> int:
        dp = [0] + [1] + [0] * (n - 1)
        for i in range(2, n + 1):
            dp[i] = ((dp[i - 1] + k - 1) % i) + 1
        return dp[n]

    # 动态规划 + 空间优化
    def findTheWinner(self, n: int, k: int) -> int:
        luckier = 1
        for i in range(2, n + 1):
            luckier = (luckier + k - 1) % i + 1
        return luckier


n = 5
k = 2
print(Solution().findTheWinner(n, k))
