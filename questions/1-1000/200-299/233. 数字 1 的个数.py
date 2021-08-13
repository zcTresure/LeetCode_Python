# -*- coding: utf-8 -*-
# File:      233. 数字 1 的个数.py
# DATA:      2021/8/13
# Software:  PyCharm
__author__ = 'zcFang'


class Solution:
    @classmethod
    def countDigitOne(self, n: int) -> int:
        k, mulk, ans = 0, 1, 0
        while n >= mulk:
            ans += (n // (mulk * 10)) * mulk + min(max(n % (mulk * 10) - mulk + 1, 0), mulk)
            k += 1
            mulk *= 10
        return ans


print(Solution.countDigitOne(13))
