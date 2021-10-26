# -*- coding: utf-8 -*-
# File:      496. 下一个更大元素 I.py
# DATA:      2021/10/26
# Software:  PyCharm
__author__ = 'zcFang'

from typing import List


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        m, n = len(nums1), len(nums2)
        ans = [0] * m
        for i in range(m):
            j = nums2.index(nums1[i])
            k = j + 1
            while k < n and nums2[k] < nums2[j]:
                k += 1
            ans[i] = nums2[k] if k < n else -1
        return ans

    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        ans = {}
        for num in reversed(nums2):
            while stack and num > stack[-1]:
                stack.pop()
            ans[num] = stack[-1] if stack else -1
            stack.append(num)
        return [ans[num] for num in nums1]


nums1 = [4, 1, 2]
nums2 = [1, 3, 4, 2]
print(Solution().nextGreaterElement(nums1, nums2))
