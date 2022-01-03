# -*- coding: utf-8 -*-
# File:      55. 跳跃游戏.py
# DATA:      2022/1/2
# Software:  PyCharm
__author__ = 'zcFang'

from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        k = 0
        for i in range(len(nums)):
            if i > k:
                return False
            k = max(k, i + nums[i])
        return True


nums = [2, 3, 1, 1, 4]
print(Solution().canJump(nums))
