# -*- coding: utf-8 -*-
# File:      2016. 增量元素之间的最大差值.py
# DATA:      2022/2/27
# Software:  PyCharm
__author__ = 'zcFang'

from typing import List


class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        prefix = float("inf")
        ans = -1
        for num in nums:
            prefix = min(prefix, num)
            if prefix < num:
                ans = max(ans, num - prefix)
        return ans


nums = [3, 1, 2, 4, 5]
print(Solution().maximumDifference(nums))
