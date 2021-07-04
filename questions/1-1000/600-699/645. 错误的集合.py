# -*- coding: utf-8 -*-
# File:      645. 错误的集合.py
# DATA:      2021/7/4
# Software:  PyCharm
__author__ = 'zcFang'

from typing import List


class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        return [sum(nums) - sum(set(nums)), (1 + len(nums)) * len(nums) // 2 - sum(set(nums))]


nums = [1, 2, 3, 4, 4]
print(Solution().findErrorNums(nums))
