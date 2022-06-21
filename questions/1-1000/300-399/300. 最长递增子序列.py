# -*- coding: utf-8 -*-
# File:      300. 最长递增子序列.py
# DATA:      2022/1/6
# Software:  PyCharm
__author__ = 'zcFang'

from typing import List


class Solution:
    # 动态规划
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

    # 贪心 + 二分查找
    def lengthOfLIS(self, nums: List[int]) -> int:
        up = []
        for num in nums:
            if not up or num > up[-1]:
                up.append(num)
            else:
                left, right = 0, len(up) - 1
                index = right
                while left <= right:
                    mid = (left + right) // 2
                    if up[mid] >= num:
                        index = mid
                        right = mid - 1
                    else:
                        left = mid + 1
                up[index] = num
        return len(up)


# print(Solution().lengthOfLIS(nums=[0, 1, 0, 3, 2, 3]))
# print(Solution().lengthOfLIS(nums=[10, 9, 2, 3, 5, 7, 4, 5, 6, 101, 18]))
print(Solution().lengthOfLIS(nums=[4, 10, 4, 3, 8, 9]))
