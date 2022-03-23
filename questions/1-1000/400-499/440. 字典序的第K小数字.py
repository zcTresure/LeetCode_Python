# -*- coding: utf-8 -*-
# File:      440. 字典序的第K小数字.py
# DATA:      2022/3/23
# Software:  PyCharm
__author__ = 'zcFang'


class Solution:
    def getSteps(self, cur: int, n: int) -> int:
        step, first, last = 0, cur, cur
        while first <= n:
            step += min(last, n) - first + 1
            first *= 10
            last = last * 10 + 9
        return step

    def findKthNumber(self, n: int, k: int) -> int:
        cur = 1
        k -= 1
        while k:
            steps = self.getSteps(cur, n)
            if steps <= k:
                k -= steps
                cur += 1
            else:
                cur *= 10
                k -= 1
        return cur


print(Solution().findKthNumber(n=13, k=2))
