# -*- coding: utf-8 -*-
# File:      33. 搜索旋转排序数组.py
# DATA:      2021/12/22
# Software:  PyCharm

from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        if n == 0:
            return -1
        if n == 1:
            return 0 if nums[0] == target else -1
        left, right = 0, n - 1
        while left <= right:
            mid = (left + right) // 2
            if (nums[mid] == target):
                return mid
            if nums[mid] >= nums[0]:
                if nums[0] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] < target <= nums[n - 1]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1


nums = [4, 5, 6, 7, 0, 1, 2, 3]
target = 0
print(Solution().search(nums, target))
