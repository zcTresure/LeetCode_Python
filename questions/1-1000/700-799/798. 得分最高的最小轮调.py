# -*- coding: utf-8 -*-
# File:      798. 得分最高的最小轮调.py
# DATA:      2022/3/9
# Software:  PyCharm
__author__ = 'zcFang'

from typing import List


class Solution:
    # 差分数组
    def bestRotation(self, nums: List[int]) -> int:
        n = len(nums)
        diffs = [0] * n
        for i, num in enumerate(nums):
            low = (i + 1) % n
            high = (i - num + n + 1) % n
            diffs[low] += 1
            diffs[high] -= 1
            if low >= high:
                diffs[0] += 1
            print(low, high, diffs)
        score, max_score, index = 0, 0, 0
        for i, diff in enumerate(diffs):
            score += diff
            if score > max_score:
                max_score, index = score, i
        return index


nums = [2, 3, 1, 4, 0]
print(Solution().bestRotation(nums))
