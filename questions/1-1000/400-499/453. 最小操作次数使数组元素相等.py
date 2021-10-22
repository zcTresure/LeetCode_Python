# -*- coding: utf-8 -*-
# File:      453. 最小操作次数使数组元素相等.py
# DATA:      2021/10/20
# Software:  PyCharm
__author__ = 'zcFang'

from typing import List


class Solution:
    def minMoves(self, nums: List[int]) -> int:
        min_num = min(nums)
        ans = 0
        for num in nums:
            ans += num - min_num
        return ans
