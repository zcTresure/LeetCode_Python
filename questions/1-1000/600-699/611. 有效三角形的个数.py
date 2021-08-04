# -*- coding: utf-8 -*-
# File:      611. 有效三角形的个数.py
# DATA:      2021/8/4
# Software:  PyCharm
__author__ = 'zcFang'

from typing import List


class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        ans, n = 0, len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                left, right, k = j + 1, n - 1, j
                while left <= right:
                    mid = (left + right) // 2
                    if nums[i] + nums[j] > nums[mid]:
                        k, left = mid, mid + 1
                    else:
                        right = mid - 1
                ans += k - j
        return ans


nums = [2, 2, 3, 4]
print(Solution().triangleNumber(nums))
