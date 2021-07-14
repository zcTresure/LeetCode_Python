# -*- coding: utf-8 -*-
# File:      1818. 绝对差值和.py
# DATA:      2021/7/14
# Software:  PyCharm
__author__ = 'zcFang'

from typing import List
from bisect import bisect_left


class Solution:
    def minAbsoluteSumDiff(self, nums1: List[int], nums2: List[int]) -> int:
        n, total, s1, ans = len(nums1), 0, sorted(nums1), float('inf')
        for i in range(n):
            diff = abs(nums1[i] - nums2[i])
            total += diff
            index = bisect_left(s1, nums2[i])
            if index:
                ans = min(ans, abs(s1[index - 1] - nums2[i]) - diff)
            if index < n:
                ans = min(ans, abs(s1[index] - nums2[i]) - diff)
        return (total + ans) % (10 ** 9 + 7) if total else total


nums1 = [1, 10, 4, 4, 2, 7]
nums2 = [9, 3, 5, 1, 7, 4]
print(Solution().minAbsoluteSumDiff(nums1, nums2))
