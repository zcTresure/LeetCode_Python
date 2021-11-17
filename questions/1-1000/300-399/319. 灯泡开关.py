# -*- coding: utf-8 -*-
# File:      319. 灯泡开关.py
# DATA:      2021/11/15
# Software:  PyCharm
__author__ = 'zcFang'

from cmath import sqrt


class Solution:
    def bulbSwitch(self, n: int) -> int:
        return int(sqrt(n + 0.5))


print(Solution().bulbSwitch(10))
