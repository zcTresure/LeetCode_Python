# -*- coding: utf-8 -*-
# File:      575. 分糖果.py
# DATA:      2021/11/1
# Software:  PyCharm
__author__ = 'zcFang'

from typing import List


class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        return min(len(set(candyType)), len(candyType) // 2)
