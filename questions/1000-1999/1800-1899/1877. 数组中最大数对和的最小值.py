# -*- coding: utf-8 -*-
# File:    1877. 数组中最大数对和的最小值.py
# Date:    2021/7/20
# Software: Pycharm
__author__ = 'zcFang'

from typing import List


class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        res, n = 0, len(nums)
        for i in range(0, n // 2):
            res = max(res, nums[i] + nums[n - i - 1])
        return res


nums = [3, 5, 2, 3]
print(Solution().minPairSum(nums))
