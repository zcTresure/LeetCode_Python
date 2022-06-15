# -*- coding: utf-8 -*-
# File:      1608. 特殊数组的特征值.py
# DATA:      2022/6/15
# Software:  PyCharm
from typing import List


class Solution:
    def specialArray(self, nums: List[int]) -> int:
        left, right = 0, len(nums)
        while left <= right:
            mid = (right - left) // 2 + left
            count = len([num for num in nums if num >= mid])
            if count > mid:
                left = mid + 1
            elif count < mid:
                right = mid - 1
            else:
                return mid
        return -1


print(Solution().specialArray(nums=[3, 5]))
print(Solution().specialArray(nums=[0, 4, 3, 0, 4]))
