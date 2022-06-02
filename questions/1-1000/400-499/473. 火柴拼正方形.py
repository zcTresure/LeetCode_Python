# -*- coding: utf-8 -*-
# File:      473. 火柴拼正方形.py
# DATA:      2022/6/1
# Software:  PyCharm
__author__ = 'zcFang'

from typing import List


class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        total = sum(matchsticks)
        if total % 4 != 0:
            return False
        matchsticks.sort(reverse=True)
        edges = [0] * 4

        def dfs(idx: int) -> bool:
            if idx == len(matchsticks):
                return True
            for i in range(4):
                edges[i] += matchsticks[idx]
                if edges[i] <= total // 4 and dfs(idx + 1):
                    return True
                edges[i] -= matchsticks
            return False

        return dfs(0)

    def makesquare(self, matchsticks: List[int]) -> bool:
        total = sum(matchsticks)
        edge_len = total // 4
        if total % 4 != 0:
            return False
        dp = [-1] * (1 << len(matchsticks))
        dp[0] = 0
        for s in range(1, len(dp)):
            for k, v in enumerate(matchsticks):
                if s & (1 << k) == 0:
                    continue
                s1 = s & ~(1 << k)
                if dp[s1] >= 0 and (dp[s1] + v) <= edge_len:
                    dp[s] = (dp[s1] + v) % edge_len
                    break
        return dp[-1] == 0


print(Solution().makesquare(matchsticks=[1, 1, 1, 1]))
print(Solution().makesquare(matchsticks=[1, 1, 2, 2, 2]))
print(Solution().makesquare(matchsticks=[1, 1, 2, 2, 3]))
