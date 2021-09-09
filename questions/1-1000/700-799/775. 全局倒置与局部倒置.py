# -*- coding: utf-8 -*-
# File:      775. 全局倒置与局部倒置.py
# DATA:      2021/9/9
# Software:  PyCharm
__author__ = 'zcFang'

from typing import List


class Solution:
    # 线性搜索
    def isIdealPermutation(self, nums: List[int]) -> bool:
        return all(abs(i - x) < 2 for i, x in enumerate(nums))


nums = [1, 0, 2]
print(Solution().isIdealPermutation(nums))
