# -*- coding: utf-8 -*-
# File:      357. 统计各位数字都不同的数字个数.py
# DATA:      2022/4/11
# Software:  PyCharm
__author__ = 'zcFang'


class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n == 0:
            return 1
        if n == 1:
            return 10
        res, cur = 10, 9
        for i in range(n - 1):
            cur *= 9 - i
            res += cur
        return res

print(Solution().countNumbersWithUniqueDigits(n=2))