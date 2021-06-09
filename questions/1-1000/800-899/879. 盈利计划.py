# -*- coding: utf-8 -*-
# File:     879. 盈利计划.py
# Date:     2021/6/9
# Software: PyCharm
__author__ = 'zcFang'

from typing import List


class Solution:
    def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
        MOD = 10 ** 9 + 7
        length = len(group)
        dp = [[[0] * (minProfit + 1) for _ in range(n + 1)] for _ in range(length + 1)]
        dp[0][0][0] = 1
        for i in range(1, length + 1):
            members, earn = group[i - 1], profit[i - 1]
            for j in range(n + 1):
                for k in range(minProfit + 1):
                    if j < members:
                        dp[i][j][k] = dp[i - 1][j][k]
                    else:
                        dp[i][j][k] = (dp[i - 1][j][k] + dp[i - 1][j - members][max(0, k - earn)]) % MOD
        total = sum(dp[length][j][minProfit] for j in range(n + 1))
        return total % MOD


n = 5
minProfit = 3
group = [2, 2]
profit = [2, 3]
print(Solution().profitableSchemes(n, minProfit, group, profit))
