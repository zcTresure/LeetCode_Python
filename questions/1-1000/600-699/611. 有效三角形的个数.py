# -*- coding: utf-8 -*-
# File:      611. 有效三角形的个数.py
# DATA:      2021/8/4
# Software:  PyCharm

from typing import List


class Solution:
    # 排序 + 二分查找
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

    # 排序 + 双指针
    def triangleNumber(self, nums: List[int]) -> int:
        ans, n = 0, len(nums)
        nums.sort()
        for i in range(n):
            k = i
            for j in range(i + 1, n):
                while k + 1 < n and nums[k + 1] < nums[i] + nums[j]:
                    k += 1
                ans += max(k - j, 0)
        return ans


nums = [2, 2, 3, 4]
print(Solution().triangleNumber(nums))
