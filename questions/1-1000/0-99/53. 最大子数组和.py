# -*- coding: utf-8 -*-
# File:      53. 最大子数组和.py
# DATA:      2021/12/8
# Software:  PyCharm
__author__ = 'zcFang'

from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans, tmp = nums[0], 0
        for num in nums:
            tmp = max(num, num + tmp)
            ans = max(ans, tmp)
        return ans


nums = [5, 4, -1, 7, 8]
print(Solution().maxSubArray(nums))
