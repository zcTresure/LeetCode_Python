# -*- coding: utf-8 -*-
# File:      1838. 最高频元素的频数.py
# DATA:      2022/6/27
# Software:  PyCharm
from typing import List


class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        left, total, ans = 0, 0, 1
        for right in range(1, n):
            total += (nums[right] - nums[right - 1]) * (right - left)
            while total > k:
                total = total - nums[right] + nums[left]
                left += 1
            ans = max(ans, right - left + 1)
        return ans


print(Solution().maxFrequency(nums=[1, 2, 4], k=5))
