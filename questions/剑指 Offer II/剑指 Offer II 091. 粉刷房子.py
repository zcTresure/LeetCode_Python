# -*- coding: utf-8 -*-
# File:      剑指 Offer II 091. 粉刷房子.py
# DATA:      2022/6/25
# Software:  PyCharm
from typing import List


class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        dp = costs[0]
        for i in range(1, len(costs)):
            dp = [min(dp[j - 1], dp[j - 2]) + c for j, c in enumerate(costs[i])]
        return min(dp)


print(Solution().minCost(costs=[[17, 2, 17], [16, 16, 5], [14, 3, 19]]))
print(Solution().minCost(costs=[[7, 6, 2]]))
