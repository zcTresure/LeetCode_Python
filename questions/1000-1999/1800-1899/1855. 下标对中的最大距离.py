# -*- coding: utf-8 -*-
# File:      1855. 下标对中的最大距离.py
# DATA:      2022/6/18
# Software:  PyCharm
from typing import List


class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        n1, n2 = len(nums1), len(nums2)
        i, ans = 0, 0
        for j in range(n2):
            while i < n1 and nums1[i] > nums2[j]:
                i += 1
            if i < n1:
                ans = max(ans, j - i)
        return ans


print(Solution().maxDistance(nums1=[55, 30, 5, 4, 2], nums2=[100, 20, 10, 10, 5]))
