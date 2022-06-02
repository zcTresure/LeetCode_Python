# -*- coding: utf-8 -*-
# File:      1493. 删掉一个元素以后全为 1 的最长子数组.py
# DATA:      2022/5/30
# Software:  PyCharm
__author__ = 'zcFang'

from typing import List


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        ans = cnt0 = cnt1 = 0
        for num in nums:
            if num == 0:
                cnt1 = cnt0
                cnt0 = 0
            else:
                cnt0 += 1
                cnt1 += 1
            ans = max(ans, cnt1)
        if ans == len(nums):
            ans -= 1
        return ans


print(Solution().longestSubarray(nums=[1, 1, 0, 1]))
print(Solution().longestSubarray(nums=[0, 1, 1, 1, 0, 0, 1, 1, 0, 1]))
print(Solution().longestSubarray(nums=[1, 1, 1]))
