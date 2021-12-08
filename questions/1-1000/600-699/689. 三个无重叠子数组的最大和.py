# -*- coding: utf-8 -*-
# File:      689. 三个无重叠子数组的最大和.py
# DATA:      2021/12/8
# Software:  PyCharm
__author__ = 'zcFang'

from typing import List


class Solution:
    # 单个子数组的最大和
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        ans = []
        sum1, max_sum1 = 0, 0
        for i, num in enumerate(nums):
            sum1 += num
            if i >= k - 1:
                if sum1 > max_sum1:
                    max_sum1 = sum1
                    ans = [i - k + 1]
                sum1 -= nums[i - k + 1]
        return ans

    # 两个无重叠子数组的最大和
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        ans = []
        sum1, max_sum1, max_sum1_idx = 0, 0, 0
        sum2, max_sum12 = 0, 0
        for i in range(k, len(nums)):
            sum1 += nums[i - k]
            sum2 += nums[i]
            if i >= k * 2 - 1:
                if sum1 > max_sum1:
                    max_sum1 = sum1
                    max_sum1_idx = i - k * 2 + 1
                if max_sum1 + sum2 > max_sum12:
                    max_sum12 = max_sum1 + sum2
                    ans = [max_sum1_idx, i - k + 1]
                sum1 -= nums[i - k * 2 + 1]
                sum2 -= nums[i - k + 1]

        return ans

    # 滑动窗口
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        ans = []
        sum1, max_sum1, max_sum1_idx = 0, 0, 0
        sum2, max_sum2, max_sum2_idx = 0, 0, ()
        sum3, max_total = 0, 0
        for i in range(k * 2, len(nums)):
            sum1 += nums[i - k * 2]
            sum2 += nums[i - k]
            sum3 += nums[i]
            if i >= k * 3 - 1:
                if sum1 > max_sum1:
                    max_sum1 = sum1
                    max_sum1_idx = i - k * 3 + 1
                if max_sum1 + sum2 > max_sum2:
                    max_sum2 = max_sum1 + sum2
                    max_sum2_idx = (max_sum1_idx, i - k * 2 + 1)
                if max_sum2 + sum3 > max_total:
                    max_total = max_sum2 + sum3
                    ans = [*max_sum2_idx, i - k + 1]
                sum1 -= nums[i - k * 3 + 1]
                sum2 -= nums[i - k * 2 + 1]
                sum3 -= nums[i - k + 1]
        return ans

    # 前缀和 + 序列 DP
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        sums = [nums[0]] + [0] * n
        for i in range(n):
            sums[i + 1] = sums[i] + nums[i]
        f = [[0] * 4 for _ in range(n + 10)]
        for i in range(n - k + 1, 0, -1):
            for j in range(1, 4):
                f[i][j] = max(f[i + 1][j], f[i + k][j - 1] + sums[i + k - 1] - sums[i - 1])
        ans = [0] * 3
        i, j, idx = 1, 3, 0
        while j > 0:
            if f[i + 1][j] > f[i + k][j - 1] + sums[i + k - 1] - sums[i - 1]:
                i += 1
            else:
                ans[idx] = i - 1
                idx += 1
                i += k
                j -= 1
        return ans

nums = [1, 2, 5, 4, 2, 5, 6, 2, 1, 4, ]
k = 2
print((Solution().maxSumOfThreeSubarrays(nums, k)))
