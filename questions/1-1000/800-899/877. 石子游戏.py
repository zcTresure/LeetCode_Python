# -*- coding: utf-8 -*-
# File:     877. 石子游戏.py
# Date:     2021/6/16
# Software: PyCharm
__author__ = 'zcFang'

from typing import List


class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        length = len(piles)
        dp = [[0] * length for _ in range(length)]
        for i, pile in enumerate(piles):
            dp[i][i] = pile
        for i in range(length - 2, -1, -1):
            for j in range(i + 1, length):
                dp[i][j] = max(piles[i] - dp[i + 1][j], piles[j] - dp[i][j - 1])
        return dp[0][length - 1] > 0

    def stoneGame(self, piles: List[int]) -> bool:
        return True


print(Solution().stoneGame([5, 3, 4, 5]))
