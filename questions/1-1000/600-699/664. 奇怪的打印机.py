# -*- coding: utf-8 -*-
# File:     664. 奇怪的打印机.py
# Date:     2021/5/24
# Software: PyCharm
__author__ = 'zcFang'


class Solution:
    def strangePrinter(self, s: str) -> int:
        n = len(s)
        dp = [[float('inf')] * n for _ in range(n)]
        for i in range(n - 1, -1, -1):
            dp[i][i] = 1
            for j in range(i + 1, n):
                if s[i] == s[j]:
                    dp[i][j] = dp[i][j - 1]
                else:
                    for k in range(i, j):
                        dp[i][j] = min(dp[i][j], dp[i][k] + dp[k + 1][j])
        return dp[0][n - 1]


test = Solution()
print(test.strangePrinter('aaabcaba'))
