# -*- coding: utf-8 -*-
# File:      166. 分数到小数.py
# DATA:      2021/10/8
# Software:  PyCharm
__author__ = 'zcFang'


class Solution:
    # 长除法
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator % denominator == 0:
            return str(numerator // denominator)

        s = []
        if (numerator < 0) != (denominator < 0):
            s.append('-')

        # 整数部分
        numerator = abs(numerator)
        denominator = abs(denominator)
        integerPart = numerator // denominator
        s.append(str(integerPart))
        s.append('.')

        # 小数部分
        indexMap = {}
        remainder = numerator % denominator
        while remainder and remainder not in indexMap:
            indexMap[remainder] = len(s)
            remainder *= 10
            s.append(str(remainder // denominator))
            remainder %= denominator
        if remainder:  # 有循环节
            insertIndex = indexMap[remainder]
            s.insert(insertIndex, '(')
            s.append(')')

        return ''.join(s)


numerator = 1
denominator = 2
print()
