# -*- coding: utf-8 -*-
# File:      594. 最长和谐子序列.py
# DATA:      2021/11/20
# Software:  PyCharm
__author__ = 'zcFang'

from typing import List

from collections import Counter


class Solution:
    def findLHS(self, nums: List[int]) -> int:
        nums.sort()
        maxLength = begin = 0
        for end in range(len(nums)):
            while nums[end] - nums[begin] > 1:
                begin += 1
            if nums[end] - nums[begin] == 1:
                maxLength = max(maxLength, end - begin + 1)
        return maxLength

    # 哈希表
    def findLHS(self, nums: List[int]) -> int:
        cnt = Counter(nums)
        return max((val + cnt[key + 1] for key, val in cnt.items() if key + 1 in cnt), default=0)


nums = [1, 2, 3, 2, 1, 1, 3, 21, 3, 4, 123, 4, 2]
print(Solution().findLHS(nums))
