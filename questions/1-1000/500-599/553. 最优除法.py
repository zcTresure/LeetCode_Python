# -*- coding: utf-8 -*-
# File:      553. 最优除法.py
# DATA:      2022/2/27
# Software:  PyCharm
__author__ = 'zcFang'

from typing import List


class Solution:
    # 数学
    def optimalDivision(self, nums: List[int]) -> str:
        if len(nums) == 1:
            return str(nums)
        elif len(nums) == 2:
            return str(nums[0]) + '/' + str(nums[1])
        else:
            return str(nums[0]) + '/(' + '/'.join(map(str, nums[1:])) + ')'


nums = [100, 100, 10, 2]
print(Solution().optimalDivision(nums))
