# -*- coding: utf-8 -*-
# File:      504. 七进制数.py
# DATA:      2022/3/7
# Software:  PyCharm
__author__ = 'zcFang'


class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return "0"
        negative = num < 0
        num = abs(num)
        digits = []
        while num:
            digits.append(str(num % 7))
            num //= 7
        if negative:
            digits.append('-')
        return ''.join(reversed(digits))



print(Solution().convertToBase7(num=100))
