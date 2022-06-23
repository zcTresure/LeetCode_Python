# -*- coding: utf-8 -*-
# File:      1283. 使结果不超过阈值的最小除数.py
# DATA:      2022/6/23
# Software:  PyCharm
from typing import List


class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        left, right, ans = 1, max(nums), -1
        while left <= right:
            mid = (left + right) // 2
            total = sum((num - 1) // mid + 1 for num in nums)
            if total <= threshold:
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
        return ans


print(Solution().smallestDivisor(nums=[1, 2, 5, 9], threshold=6))
print(Solution().smallestDivisor(nums=[2, 3, 5, 7, 11], threshold=11))
