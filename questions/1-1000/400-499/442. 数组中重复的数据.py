# -*- coding: utf-8 -*-
# File:      442. 数组中重复的数据.py
# DATA:      2022/5/8
# Software:  PyCharm
__author__ = 'zcFang'

from typing import List


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            while nums[i] != nums[nums[i] - 1]:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
        return [num for i, num in enumerate(nums) if num - 1 != i]

    def findDuplicates(self, nums: List[int]) -> List[int]:
        ans = []
        for x in nums:
            x = abs(x)
            if nums[x - 1] > 0:
                nums[x - 1] = -nums[x - 1]
            else:
                ans.append(x)
        return ans


nums = [4, 3, 2, 7, 8, 2, 3, 1]
print(Solution().findDuplicates(nums))
