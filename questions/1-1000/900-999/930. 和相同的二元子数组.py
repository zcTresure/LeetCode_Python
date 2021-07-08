# -*- coding: utf-8 -*-
# File:      930. 和相同的二元子数组.py
# DATA:      2021/7/8
# Software:  PyCharm
__author__ = 'zcFang'

from typing import List
from collections import defaultdict, Counter


class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        sub_sum, res = 0, 0
        counters = defaultdict()
        for num in nums:
            counters[sub_sum] = 1 if sub_sum not in counters else counters[sub_sum] + 1
            sub_sum += num
            res += 0 if sub_sum - goal not in counters else counters[sub_sum - goal]
        print(counters)
        return res

    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        sub_sum, res = 0, 0
        counters = Counter({0: 1})
        for num in nums:
            sub_sum += num
            res += counters[sub_sum - goal]
            counters[sub_sum] += 1
        return res


nums = [1, 0, 1, 0, 1]
goal = 2
print(Solution().numSubarraysWithSum(nums, goal))
