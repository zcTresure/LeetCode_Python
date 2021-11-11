# -*- coding: utf-8 -*-
# File:      1218. 最长定差子序列.py
# DATA:      2021/11/5
# Software:  PyCharm
__author__ = 'zcFang'

from typing import List
from collections import defaultdict


class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        dp = defaultdict(int)
        for val in arr:
            dp[val] = dp[val - difference] + 1
        print(dp)
        return max(dp.values())


arr = [1, 2, 3, 4, 5]
difference = 1
print(Solution().longestSubsequence(arr, difference))
