# -*- coding: utf-8 -*-
# File:      896. 单调数列.py
# DATA:      2021/9/10
# Software:  PyCharm
__author__ = 'zcFang'

from typing import List


class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        up = down = True
        for i in range(1, len(nums)):
            if nums[i - 1] > nums[i]:
                up = False
            if nums[i - 1] < nums[i]:
                down = False
        return up or down

nums = [1,2,2,3]
print(Solution().isMonotonic(nums))
