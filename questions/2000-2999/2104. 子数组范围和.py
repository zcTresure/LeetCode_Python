# -*- coding: utf-8 -*-
# File:      2104. 子数组范围和.py
# DATA:      2022/3/4
# Software:  PyCharm
__author__ = 'zcFang'

from typing import List


class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        ans, n = 0, len(nums)
        for i in range(n):
            min_val, max_val = float('inf'), -float('inf')
            for j in range(i, n):
                min_val = min(min_val, nums[j])
                max_val = max(max_val, nums[j])
                ans += max_val - min_val
        return ans

    # 单调栈
    def subArrayRanges(self, nums: List[int]) -> int:
        n = len(nums)
        min_left, max_left = [0] * n, [0] * n
        min_stk, max_stk = [], []
        for i, num in enumerate(nums):
            while min_stk and nums[min_stk[-1]] > num:
                min_stk.pop()
            min_left[i] = min_stk[-1] if min_stk else -1
            min_stk.append(i)
            # 如果 num[max_stk[-1] == num, 那根据定义
            # nums[max_stk[-1]] 逻辑下小于 num，因为 max_stk[-1] < i
            while max_stk and nums[max_stk[-1]] <= num:
                max_stk.pop()
            max_left[i] = max_stk[-1] if max_stk else -1
            max_stk.append(i)

        min_right, max_right = [0] * n, [0] * n
        min_stk, max_stk = [], []
        for i in range(n - 1, -1, -1):
            num = nums[i]
            # 如果 nums[minStack[-1]] == num, 那么根据定义，
            # nums[minStack[-1]] 逻辑上大于 num，因为 minStack[-1] > i
            while min_stk and nums[min_stk[-1]] >= num:
                min_stk.pop()
            min_right[i] = min_stk[-1] if min_stk else n
            min_stk.append(i)
            while max_stk and nums[max_stk[-1]] < num:
                max_stk.pop()
            max_right[i] = max_stk[-1] if max_stk else n
            max_stk.append(i)
        sum_max, sum_min = 0, 0
        for i, num in enumerate(nums):
            sum_max += (max_right[i] - i) * (i - max_left[i]) * num
            sum_min += (min_right[i] - i) * (i - min_left[i]) * num
        return sum_max - sum_min



nums = [1, 2, 3]
print(Solution().subArrayRanges(nums))
