# -*- coding: utf-8 -*-
# File:     1035. 不相交的线.py
# Date:     2021/5/21
# Software: PyCharm
__author__ = 'zcFang'

from typing import List


class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        m, n = len(nums1), len(nums2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i, num1 in enumerate(nums1):
            for j, num2 in enumerate(nums2):
                if num1 == num2:
                    dp[i + 1][j + 1] = dp[i][j] + 1
                else:
                    dp[i + 1][j + 1] = max(dp[i][j + 1], dp[i + 1][j])
        return dp[m][n]


nums1 = [1, 3, 7, 1, 7, 5]
nums2 = [1, 9, 2, 5, 1]
test = Solution()
print(test.maxUncrossedLines(nums1, nums2))
