# -*- coding: utf-8 -*-
# File:     852. 山脉数组的峰顶索引.py
# Date:     2021/6/15
# Software: PyCharm
__author__ = 'zcFang'

from typing import List


class Solution():
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        for i in range(1, len(arr) - 1):
            if arr[i - 1] < arr[i] and arr[i] > arr[i + 1]:
                return i

    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        left, right, ans = 1, len(arr) - 2, 0
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] > arr[mid + 1]:
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
        return ans


arr = [24, 69, 100, 99, 79, 78, 67, 36, 26, 19]
print(Solution().peakIndexInMountainArray(arr))
