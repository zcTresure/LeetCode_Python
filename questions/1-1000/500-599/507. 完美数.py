# -*- coding: utf-8 -*-
# File:      507. 完美数.py
# DATA:      2021/12/31
# Software:  PyCharm
__author__ = 'zcFang'


class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num == 1:
            return False
        d_sum = 1
        d = 2
        while d * d <= num:
            if num % d == 0:
                d_sum += d
                if d * d < num:
                    d_sum += num // d
            d += 1
        return d_sum == num

print(Solution().checkPerfectNumber(6))
