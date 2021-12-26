# -*- coding: utf-8 -*-
# File:    334. 递增的三元子序列.py
# Date:    2021/12/26
# Software: Pycharm
__author__ = 'zcFang'

from typing import List


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        n = len(nums)
        if n < 3: return False
        small = mid = float('inf')
        for num in nums:
            if num <= small:
                small = num
            elif num <= mid:
                mid = num
            elif num > mid:
                return True
        return False

# nums = [1, 2, 3, 4, 5]
nums = [2, 1, 5, 0, 4, 6]
print(Solution().increasingTriplet(nums))
