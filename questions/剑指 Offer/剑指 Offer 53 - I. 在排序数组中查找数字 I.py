# -*- coding: utf-8 -*-
# File:    剑指 Offer 53 - I. 在排序数组中查找数字 I.py
# Date:    2021/7/16
# Software: Pycharm
__author__ = 'zcFang'

from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return self.helper(nums, target) - self.helper(nums, target - 1)

    def helper(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (right - left) // 2 + left
            if nums[mid] <= target:
                left = mid + 1
            else:
                right = mid - 1
        return left


nums = [5, 6, 7, 8, 8, 8, 9, 9]
target = 8
print(Solution().search(nums, target))
