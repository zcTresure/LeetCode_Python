# -*- coding: utf-8 -*-
# File:      300. 最长递增子序列.py
# DATA:      2022/1/6
# Software:  PyCharm
__author__ = 'zcFang'

from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0: return 0
        dp = []
        for i in range(n):
            dp.append(1)
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)


nums = [0, 1, 0, 3, 2, 3]
print(Solution().lengthOfLIS(nums))
