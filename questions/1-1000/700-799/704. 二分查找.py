# -*- coding: utf-8 -*-
# File:      704. 二分查找.py
# DATA:      2021/9/6
# Software:  PyCharm
__author__ = 'zcFang'

from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (right - left) // 2 + left
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1
