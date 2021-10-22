# -*- coding: utf-8 -*-
# File:      66. 加一.py
# DATA:      2021/10/21
# Software:  PyCharm
__author__ = 'zcFang'

from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits = [0] + digits
        digit = 1
        for i in range(len(digits) - 1, -1, -1):
            tmp = digits[i]
            digits[i] = (digit + tmp) % 10
            digit = (digit + tmp) // 10
        return digits if digits[0] > 0 else digits[1:]


nums = [1, 2, 3]
print(Solution().plusOne(nums))
