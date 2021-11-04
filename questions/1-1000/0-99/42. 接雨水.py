# -*- coding: utf-8 -*-
# File:      42. 接雨水.py
# DATA:      2021/11/3
# Software:  PyCharm
__author__ = 'zcFang'

from typing import List


class Solution:
    # 动态规划
    def trap(self, height: List[int]) -> int:
        ans = 0
        n = len(height)
        lmax = [height[0]] + [0] * (n - 1)
        rmax = [0] * (n - 1) + [height[n - 1]]
        # 水池左视图
        for i in range(1, n):
            lmax[i] = max(height[i], lmax[i - 1])
        # 水池右视图
        for i in range(n - 2, -1, -1):
            rmax[i] = max(rmax[i + 1], height[i])
        ans = sum(min(rmax[i], lmax[i]) - height[i] for i in range(n))
        return ans

    # 单调栈
    def trap(self, height: List[int]) -> int:
        ans = 0
        # 单调栈，存储高度递减的下标
        stack = []
        for i, h in enumerate(height):
            while stack and h > height[stack[-1]]:
                top = stack.pop()
                if not stack:
                    break
                left = stack[-1]
                curr_width = i - left - 1
                curr_heidth = min(h, height[left]) - height[top]
                ans += curr_heidth * curr_width
            stack.append(i)
        return ans

    # 双指针
    def trap(self, height: List[int]) -> int:
        ans = 0
        left, right = 0, len(height) - 1
        left_max, right_max = 0, 0
        while left < right:
            left_max = max(left_max, height[left])
            right_max = max(right_max, height[right])
            if height[left] < height[right]:
                ans += left_max - height[left]
                left += 1
            else:
                ans += right_max - height[right]
                right -= 1
        return ans


height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
print(Solution().trap(height))
