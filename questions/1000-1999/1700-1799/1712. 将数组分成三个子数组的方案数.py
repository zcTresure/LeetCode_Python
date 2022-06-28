# -*- coding: utf-8 -*-
# File:      1712. 将数组分成三个子数组的方案数.py
# DATA:      2022/6/28
# Software:  PyCharm
from bisect import bisect_left, bisect_right
from itertools import accumulate
from typing import List


class Solution:
    def waysToSplit(self, nums: List[int]) -> int:
        pre_sum = list(accumulate(nums))
        # print(pre_sum)
        n = len(nums)
        ans = 0
        for i in range(n - 2):
            left = bisect_left(pre_sum, 2 * pre_sum[i], i + 1, n - 1)
            right = bisect_right(pre_sum, (pre_sum[i] + pre_sum[-1]) / 2, left, n - 1)
            print(left,right)
            ans = (ans + right - left) % (10 ** 9 + 7)
        return ans

print(Solution().waysToSplit(nums=[1, 1, 1]))
# print(Solution().waysToSplit(nums=[1, 2, 2, 2, 5, 0]))
# print(Solution().waysToSplit(nums=[3, 2, 1]))
print(Solution().waysToSplit(nums=[7, 2, 5, 5, 6, 2, 10, 9]))
