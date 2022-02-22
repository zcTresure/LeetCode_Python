# -*- coding: utf-8 -*-
# File:      717. 1 比特与 2 比特字符.py
# DATA:      2022/2/21
# Software:  PyCharm
__author__ = 'zcFang'

from typing import List


class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        index, n = 0, len(bits)
        while index < n - 1:
            index += bits[index] + 1
        return index == n - 1


print(Solution().isOneBitCharacter(bits=[1, 0, 0]))
