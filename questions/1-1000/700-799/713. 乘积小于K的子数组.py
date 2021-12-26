# -*- coding: utf-8 -*-
# File:    713. 乘积小于K的子数组.py
# Date:    2021/12/26
# Software: Pycharm
__author__ = 'zcFang'

from typing import List


class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0
        ans, product = 0, 1
        left = 0
        for right, val in enumerate(nums):
            product *= val
            while product >= k:
                product //= nums[left]
                left += 1
            ans += right - left + 1
        return ans


nums = [10, 5, 2, 6]
k = 100
print(Solution().numSubarrayProductLessThanK(nums, k))
