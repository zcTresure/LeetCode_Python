# -*- coding: utf-8 -*-
# File:     518. 零钱兑换 II.py
# Date:     2021/6/10
# Software: PyCharm
__author__ = 'zcFang'

from typing import List


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        coins.sort()
        dp = [1] + [0] * amount
        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] += dp[i - coin]
        return dp[amount]


amount = 5
coins = [1, 2, 5]
print(Solution().change(amount, coins))
