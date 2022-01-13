# -*- coding: utf-8 -*-
# File:    747. 至少是其他数字两倍的最大数.py
# Date:    2022/1/13
# Software: Pycharm
__author__ = 'zcFang'

from typing import List


class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        m1, m2, idx = -1, -1, 0
        for i, num in enumerate(nums):
            if num > m1:
                m1, m2, idx = num, m1, i
            elif num > m2:
                m2 = num
        return idx if m1 >= m2 * 2 else -1


nums = [1, 2, 3, 6]
print(Solution().dominantIndex(nums))
