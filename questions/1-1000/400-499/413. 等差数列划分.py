# -*- coding: utf-8 -*-
# File:      413. 等差数列划分.py
# DATA:      2021/8/10
# Software:  PyCharm
__author__ = 'zcFang'

from typing import List


class Solution:
    @classmethod
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return 0
        ans = 0
        diff, tmp = nums[1] - nums[0], 0
        for i in range(2, n):
            if nums[i] - nums[i - 1] == diff:
                tmp += 1
            else:
                diff = nums[i] - nums[i - 1]
                tmp = 0
            ans += tmp
        return ans


nums = [1, 2, 3, 8, 9, 10]
print(Solution.numberOfArithmeticSlices(nums))
