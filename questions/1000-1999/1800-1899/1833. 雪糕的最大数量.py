# -*- coding: utf-8 -*-
# File:     1833. 雪糕的最大数量.py
# Date:     2021/7/2
# Software: PyCharm
__author__ = 'zcFang'


class Solution(object):
    def maxIceCream(self, costs, coins):
        """
        :type costs: List[int]
        :type coins: int
        :rtype: int
        """
        costs.sort()
        res, money = 0, 0
        for cost in costs:
            if cost <= coins:
                res += 1
                coins -= cost
            else:
                break
        return res


costs = [1, 3, 2, 4, 1]
coins = 7
print(Solution().maxIceCream(costs, coins))
