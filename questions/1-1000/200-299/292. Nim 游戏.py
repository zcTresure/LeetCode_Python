# -*- coding: utf-8 -*-
# File:      292. Nim 游戏.py
# DATA:      2021/9/18
# Software:  PyCharm
__author__ = 'zcFang'


class Solution:
    def canWinNim(self, n: int) -> bool:
        return n % 4 != 0
