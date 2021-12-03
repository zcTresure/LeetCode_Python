# -*- coding: utf-8 -*-
# File:      1005. K 次取反后最大化的数组和.py
# DATA:      2021/9/13
# Software:  PyCharm
__author__ = 'zcFang'

import heapq
from collections import Counter
from typing import List


class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        freq = Counter(nums)
        ans = sum(nums)
        for i in range(-100, 0):
            if freq[i]:
                ops = min(k, freq[i])
                ans += -i * ops * 2
                freq[i] -= ops
                freq[-i] += ops
                k -= ops
                if k == 0:
                    break

        if k > 0 and k % 2 == 1 and not freq[0]:
            for i in range(1, 101):
                if freq[i]:
                    ans -= i * 2
                    break

        return ans

    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        for _ in range(k):
            heapq.heappush(nums, -heapq.heappop(nums))
        return sum(nums)


nums = [0, -1, 2, 3, 4, -3, -2]
print(Solution().largestSumAfterKNegations(nums, 3))
