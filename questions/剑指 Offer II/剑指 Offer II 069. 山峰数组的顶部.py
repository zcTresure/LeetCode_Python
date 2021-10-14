# -*- coding: utf-8 -*-
# File:      剑指 Offer II 069. 山峰数组的顶部.py
# DATA:      2021/10/14
# Software:  PyCharm
__author__ = 'zcFang'

from typing import List


class Solution:
    # 顺序查找
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        ans = 0
        for i in range(1, len(arr)):
            if arr[i - 1] > arr[i]:
                ans = i - 1
                break
        return ans

    # 二分查找
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        left, right = 1, len(arr) - 2
        ans = 0
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] > arr[mid + 1]:
                ans = mid
                right = mid - 1
            else:
                left = mid + 1

        return ans


nums = [1, 3, 5, 4, 2]
print(Solution().peakIndexInMountainArray(nums))
