# -*- coding: utf-8 -*-
# File:      905. 按奇偶排序数组.py
# DATA:      2022/4/28
# Software:  PyCharm
__author__ = 'zcFang'

from typing import List


class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        left, right = 0, len(nums) - 1
        while left <= right:
            while left < right and nums[left] % 2 == 0:
                left += 1
            while left < right and nums[right] % 2 != 0:
                right -= 1
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
        return nums


print(Solution().sortArrayByParity(nums=[1, 2, 3, 4]))
print(Solution().sortArrayByParity(nums=[0]))
