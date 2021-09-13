# -*- coding: utf-8 -*-
# File:      1005. K 次取反后最大化的数组和.py
# DATA:      2021/9/13
# Software:  PyCharm
__author__ = 'zcFang'

import heapq
from typing import List


class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        for _ in range(k):
            heapq.heappush(nums, -heapq.heappop(nums))
        return sum(nums)


nums = [0, -1, 2, 3, 4, -3, -2]
print(Solution().largestSumAfterKNegations(nums, 3))
