# -*- coding: utf-8 -*-
# File:    540. 有序数组中的单一元素.py
# Date:    2022/2/14
# Software: Pycharm
__author__ = 'zcFang'

from typing import List


class Solution:
    # 顺序查找
    def singleNonDuplicate(self, nums: List[int]) -> int:
        for i in range(1, len(nums), 2):
            if nums[i] != nums[i - 1]:
                return nums[i - 1]

    # 全数组的二分查找
    def singleNonDuplicate(self, nums: List[int]) -> int:
        low, high = 0, len(nums) - 1
        while low < high:
            mid = (high - low) // 2 + low
            if nums[mid] == nums[mid ^ 1]:
                low = mid + 1
            else:
                high = mid
        return nums[low]

    # 偶数下标的二分查找
    def singleNonDuplicate(self, nums: List[int]) -> int:
        low, high = 0, len(nums) - 1
        while low < high:
            mid = (low + high) // 2
            mid -= mid & 1
            if nums[mid] == nums[mid + 1]:
                low = mid + 2
            else:
                high = mid
        return nums[low]


print(Solution().singleNonDuplicate(nums=[1, 1, 2, 2, 3, 4, 4, 5, 5]))
