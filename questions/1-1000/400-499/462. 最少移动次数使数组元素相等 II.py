# -*- coding: utf-8 -*-
# File:      462. 最少移动次数使数组元素相等 II.py
# DATA:      2022/5/19
# Software:  PyCharm
__author__ = 'zcFang'

from datetime import time
from random import randint, seed
from typing import List


class Helper:
    @staticmethod
    def partition(nums: List[int], left: int, right: int) -> int:
        pivot = nums[right]
        i = left - 1
        for j in range(left, right):
            if nums[j] <= pivot:
                i += 1
                nums[i], nums[j] = nums[j], nums[i]
        nums[i + 1], nums[right] = nums[right], nums[i + 1]
        return i + 1

    @staticmethod
    def randomPartition(nums: List[int], left: int, right: int) -> int:
        i = randint(left, right)
        nums[right], nums[i] = nums[i], nums[right]
        return Helper.partition(nums, left, right)

    @staticmethod
    def quickSelected(nums: List[int], left: int, right: int, k: int) -> int:
        index = Helper.randomPartition(nums, left, right)
        if k == index:
            return nums[k]
        if k < index:
            return Helper.quickSelected(nums, left, index - 1, k)
        return Helper.quickSelected(nums, index + 1, right, k)


class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()
        return sum(abs(num - nums[len(nums) // 2]) for num in nums)

    def minMoves2(self, nums: List[int]) -> int:
        seed(time())
        x = Helper.quickSelected(nums, 0, len(nums) - 1, len(nums) // 2)
        return sum(abs(num - x) for num in nums)


print(Solution().minMoves2(nums=[1, 2, 3]))
