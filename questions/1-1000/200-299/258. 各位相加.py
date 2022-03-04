# -*- coding: utf-8 -*-
# File:      258. 各位相加.py
# DATA:      2022/3/3
# Software:  PyCharm
__author__ = 'zcFang'


class Solution:
    def addDigits(self, num: int) -> int:
        while num >= 10:
            tmp = 0
            while num > 0:
                tmp += num % 10
                num //= 10
            num = tmp
        return num


print(Solution().addDigits(num=38))
