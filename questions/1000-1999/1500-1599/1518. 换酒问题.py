# -*- coding: utf-8 -*-
# File:      1518. 换酒问题.py
# DATA:      2021/12/17
# Software:  PyCharm
__author__ = 'zcFang'


class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        ans, bottle = numBottles, numBottles
        while bottle >= numExchange:
            bottle -= numExchange
            ans += 1
            bottle += 1
        return ans

    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        return (numBottles - numExchange) // (numExchange - 1) + 1 + numBottles if numBottles >= numExchange else numBottles


if __name__ == '__main__':
    numBottles = 15
    numExchange = 4
    print(Solution().numWaterBottles(numBottles, numExchange))
