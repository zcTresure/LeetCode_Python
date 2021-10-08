# -*- coding: utf-8 -*-
# File:      414. 第三大的数.py
# DATA:      2021/10/8
# Software:  PyCharm
__author__ = 'zcFang'

from typing import List


class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        a, b, c = None, None, None
        for num in nums:
            if a is None or num > a:
                a, b, c = num, a, b
            elif a > num and (b is None or num > b):
                b, c = num, b
            elif b is not None and b > num and (c is None or num > c):
                c = num
        return a if c is None else c


nums = [3, 2, 1]
print(Solution().thirdMax(nums))
