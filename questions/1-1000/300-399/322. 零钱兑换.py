# -*- coding: utf-8 -*-
# File:    322. 零钱兑换.py
# Date:    2022/1/8
# Software: Pycharm
__author__ = 'zcFang'

from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0

        for coin in coins:
            for x in range(coin, amount + 1):
                dp[x] = min(dp[x], dp[x - coin] + 1)
        return dp[amount] if dp[amount] != float('inf') else -1


coins = [1, 2, 5]
amount = 11
print(Solution().coinChange(coins, amount))
