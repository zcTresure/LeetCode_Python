# -*- coding: utf-8 -*-
# File:     1449. 数位成本和为目标值的最大数字.py
# Date:     2021/6/14
# Software: PyCharm
__author__ = 'zcFang'


class Solution:
    def largestNumber(self, cost: List[int], target: int) -> str:
        dp = [[float("-inf")] * (target + 1) for _ in range(10)]
        where = [[0] * (target + 1) for _ in range(10)]
        dp[0][0] = 0

        for i, c in enumerate(cost):
            for j in range(target + 1):
                if j < c:
                    dp[i + 1][j] = dp[i][j]
                    where[i + 1][j] = j
                else:
                    if dp[i][j] > dp[i + 1][j - c] + 1:
                        dp[i + 1][j] = dp[i][j]
                        where[i + 1][j] = j
                    else:
                        dp[i + 1][j] = dp[i + 1][j - c] + 1
                        where[i + 1][j] = j - c

        if dp[9][target] < 0:
            return "0"

        ans = list()
        i, j = 9, target
        while i > 0:
            if j == where[i][j]:
                i -= 1
            else:
                ans.append(str(i))
                j = where[i][j]

        return "".join(ans)
